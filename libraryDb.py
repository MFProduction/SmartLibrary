from peewee import *
from sys import argv
database = MySQLDatabase('libraryDb', **{'passwd': 'adelaa', 'user': 'mf'})

libDb_tables_name = ["Books", "Author"] #edded for scripts

class UnknownField(object):
    pass

class BaseModel(Model):
    class Meta:
        database = database

class Author(BaseModel):
    alastname = CharField(max_length=45, null=True)
    aname = CharField(max_length=45, null=True)
    idauthor = PrimaryKeyField()

    class Meta:
        db_table = 'author'

class Books(BaseModel):
    bauthor = IntegerField(null=True)
    bbc = CharField(max_length=20, null=True)
    bname = CharField(max_length=45, null=True)
    idbooks = PrimaryKeyField()

    class Meta:
        db_table = 'books'
