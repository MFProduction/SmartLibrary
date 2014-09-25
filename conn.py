#! /usr/bin/python
import peewee as pw
from  libraryDb import *
import zbar
from sys import argv


def read_barcode():
# Read barcode from sorce and return barcode data
# Still neds optimization. try:,  
    # create a Processor
    proc = zbar.Processor()
    # configure the Processor
    proc.parse_config('enable')
    # initialize the Processor    
    device = '/dev/video0'
    if len(argv) > 1:
        device = argv[1]
    proc.init(device)
    # enable the preview window    
    proc.visible = True
    # read at least one barcode (or until window close)    
    proc.process_one()
    # hide the preview window    
    proc.visible = False
    # extract results    
    for symbol in proc.results:
        # do something useful with results
        print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data
        return symbol.data
def generate_barcode():
    pass

def add_book():
    print "add book to library:"
    book_name = raw_input("Book Name: ")
    
    print "authors:"
    for aut in Author.select():
        print aut.idauthor, aut.aname, aut.alastname
    arg = raw_input("press n or author id number: ")
    if arg == "n":
        book_author =  add_author(True)
    else:
        book_author = arg
    book_barcode = read_barcode()    
    
    nbook = Books.create(bname= book_name, bauthor= book_author, bbc= book_barcode)

def change_book_name(book_name, new_book_name):
    for book in Books.select().where(Books.bname==book_name):
        print book.bname
        book.bname = new_book_name
        book.save()
        print book.bname

def change_bcc(bbc, new_bbc):
    for bc in Books.select().where(Books.bbc == bbc):
        bc.bbc = new_bbc
        bc.save()

def change_author (book_name, new_author): ## se ni koncano
    for book in Book.select().where(Book.bname==book_name):
        for author in Author.select().where(Author.idauthor==book.bauthor):
            book.bauthor = new_author
            book.seve()


def add_author(x): #true returns id of the authord
    print "add author to library"
    author_name = raw_input("author name: ")
    author_last = raw_input("author last name: ")
    naut = Author.create(aname= author_name, alastname= author_last)
    if x == True:
        return naut.idauthor



def print_books():
    print "all books in library:"
    for book in Books.select():
        for author in Author.select().where(Author.idauthor == book.bauthor):
            print book.bname, '- ', author.aname, author.alastname

def print_barcode():
    barcode = read_barcode()
    for book in Books.select().where(Books.bbc == barcode):
        for author in Author.select().where(Author.idauthor == book.bauthor):
            print book.bname, '-', author.aname, author.alastname

def print_by_author():
    print "authors:"
    for author in Author.select().order_by(Author.aname):
        print author.idauthor, author.aname, author.alastname
    arg = raw_input("pick author: ")
    for author in Author.select().where(Author.idauthor == arg):
        print author.aname, author.alastname, ':'
        for book in Books.select().where(Books.bauthor == arg):
            print '    ', book.bname

#main program
help = "Usage: (b)add book (a)add author (p)rint books (h)elp (s)top program  r pbr"
print "Backand scrpit for library" 
print help
stop = False
while (stop != True):
    arg = raw_input("> ")

    if arg == "b":
        add_book()
        print "book added-"
    elif arg == "a":
        add_author(False)
        print "Author added."
    elif arg == 'p':
        print_books()
    elif arg == 'r':
        print_barcode()
    elif arg == 's':
        stop = True
    elif arg == 'h':
          print help
    elif arg == 'pba':
        print_by_author()
    else:
        print help

