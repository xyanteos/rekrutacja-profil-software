#!/usr/bin/python3.7
import random
#Ponizej class-a do tworzenia obiektow i jej funkcje \/
class Slowo(object):
    def __init__(self):
        self.ID = ID
    def przeczytaj(plik):
        listaP = []
        for linijka in open(plik,'r'):
            listaP.append(linijka)
        for i in range(len(listaP)):
                listaP[i] = listaP[i].strip("\n")
                if listaP[i].isupper == False:
                    listaP[i].isupper()
        for i in range(len(listaP)):
                listaP[i] = listaP[i].upper()

        return listaP
    def podliczPunkty(slowo):
            wartosc = 0
            SCRABBLES_SCORES = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                        (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]

            LETTER_SCORES = {letter: score for score, letters in SCRABBLES_SCORES
                     for letter in letters.split()}
            lista = list(slowo)
            for i in range(len(slowo)):
                lista[i] = lista[i].upper()
            #print ('Podane slowo w liscie : ')
            #print(''.join(lista))
            for i in range(len(slowo)):
                    wartosc += LETTER_SCORES[lista[i]]
            return wartosc
    def wyswietlMax(sciezkaPliku):
        slowa = Slowo
        print ('slowa z dictionary.txt: ' + str(slowa.przeczytaj('dictionary.txt')))
        listaSlow = slowa.przeczytaj('dictionary.txt')
        dlugosc = len(listaSlow)
        maximum = 0
        for i in range(dlugosc):
            Punkty = slowa.podliczPunkty(listaSlow[i])
            #print('punkty ze slowa : ' + str(Punkty))
            if Punkty > maximum :
                maximum = Punkty
        print('\n\nmax pkt wszystkich slow : ' + str(maximum) + '\n\n')
    def losujSlowo(lista):
        liczba=input('Podaj liczbe punktow jakiej mam szukac w pliku dictionary.txt : ')
        try:
            liczba = int(liczba)
        except Exception as mhh:
            print(mhh)
        wyniki = []
        iloscLiczb=0
        for i in range(len(lista)):
            if pliczek.podliczPunkty(lista[i])==liczba:
                iloscLiczb+=1
                wyniki.append(lista[i])
        if iloscLiczb>=1:
            print ('program znalazl {0} slow/o/a z wynikiem {1}\n'.format(iloscLiczb,liczba))
            for i in range(len(wyniki)):
                print('program znalazl {0} '.format(wyniki[i]))
            randomowa = random.randint(0,iloscLiczb-1)
            print('wylosowane slowo : {0} : {1}\n\n\n'.format(randomowa,wyniki[randomowa]))
        else:
            print()



#dictionary.txt

#do dzialania programu if-elif-else w petli while:
while(True):
    k = input('Witam, jaka akcje chcesz wykonac? \n 1.Podaj max wartosc z pliku dictionary.txt\n 2.Wprowadz wlasne slowo do oceny punktow\n 3.Pokaz slowo z pliku zawierajace dana ilosc punktow lub wylosuj jedno jesli jest ich wiecej\n 0.Wyjdz z programu.')
    #if k is not int:
    #    print('zla wartosc! Przyjmuję jedynie liczby.\n')
    try:
        k = int(k)
    except Exception as e:
        print(e)
    if k==1:
        pliczek = Slowo
        pliczek.wyswietlMax('dictionary.txt')
    elif k==2:
        slowo = input('Podaj slowo do oceny ilosci punktow (moze byc z duzych lub malych liter): ')
        if slowo.isalpha():
            slowko = Slowo
            slowo = str(slowo)
            print(slowko.podliczPunkty(slowo))
        else:
            print('SLOWO... miales wpisac slowo.')

    elif k==3:
        pliczek = Slowo
        lista = pliczek.przeczytaj('dictionary.txt')
        pliczek.losujSlowo(lista)            
    elif k==0:
        exit()
    else:
        print('Nie rozumiem.')




