SmartLibrary
============

## 1.0 - Introduction
SmartLibrary is GUI, engine and dbase for books, movies, and music with barcode reader in python.  
## 2.0 -  Installing SmarLibrary

### 2.1 - Pre Instalation

Required packeges for Smart Library to work:

python (apt-get install python
zbar library for python (barcode reader; apt-get install  python-zbar || pip zbar)
peewee library for python (creating classes for db tables etc.; pip install peeweee)	
MySQLdb library for python (connection to mysql database) 
Mysql datbase (apt-get install mysql-server)
PyGTK GUI interface
I will try to include this installation in the script 

### 2.2 - Instalation

Open Librarydb.py and change the varables for the mysql database (usr, password, location...)
```python
class DbConn:
    ip = "localhost"
    usr = "mf"
    pwd = "******"
    name = "librarydb"
```
Run the following command:
```bash
$ dbManipulatuon.py -c 
```
to create database and tables
Run backand.py (it's a small program to add and print the books in terminal

## 3.0 - More Coming

Backand that works on windows
Python ||&& php GUI
Python gui is in 
Movie and music database 


## X.O Post Instalation and Contact Info

- Matej Ferenc (ferenc.matej@gmail.com)

*Have fun and read more books :)  

