from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *


"""
    Classe responsável por criar a janela de registro.

    - def: __init__
        :param: self
        :param: *args
        :param: **kwargs
    - def: add_student
        :param: self
"""
class InsertDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(InsertDialog, self).__init__(*args, **kwargs)
        self.setWindowIcon(QIcon("icon/note.png"))
        
        # Botão registrar.
        self.QBtn = QPushButton()
        self.QBtn.setText("Registrar")

        # Formulário.
        self.setWindowTitle("Dados do aluno")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        # Conexão.
        self.QBtn.clicked.connect(self.add_student)

        # Cria o layout.
        layout = QVBoxLayout()

        # Caixa de texto do nome.
        label_first_name = QLabel('<font size="4"> Nome </font>')
        self.first_nameInput = QLineEdit()
        self.first_nameInput.setPlaceholderText("Nome")
        layout.addWidget(label_first_name)
        layout.addWidget(self.first_nameInput)

        # Caixa de texto do nome do meio.
        label_middle_name = QLabel('<font size="4"> Nome do Meio </font>')
        self.middle_nameInput = QLineEdit()
        self.middle_nameInput.setPlaceholderText("Nome do Meio")
        layout.addWidget(label_middle_name)
        layout.addWidget(self.middle_nameInput)

        # Caixa de texto do apelido.
        label_last_name = QLabel('<font size="4"> Apelido </font>')
        self.last_nameInput = QLineEdit()
        self.last_nameInput.setPlaceholderText("Apelido")
        layout.addWidget(label_last_name)
        layout.addWidget(self.last_nameInput)

        # Caixa de texto para o email.
        label_email = QLabel('<font size="4"> E-Mail </font>')
        self.emailInput = QLineEdit()
        self.emailInput.setPlaceholderText("E-Mail")
        layout.addWidget(label_email)
        layout.addWidget(self.emailInput)

        # Caixa de texto para o email.
        # label_enrolled = QLabel('<font size="4"> Matriculado </font>')
        self.enrolled = QCheckBox(text="Matriculado")
        self.enrolled.setTristate(False)
        # layout.addWidget(label_enrolled)
        layout.addWidget(self.enrolled)

        # Combo Box.
        label_course = QLabel('<font size="4"> Curso </font>')
        self.courseInput = QComboBox()
        self.courseInput.addItem("Português")
        self.courseInput.addItem("Inglês")
        self.courseInput.addItem("Matemática")
        self.courseInput.addItem("Física")
        self.courseInput.addItem("Química")
        self.courseInput.addItem("Ed. Física")
        self.courseInput.addItem("Biologia")
        self.courseInput.addItem("História")
        self.courseInput.addItem("Geografia")
        layout.addWidget(label_course)
        layout.addWidget(self.courseInput)

        # Selecionar no combo box.
        label_sem = QLabel('<font size="4"> Semestre </font>')
        self.semInput = QComboBox()
        self.semInput.addItem("1")
        self.semInput.addItem("2")
        self.semInput.addItem("3")
        self.semInput.addItem("4")
        self.semInput.addItem("5")
        self.semInput.addItem("6")
        self.semInput.addItem("7")
        self.semInput.addItem("8")
        self.semInput.addItem("9")
        layout.addWidget(label_sem)
        layout.addWidget(self.semInput)

        # Layout do local de texto para telefone.
        label_tel = QLabel('<font size="4"> Telefone </font>')
        self.telInput = QLineEdit()
        self.telInput.setPlaceholderText("Nº Telefone")
        layout.addWidget(label_tel)
        layout.addWidget(self.telInput)

        # Layout do local de texto para endereço.
        label_address = QLabel('<font size="4"> Endereço </font>')
        self.addressInput = QLineEdit()
        self.addressInput.setPlaceholderText("Endereço")
        layout.addWidget(label_address)
        layout.addWidget(self.addressInput)

        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def add_student(self):
        first_name = ""
        middle_name = ""
        last_name = ""
        email = ""
        is_enrolled = False
        course = ""
        semester = -1
        tel = ""
        address = ""

        first_name = self.first_nameInput.text()
        middle_name = self.middle_nameInput.text()
        last_name = self.last_nameInput.text()
        email = self.emailInput.text()
        course = self.courseInput.itemText(self.courseInput.currentIndex())
        semester = self.semInput.itemText(self.semInput.currentIndex())
        tel = self.telInput.text()
        address = self.addressInput.text()

        if self.enrolled.isTristate() == False:
            return self.enrolled.setCheckState(0)
        else:
            return self.enrolled.setCheckState(2)
