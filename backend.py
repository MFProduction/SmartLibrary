#! /usr/bin/python
import peewee as pw
from  smartLibrary import *
import zbar
from sys import argv #only for barcod scaner or cam (will be removed probably)

def read_barcode():
    '''
    Read barcode from sorce and return barcode data
    Still neds optimization. try:,  
    '''
    try:
        proc = zbar.Processor()
        proc.parse_config('enable')
        device = '/dev/video0'
        if len(argv) > 1:
            device = argv[1]
        proc.init(device)
        proc.visible = True
        proc.process_one()
        proc.visible = False
    except:
        print "reading barcode:" + bcolors.F + " FAIL " + bcolors.E
        return False #returns False, that means error
    for symbol in proc.results:
        print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data #just for debuging
        return symbol.data

def generate_barcode():
    '''
    Generate barcode that doesn't exsist in the database
    problem is  if the book has the barcode that you generated before
    '''
    pass
               
def add_book():
    '''
    Add book  adds book in the library with author that you select or
    create new avtor; problably just for the terminal not gui
    '''
    print "add book to library:"
    book_name = raw_input("Book Name: ")
    
    print "authors:"
    for aut in Author.select():
        print aut.idauthor, aut.name, aut.lastname
    arg = raw_input("press n or author id number: ")
    if arg == "n":
        book_author =  add_author(True)
    else:
        book_author = arg
    barcode = read_barcode()    
    if barcode != False:
        nbook = Books.create(name= book_name, author= book_author, barcode=barcode)
    else:
        nbook = Books.create(name= book_name, author= book_author)

def change_book_name(book_name, new_book_name):
    '''
    change the name of the book, input book name, new book name
    '''
    for book in Books.select().where(Books.name==book_name):
        book.name = new_book_name
        book.save()

def change_bcc(bbc, new_bbc):
    '''
    Change barcode for the book
    '''
    for bc in Books.select().where(Books.barcode == bbc):
        bc.barcode = new_bbc
        bc.save()

def change_author (book_name, new_author): ## se ni koncano
    '''
    change author by book name (still not working; porbably have to change db
    collum. Don't know if its better to have book name input or book id input?
    '''
    for book in Book.select().where(Book.name==book_name):
        for author in Author.select().where(Author.idauthor==book.author):
            book.author = new_author
            book.seve()


def add_author(x=False):
    '''
    adds author to db (only for terminal script) if input is true returns id of
    author
    '''
    print "add author to library"
    author_name = raw_input("author name: ")
    author_last = raw_input("author last name: ")
    naut = Author.create(name= author_name, lastname= author_last)
    if x == True:
        return naut.idauthor


def print_book(bn):
    '''
    print book with book name
    '''
    for book in Books.select().where(Books.name==bn):
        for author in Author.select().where(Author.idauthor == book.author):
            if book.name != 'none':
                return "fuck you" #, author.name, author.lastname
            else: return "fuck you to"

def print_books():
    '''
    print all books in the library
    '''
    print "all books in library:"
    for book in Books.select():
        for author in Author.select().where(Author.idauthor == book.author):
            print book.name, '- ', author.name, author.lastname

def print_barcode():
    '''
    Prints books that have that barcode
    '''
    barcode = read_barcode()
    if barcode == False:
        pass
    else:
        for book in Books.select().where(Books.barcode == barcode):
            for author in Author.select().where(Author.idauthor == book.author):
                print book.name, '-', author.name, author.lastname

def print_by_author():
    '''
    prints author, you select author and it prits all the books written by him.
    change: input author id or name/lastname and print (return) all the books
    '''
    print "authors:"
    for author in Author.select():
        print author.idauthor, author.name, author.lastname
    arg = raw_input("pick author: ")
    for author in Author.select().where(Author.idauthor == arg):
        print author.name, author.lastname, ':'
        for book in Books.select().where(Books.author == arg):
            print '    ', book.name



def usage():
    '''
    no need to put info here :)
    '''
    print "Usage: python backend.py [path to camera or barcode reader]"
    print "       b  Addd book" 
    print "       a  Add author" 
    print "       p  Print books" 
    print "       pa Print by author"
    print "       h  Help" 
    print "       s  Stop program"  
    print "       r  Read fom barcode reader "

def main(x = False):
    if x == False:
        print "Backand scrpit for library" 
        check_conn()
        usage()
    stop = False
    while (stop != True):
        arg = raw_input("> ")

        if arg == "b":
            add_book()
            print "book added"
        elif arg == "a":
            add_author()
            print "Author added"
        elif arg == 'p':
            print_books()
        elif arg == 'r':
            print_barcode()
        elif arg == 's':
            stop = True
        elif arg == 'h':
            usage()
        elif arg == 'pa':
            print_by_author()
        else:
            usage()


if __name__ == '__main__': 
    main()
