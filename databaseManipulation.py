from peewee import *
from libraryDb import *
from sys import argv

#tables_name = ["Books", "Author"]
def create_tab():
    #all the table names must be in tabels_name and in for loop. Ist's not clean but it works
    i = 0
    for table in Books, Author:
        try:
            database.create_tables([table])
            print "create table %s: OK" % libDb_tables_name[i]
        except:
            print "create table %s: FAIL" % libDb_tables_name[i]
        i += 1     
     #database.create_tables([Author, Books], True)

def drop_tab():
    req = raw_input("All the data will be lost (y,n): ")
    if req == "y":
        i = 0
        for table in Books, Author:
            try:
                database.drop_tables([table])
                print "drop table %s: OK" % libDb_tables_name[i]
            except:
                print "drop table %s: FAIL" % libDb_tables_name[i]
            i += 1     
     #database.create_tables([Author, Books], True)
    
def random_data():
    #just for quick debuging
    #first create authors and than books
    try:
        KarlMarx = Author.create(aname="Karl", alastname="Marx")
        AdolfHitler = Author.create(aname="Adolf", alastname="Hitler")
        Kapital1 = Books.create(bname="Kapital vol.1", bauthor=1, bbc=3831000242926)
        Kapital2 = Books.create(bname="Kapital vol.2", bauthor=1)
        Kapital3 = Books.create(bname="Kapital vol.3", bauthor=1)
        MeinKampf = Books.create(bname="Mein Kampf.", bauthor=2)
        print "Random data added: OK"
    except: print "Random data added: Fail"

#main script
usage = "usage: -c Create Database and tabels, -d Drop Db and tables, -h Help"
if len(argv) < 1:
    print usage 
elif argv[1] == "-c":
    create_tab()
elif argv[1] == "-rd":
    random_data()
elif argv[1] == "-d":
    drop_tab()
elif argv[1] == "-cl":
    drop_tab()
    create_tab()
    random_data()
elif argv[1] == "-h":
    print usage 
else:
    print usage

