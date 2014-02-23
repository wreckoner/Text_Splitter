#!usr/bin/env python

'''
Created on Feb 21, 2014

@author: Dibyendu
'''
import wx
from main_frame_child import main_frame_child

def main():
    app = wx.App(False)
    main_frame_child(None)
    app.MainLoop()

if __name__ == '__main__':
    main()