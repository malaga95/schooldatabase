role = input("Z kim mam przyjemnosc ?\n")
roles = ('Wychowawca', 'Nauczyciel', 'Uczen','wychowawca', 'nauczyciel', 
        'uczen', 'koniec', 'Koniec')
przedmioty = {}
klasy = [] #przechowuje klasy dla wychowawcy
while role:
    
    if role == 'wychowawca' or 'Wychowawca':
        klasa = input("Podaj numer klasy : \n")
        while klasa:   
            klasy.append(klasa)
            print(klasy)   
            break  
        else:  
            break  
        break #poprawic calkowite wyjscie z petli
    
    if role == 'nauczyciel' or 'Nauczyciel':
        name = input("Podaj swoje imie i nazwisko : \n")
        przedmiot = input("jakiego przedmiotu nauczasz ?\n")
        if przedmiot:
            klasa = input("Podaj numer klasy :\n")
            while klasa:
                klasy.append(klasa)
    
    if role == 'uczen' or 'Uczen':
        klasa = input("Do jakiej klasy chodzisz ? \n")
        
        



'''Struktura przechowywawnia danych !!
    Uczen chodzi do klasy
    Nauczyciel Uczy przedmiotow poszczegolne klasy
    Wychowawca zajmuje sie klasami
    Czyli 
    Nauczyciel bedzie mial przedmiot który bedzie lista zawierajaca klasy
    Wychowawca liste zawierajaca klasy 
    uczen klasa
    '''