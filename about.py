import sys
import os
import time
# import sqlite3

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
# from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtPrintSupport import *


"""
    Classe responsável por criar a janela de sobre.

    - def: __init__
        :param: self
        :param: *args
        :param: **kwargs
"""
class AboutDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)
        self.setWindowIcon(QIcon("icon/presentation.png"))
        
        # Set o tamanho da janela.
        self.setFixedWidth(600)
        self.setFixedHeight(500)

        # Aqui é gerado o botão de OK na janela.
        QBtn = QDialogButtonBox.Ok
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.rejected)

        layout = QVBoxLayout()

        # Janela do sobre.
        self.setWindowTitle("Sobre:")
        title = QLabel("Cadastro de alunos feito pela PyRate Enterprises")
        font = title.font()
        font.setPointSize(20)
        title.setFont(font)

        # Imagem que é apresentada na janela.
        labelpic = QLabel()
        pixmap = QPixmap("icon/developer.jpeg")
        pixmap = pixmap.scaledToWidth(300)
        labelpic.setPixmap(pixmap)
        labelpic.setFixedHeight(200)

        layout.addWidget(title)

        layout.addWidget(QLabel("Versão 1.0"))
        layout.addWidget(QLabel("Copyright © PyRate Enterprises 2020"))

        layout.addWidget(labelpic)

        layout.addWidget(self.buttonBox)
        self.setLayout(layout)
