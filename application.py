#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *

from about import AboutDialog
from insert import InsertDialog
from login import LoginForm
from search import SearchDialog
from delete import DeleteDialog
from db import ConnectionDB

"""
    Classe responsável por criar a janela principal.

    - def: __init__
        :param: self
        :param: *args
        :param: **kwargs
    - def: about
        :param: self
"""
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowIcon(QIcon("icon/book.png"))

        # Botões da barra de ferramentas.
        # file_menu = self.menuBar().addMenu("&Arquivo")
        lang_menu = self.menuBar().addMenu("&Idioma")
        help_menu = self.menuBar().addMenu("&Ajuda")
        self.setWindowTitle("Cadastro de alunos")
        # Tamanho default da janela.
        self.setMinimumSize(800,600)

        # Criação da tabela com as informações a serem cadastradas.
        self.tableWidget = QTableWidget()
        self.setCentralWidget(self.tableWidget)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.tableWidget.setHorizontalHeaderLabels(("Inscrição nº", "Nome", "E-Mail", "Curso", "Semestre", "Telefone", "Endereço"))

        # Inclusão de botões.
        toolbar = QToolBar()
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        ###################
        #   Status bar.   #
        ###################

        status_bar = QStatusBar()
        self.setStatusBar(status_bar)

        ###################################
        #   Botões na barra de tarefas.  #
        ###################################

        # Botão de login de usuário.
        btn_ac_loginUser = QAction(QIcon("icon/login.png"), "Login", self)
        btn_ac_loginUser.triggered.connect(self.login)
        btn_ac_loginUser.setStatusTip("Login")
        toolbar.addAction(btn_ac_loginUser)

        # Botão de adicionar usuário.
        btn_ac_addUser = QAction(QIcon("icon/add1.png"), "Adicionar Aluno", self)
        btn_ac_addUser.triggered.connect(self.insert)
        btn_ac_addUser.setStatusTip("Add Aluno")
        toolbar.addAction(btn_ac_addUser)

        # Botão de atualizar usuário.
        btn_ac_refresh = QAction(QIcon("icon/refresh.png"), "Atualizar Aluno", self)
        btn_ac_refresh.setStatusTip("Atualizar Aluno")
        toolbar.addAction(btn_ac_refresh)

        # Botão de pesquisar usuário.
        btn_ac_search = QAction(QIcon("icon/search.png"), "Pesquisar Aluno", self)
        # ToDo: testar o sqlite3 na minha própria máquina, pois nessa aqui não está a funcionar.
        # btn_ac_search.triggered.connect(ConnectionDB().select_one_student(number))
        btn_ac_search.triggered.connect(self.search)
        btn_ac_search.setStatusTip("Pesquisar Aluno")
        toolbar.addAction(btn_ac_search)

        # Botão de deletar usuário.
        btn_ac_delete = QAction(QIcon("icon/delete.png"), "Deletar Aluno", self)
        btn_ac_delete.triggered.connect(self.delete)
        btn_ac_delete.setStatusTip("Deletar Aluno")
        toolbar.addAction(btn_ac_delete)

        # Botão de fechar.
        btn_ac_quit = QAction(QIcon("icon/exit.png"), "Sair", self)
        btn_ac_quit.triggered.connect(self.quit)
        btn_ac_quit.setStatusTip("Fechar Programa")
        toolbar.addAction(btn_ac_quit)

        # Botão sobre o desenvolvedor.
        about_action = QAction(QIcon("icon/data.png"), "Desenvolvedor", self)
        about_action.triggered.connect(self.about)
        help_menu.addAction(about_action)

        # Botão para seleção de idioma. PT
        lang_action_pt = QAction(QIcon("icon/portugal.png"), "Portugués", self)
        lang_action_pt.triggered.connect(self.language)
        lang_menu.addAction(lang_action_pt)

        # Botão para seleção de idioma. ES
        lang_action_es = QAction(QIcon("icon/spain.png"), "Español", self)
        lang_action_es.triggered.connect(self.language)
        lang_menu.addAction(lang_action_es)

        # Botão para seleção de idioma. US
        lang_action_us = QAction(QIcon("icon/us-america.png"), "English", self)
        lang_action_us.triggered.connect(self.language)
        lang_menu.addAction(lang_action_us)

    def login(self):
        dlg = LoginForm()
        dlg.exec_()

    def connection(self):
        dlg = ConnectionDB()
        dlg.exec_()

    def insert(self):
        dlg = InsertDialog()
        dlg.exec_()
    
    def search(self):
        dlg = SearchDialog() # .search_student()
        dlg.exec_()

    def delete(self):
        dlg = DeleteDialog() # .delete_student()
        dlg.exec_()
    
    def language(self):
        pass

    def about(self):
        dlg = AboutDialog()
        dlg.exec_()

    def quit(self):
        return sys.exit()
        