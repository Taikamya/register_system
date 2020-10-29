import sqlite3
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *
from insert import InsertDialog

"""
    Classe responsável por criar o banco de dados.

    - def: __init__
        :param: self
        :param: *args
        :param: **kwargs
    - def: load_one_student
        :param: self
    - def: select_one_student
        :param: self
    - def: delete_one_student
        :param: self
"""
class ConnectionDB():
    def __init__(self, *args, **kwargs):
        super(ConnectionDB, self).__init__(*args, **kwargs)
        # Realiza a conexão do banco de dados.
        self.conn = sqlite3.connect("register.db")
        self.db_cursor = self.conn.cursor()

        # row -> id // Primary Key, name, course and enrolled -> NOT NULL // Added "enrolled" option // Dimitri Dias Moerira (Taikamya)
        self.db_cursor.execute('''CREATE TABLE IF NOT EXISTS students 
                                    (id INTEGER PRIMARY KEY NOT NULL AUTOINCREMENT,
                                    name TEXT NOT NULL,
                                    course TEXT NOT NULL,
                                    enrolled INTEGER NOT NULL,
                                    semester INTEGER,
                                    telephone INTEGER,
                                    address TEXT)''')
        # self.db_cursor.close() --> Não pode fechar o cursor
        # self.conn.close() --> Não pode fechar o DB

    # Função responsável por manter o painel com os dados atualizados do sistema.
    def load_one_student(self, id):
        result = self.db_cursor.execute('''SELECT * FROM students''')
        self.db_cursor.rowcount(0) # -- Também dá erro, mas deixa funcionar até certo momento.
        # self.tableWidget.setRowCount(0)  --> Isso tinha que estar aqui mesmo? Dá erro.
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        self.db_cursor.close()
        self.conn.close()

    # Função responsável por realizar a pesquisa no sistema.
    def select_one_student(self, id):
        try:
            result = self.db_cursor.execute("SELECT * FROM students WHERE row =?", id) # Consertada sintaxe // Não pode transformar em str o que é validado como int
            row = result.fetchone()
            search_result = "Nº INSCRIÇÃO: " + str(row[0]) + "\n" + "NOME: " + str(row[1]) + "\n" + "CURSO: " + str(row[2]) + "\n" + "SEMESTRE: " + str(row[3]) + "\n" + "TELEFONE" + str(row[4]) + "\n" + "ENDEREÇO" + str(row[5])
            QMessageBox.information(QMessageBox(), "Pesquisa realizada com sucesso", search_result)
            self.conn.commit()
            self.db_cursor.close()
            self.conn.close()
        except Exception as err:
            QMessageBox.warning(QMessageBox(), "Aluno não encontrado", "Contacte o administrador do sistema.")

    # Função responsável por deletar a informação do sistema.
    def delete_one_student(self, id):
        try:
            result = self.db_cursor.execute("DELETE FROM students WHERE row =?", id) # Consertada sintaxe // Não pode transformar em str o que é validado como int
            self.conn.commit()
            self.db_cursor.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(), "Deletado com sucesso", "Tudo ok")
            self.close()

        except Exception as err:
            QMessageBox.warning(QMessageBox(), "Aluno não encontrado", "Contacte o administrador do sistema.")

            