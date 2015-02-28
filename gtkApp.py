#!/usr/bin/env python

from gi.repository import Gtk
import subprocess

class FileChooserWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="Wallpaper Changer")
		box = Gtk.Box(spacing=6)
		self.add(box)
		button2 = Gtk.Button("Choose Folder")
		button2.connect("clicked", self.on_folder_clicked)
		button3 = Gtk.Button("Set")
		button3.connect("clicked", self.on_set_clicked)
		global lbl1
		lbl1 = Gtk.Label()
		lbl2 = Gtk.Label("Time Interval:")
		global text
		text = Gtk.Entry()
		box.add(button2)
		box.add(button3)
 		box.add(lbl1)
		box.add(lbl2)
		box.add(text)
		rb1 = Gtk.RadioButton.new_with_label_from_widget(None, "GNOME")
		rb1.connect("toggled", self.on_radio_button_clicked, "gnome")
		box.pack_start(rb1, False, False, 0)
		rb2 = Gtk.RadioButton.new_from_widget(rb1)
		rb2.set_label("mate")
		rb2.connect("toggled", self.on_radio_button_clicked, "mate")
		box.pack_start(rb2, False, False, 0)
	
	def on_radio_button_clicked(self, button, name):
		global arg2
		if button.get_active():
		   arg2 = name
		   print name
		
	def on_set_clicked(self, widget):
		arglist1 = str(folderpath)
		arglist2 = arg2
		arglist3 = str(text.get_text())
		subprocess.call(["./changebg.sh",arglist1,arglist3,arglist2]) 
		
	def on_folder_clicked(self, widget):
		folderselectflag = "Y"
		dialog = Gtk.FileChooserDialog("Please choose a folder", self,
		Gtk.FileChooserAction.SELECT_FOLDER,
		 (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
		 "Select", Gtk.ResponseType.OK))
		dialog.set_default_size(800, 400)
		response = dialog.run()
		if response == Gtk.ResponseType.OK:
		   print("Select clicked")
		   print("Folder selected: " + dialog.get_filename())
		   lbl1.set_text(dialog.get_filename())
		   global folderpath
		   folderpath = dialog.get_filename()
		elif response == Gtk.ResponseType.CANCEL:
		   print("Cancel clicked")
		dialog.destroy()

win = FileChooserWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
