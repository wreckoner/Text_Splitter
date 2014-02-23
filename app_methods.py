#!/usr/bin/env python
'''
Created on Feb 21, 2014

@author: Dibyendu
'''
#Module contains methods called by main frame child
import os

def FilePreview(textCtrl, filename):
    x = open(filename, 'r')
    y = x.read(2000)
    z = x.read(2001)
    x.close()
    if y.count('\n') > 20:
        z = ''
        y = y.split('\n')
        for line in y[:20]:
            z = z + line + '\n'
        y = z + '....(contd.)'
    elif len(y) < len(z):
        y = y + '....(contd.)'
    textCtrl.SetLabel('')
    textCtrl.AppendText(y)
    
def Splitter(filename, outputPath, num, textCtrl, progress_bar, split_button):
    try :
        num = int(num)
        lines = GetNumberOfLines(None, filename)
        filepath = filename
        filename = FileNameExtractor(filename)
        i, c = 1, 1
        #z = 1
        textCtrl.SetLabel('')
        progress_bar.SetRange(lines/num)
        #progress_bar.SetRange(z)
        split_button.Disable()
        
        x=open(outputPath + '\\' + str(filename[:-4]+'_part'+str(c)+filename[-4:]),'a')
        x.close
        
        textCtrl.AppendText('Splitting file...')
        #textCtrl.AppendText('creating : '+str(filename[:-4]+'_part'+str(c)+filename[-4:]) + '\n')
        progress_bar.SetValue(c)
        with open(filepath, 'r') as fileobject:
            for line in fileobject:
                x=open(outputPath + '\\' + str(filename[:-4]+'_part'+str(c)+filename[-4:]),'a')
                x.write(line)
                x.close
                i = i + 1
                #z = z + 1
                #progress_bar.SetRange(z)
                if i > num:
                    i, c = 1, c+1
                    #textCtrl.AppendText('creating : '+str(filename[:-4]+'_part'+str(c)+filename[-4:]) + '\n')
                    progress_bar.SetValue(c)
        textCtrl.AppendText('Total number of parts created : ' + str(c) + '\n')
        textCtrl.AppendText('Total number of lines read : ' + str(i+c*num))
        split_button.Enable()            
    except IOError, e:
        textCtrl.Clear()
        split_button.Enable()
        textCtrl.SetLabel(PythonIOErrorHandler(e.errno))
    except ValueError, e:
        textCtrl.Clear()
        split_button.Enable()
        textCtrl.SetLabel(PythonValueErrorHandler(e))
        
def GetFileSize(filepath):
    x = os.stat(filepath).st_size
    y='bytes'
    if x > 1024:
        x = round(float(x)/1024, 2)
        y = 'KB'
        if x > 1024:
            x = round(x/1024, 2)
            y = 'MB'
            if x > 1024:
                x = round(x/1024, 2)
                y='GB'
    return str(x) + ' ' + y

def GetNumberOfLines(textCtrl, filepath):
    if textCtrl != None:
        textCtrl.SetLabel('Scanning')
    c = 0
    with open(filepath, 'r') as fileobject:
        for line in fileobject:
            c = c+1
    if textCtrl == None:
        return c
    else:
        textCtrl.SetLabel(str(c))
    
def FileNameExtractor(filename):
    filename = filename.split('\\')[filename.count('\\')]
    return filename

def PythonIOErrorHandler(errno):
    if errno == 13:
        message = 'Select Output Directory!!!'
    elif errno == 22:
        message = 'Select a File!!!'
    else:
        message = 'Unknown Error. Report Bug!!!'
    return message

def PythonValueErrorHandler(error):
    if str(error[0]).find('invalid literal for int() with base 10:') == 0:
        message = 'Enter proper number of lines!!!'
    else:
        message = 'Unknown Error. Report Bug!!!'
    return message
    