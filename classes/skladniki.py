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

    def  getName(self):
        return self.nazwa

    def  getProt(self):
        return (self.protein/100) * self.masa

    def getFat(self):
        return (self.fat/100) * self.masa

    def getCarb(self):
        return (self.carb/100) * self.masa

    def  getMasa(self):
        return self.masa

    def getKcal(self):
        return (self.kcal/100) * self.masa

    def  getProt100(self):
        return self.protein

    def getFat100(self):
        return self.fat

    def getCarb100(self):
        return self.carb

    def getKcal100(self):
        return self.kcal

    def getTyp(self):
        return self.typ


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
    def __init__(self, protein, fat, carb, masa, kcal, skladniki):
        skladnik.__init__(self, "Salatka warzywna", protein, fat, carb, masa, kcal, "salatka")
        self.grupy = ["Baza salatki", "Warzywa", "Bialko", "Sos", "Zacznij od nowa", "Zakoncz"]
        self.skladniki = skladniki

    def getSkladniki(self):
        return self.skladniki

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

    def zeruj(self):
        self.protein = 0
        self.fat = 0
        self.carb = 0
        self.masa = 0
        self.Kcal = 0


#    def addCecha(self, itemCecha):
#           dodawanie kolejnego stringu jako element setu