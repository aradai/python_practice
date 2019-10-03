#!/usr/bin/env python3
import sqlite3

def develop():
    """NEVER CALL THIS FUNCTION
    it's only for develop.
    So please leave it clean when you finished"""
    #MAKE CONNECTION
    conn=sqlite3.connect("lite.db") #connection class
    cur=conn.cursor() #cursor class
    #THE REAL CODE COMES HERE
    
    #CLOSE CONECTION
    conn.commit()
    conn.close()



def create_table(cur):
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")

def insert(cur,item,quantity,price):
    cur.execute("INSERT INTO store VALUES (?,?,?)",(item,quantity,price))

def view(cur):
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    return rows

def delete(cur,item):
    cur.execute("DELETE FROM store WHERE item=?",(item,))

def update(cur, item, quantity, price):
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quantity,price,item))

def main():
    #MAKE CONNECTION
    conn=sqlite3.connect("lite.db") #connection class
    cur=conn.cursor() #cursor class
    #THE REAL CODE COMES HERE
    update(cur,"Coffee Cup",25,5.5)
    print(view(cur))
    #CLOSE CONECTION
    conn.commit()
    conn.close()

main()