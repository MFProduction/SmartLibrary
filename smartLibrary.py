try :
    from peewee import *
    import MySQLdb as db
except:
    print "peewee or MySQLdb Error"

class DbConn:
    #connection info change if nececery 
    ip = "localhost"
    usr = "mf"
    pwd = "adelaa"
    name = "librarydb"
    tab_name = ["Books", "Author"] # manualy add names of tablesedded for scripts
    
def check_conn():
    #just try to connect to the mysql and see if it response
    try:
        dbx = db.connect(DbConn.ip, DbConn.usr, DbConn.pwd)                         
        cursor = dbx.cursor() 
        dbx.close()
    except:
        print "MySQL connection:" + bcolors.F + " FAIL " + bcolors.E
        exit(0) #exit the program is not working

class bcolors:
    #Just for improved visualization in scripts
    H = '\033[95m' #header
    OB = '\033[94m' #okblue
    OG = '\033[92m' #okgreen
    W = '\033[93m' #warning
    F = '\033[91m' #fail
    E = '\033[0m' #endc (end of color)
    def type(x):
        if x == "ok":
            return + bcolors.OG + " OK " + bcolors.E
        elif x == "fail":
            return + bcolors.F + " FAIL " + bcolors.E

'''
classes for database
'''
database = MySQLDatabase(DbConn.name, **{'passwd': DbConn.pwd, 'user': DbConn.usr})

class UnknownField(object):
    pass

class BaseModel(Model):
    class Meta:
        database = database

class Author(BaseModel):
    idauthor = PrimaryKeyField()
    lastname = CharField(db_column='lastName', max_length=45, null=True)
    name = CharField(max_length=45, null=True)

    class Meta:
        db_table = 'author'

class Books(BaseModel):
    author = IntegerField(null=True)
    barcode = CharField(max_length=20, null=True)
    desc = CharField(max_length=200, null=True)
    idbooks = PrimaryKeyField()
    in_stock = CharField(max_length=1, null=True)
    isbn = IntegerField(null=True)
    location = CharField(max_length=45, null=True)
    name = CharField(max_length=45, null=True)
   # year = UnknownField(null=True)  # year
    zalozba = CharField(max_length=45, null=True)

    class Meta:
        db_table = 'books'

