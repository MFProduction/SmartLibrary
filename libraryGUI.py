#!/usr/bin/env python

# GUI for library in pygtk

import pygtk
pygtk.require('2.0')
import gtk
from backendGui import *


class LibraryGui:

     def addBookC(self, widget, bn, ban, bal):
        bookn = bn.get_text()
        autn = ban.get_text()
        autf = bal.get_text()
        add_book(bookn, autn, autf)

     def __init__(self):
         #init#
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_title("Smart Library")
        #window.set_size_request(500, 300)
        window.connect("delete_event", lambda w,e: gtk.main_quit())
        window.set_border_width(10)
        
        #entry box#
        entryBox = gtk.VBox(False, 0)
        window.add(entryBox)
        entryBox.show()
        
        bookBox = gtk.HBox(False, 0)
        entryBox.add(bookBox)
        bookBox.show()

        bookNameL = gtk.Label("Book Name:")
        bookNameL.show()
        bookBox.pack_start(bookNameL, False, False, 0)
        
        #entery book Name#
        bookName = gtk.Entry()
        bookName.set_max_length(50)
        bookName.set_text("enter text")
        bookName.select_region(0, len(bookName.get_text()))
        bookBox.pack_start(bookName, False, False, 0)
        bookName.show()
        
#####################

        auBox = gtk.HBox(False, 0)
        entryBox.add(auBox)
        auBox.show()
        
        LAuthorName = gtk.Label("Author Name:")
        LAuthorName.show()
        auBox.pack_start(LAuthorName, False, False, 0)
        
        #entery book Name#
        authorName = gtk.Entry()
        authorName.set_max_length(50)
        authorName.set_text("enter text")
        authorName.select_region(0, len(bookName.get_text()))
        auBox.pack_start(authorName, False, False, 0)
        authorName.show()

#####################

        aufBox = gtk.HBox(False, 0)
        entryBox.add(aufBox)
        aufBox.show()
        
        LAuthorNamef = gtk.Label("Author Last Name:")
        LAuthorNamef.show()
        aufBox.pack_start(LAuthorNamef, False, False, 0)
        
        #entery book Name#
        authorNamef = gtk.Entry()
        authorNamef.set_max_length(50)
        authorNamef.set_text("enter text")
        authorNamef.select_region(0, len(bookName.get_text()))
        aufBox.pack_start(authorNamef, False, False, 0)
        authorNamef.show()
        
        
        #do button#
        addB = gtk.Button("ADD")
        addB.connect("clicked", self.addBookC, bookName, authorName, authorNamef)
        entryBox.pack_start(addB, False, False, 0)
        addB.show()

        window.show()

def main():
    gtk.main()

if __name__ == "__main__":
    library = LibraryGui()
    main()


'''
        #buttons#
        button1 = gtk.Button("Button 1")
        button1.connect("clicked", self.callback, "button 1")
        buttonBox.pack_start(button1, True, True, 0)
        button1.show()

        button2 = gtk.Button("Button 2")
        button2.connect("clicked", self.callback, "button 2")
        buttonBox.pack_start(button2, True, True, 0)
        button2.show()
        
        button = gtk.Button(stock=gtk.STOCK_CLOSE)
        button.connect("clicked", lambda w: gtk.main_quit())
        buttonBox.pack_start(button, True, True, 0)
        button.set_flags(gtk.CAN_DEFAULT)
        button.grab_default()
        button.show()
     
'''
