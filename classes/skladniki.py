#Bazowa klasa ze wspolnymi metodami

class skladnik:
    def __init__(self, nazwa, protein, fat, carb, masa, kcal, typ):
        self.nazwa = nazwa
        self.protein = protein
        self.fat = fat
        self.carb = carb
        self.masa = masa
        self.kcal = kcal
        self.typ = typ
        self.used = 0

    def getName(self):
        return self.nazwa

    def getProt(self):
        return (self.protein/100) * self.masa

    def getFat(self):
        return (self.fat/100) * self.masa

    def getCarb(self):
        return (self.carb/100) * self.masa

    def getMasa(self):
        return self.masa

    def getKcal(self):
        return (self.kcal/100) * self.masa

    def getProt100(self):
        return self.protein

    def getFat100(self):
        return self.fat

    def getCarb100(self):
        return self.carb

    def getKcal100(self):
        return self.kcal

    def getTyp(self):
        return self.typ

    def getUsed(self):
        return self.used

    def wasUsed(self):
        self.used += 1
        return self.used

    def resetUsed(self):
        self.used = 0
        return self.used


#Klasa dodatek rozszerzona o cechy danego produktu (zawartosc witamin itd.) ============================================

class dodatek(skladnik):
    def __init__(self, nazwa, protein, fat, carb, masa, kcal, typ, cecha):
        skladnik.__init__(self, nazwa, protein, fat, carb, masa, kcal, typ)
        self.cecha = cecha

    def getCecha(self):
        return self.cecha


#Klasa sos rozszerzona o smak - przy kompozycji sosu istotne jest dobranie skladnikow wg ich smaku =====================

class sos(skladnik):
    def __init__(self, nazwa, protein, fat, carb, masa, kcal, smak):
        skladnik.__init__(self, nazwa, protein, fat, carb, masa, kcal, "sos")
        self.smak = smak

    def getSmak(self):
        return self.smak


#Klasa salatka to gotowy produkt z lista uzytych skladnikow i sumaryczna iloscia makroskladnikow =======================

class salatka(skladnik):
    def __init__(self, protein, fat, carb, masa, kcal, skladniki, cecha):
        skladnik.__init__(self, "Salatka warzywna", protein, fat, carb, masa, kcal, "salatka")
        self.grupy = ["Baza salatki", "Warzywa", "Bialko", "Sos", "Zacznij od nowa", "Podgląd sałatki i tips&tricks", "Dodaj wlasny skladnik", "Zakoncz i zapisz do pliku", "Zakoncz bez zapisywania"]
        self.skladniki = skladniki
        self.cecha = cecha

    def getSkladniki(self):
        return self.skladniki

    def getCecha(self):
        return self.cecha

    def chooseItem(self):
        i = 1
        for item in self.grupy:
            print(str(i) + ":", item)
            i += 1

    def addItem(self, itemProtein, itemFat, itemCarb, itemMasa, itemKcal, itemName):
        self.protein += itemProtein
        self.fat += itemFat
        self.carb += itemCarb
        self.masa += itemMasa
        self.kcal += itemKcal
        self.skladniki.append(itemName)

    def addWarzywo(self, itemProtein, itemFat, itemCarb, itemMasa, itemKcal, itemName, itemCecha):
        self.protein += itemProtein
        self.fat += itemFat
        self.carb += itemCarb
        self.masa += itemMasa
        self.kcal += itemKcal
        self.skladniki.append(itemName)
        self.cecha.append(itemCecha)

    def zeruj(self):
        self.protein = 0
        self.fat = 0
        self.carb = 0
        self.masa = 0
        self.Kcal = 0
        self.skladniki = []

    def wyswietl(self):

#Poukladanie po kolei skladnikow zeby ewentualne zwielokrotnienia byly kolo siebie
        self.getSkladniki().sort()

#Wrzucenie listy cech kazdego warzywa z tablicy tablic na 1 wymiarowa tablice i potem do setu zeby wywalic duplikaty
        konkat = []
        for i in self.getCecha():
            konkat=konkat+i

        if len(set(konkat)) == 0:
            print("Masa:", round(self.getMasa(), 2), "g, " \
                  "Kalorie:", round(self.getKcal100(),2),"Kcal, " \
                  "\nMakroskładniki: Bialko:", round(self.getProt100(), 2), "g, " \
                  "Tluszcz:", round(self.getFat100(), 2), "g, "\
                  "Wegle:", round(self.getCarb100(), 2), "g, "\
                  
                  "\nSkladniki:", self.getSkladniki())


        else:
            print("Masa:", round(self.getMasa(), 2), "g, " \
                  "Kalorie:", round(self.getKcal100(),2),"Kcal, " \
                  "\nMakroskładniki: Bialko:", round(self.getProt100(), 2), "g, " \
                  "Tluszcz:", round(self.getFat100(), 2), "g, "\
                  "Wegle:", round(self.getCarb100(), 2), "g, "\
                  "\nSkladniki:", self.getSkladniki(), \
                  "\nZawiera:", set(konkat))


#Klasa z neta do zmieniania kolorow tekstu

class bcolors:
    GREEN = '\33[94m'
    RED = '\33[91m'
    ENDC = '\33[0m'
    BOLD = '\33[1m'
