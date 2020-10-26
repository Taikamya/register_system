from ..modules.database import *
from WTForms import Form, StringField, IntegerField


class User(Form):
    # name = StringField
    # telephone = StringField # converter Integer to String
    # address = StringField
    pass


class Student(User):
    # name = User.name
    # enrolled = IntegerField
    # course = IntegerField  # usando de 1 até X para identificar as matérias. Exemplo: 1 = Português, etc
    # semester = IntegerField
    # telephone = User.telephone
    # address = User.address
    pass
