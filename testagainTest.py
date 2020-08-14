import sqlite3 as s
import os


if(not os.path.isfile('./test.db')):
    print('yes')
    with s.connect('test.db') as db:
        c = s.Cursor(db)
        c.execute('CREATE TABLE MEMBERS(name text, hp integer, power integer, SApower integer, speed integer, type text)')
        db.commit()

def read():
    with s.connect('test.db') as db:
        c = s.Cursor(db)
        c.execute("SELECT * FROM MEMBERS")
        rows = c.fetchall()
        for row in rows:
            print(row)
        db.commit()

def write(op):
    with s.connect('test.db') as db:
        if op == 'add':
            c = s.Cursor(db)
            name = 'test2'
            hp=32
            pwr=42
            SA=22
            sp=9992
            ty='op2'
            c.execute(f"INSERT INTO MEMBERS VALUES('{name}', '{hp}', '{pwr}', '{SA}', '{sp}', '{ty}')")
            db.commit()
        else:
            c = s.Cursor(db)
            name = 'test'
            c.execute(f"DELETE FROM MEMBERS WHERE name='{name}'")
            db.commit()
write('del')
read()