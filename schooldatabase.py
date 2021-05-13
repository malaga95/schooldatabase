role = input("Z kim mam przyjemnosc ?\n")
roles = ('Wychowawca', 'Nauczyciel', 'Uczen','wychowawca', 'nauczyciel', 
        'uczen', 'koniec', 'Koniec')
przedmioty = {} #slownik czy lista???
klasy = [] #przechowuje klasy dla wychowawcy
#jeszcze jedna petla "poziom wyzej", ktora bedzie zapewniac dzialanie do wydrukowywania na podstawie podanego klucza
while role in roles:
    if role == 'wychowawca' or role == 'Wychowawca':
        klasa = input("Podaj numer klasy : \n")
        while klasa:   
            klasy.append(klasa)
            print(klasy)   
            break  
        #poprawic calkowite wyjscie z petli
    
    elif role == 'nauczyciel' or role == 'Nauczyciel':
        name = input("Podaj swoje imie i nazwisko : \n")
        przedmiot = input("jakiego przedmiotu nauczasz ?\n")
        if przedmiot:
            klasa = input("Podaj numer klasy :\n")
            while klasa:
                klasy.append(klasa)
    
    elif role == 'uczen' or role == 'Uczen':
        klasa = input("Do jakiej klasy chodzisz ? \n")
    
        

#uczen kklasy nauczycuel wychowawca, uczen - przypisac atrybuty (przedmiot, klasa, imie nazwisko), metoda zwracac porzadane wlasciwosci
'''Struktura przechowywawnia danych !!
    Uczen chodzi do klasy
    Nauczyciel Uczy przedmiotow poszczegolne klasy
    Wychowawca zajmuje sie klasami
    Czyli 
    Nauczyciel bedzie mial przedmiot który bedzie lista zawierajaca klasy
    Wychowawca liste zawierajaca klasy 
    uczen klasa
    '''



    class Period():
        def __init__(self, name, klasa):
            self.name = name
            self.klasa = klasa

        def przypisanie(self):
            name = input("Podaj nazwisko\n")
