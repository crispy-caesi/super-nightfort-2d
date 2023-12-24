# ===================== import ===================== #

import sqlite3
from sqlite3 import Error

# ===================== db ===================== #

def connect():
    conn = None
    try:
        conn = sqlite3.connect("progress.db")
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn

def create_table(conn):
    try:
        c = conn.cursor()
        sql = """CREATE TABLE IF NOT EXISTS progress (
                                            id integer PRIMARY KEY, 
                                            category text, 
                                            name text,
                                            quantity integer);"""
        c.execute(sql)
    except Error as e:
        print(e)

def create_entry(conn, values):
    try:
        sql = '''INSERT INTO progress(category, name, quantity)
                VALUES(?,?,?)'''
        c = conn.cursor()
        c.execute(sql, values)
        conn.commit()
    except Error as e:
        print(e)
    return c.lastrowid

def update_entry(conn, values):
    try:
        sql = '''   UPDATE progress
                    SET quantity = ?
                    WHERE id = ?'''
        c = conn.cursor()
        c.execute(sql, values)
        conn.commit()
    except Error as e:
        print(e)

def delete_entry(conn, id):
    sql = 'DELETE FROM progress WHERE id = ?'
    c = conn.cursor()
    c.execute(sql, (id,))
    conn.commit()

def delete_all_entries(conn):
    sql = 'DELETE FROM progress'
    c = conn.cursor()
    c.execute(sql)
    conn.commit()

def select_all_entries(conn):
    c = conn.cursor()
    c.execute('SELECT * FROM progress')

    rows = c.fetchall()

    return rows
