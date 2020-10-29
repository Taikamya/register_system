# _author = Dimitri Dias Moreira
# _version = 0.0.2_500 (Oct 29th, 2020)

''' Atualizado em 29/10/2020 '''

from models.model import Student
import sqlite3

conn = sqlite3.connect("register.db")
c = conn.cursor()

def connect_to_DB():
    """Conecta a um determinado banco de dados"""
    
    with conn:
        c.execute("""CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY NOT NULL AUTOINCREMENT,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL,
                    firstname TEXT NOT NULL,
                    middlename TEXT,
                    lastname TEXT NOT NULL,
                    email TEXT NOT NULL,
                    enrolled INTEGER NOT NULL,
                    course TEXT NOT NULL,
                    semester INTEGER,
                    tel INTEGER,
                    address TEXT
                    )""")
        conn.commit()


def view_all_students():
    with conn:
        c.execute("SELECT * FROM students ORDER BY id")
        return c.fetchall()

def search_student_by_id(id=""):
    with conn:
        c.execute("SELECT FROM students WHERE id=?", (id,))
        return c.fetchone()

def search_student_by_firstname(firstname=Student.fullname[0]):
    with conn:
        c.execute("SELECT * FROM students WHERE firstname=?", (firstname,))
        return c.fetchall()

def search_student_by_lastname(lastname=Student.fullname[2]):
    with conn:
        c.execute("SELECT * FROM students WHERE lastname=?", (lastname,))
        return c.fetchall()

def insert_student(firstname=Student.fullname[0], middlename=Student.fullname[1], lastname=Student.fullname[2],
                    email=Student.email, enrolled=Student.is_enrolled, course=Student.course, semester=Student.semester,
                    tel=Student.phone, address=Student.address):
    with conn:
        c.execute("INSERT INTO students VALUES (id, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (firstname, middlename, lastname, email, enrolled, course, semester, tel, address,))
        conn.commit()

def update_student(id, firstname, middlename, lastname, email, course, enrolled, semester, tel, address):
    with conn:
        c.execute("UPDATE students SET firstname=?, middlename=?, lastname=?, email=?, course=?, enrolled=?, semester=?, phone=?, address=? WHERE id=?", (firstname, middlename, lastname, email, course, enrolled, semester, tel, address, id,))
        conn.commit()

def delete_student(id):
    with conn:
        c.execute("DELETE FROM students WHERE id=?", (id,))
        conn.commit()


conn.close()
