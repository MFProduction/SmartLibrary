from peewee import *

database = MySQLDatabase('libraryDb', **{'passwd': 'adelaa', 'user': 'mf'})

class UnknownField(object):
    pass

class BaseModel(Model):
    class Meta:
        database = database

class Books(BaseModel):
    bauthor = CharField(max_length=45)
    bc = IntegerField(null=True)
    bname = CharField(max_length=45)
    idbooks = PrimaryKeyField()
    isbn = IntegerField(null=True)

    class Meta:
        db_table = 'books'

