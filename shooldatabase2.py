class Tutor: #Nauczyciel ma przedmioty oraz klasy ktore uczeszczaja na dany przedmiot.
             #{Tadeusz nowak : {biologia: [2a,2b]} 
             # Amadeusz Powrot :{chemia: [2a, 2b]}}
    def __init__(self, name, subject, group):
        self.name = name
        self.subject = subject
        self.group = group
    def data(self):
        #Dictonary that contains data of tutor
        data = {}
        subject = {}
        classes = []
        classes.append(group)
        new_dict = {self.subject : classes}
        data = {self.name : new_dict}
        return data


class Student:
    #Struktura danych 
        #{Andrzej nowak : 3c
        # Marcin niebrzydki :3a
        # }
    def __init__(self, name, group):
        self.name = name
        self.group = group
   
    def data(self):
        data={}
        data = {self.name : self.group}
        return data
    '''def klasa_przypis(self):
        if group in students_in_class:
            students.append(name)
            students_in_class[group] = students
        else:
            students = []
            students.append(name)
            students_in_class[group] = students
        return students_in_class'''

class Keeper:
    #Struktura
    #{Tadeusz Nowak :[]
    # Amadeusz Pi :[]}
    def __init__(self, name, group):
        self.name = name
        self.group = group
    def data(self):
        data={}
        klasy=[]
        data[self.name] = [self.group]
        return data
#w jaki sposob zapisywac wprowadzone dane w "kodzie"
#w jaki sposob wyciagac dane ? np drukowac klasy uczniow
#tworzyc nowa strukture po wykonaniu intrukcji


students_in_class = {}   #{3a:[tadek,andrzej,mateusz]}
students = []
keepers = []
subjects = []
probing = {}
roles = ('Wychowawca', 'Nauczyciel', 'Uczen','wychowawca', 'nauczyciel', 
    'uczen', 'koniec', 'Koniec')   
while True:
    role = input('kim jestes ?')
    if role == "Nauczyciel" or role == 'nauczyciel':
        name = input('Podaj swoje imie i nazwisko :\n')
        subject = input('jakiego przedmiotu nauczasz ?\n')
        group = input('jakiej klasy uczysz tego przedmiotu? \n')
        personal_data = Tutor(name, subject, group)
        print_data = personal_data.data()
        print(print_data)

        '''sample_dict[students_group] = subject
        tutors[name] = sample_dict'''
        
    if role == "Uczen" or role == 'uczen':
        name = input('Podaj swoje imie i nazwisko :\n')
        group = input('Podaj numer swojej klasy\n')
        personal_data = Student(name, group) #wywoluje klase
        print_data = personal_data.data() #wykonuje metode na obiekcie
        '''klasa = personal_data.klasa_przypis()'''
        if group in students_in_class: #nie dziala mi w metodzie, prawdopodobnie z powodu pustego atrybutu
            students.append(name)
            students_in_class[group] = students
        else:
            students = []
            students.append(name)
            students_in_class[group] = students
        #students_in_class = {group: students}
        print(students_in_class)
        #klasa1 = personal_data.klasa_przypis()
        
         #dodaje studentow do listy w klasie
        #lista studentów potrzebny if
    if role == "Wychowawca" or role == 'wychowawca':
        name = input('Podaj swoje imie i nazwisko :\n')
        group = input('Podaj numer klasy, ktorej jestes opiekunem\n')
        personal_data = Keeper(name, group)
        print_data = personal_data.data()
        print(print_data)

