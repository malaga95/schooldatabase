

class School:
    
    def __init__(self):
        self.keeper = {}
        self.students = {}
        self.klasa = []
        self.tutor = {}

    def data(self):
        group_of_students.append(students)
        return group_of_students

    def add_student(self, student):
        if student.class_no not in self.students:
            self.students[student.class_no] = []
        self.students[student.class_no].append(student)
    
    def tutor_processing(self, tutor):
        if tutor.name not in self.tutor:
            self.tutor[tutor.name] = self.subjects
        else:
            self.tutor.update(self.subjects)


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

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.name}'

class Keeper:
    def __init__(self, school):
        self.name = ''
        self.classes = []
        self.school = school
    
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
    
    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.name}'
        
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
        person_data = Keeper(school)
        person_data.read()
        person_processing = person_data.data()
        print(school.keeper) #
    
    if role == "Nauczyciel" or role == "nauczyciel":
        tutor_data = Tutor()
        tutor_data.read()
        tutor_processing = tutor_data.data()
        #school.tutor_processing()
        print(school.tutor_processing) 
    if role == 'stop':
        break

while True:
    var = input('Type name')   #wpisuje klucz na podstawie ktorego przeszukuje dane
    if var in school.students: #sprawdzam slownik studentow w szkole
        print(school.students[var])  #drukuje wartosc slownika dla klucza wpisanego
    if var in school.keeper:
        print(school.keeper[var])
    else:
        print('nie ma takiego wpisu')
    print(school.students)  #drukuje caly slownik students
    for group,student_list in school.students.items():  #przeszukuje 
        print(group, student_list)
        for student in student_list:      #student w tym miejscu prezentuje kazda kolejna wartosc w petli for, nazywam ja w instrukcji
            if var == student.name:
                print(group)
    