import sys
import os
import time

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
# from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtPrintSupport import *


"""
    Classe responsável por criar a janela de pesquisa.

    - def: __init__
        :param: self
        :param: *args
        :param: **kwargs
    - def: delete_student
        :param: self
"""
class DeleteDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(DeleteDialog, self).__init__(*args, **kwargs)
        self.setWindowIcon(QIcon("icon/note.png"))
        
        # Botão deletar.
        self.QBtn = QPushButton()
        self.QBtn.setText("Deletar")

        # Janela do pesquisar.
        self.setWindowTitle("Deletar registro")
        self.setFixedWidth(300)
        self.setFixedHeight(100)

        # Botão de clique.
        self.QBtn.clicked.connect(self.delete_student)

        # Cria o layout.
        layout = QVBoxLayout()

        # Layout do local de texto para pesquisar e validar o nº de inscrição.
        label_delete = QLabel('<font size="4"> Nº Inscrição </font>')
        self.deleteInput = QLineEdit()
        self.onlyInt = QIntValidator()
        self.deleteInput.setValidator(self.onlyInt)
        self.deleteInput.setPlaceholderText("Nº Inscrição")
        layout.addWidget(label_delete)
        layout.addWidget(self.deleteInput)

        # Botão validador
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def delete_student(self):
        delete_row = ""
        delete_row = self.deleteInput.text()
        # ConnectionDB().delete_one_student(delete_row)
