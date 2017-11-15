# -*- coding: utf-8 -*-

from classes.skladniki import skladnik, dodatek, sos, salatka, bcolors
import json


#inicjalizacja pustych list do listowania skladnikow i wynikowej salatki ===============================================
dict_bazy = []
dict_dodatki = []
dict_bialko = []
dict_sosy = []

bazy = []
dodatki = []
sosy = []
bialko = []
smaki = set()

Salatka = salatka(0, 0, 0, 0, 0, [], [])


#Dwie funkcje bo warzywa maja inny konstruktor niz reszta skladnikow ===================================================
def dodajItem(grupa, index):
    global Salatka
    return Salatka.addItem(grupa[index].getProt(), grupa[index].getFat(), grupa[index].getCarb(), \
                           grupa[index].getMasa(),grupa[index].getKcal(), grupa[index].getName())


def dodajWarzywo(grupa, index):
    global Salatka
    return Salatka.addWarzywo(grupa[index].getProt(), grupa[index].getFat(), grupa[index].getCarb(), \
                           grupa[index].getMasa(),grupa[index].getKcal(), grupa[index].getName(), grupa[index].getCecha())


def uzyto(grupa, index):
    global Salatka
    grupa[index].wasUsed()



# Typy: baza, mieso, warzywo, sos

#Ladowanie plikow ze skladnikami i konwersja na obiekty ================================================================
try:
    plik = open("./bazy.json", "r")
    dict_bazy = json.loads(plik.read())
    plik.close()
except:
    print("Blad ladowania pliku ze skladnikami bazowymi!")
    print("Sprawdz czy plik istnieje i ma poprawna skladnie")
else:
    for i in dict_bazy:
         if i['typ'] == "baza":
             obiekt = skladnik(i['nazwa'], i['protein'], i['fat'], i['carb'], i['masa'], i['kcal'], i['typ'])
             bazy.append(obiekt)

try:
    plik = open("./bialko.json", "r")
    dict_bialko = json.loads(plik.read())
    plik.close()
except:
    print("Blad ladowania pliku ze skladnikami bialkowymi!")
    print("Sprawdz czy plik istnieje i ma poprawna skladnie")
else:
    for i in dict_bialko:
        if i['typ'] == "bialko":
            obiekt = skladnik(i['nazwa'], i['protein'], i['fat'], i['carb'], i['masa'], i['kcal'], i['typ'])
            bialko.append(obiekt)

try:
    plik = open("./dodatki.json", "r")
    dict_dodatki = json.loads(plik.read())
    plik.close()
except:
    print("Blad ladowania pliku z dodatkami warzywnymi!")
    print("Sprawdz czy plik istnieje i ma poprawna skladnie")
else:
    for i in dict_dodatki:
        if i['typ'] == "dodatek":
            obiekt = dodatek(i['nazwa'], i['protein'], i['fat'], i['carb'], i['masa'], i['kcal'], i['typ'], i['cecha'])
            dodatki.append(obiekt)

try:
    plik = open("./sosy.json", "r")
    dict_sosy = json.loads(plik.read())
    plik.close()
except:
    print("Blad ladowania pliku ze skladnikami sosow!")
    print("Sprawdz czy plik istnieje i ma poprawna skladnie")
else:
    for i in dict_sosy:
        obiekt = sos(i['nazwa'], i['protein'], i['fat'], i['carb'], i['masa'], i['kcal'],i['smak'])
        sosy.append(obiekt)
#=======================================================================================================================



print(bcolors.BOLD + "\nPrawilna sałatka powinna składać się z zieleniny stanowiącej bazę,")
print("z kilku składników warzywnych i ze składnika białkowego - mięsa/ryby/sera.")
print("Całość najlepiej zalać vinegretem składającym się z oleju, czegoś kwaśnego i czegoś słodkiego.\n" + bcolors.ENDC)


Loop = True

while Loop:

    Salatka.chooseItem()

    try:
        wybor = input("\nWybierz akcje:")
    except:
        print("Wprowadź poprawny numer opcji")
    else:

        if wybor == "1":
            i = 1
            for j in bazy:
                if j.getUsed() > 0:
                    print(bcolors.BOLD + bcolors.RED + str(i) + ":", j.getName(), j.getMasa(), "g" + bcolors.ENDC)
                else:
                    print(str(i) + ":", j.getName(), j.getMasa(), "g")
                i += 1
            try:
                dodaj = input("\nWybierz skladnik:")
            except:
                print("Wprowadź poprawny numer opcji")
            else:
                index = int(dodaj) -1
                print("Wybrano: ", bazy[index].getName(), "\n")
                uzyto(bazy,index)
                dodajItem(bazy, index)
                continue

        if wybor == "2":
            i = 1
            for j in dodatki:
                if j.getUsed() > 0:
                    print(bcolors.BOLD + bcolors.RED + str(i) + ":", j.getName(), j.getMasa(), "g" + bcolors.ENDC)
                else:
                    print(str(i) + ":", j.getName(), j.getMasa(), "g")
                i += 1
            try:
                dodaj = input("\nWybierz skladnik:")
            except:
                print("Wprowadź poprawny numer opcji")
            else:
                index = int(dodaj) -1
                print("Wybrano: ", dodatki[index].getName(), "\n")
                uzyto(dodatki, index)
                dodajWarzywo(dodatki, index)
                continue

        if wybor == "3":
            i = 1
            for j in bialko:
                if j.getUsed() > 0:
                    print(bcolors.BOLD + bcolors.RED + str(i) + ":", j.getName(), j.getMasa(), "g" + bcolors.ENDC)
                else:
                    print(str(i) + ":", j.getName(), j.getMasa(), "g")
                i += 1
            try:
                dodaj = input("\nWybierz skladnik:")
            except:
                print("Wprowadź poprawny numer opcji")
            else:
                index = int(dodaj) -1
                print("Wybrano: ", bialko[index].getName(), "\n")
                uzyto(bialko, index)
                dodajItem(bialko, index)
                continue


        if wybor == "4":
            i = 1
            for j in sosy:
                if j.getUsed() > 0:
                    print(bcolors.BOLD + bcolors.RED + str(i) + ":", j.getName(), j.getMasa(), "g" + bcolors.ENDC)
                else:
                    print(str(i) + ":", j.getName(), j.getMasa(), "g")
                i += 1
            try:
                dodaj = input("\nWybierz skladnik:")
            except:
                print("Wprowadź poprawny numer opcji")
            else:
                index = int(dodaj) -1
                print("Wybrano: ", sosy[index].getName(), "\n")
                uzyto(sosy, index)
                dodajItem(sosy, index)
                smaki.add(sosy[index].getSmak())
                continue

        if wybor == "5":
            Salatka.zeruj()
            for j in sosy:
                j.resetUsed()
            for j in bialko:
                j.resetUsed()
            for j in dodatki:
                j.resetUsed()
            for j in bazy:
                j.resetUsed()
            smaki.clear()

        if wybor == "6":
            Salatka.wyswietl()
            continue


        if wybor == "7":
            Loop2 = True

            while Loop2:
                print("1. Baza sałatki \n2. Warzywo \n3. Białko \n4. Składnik sosu")

                try:
                    dodaj_skladnik = input("Do jakiej grupy należy twój składnik?:")
                except:
                    print("Wprowadź poprawny numer opcji")
                else:
                    if dodaj_skladnik == "1":
                        try:
                            print("Wszystkie wagi podawaj w gramach, np 13.37")
                            cnazwa = input("Wpisz nazwę: ")
                            cprotein = input("Wpisz ilość białka na 100g: ")
                            cfat = input("Wpisz ilość tłuszczu na 100g: ")
                            ccarb = input("Wpisz ilość węgli na 100g: ")
                            cmasa = input("Wpisz masę w gramach: ")
                            ckcal = input("Wpisz ilość kcal na 100g: ")
                            customowy = skladnik(cnazwa, float(cprotein), float(cfat), float(ccarb), float(cmasa), float(ckcal), "baza")
                        except:
                            print("Blad wprowadzania, pamiętaj, że nazwa to słowo a pozostałe składowe to liczby.")
                            continue
                        else:
                            print("Stworzono nowy obiekt, powinien być widoczny na końcu wybranej kategorii")
                            bazy.append(customowy)
                            Loop2 = False


                    if dodaj_skladnik == "2":

                        def getCCecha():
                            try:
                                value = input("Wpisz dodatkowe cechy np 'wit. C', pusty wpis kończy wprowadzanie: ")
                            except ValueError:
                                value = input("Wpisz poprawną cechę: ")
                            return value

                        try:
                            print("Wszystkie wagi podawaj w gramach, np 13.37")
                            cnazwa = input("Wpisz nazwę: ")
                            cprotein = input("Wpisz ilość białka na 100g: ")
                            cfat = input("Wpisz ilość tłuszczu na 100g: ")
                            ccarb = input("Wpisz ilość węgli na 100g: ")
                            cmasa = input("Wpisz masę w gramach: ")
                            ckcal = input("Wpisz ilość kcal na 100g: ")

                            lista_cech = []
                            ccecha = getCCecha()
                            while ccecha != "":
                                lista_cech += [ccecha]
                                ccecha = getCCecha()

                            customowy = dodatek(cnazwa, float(cprotein), float(cfat), float(ccarb), float(cmasa), float(ckcal), "dodatek", lista_cech)
                        except:
                            print("Blad wprowadzania, pamiętaj, że nazwa to słowo a pozostałe składowe to liczby\n")
                            continue
                        else:
                            print("Stworzono nowy obiekt, powinien być widoczny na końcu wybranej kategorii\n")
                            dodatki.append(customowy)
                            Loop2 = False


                    if dodaj_skladnik == "3":
                        try:
                            print("Wszystkie wagi podawaj w gramach, np 13.37")
                            cnazwa = input("Wpisz nazwę: ")
                            cprotein = input("Wpisz ilość białka na 100g: ")
                            cfat = input("Wpisz ilość tłuszczu na 100g: ")
                            ccarb = input("Wpisz ilość węgli na 100g: ")
                            cmasa = input("Wpisz masę w gramach: ")
                            ckcal = input("Wpisz ilość kcal na 100g: ")
                            customowy = skladnik(cnazwa, float(cprotein), float(cfat), float(ccarb), float(cmasa), float(ckcal), "bialko")
                        except:
                            print("Blad wprowadzania, pamiętaj, że nazwa to słowo a pozostałe składowe to liczby.")
                            continue
                        else:
                            print("Stworzono nowy obiekt, powinien być widoczny na końcu wybranej kategorii")
                            bialko.append(customowy)
                            Loop2 = False


                    if dodaj_skladnik == "4":
                        try:
                            print("Wszystkie wagi podawaj w gramach, np 13.37")
                            cnazwa = input("Wpisz nazwę: ")
                            cprotein = input("Wpisz ilość białka na 100g: ")
                            cfat = input("Wpisz ilość tłuszczu na 100g: ")
                            ccarb = input("Wpisz ilość węgli na 100g: ")
                            cmasa = input("Wpisz masę w gramach: ")
                            ckcal = input("Wpisz ilość kcal na 100g: ")
                            csmak = input("Wpisz dominujacy smak/typ (slony, slodki, kwasny, olej): ")
                            customowy = sos(cnazwa, float(cprotein), float(cfat), float(ccarb), float(cmasa), float(ckcal), csmak)
                        except:
                            print("Blad wprowadzania, pamiętaj, że nazwa i smak to słowo a pozostałe składowe to liczby.")
                            continue
                        else:
                            print("Stworzono nowy obiekt, powinien być widoczny na końcu wybranej kategorii")
                            sosy.append(customowy)
                            Loop2 = False
                        Loop2 = False
                    else:
                        print("Wybierz poprawny numer opcji")
                        continue


        if wybor == "8":
            Loop = False
            Salatka.wyswietl()
            #Zapis do pliku

        else:
            print("Wprowadź poprawny numer opcji")



#=======================================================================================================================
#cechy z dodatkow wrzuc w jeden set zeby usunac duplikaty

#funkcja do wyboru i dodawania skladnikow

#funkcja zliczajaca makro i kalorie z przeliczeniem na 100g

#funkcja zapisujaca przepis do pliku



#===================================================================================================
#Testy zapisu do jsona


#plik = open("./skladniki.json", "w+")

# Produkt = skladnik("nazwa",bialko per 100g, tluszcz per 100g, wegle per 100g, typowa masa w opakowaniu, kcal per 100g, typ = baza, warzywo, bialko, sos)

# Kurczak = dodatek("Kurczak",23, 20, 40, 200, 500, "bialko", ['mieso', 'lekkostrawne'])
# Tunczyk = skladnik("Mieso",23, 20, 40, 200, 500, "bialko")
# Salata = skladnik("Salata", 10,10,40, 300,100, "baza")
# Kukurydza = dodatek("Kukurydza", 10,10,60,200,400,"warzywo","slodka")
# papryka = dodatek("papryka",20,10,10,300,200,"warzywo","duzo wit c")
# ocet = sos("ocet", 5,0,0,100,50,"kwasny")

# slownik = {"nazwa": Kurczak.getName(), "protein": Kurczak.getProt(), "fat": Kurczak.getFat(), "carb": Kurczak.getCarb(), "masa": Kurczak.getMasa(), "kcal": Kurczak.getKcal(),"typ": Kurczak.getTyp(), "cecha": Kurczak.getCecha()}
# slownik2 = {"nazwa": Tunczyk.getName(), "protein": Tunczyk.getProt(), "fat": Tunczyk.getFat(), "carb": Tunczyk.getCarb(), "masa": Tunczyk.getMasa(), "kcal": Tunczyk.getKcal(),"typ": Tunczyk.getTyp()}
# slownik3 = {"nazwa": Tunczyk.getName(), "protein": Tunczyk.getProt(), "fat": Tunczyk.getFat(), "carb": Tunczyk.getCarb(), "masa": Tunczyk.getMasa(), "kcal": Tunczyk.getKcal(),"typ": Tunczyk.getTyp()}
#
#dodatki.append(slownik)
# dodatki.append(slownik2)
# dodatki.append(slownik3)
#
# #print(dodatki)
#plik.write(json.dumps(dodatki))
#plik.close()

#==================================================================================================