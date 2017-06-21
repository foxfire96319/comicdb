import mysql

def main():

    conn = mysql.connector.connect(user='root', host='127.0.0.1', database='comic_database')
    transaction = "SELECT * FROM comics WHERE title='europa'"
    conn.cmd_query(transaction)
    for row in conn.get_rows():
        print row
        print '\n'
