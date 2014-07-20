#!/usr/bin/python
import MySQLdb
import nltk

db = MySQLdb.connect(host='localhost', # your host, usually localhost
                     user="root", # your username
                      passwd="msgp02", # your password
                      db="Enron") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute('SELECT * FROM bodies where messageid=1')
db.commit()

# print all the first cell of all the rows
for row in cur.fetchall():
    for word in nltk.word_tokenize(row[1]):
        print word