#!/usr/bin/env python
#Author : Dibyendu Das
#Created : 2/21/2014
#This module contains some regular wxPython features not found in wxFormBuilder. Using this as a library instead.

import wx

def OnOpenFile(parent):
    y = wx.FileDialog(parent, 'Open File', wildcard = 'Text file (*.txt)|*.txt|All files (*.*)|*.*', style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST | wx.FD_CHANGE_DIR, pos = wx.DefaultPosition)
    if y.ShowModal() == wx.ID_OK:
        return y.GetPath()

def OnSelectFolder(parent):
    y = wx.DirDialog(parent, 'Select Output Folder', style = wx.DEFAULT_DIALOG_STYLE | wx.DD_CHANGE_DIR, pos = wx.DefaultPosition, name = 'Boomshine')
    if y.ShowModal() == wx.ID_OK:
        return y.GetPath()
    
def TextCtrlWriter(textCtrl, filename):
    with open(filename, 'r') as fileobject:
        for line in fileobject:
            textCtrl.AppendText(line)
        
    

def debug():
    y = wx.App()
    y.MainLoop()
    print OnOpenFile(None)
    print OnSelectFolder(None)

#if __name__ == "__main__":
    #print 'starting debug'
    #debug()
