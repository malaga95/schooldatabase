from os import name


class School:
    
    def __init__(self):
        self.keeper = keeper
        self.students = {}
        self.klasa = []

    def data(self):
        group_of_students.append(students)
        return group_of_students

    def add_student(self, student):
        if student.class_no not in self.students:
            self.students[student.class_no] = []
        self.students[student.class_no].append(student)
    



class Tutor:
   
    def __init__(self):
       self.name = ''
       self.subject = ''
       self.classes = []
    
    def data(self):
       subjects = {self.subject : self.classes}
       teacher = {self.name : subjects}   
       return teacher
    
    def read(self):
       self.name = input('Type your name')
       self.subject = input('type your subject')
       class_= input('type your class')
       while class_:
           self.classes.append(class_)
           class_= input('type your class')


class Keeper:
    def __init__(self):
        self.name = ''
        self.classes = []
    
    def data(self): 
        keeper = {self.name : self.classes}
        return keeper
    
    def read(self):
        self.name = input('Type your name')
        class_= input('type your class')
        while class_:
            self.classes.append(class_)
            class_= input('type your class')


class Student:
    def __init__(self, school):
        self.name = ''
        self.class_no = ''
        self.school = school

    def read(self):
        self.name = input('Type your name')
        self.class_no = input('type your class')
        self.school.add_student(self)


    def data(self): 
        list_of_class.append(self.class_no)
        return list_of_class
        
klasa = []
list_of_class_per_subject = []
subjects = {} #subjects to create data for teacher
students = [] # Spare
list_of_class = []     # list of all classes            # wszystkie te zmienne wrzucic do School !!
group_of_students = [] # students in a class
teacher = {}          # {Name : {Subject : [classes]}}  
keeper = {}           # {name : [list_of class]}
list_of_students = {} # {2a : [students_in_class]}
roles = ('Wychowawca', 'wychowawca', 'Nauczyciel', 'nauczyciel', 'uczen', 'Uczen', 'koniec', 'Koniec')
school = School()
while True:
    role = input('Who are You ?')
   
    if role == "uczen" or role == "Uczen": #I'm getting data from student so i want to put his information into my list of interests
        person_data = Student(school)
        person_data.read()
        person_processing = person_data.data()
        print(school.students)
   
    if role == "Wychowawca" or role == "wychowawca":
        person_data = Keeper()
        person_data.read()
        person_processing = person_data.data()
        print(person_processing)
    
    if role == "Nauczyciel" or role == "nauczyciel":
        tutor_data = Tutor()
        tutor_data.read()
        tutor_processing = tutor_data.data()
        print(tutor_processing)