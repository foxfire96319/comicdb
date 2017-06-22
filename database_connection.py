#usr/bin/python2.7

import mysql.connector

conn = mysql.connector.connect(user='root', host='127.0.0.1', database='comic_database')
transaction = "SELECT * FROM comics WHERE title='europa'"
cursor = conn.cursor()
cursor.execute(transaction)
for results in  cursor.fetchall():
    print results
