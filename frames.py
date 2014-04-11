# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Nov  6 2013)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class main_frame
###########################################################################

class main_frame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Partition Text", pos = wx.DefaultPosition, size = wx.Size( 700,500 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer41 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer27 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer271 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer23 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer24 = wx.BoxSizer( wx.VERTICAL )
		
		self.filename_label = wx.StaticText( self.m_panel1, wx.ID_ANY, u"File", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.filename_label.Wrap( -1 )
		bSizer24.Add( self.filename_label, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer23.Add( bSizer24, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer25 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer241 = wx.BoxSizer( wx.VERTICAL )
		
		self.file_box = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_NO_VSCROLL )
		bSizer241.Add( self.file_box, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer25.Add( bSizer241, 1, wx.EXPAND, 5 )
		
		bSizer251 = wx.BoxSizer( wx.VERTICAL )
		
		self.file_open_button = wx.Button( self.m_panel1, wx.ID_ANY, u"...", wx.DefaultPosition, wx.Size( 20,-1 ), 0 )
		bSizer251.Add( self.file_open_button, 0, wx.ALL, 5 )
		
		
		bSizer25.Add( bSizer251, 0, wx.EXPAND, 5 )
		
		
		bSizer23.Add( bSizer25, 3, wx.EXPAND, 5 )
		
		
		bSizer271.Add( bSizer23, 0, wx.EXPAND, 5 )
		
		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer20 = wx.BoxSizer( wx.VERTICAL )
		
		self.output_folder_label = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Output Folder", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.output_folder_label.Wrap( -1 )
		bSizer20.Add( self.output_folder_label, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer19.Add( bSizer20, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer22 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer28 = wx.BoxSizer( wx.VERTICAL )
		
		self.output_folder_box = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_NO_VSCROLL )
		bSizer28.Add( self.output_folder_box, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer22.Add( bSizer28, 1, wx.EXPAND, 5 )
		
		bSizer29 = wx.BoxSizer( wx.VERTICAL )
		
		self.output_folder_browse = wx.Button( self.m_panel1, wx.ID_ANY, u"...", wx.DefaultPosition, wx.Size( 20,-1 ), 0 )
		bSizer29.Add( self.output_folder_browse, 0, wx.ALL, 5 )
		
		
		bSizer22.Add( bSizer29, 0, wx.EXPAND, 5 )
		
		
		bSizer19.Add( bSizer22, 3, wx.EXPAND, 5 )
		
		
		bSizer271.Add( bSizer19, 0, wx.EXPAND, 5 )
		
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.lines_label = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Lines per file", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lines_label.Wrap( -1 )
		bSizer8.Add( self.lines_label, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer7.Add( bSizer8, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		self.lines_box = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,20 ), wx.TE_NO_VSCROLL )
		self.lines_box.SetMaxLength( 999 ) 
		bSizer10.Add( self.lines_box, 1, wx.ALL, 5 )
		
		
		bSizer7.Add( bSizer10, 3, wx.EXPAND, 5 )
		
		
		bSizer271.Add( bSizer7, 0, wx.EXPAND, 5 )
		
		
		bSizer27.Add( bSizer271, 2, wx.EXPAND, 5 )
		
		bSizer281 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticline1 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer281.Add( self.m_staticline1, 0, wx.EXPAND|wx.LEFT, 5 )
		
		bSizer282 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer291 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer33 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText6 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Size", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		bSizer33.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		self.file_size_diplay = wx.StaticText( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.file_size_diplay.Wrap( -1 )
		bSizer33.Add( self.file_size_diplay, 1, wx.ALL, 5 )
		
		
		bSizer291.Add( bSizer33, 1, wx.EXPAND, 5 )
		
		bSizer34 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText8 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Lines", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		bSizer34.Add( self.m_staticText8, 0, wx.ALL, 5 )
		
		self.lines_label = wx.StaticText( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lines_label.Wrap( -1 )
		bSizer34.Add( self.lines_label, 1, wx.ALL, 5 )
		
		
		bSizer291.Add( bSizer34, 1, wx.EXPAND, 5 )
		
		
		bSizer282.Add( bSizer291, 0, wx.ALL|wx.EXPAND, 5 )
		
		bSizer30 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer282.Add( bSizer30, 1, wx.EXPAND, 5 )
		
		bSizer32 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer282.Add( bSizer32, 1, wx.EXPAND, 5 )
		
		
		bSizer281.Add( bSizer282, 1, wx.EXPAND, 5 )
		
		
		bSizer27.Add( bSizer281, 1, wx.EXPAND, 5 )
		
		
		bSizer41.Add( bSizer27, 0, wx.EXPAND, 5 )
		
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		self.split_button = wx.Button( self.m_panel1, wx.ID_ANY, u"&Split", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.split_button, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer41.Add( bSizer11, 0, wx.EXPAND, 5 )
		
		bSizer26 = wx.BoxSizer( wx.VERTICAL )
		
		self.text_display = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer26.Add( self.text_display, 1, wx.EXPAND, 5 )
		
		self.progress_bar = wx.Gauge( self.m_panel1, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( -1,20 ), wx.GA_HORIZONTAL|wx.GA_SMOOTH )
		self.progress_bar.SetValue( 0 ) 
		bSizer26.Add( self.progress_bar, 0, wx.ALL|wx.EXPAND, 3 )
		
		
		bSizer41.Add( bSizer26, 1, wx.EXPAND, 5 )
		
		
		bSizer3.Add( bSizer41, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel1.SetSizer( bSizer3 )
		self.m_panel1.Layout()
		bSizer3.Fit( self.m_panel1 )
		bSizer4.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 0 )
		
		
		self.SetSizer( bSizer4 )
		self.Layout()
		self.m_statusBar2 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.m_menubar2 = wx.MenuBar( 0 )
		self.file_menu = wx.Menu()
		self.file_menu_open = wx.MenuItem( self.file_menu, wx.ID_ANY, u"&Open"+ u"\t" + u"Ctrl+O", u"Open file to split or extract from..", wx.ITEM_NORMAL )
		self.file_menu_open.SetBitmap( wx.Bitmap( u"icon/open_icon.png", wx.BITMAP_TYPE_ANY ) )
		self.file_menu.AppendItem( self.file_menu_open )
		
		self.file_menu_exit = wx.MenuItem( self.file_menu, wx.ID_ANY, u"&Exit"+ u"\t" + u"ALT+F4", u"Exit Partition Text", wx.ITEM_NORMAL )
		self.file_menu_exit.SetBitmap( wx.Bitmap( u"icon/close_icon.png", wx.BITMAP_TYPE_ANY ) )
		self.file_menu.AppendItem( self.file_menu_exit )
		
		self.m_menubar2.Append( self.file_menu, u"&File" ) 
		
		self.help_menu = wx.Menu()
		self.help_menu_about = wx.MenuItem( self.help_menu, wx.ID_ANY, u"&About"+ u"\t" + u"F1", u"About Partition Text", wx.ITEM_NORMAL )
		self.help_menu_about.SetBitmap( wx.Bitmap( u"icon/about_icon.png", wx.BITMAP_TYPE_ANY ) )
		self.help_menu.AppendItem( self.help_menu_about )
		
		self.m_menubar2.Append( self.help_menu, u"&Help" ) 
		
		self.SetMenuBar( self.m_menubar2 )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.file_open_button.Bind( wx.EVT_BUTTON, self.OnOpenFile )
		self.output_folder_browse.Bind( wx.EVT_BUTTON, self.OnOutputFolderSelect )
		self.split_button.Bind( wx.EVT_BUTTON, self.OnSplit )
		self.Bind( wx.EVT_MENU, self.OnOpenFile, id = self.file_menu_open.GetId() )
		self.Bind( wx.EVT_MENU, self.OnExit, id = self.file_menu_exit.GetId() )
		self.Bind( wx.EVT_MENU, self.OnAbout, id = self.help_menu_about.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnOpenFile( self, event ):
		event.Skip()
	
	def OnOutputFolderSelect( self, event ):
		event.Skip()
	
	def OnSplit( self, event ):
		event.Skip()
	
	
	def OnExit( self, event ):
		event.Skip()
	
	def OnAbout( self, event ):
		event.Skip()
	

###########################################################################
## Class about_frame
###########################################################################

class about_frame ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"About Partition Text", pos = wx.DefaultPosition, size = wx.Size( 232,178 ), style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer121 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer15 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_bitmap1 = wx.StaticBitmap( self.m_panel4, wx.ID_ANY, wx.Bitmap( u"icon/about_pic.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.m_bitmap1, 0, wx.ALL, 5 )
		
		
		bSizer121.Add( bSizer15, 1, wx.EXPAND, 5 )
		
		bSizer17 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText7 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"PARTITION TEXT\n    Version 1.0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		self.m_staticText7.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, "Arial" ) )
		
		bSizer17.Add( self.m_staticText7, 0, wx.ALL, 10 )
		
		
		bSizer121.Add( bSizer17, 3, wx.EXPAND, 0 )
		
		
		bSizer13.Add( bSizer121, 1, wx.EXPAND, 0 )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText8 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Created By : Dibyendu Das", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		bSizer14.Add( self.m_staticText8, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		
		bSizer13.Add( bSizer14, 1, wx.EXPAND, 5 )
		
		
		self.m_panel4.SetSizer( bSizer13 )
		self.m_panel4.Layout()
		bSizer13.Fit( self.m_panel4 )
		bSizer12.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 10 )
		
		
		self.SetSizer( bSizer12 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

