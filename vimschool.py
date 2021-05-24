

from os import name


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
        self.tutor.update(tutor)
        #if tutor.name not in self.tutor:

        #    self.tutor[tutor.name] = self.subjects
        #else:
        #    self.tutor.update(self.subjects)
    def keeper_proc(self, keeper):
        self.keeper.update(keeper)


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
        school.keeper_proc(person_processing)
        print(school.keeper) #
    
    if role == "Nauczyciel" or role == "nauczyciel":
        tutor_data = Tutor()
        tutor_data.read()
        tutor_proc = tutor_data.data()
        school.tutor_processing(tutor_proc)
        print(school.tutor) 
    if role == 'stop':
        break

while True:
    var = input('Type name')   #wpisuje klucz na podstawie ktorego przeszukuje dane
    #if var in school.students: #sprawdzam slownik studentow w szkole
    #    print(school.students[var])  #drukuje wartosc slownika dla klucza wpisanego
        #przyrownaj aby wyszukac wychowawce
    if var in school.keeper:
        print(school.keeper[var])
    
    else:
        print('nie ma takiego wpisu')
    for group,student_list in school.students.items():  #przeszukuje 
        for student in student_list:      #student w tym miejscu prezentuje kazda kolejna wartosc w petli for, nazywam ja w instrukcji
            if var == student:
                for keeper,grupa in school.keeper.items():
                    if group == grupa:
                        print(keeper)
                print(list_of_students[var])
    #for keeper,group in school.keeper.items():
    #    for klasa in group:
    #        if var == klasa.name:
    #            print(klasa)
    if var in school.tutor.keys():
        for v,classes in school.tutor[var].items():
            for grupa in classes:
                for name,klasy in school.keeper.items():
                    for klasa in klasy:
                        if klasa == grupa:
                            print(name)
    #jeśli phrase to uczeń: wypisz wszystkie lekcje, które ma uczeń i nauczycieli, którzy je prowadzą
    for group, student in school.students.items(): #przeszukuje liste studentów
        if var in group:
            print(group) #nazwa klasy do ktorej uczeszcza student
        for name in student:
            if var == name:
                for name,grupa in school.keeper.items():
                    for var in grupa:
                        print(name) #tutaj powinienem wydrukowac imie wychowawcy dla klasy ?
        for v,subjects in school.tutor.items(): #dziele sobie slownik na v - imie nauczyciela, subjects - slowniki z przedmiotami 
            print(v,subjects)
            for sub,grupa in subjects: 
                if var in grupa:
                    print(subjects) #tutaj powinien drukowac liste przedmiotow
        
   # for a,b
   #  {name : [list_of class]}
    #{Name : {Subject : [classes]}}
    