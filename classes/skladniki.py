#Bazowa klasa ze wspolnymi metodami

class skladnik:
    def __init__(self, nazwa, protein, fat, carb, masa, kcal, typ):
        self.nazwa = nazwa
#Potrzebujemy przelicznik makroskladnikow per gram zeby przeliczac ilosci w dowolnej masie
        self.protein = protein/100
        self.fat = fat/100
        self.carb = carb/100
        self.masa = masa
        self.kcal = kcal/100
        self.typ = typ

    def  getName(self):
        return self.nazwa

    def  getProt(self):
        return self.protein * self.masa

    def getFat(self):
        return self.fat * self.masa

    def getCarb(self):
        return self.carb * self.masa

    def  getMasa(self):
        return self.masa

    def getKcal(self):
        return self.kcal * self.masa

    def getTyp(self):
        return self.typ


#Klasa dodatek rozszerzona o cechy danego produktu (zawartosc witamin itd.)
class dodatek(skladnik):
    def __init__(self, nazwa, protein, fat, carb, masa, kcal, typ, cecha):
        skladnik.__init__(self, nazwa, protein, fat, carb, masa, kcal, typ)
        self.cecha = cecha

    def getCecha(self):
        return self.cecha


#Klasa sos rozszerzona o smak - przy kompozycji sosu istotne jest dobranie skladnikow wg ich smaku
class sos(skladnik):
    def __init__(self, nazwa, protein, fat, carb, masa, kcal, smak):
        skladnik.__init__(self, nazwa, protein, fat, carb, masa, kcal, "sos")
        self.smak = smak

    def getSmak(self):
        return self.smak

#Klasa salatka to gotowy produkt z lista uzytych skladnikow i sumaryczna iloscia makroskladnikow
class salatka(skladnik):
    def __init__(self, protein, fat, carb, masa, kcal, skladniki):
        skladnik.__init__(self, protein, fat, carb, masa, kcal)

    def getSkladniki(self):
        self.skladniki = skladniki