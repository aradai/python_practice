#!/usr/bin/env python3
import psycopg2
import sys

def develop():
    """NEVER CALL THIS FUNCTION
    it's only for develop.
    So please leave it clean when you finished"""
    if len(sys.argv) != 3:
        print("Please the sufficient number: username, password")
    else:
        user = sys.argv[1]
        password = sys.argv[2]
        #MAKE CONNECTION
        conn=psycopg2.connect("dbname='database1' user='{0}' password='{1}' host='localhost' port='5432'".format(user,password)) #connection class
        #connection class
        cur=conn.cursor() #cursor class
        #THE REAL CODE COMES HERE
        
        #CLOSE CONECTION
        conn.commit()
        conn.close()



def create_table(cur):
    """for creating table"""
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")

def insert(cur,item,quantity,price):
    """for insert data"""
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)",(item,quantity,price))

def view(cur):
    """for view current status of the table"""
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    return rows

def delete(cur,item):
    """for delete item"""
    cur.execute("DELETE FROM store WHERE item=%s",(item,))

def update(cur, item, quantity, price):
    """for update item qunatity or/and price"""
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",(quantity,price,item))

def main():
    if len(sys.argv) != 3:
        print("Please the sufficient number: username, password")
    else:
        user = sys.argv[1]
        password = sys.argv[2]
        #MAKE CONNECTION
        conn=psycopg2.connect("dbname='database1' user='{0}' password='{1}' host='localhost' port='5432'".format(user,password)) #connection class
        cur=conn.cursor() #cursor class
        #THE REAL CODE COMES HERE
        create_table(cur)
        #insert(cur,"Coffee Cup",25,5.5)
        #insert(cur,"Wine Glass",30,7.6)
        #delete(cur,"Coffee Cup")
        update(cur,"Wine Glass",25,5.5)
        print(view(cur))
        #CLOSE CONECTION
        conn.commit()
        conn.close()

main()