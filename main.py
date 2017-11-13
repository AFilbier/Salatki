# -*- coding: utf-8 -*-

from classes.skladniki import skladnik, dodatek, sos
import json




#inicjalizacja pustych list do listowania skladnikow
dict_bazy = []
dict_dodatki = []
dict_bialko = []
dict_sosy = []

bazy = []
dodatki = []
sosy = []
bialko = []

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