'''
Created on Aug 12, 2014
@author: Dibyendu

Contains all the methods pertaining to the file that is to be split.
'''
import os, ntpath, threading
from methods.error_handlers import Python_IO_Error_Handler,\
    Python_Value_Error_Handler
    
class line_counter(threading.Thread):
    ''' A line counting class extending the Thread class.'''
    def __init__(self, staticText_lineCount, filename, animCtrl):
        threading.Thread.__init__(self)
        self.filename = filename
        self.staticText = staticText_lineCount
        self.animCtrl = animCtrl
        
    def run(self):
        self.exit = False
        self.animCtrl.Show()
        self.staticText.Hide()
        self.staticText.Parent.Layout()
        with open(self.filename) as f:
            if self.exit:
                self.animCtrl.Hide()
                self.staticText.Show()
                self.staticText.Parent.Layout()
                return
            for count, _ in enumerate(f):   pass
        self.staticText.SetLabel(str(count + 1))
        self.animCtrl.Hide()
        self.staticText.Show()
        self.staticText.Parent.Layout()
        
    def abort(self):
        self.exit = True

def Split_File(input_file, output_folder, split_mode, num, display_text, progress_bar, split_button):
    ''' Splits the file. If split_mode is 0 then divide into number of parts else divide by number of lines per file'''
    if split_mode == 1:
        Split_By_Lines(input_file, output_folder, num, display_text, progress_bar, split_button)
    else:
        Split_By_Parts(input_file, output_folder, num, display_text, progress_bar, split_button)
    
def Split_By_Lines(input_file, output_folder, num, display_text, progress_bar, split_button):
    ''' Splits the files according to the number of lines'''
    try :
        num = int(num)
        lines = Get_Number_Of_Lines(input_file)
        filepath = input_file
        filename = File_Name_From_Path(input_file)
        i, c = 1, 1
        #z = 1
        display_text.SetLabel('')
        progress_bar.SetRange(lines/num)
        #progress_bar.SetRange(z)
        split_button.Disable()
        
        x=open(os.path.join(output_folder, str(filename[:-4]+'_part'+str(c)+filename[-4:])),'a')
        x.close
        
        display_text.AppendText('Splitting file...')
        #textCtrl.AppendText('creating : '+str(filename[:-4]+'_part'+str(c)+filename[-4:]) + '\n')
        progress_bar.SetValue(c)
        with open(filepath, 'r') as fileobject:
            for line in fileobject:
                x=open(os.path.join(output_folder, str(filename[:-4]+'_part'+str(c)+filename[-4:])),'a')
                x.write(line)
                x.close
                i = i + 1
                #z = z + 1
                #progress_bar.SetRange(z)
                if i > num:
                    i, c = 1, c+1
                    #textCtrl.AppendText('creating : '+str(filename[:-4]+'_part'+str(c)+filename[-4:]) + '\n')
                    progress_bar.SetValue(c)
        display_text.AppendText('Total number of parts created : ' + str(c) + '\n')
        display_text.AppendText('Total number of lines read : ' + str(i+c*num))
        split_button.Enable()            
    except IOError as e:
        print str(e)                # Delete this in final release
        display_text.Clear()
        split_button.Enable()
        display_text.SetLabel(Python_IO_Error_Handler(e.errno))
    except ValueError as e:
        print str(e)                # Delete this is final release
        display_text.Clear()
        split_button.Enable()
        display_text.SetLabel(Python_Value_Error_Handler(e))
        
def Split_By_Parts(input_file, output_folder, num, display_text, progress_bar, split_button):
    ''' Splits file into number of parts as given by num parameter'''
    split_button.Disable()          # Disabling Split button while process is running.
    
    file_size = os.stat(input_file).st_size
    split_size = file_size/num
    part = 1
    
    with open(input_file) as f_in:
        input_file = File_Name_From_Path(input_file)
        while part <= num:
            output_file = '_'.join(('.'.join(input_file.split('.')[:-1]), 'part', str(part), '.%s'%input_file.split('.')[-1]))
            with open(ntpath.join(output_folder, output_file), 'w') as f_out:
                f_out.write(f_in.read(split_size))
            f_in.seek(split_size * part)
            part += 1
                
    display_text.write('Splitting complete.\nCreated %s files'%(part - 1))
    
    split_button.Enable()           # Enabling Split button.
        
def File_Name_From_Path(path):
    '''Finds the filename from the path, and returns it'''
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def Get_Number_Of_Lines(path):
    '''Returns the number of lines (newline characters) in a file.'''
    with open(path) as f:
        for i, _ in enumerate(f):
            pass
    return i
        
        
def Get_File_Size(filepath):
    '''Returns a string format of the file size'''
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
    return ' '.join((str(x), y))

def Display_Number_Of_Lines(path, textCtrl, animCtrl):
    ''' Not being used in the current version, but code kept as a backup'''
    textCtrl.SetLabel('')
    animCtrl.Show()
    animCtrl.Parent.Layout()
    x = Get_Number_Of_Lines(path)
    animCtrl.Hide()
    textCtrl.SetLabel(str(x))
    animCtrl.Parent.Layout()