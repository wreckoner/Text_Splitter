#!/usr/bin/env python
"""Subclass of about_frame, which is generated by wxFormBuilder."""

import wx
import frames

# Implementing about_frame
class about_frame_child( frames.about_frame ):
	def __init__( self, parent ):
		frames.about_frame.__init__( self, parent )
		self.Bind(wx.EVT_CLOSE, self.OnClose)
		self.Show()
		self.Center()
		
	def OnClose(self, event):
		self.GetParent().Enable()
		self.Destroy()
		pass
	
