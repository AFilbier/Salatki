from classes.skladniki import skladnik, dodatek, sos
import simplejson as json
import os



#inicjalizacja pustych tupli do listowania skladnikow
bazy = []
dodatki = []
sosy = []

#Produkt = skladnik("nazwa",bialko per 100g, tluszcz per 100g, wegle per 100g, typowa masa w opakowaniu, kcal per 100g, typ = baza, warzywo, bialko, sos)

# Kurczak = skladnik("Kurczak",23, 20, 40, 200, 500, "bialko")
# Tunczyk = skladnik("Mieso",23, 20, 40, 200, 500, "bialko")
# Salata = skladnik("Salata", 10,10,40, 300,100, "baza")
# Kukurydza = dodatek("Kukurydza", 10,10,60,200,400,"warzywo","slodka")
# papryka = dodatek("papryka",20,10,10,300,200,"warzywo","duzo wit c")
# ocet = sos("ocet", 5,0,0,100,50,"kwasny")


slownik = {}
plik = open("./skladniki.json", "r")
slownik = (json.loads(plik.readline()))


#Typy: baza, mieso, warzywo, sos

if slownik['typ'] == "bialko":
    obiekt = skladnik(slownik['nazwa'], slownik['protein'], slownik['fat'], slownik['carb'], slownik['masa'], slownik['kcal'], slownik['typ'])

if obiekt.getTyp() == "bialko" or obiekt.getTyp == "warzywo":
    dodatki.append(obiekt.getName())
elif obiekt.getTyp() == "baza":
    bazy.append(obiekt.getName())
elif obiekt.getTyp() == "sos":
    sosy.append(obiekt.getName())
else:
    print("Nie rozpoznano typu: ", obiekt.getTyp(), "skladnika ", obiekt.getName())


plik.close()



#cechy z dodatkow wrzuc w jeden set zeby usunac duplikaty

#wrzucaj kolejne skladniki do listy? slownika?

#funkcja odczytujaca z pliku skladniki

#funkcja do wyboru i dodawania skladnikow

#funkcja zliczajaca makro i kalorie z przeliczeniem na 100g

#funkcja zapisujaca przepis do pliku


#Testowy zapis 1 obiektu do jsona
# slownik = {"nazwa": Kurczak.getName(), "protein": Kurczak.getProt(), "fat": Kurczak.getFat(), "carb": Kurczak.getCarb(), "masa": Kurczak.getMasa(), "kcal": Kurczak.getKcal(),"typ": Kurczak.getTyp()}
#
# plik = open("./skladniki.json", "r+")
# plik.write(json.dumps(slownik))
# plik.close()