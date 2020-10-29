
class User:
    '''Base User class'''

    def __init__(self, _id, _username, _password, firstname, middlename, lastname, email, tel, address):
        self.id = _id
        self.user = _username
        self.pwd = _password
        self.f_name = firstname
        self.m_name = middlename
        self.l_name = lastname
        self.email = email
        self.tel = tel
        self.address = address

    @property
    def get_user_id(self):
        return self.id

    def get_username(self):
        return self.user

    def get_password(self):
        return self.pwd

    @property
    def first_name(self):
        return self.f_name
    
    @property
    def middle_name(self):
        return self.m_name

    @property
    def last_name(self):
        return self.l_name

    @property
    def email(self):
        return self.email

    @property
    def phone(self):
        return self.tel

    @property
    def address(self):
        return self.address


class Student(User):
    '''Student class extended from User base class'''

    def __init__(self, enrolled, course, semester):
        self.enrolled = enrolled
        self.course = course
        self.semester = semester

    def student_id(self):
        return User.get_user_id

    def student_username(self):
        return User.get_username()

    def student_pwd(self):
        return User.get_password()

    @property
    def fullname(self):
        return f"{User.first_name} + ' ' + {User.middle_name} + ' ' + {User.last_name}"

    def email(self):
        return User.email

    @property
    def is_enrolled(self):
        return bool(self.enrolled)

    @property
    def course(self):
        return self.course

    @property
    def semester(self):
        return self.semester

    def phone(self):
        return User.phone
    
    def address(self):
        return User.address

    def __repr__(self):
        if self.enrolled == True:
            return f"Student: {self.fullname} is enrolled at {self.course}, on its {self.semester}."
        else:
            return f"Student: {self.fullname} is not enrolled in any of our courses."
