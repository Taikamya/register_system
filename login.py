import sys
import os
import time

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
# from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtPrintSupport import *

""""
    Aqui é criada a tela de login.
"""

"""
    Classe responsável por criar a janela de login.

    - def: __init__
        :param: self
        :param: *args
        :param: **kwargs
    - def: check_password
        :param: self
"""
class LoginForm(QDialog):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.setWindowIcon(QIcon("icon/login_icon.png"))

        # Botão deletar.
        self.QBtn = QPushButton()
        self.QBtn.setText("Login")

        # Janela de login
        self.setWindowTitle("Login")
        self.setFixedSize(300, 200)

        # Conexão.
        self.QBtn.clicked.connect(self.check_password)

        # Cria o grid do login.
        layout = QVBoxLayout()

        # Local onde se coloca o usuário.
        label_name = QLabel('<font size="4"> Usuário </font>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText("Digite seu nome de usuário")
        self.lineEdit_username.setMaxLength(20) # Limite máximo de 30 chars para o nome de usuário
        layout.addWidget(label_name)
        layout.addWidget(self.lineEdit_username)

        # Layout para password.
        label_password = QLabel('<font size="4"> Senha </font>')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setMaxLength(20) # Limite máximo de 20 chars para a senha
        self.lineEdit_password.setEchoMode(3) # EchoMode configurado para modo "PasswordOnEchoEdit" (esconde a senha após a digitação) 
        self.lineEdit_password.setPlaceholderText("Digite sua palavra-passe")
        layout.addWidget(label_password)
        layout.addWidget(self.lineEdit_password)

        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def check_password(self):
        msg = QMessageBox()
        
        # Tem que tirar esse usuário hardcoded e cadastrar e puxar de um DB!!
        if self.lineEdit_username.text() == "Username" and self.lineEdit_password.text() == "000":
            msg.setWindowIcon(QIcon("icon/done.png"))
            msg.setWindowTitle("Efetuado")
            msg.setText("Sucesso")
            msg.exec_()
        else:
            msg.setWindowIcon(QIcon("icon/failure.png"))
            msg.setWindowTitle("Não efetuado")
            msg.setText("Palavra-passe incorreta")
            msg.exec_()
