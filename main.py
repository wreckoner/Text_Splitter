'''
Created on Feb 13, 2014

@author: Dibyendu
'''
import wx
from main_frame_child import main_frame_child

def main():
    app = wx.App()
    main_frame_child(None)
    app.MainLoop()

if __name__ == '__main__':
    main()