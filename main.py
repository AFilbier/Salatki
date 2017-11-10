from classes.skladniki import skladnik, warzywo, sos


#Produkt = skladnik("nazwa",bialko per 100g, tluszcz per 100g, wegle per 100g, typowa masa w opakowaniu, kcal per 100g, typ = baza, warzywo, bialko, sos)

Mieso = skladnik("Mieso",23, 20, 40, 200, 500, "bialko")

print(Mieso.getCarb())
print(Mieso.getName())



papryka = warzywo("papryka",20,10,10,300,200,"warzywo","duzo wit c")


ocet = sos("ocet", 5,0,0,100,50,"kwasny")

print(ocet.getTyp())