from smartLibrary import *
from sys import argv

        
def create_db(): #import db_ip, username, pass. db_name /or static? 
    # we will have to import MySQLdb because peewee can't create it!
    dbx = db.connect(DbConn.ip, DbConn.usr, DbConn.pwd)                                 
    cursor = dbx.cursor() 
    try:
        sql = "CREATE DATABASE %s " % DbConn.name
        cursor.execute(sql)
        print "Create database %s: " % DbConn.name + bcolors.OG + "OK " + bcolors.E 
    except:
        print "Create database %s:" % DbConn.name + bcolors.F + " FAIL " + bcolors.E
    dbx.close()

def create_tab(): #import table name?
    #all the table names must be in tabels_name and in for loop. Ist's not clean but it works. I will try to change that after I see other things.
    i = 0
    for table in Books, Author:
        try:
            database.create_tables([table]) #error doda tabelo ampak naredi fail?? debug
            print "Create table %s:" % DbConn.tab_name[i] + bcolors.OG + " OK  " + bcolors.E
        except:
            print "Create table %s:" % DbConn.tab_name[i] + bcolors.F + " FAIL " + bcolors.E
        i += 1     
     
def drop_tab():
    #drops both tables; have to change to import table name?
    req = raw_input("All the data will be lost (y,n): ")
    if req == "y":
        i = 0
        for table in Books, Author: ##
            try:
                database.drop_tables([table])
                print "Drop table %s:" % DbConn.tab_name[i] + bcolors.OG + " OK " + bcolors.E
            except:
                print "Drop table %s:" % DbConn.tab_name[i] + bcolors.F + " FAIL " + bcolors.E
            i += 1     
         
def random_data():
    #just for quick debuging
    #first create authors and than books
    try:
        KarlMarx = Author.create(name="Karl", lastname="Marx")
        AdolfHitler = Author.create(name="Adolf", lastname="Hitler")
        Kapital1 = Books.create(name="Kapital vol.1", author=1, barcode=3831000242926)
        Kapital2 = Books.create(name="Kapital vol.2", author=1)
        Kapital3 = Books.create(name="Kapital vol.3", author=1)
        MeinKampf = Books.create(name="Mein Kampf.", author=2)
        print "Random data added:" + bcolors.OG + " OK " + bcolors.E
    except: print "Random data added:" + bcolors.F + " FAIL " + bcolors.E

def usage():
    print "Usage: python dbManipulation.py [option]"
    print "      -c Create db and tabels"
    print "      -d Drop db and tables"
    print "      -h show this message"

def main():
    check_conn()#always check the connection before start
    try:
        if argv[1] == "-c":
            create_db()
            create_tab()
        elif argv[1] == "-rd": #not in usage just for debug
            random_data()
        elif argv[1] == "-d":
            drop_tab()
        elif argv[1] == "-cl":
            drop_tab()
            create_tab()
            random_data()
        elif argv[1] == "-h" or argv[1] == "--help":
            usage() 
        else:
            usage()
    except:
        usage()
 
if __name__ == '__main__':
    main()
