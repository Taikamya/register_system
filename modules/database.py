# _author = Dimitri Dias Moreira
# _version = 0.0.2_200 (Oct 26th, 2020)

'''
Em construção desde 21/10/2020
'''

import sqlite3


def connect():
    conn = sqlite3.connect("register.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS students 
                (id INTEGER PRIMARY KEY NOT NULL AUTOINCREMENT,
                name TEXT NOT NULL,
                course TEXT NOT NULL,
                enrolled INTEGER NOT NULL,
                semester INTEGER,
                telephone INTEGER,
                address TEXT)""")
    conn.commit()
    conn.close()


def view_all_students():
    conn = sqlite3.connect("register.db")
    c = conn.cursor()
    c.execute("SELECT * FROM students ORDER BY id")
    all_rows = c.fetchall()
    conn.close()
    return all_rows

def search_student_by_id(id=""):
    conn = sqlite3.connect("register.db")
    c = conn.cursor()
    c.execute("SELECT * FROM students WHERE id=?", (id,))
    all_rows = c.fetchone()
    conn.close()
    return all_rows

def search_student_by_name(name=""):
    conn = sqlite3.connect("register.db")
    c = conn.cursor()
    c.execute("SELECT * FROM students WHERE username=?", (name,))
    all_rows = c.fetchall()
    conn.close()
    return all_rows

def insert_student(name, course, enrolled, semester, telephone, address):
    conn = sqlite3.connect("register.db")
    c = conn.cursor()
    c.execute("INSERT INTO students VALUES (NULL, ?, ?, ?, ?, ?, ?)", (name, course, enrolled, semester, telephone, address,))
    conn.commit()
    conn.close()


def update_student(id, name, course, enrolled, semester, telephone, address):
    conn = sqlite3.connect("register.db")
    c = conn.cursor()
    c.execute("UPDATE students SET name=?, course=?, enrolled=?, semester=?, telephone=?, address=? WHERE id=?", (name, course, enrolled, semester, telephone, address, id,))
    conn.commit()
    conn.close()


def delete_student(id):
    conn = sqlite3.connect("register.db")
    c = conn.cursor()
    c.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    conn.close()


connect()
