# -*- coding: utf-8 -*-

from classes.ingredients import ingredient, vegetable, sauce, salad, bcolors
import json
import time


#Initializing some lists and salad object ==============================================================================
dict_bases = []
dict_vegetables = []
dict_proteins = []
dict_sauces = []

bases = []
vegetables = []
sauce = []
proteins = []
flavour = set()

Salad = salad(0, 0, 0, 0, 0, [], [])


#Function that loads json files into class objects =====================================================================
def Load_json(fname, dict_name):
    try:
        Jfile = open(fname, "r")
        dict_name = json.loads(Jfile.read())
        Jfile.close()
    except:
        print("Error loading JSON file:", fname)
        print("Check if the file exists and got proper syntax")
    else:
        for i in dict_name:
            if i['type'] == "base":
                object = ingredient(i['name'], i['protein'], i['fat'], i['carb'], i['weight'], i['kcal'], i['type'])
                bases.append(object)
            if i['type'] == "proteins":
                object = ingredient(i['name'], i['protein'], i['fat'], i['carb'], i['weight'], i['kcal'], i['type'])
                proteins.append(object)
            if i['type'] == "vegetable":
                object = vegetable(i['name'], i['protein'], i['fat'], i['carb'], i['weight'], i['kcal'], i['type'], i['properties'])
                vegetables.append(object)
            if i['type'] == "sauce":
                object = sauce(i['name'], i['protein'], i['fat'], i['carb'], i['weight'], i['kcal'], i['flavour'])
                sauce.append(object)

def addNewItem(group, index):
    global Salad
    return Salad.addItem(group[index].getProt(), group[index].getFat(), group[index].getCarb(), \
                           group[index].getWeight(),group[index].getKcal(), group[index].getName())

def addNewVegetable(group, index):
    global Salad
    return Salad.addVegetable(group[index].getProt(), group[index].getFat(), group[index].getCarb(), \
                           group[index].getWeight(),group[index].getKcal(), group[index].getName(), group[index].getProperties())


def itemWasUsed(group, index):
    global Salad
    group[index].wasUsed()



#=======================================================================================================================



print(bcolors.BOLD + "\nPrawilna sałatka powinna składać się z zieleniny stanowiącej bazę,")
print("z kilku składników warzywnych i ze składnika białkowego - mięsa/ryby/sera.")
print("Całość najlepiej zalać vinegretem składającym się z oleju, czegoś kwaśnego i czegoś słodkiego.\n" + bcolors.ENDC)


Load_json("bases.json", dict_bases)
Load_json("vegetables.json", dict_vegetables)
Load_json("proteins.json", dict_proteins)
Load_json("sauces.json", dict_sauces)

Loop = True

while Loop:

    Salad.chooseItem()

    try:
        wybor = input("\nWybierz akcje:")
    except:
        print("Wprowadź poprawny numer opcji")
    else:


#===================================== OPCJE 1-4 DODAWANIE ingredientOW ==================================================

        if wybor == "1":
            for i,j in enumerate(bases, start=1):
                if j.getUsed() > 0:
                    print(bcolors.BOLD + bcolors.RED + str(i) + ":", j.getName(), j.getWeight(), "g" + bcolors.ENDC)
                else:
                    print(str(i) + ":", j.getName(), j.getWeight(), "g")
            try:
                addNew = input("\nChoose ingredient:")
            except:
                print("Wprowadź poprawny numer opcji")
            else:
                index = int(addNew) -1
                print("Wybrano: ", bases[index].getName(), "\n")
                itemWasUsed(bases,index)
                addNewItem(bases, index)
                continue

        if wybor == "2":
            for i,j in enumerate(vegetables, start=1):
                if j.getUsed() > 0:
                    print(bcolors.BOLD + bcolors.RED + str(i) + ":", j.getName(), j.getWeight(), "g" + bcolors.ENDC)
                else:
                    print(str(i) + ":", j.getName(), j.getWeight(), "g")
            try:
                addNew = input("\nWybierz ingredient:")
            except:
                print("Wprowadź poprawny numer opcji")
            else:
                index = int(addNew) -1
                print("Wybrano: ", vegetables[index].getName(), "\n")
                itemWasUsed(vegetables, index)
                addNewVegetable(vegetables, index)
                continue

        if wybor == "3":
            for i,j in enumerate(proteins, start=1):
                if j.getUsed() > 0:
                    print(bcolors.BOLD + bcolors.RED + str(i) + ":", j.getName(), j.getWeight(), "g" + bcolors.ENDC)
                else:
                    print(str(i) + ":", j.getName(), j.getWeight(), "g")
            try:
                addNew = input("\nWybierz ingredient:")
            except:
                print("Wprowadź poprawny numer opcji")
            else:
                index = int(addNew) -1
                print("Wybrano: ", proteins[index].getName(), "\n")
                itemWasUsed(proteins, index)
                addNewItem(proteins, index)
                continue


        if wybor == "4":
            for i,j in enumerate(sauce, start=1):
                if j.getUsed() > 0:
                    print(bcolors.BOLD + bcolors.RED + str(i) + ":", j.getName(), j.getWeight(), "g" + bcolors.ENDC)
                else:
                    print(str(i) + ":", j.getName(), j.getWeight(), "g")
                i += 1
            try:
                addNew = input("\nWybierz ingredient:")
            except:
                print("Wprowadź poprawny numer opcji")
            else:
                index = int(addNew) -1
                print("Wybrano: ", sauce[index].getName(), "\n")
                itemWasUsed(sauce, index)
                addNewItem(sauce, index)
                flavour.add(sauce[index].getflavour())
                continue


#============================================ RESET ingredientOW =========================================================

        if wybor == "5":
            Salad.reset()
            for j in sauce:
                j.resetUsed()
            for j in proteins:
                j.resetUsed()
            for j in vegetables:
                j.resetUsed()
            for j in bases:
                j.resetUsed()
            flavour.clear()
            continue

#============================================ WYSWIETLANIE SKLADU I SUGESTII ===========================================

        if wybor == "6":
            print("\nTwoja obecna sałatka:\n")
            Salad.preview()
            print("")

#Tips & tricks =========================================================================================================
            if "Pomidory" in Salad.getIngredients():
                if "Ogorek" in Salad.getIngredients():
                    print("Nie łącz ogórka z pomidorem - zniszczysz wit. C\n")
                if "Awokado (polowka)" not in Salad.getIngredients():
                    if "olej" not in flavour:
                        print("Do pomidorów dobrze dodać awokado czy olej - tłuszcz poprawia przyswajanie likopenu z pomidorów\n")
            if "Awokado (polowka)" in Salad.getIngredients():
                if "Pomidory" not in Salad.getIngredients():
                    print("Do awokado dobrze dodać pomidory - składniki awokado poprawiają przyswajanie likopenu z pomidorów\n")
            if "Papryka" in Salad.getIngredients():
                if "Ogorek" in Salad.getIngredients():
                    print("Nie zalecane jest łączenie ogórka z papryką - zniszczysz wit. C zawartą w papryce\n")

            licznik = 0
            for j in bases:
                if j.getUsed() > 0:
                    licznik += 1
            if licznik == 0:
                print("Sałatka nie ma jeszcze bazowej zieleniny, addNew np. sałatę czy rukolę\n")

            licznik = 0
            for j in vegetables:
                if j.getUsed() > 0:
                    licznik += 1
            if licznik == 0:
                print("Sałatka nie ma jeszcze żadnych warzyw, addNew np. kukurydzę pomidory i połówkę awokado\n")

            licznik = 0
            for j in proteins:
                if j.getUsed() > 0:
                    licznik += 1
            if licznik == 0:
                print("Sałatka nie ma jeszcze żadnego białkowego składnika, addNew np. fileta z kury albo puszkę tuńczyka\n")

            licznik = 0
            for j in sauce:
                if j.getUsed() > 0:
                    licznik += 1
            if licznik == 0:
                print("Sałatka nie ma jeszcze żadnych składników sauceu, addNew np. oliwę, ocet i miód\n")

            if "slodki" not in flavour:
                print("Przy komponowaniu sauceu addNew do niego czegoś słodkiego np. łyżeczkę miodu czy syropu owocowego\n")
            if "kwasny" not in flavour:
                print("Przy komponowaniu sauceu addNew do niego czegoś kwaśnego np. octu czy soku z cytryny\n")
            if "olej" not in flavour:
                print("Przy komponowaniu sauceu addNew do niego dobry olej, np oliwę czy olej z pestek winogron\n")


            continue


#============================================ WPROWADZANIE CUSTOMOWEGO ingredientA =======================================
        if wybor == "7":
            Loop2 = True

            while Loop2:
                print("1. Baza sałatki \n2. Vegetable \n3. Białko \n4. Składnik sauceu")

                try:
                    addNew_ingredient = input("Do jakiej grupy należy twój składnik?:")
                except:
                    print("Wprowadź poprawny numer opcji")
                else:
                    if addNew_ingredient == "1":
                        try:
                            print("Wszystkie wagi podawaj w gramach, np 13.37")
                            cname = input("Wpisz nazwę: ")
                            cprotein = input("Wpisz ilość białka na 100g: ")
                            cfat = input("Wpisz ilość tłuszczu na 100g: ")
                            ccarb = input("Wpisz ilość węgli na 100g: ")
                            cweight = input("Wpisz masę w gramach: ")
                            ckcal = input("Wpisz ilość kcal na 100g: ")
                            customowy = ingredient(cname, float(cprotein), float(cfat), float(ccarb), float(cweight), float(ckcal), "baza")
                        except:
                            print("Blad wprowadzania, pamiętaj, że name to słowo a pozostałe składowe to liczby.")
                            continue
                        else:
                            print("Stworzono nowy obiekt, powinien być widoczny na końcu wybranej kategorii")
                            bases.append(customowy)
                            Loop2 = False


                    if addNew_ingredient == "2":

                        def getCproperties():
                            try:
                                value = input("Wpisz dodatkowe cechy np 'wit. C', pusty wpis kończy wprowadzanie: ")
                            except ValueError:
                                value = input("Wpisz poprawną cechę: ")
                            return value

                        try:
                            print("Wszystkie wagi podawaj w gramach, np 13.37")
                            cname = input("Wpisz nazwę: ")
                            cprotein = input("Wpisz ilość białka na 100g: ")
                            cfat = input("Wpisz ilość tłuszczu na 100g: ")
                            ccarb = input("Wpisz ilość węgli na 100g: ")
                            cweight = input("Wpisz masę w gramach: ")
                            ckcal = input("Wpisz ilość kcal na 100g: ")

                            lista_cech = []
                            cproperties = getCproperties()
                            while cproperties != "":
                                lista_cech += [cproperties]
                                cproperties = getCproperties()

                            customowy = vegetable(cname, float(cprotein), float(cfat), float(ccarb), float(cweight), float(ckcal), "vegetable", lista_cech)
                        except:
                            print("Blad wprowadzania, pamiętaj, że name to słowo a pozostałe składowe to liczby\n")
                            continue
                        else:
                            print("Stworzono nowy obiekt, powinien być widoczny na końcu wybranej kategorii\n")
                            vegetables.append(customowy)
                            Loop2 = False


                    if addNew_ingredient == "3":
                        try:
                            print("Wszystkie wagi podawaj w gramach, np 13.37")
                            cname = input("Wpisz nazwę: ")
                            cprotein = input("Wpisz ilość białka na 100g: ")
                            cfat = input("Wpisz ilość tłuszczu na 100g: ")
                            ccarb = input("Wpisz ilość węgli na 100g: ")
                            cweight = input("Wpisz masę w gramach: ")
                            ckcal = input("Wpisz ilość kcal na 100g: ")
                            customowy = ingredient(cname, float(cprotein), float(cfat), float(ccarb), float(cweight), float(ckcal), "proteins")
                        except:
                            print("Blad wprowadzania, pamiętaj, że name to słowo a pozostałe składowe to liczby.")
                            continue
                        else:
                            print("Stworzono nowy obiekt, powinien być widoczny na końcu wybranej kategorii")
                            proteins.append(customowy)
                            Loop2 = False


                    if addNew_ingredient == "4":
                        try:
                            print("Wszystkie wagi podawaj w gramach, np 13.37")
                            cname = input("Wpisz nazwę: ")
                            cprotein = input("Wpisz ilość białka na 100g: ")
                            cfat = input("Wpisz ilość tłuszczu na 100g: ")
                            ccarb = input("Wpisz ilość węgli na 100g: ")
                            cweight = input("Wpisz masę w gramach: ")
                            ckcal = input("Wpisz ilość kcal na 100g: ")
                            cflavour = input("Wpisz dominujacy flavour/type (slony, slodki, kwasny, olej): ")
                            customowy = sauce(cname, float(cprotein), float(cfat), float(ccarb), float(cweight), float(ckcal), cflavour)
                        except:
                            print("Blad wprowadzania, pamiętaj, że name i flavour to słowo a pozostałe składowe to liczby.")
                            continue
                        else:
                            print("Stworzono nowy obiekt, powinien być widoczny na końcu wybranej kategorii")
                            sauce.append(customowy)
                            Loop2 = False
                        Loop2 = False
                    else:
                        print("Wybierz poprawny numer opcji")
                        continue




#========================== ZAPIS DO PLIKU =============================================================================

        if wybor == "8":
            Loop = False
            Salad.preview()

            ts = time.localtime()
            readable_ts = time.strftime("%Y-%m-%d %H:%M:%S", ts)
            nowa_salad = "Salad_" + time.strftime("%Y-%m-%d_%H;%M;%S", ts) + ".txt"
            print("\nUtworzono nowy plik: " + nowa_salad)
            try:
                plik = open(nowa_salad, "w")
            except IOError:
                print("Blad tworzenia pliku")

            plik.write("====== Sałatka warzywna ========================\n")
            plik.write("================================================\n")
            plik.write("Utworzono " + readable_ts + "\n\n")

            plik.write("\n== Baza sałatki ================================\n\n")
            for j in bases:
                if j.getUsed() > 0:
                    plik.write(j.getName() + " (x" + str(j.getUsed()) +"): " + str(j.getWeight()*j.getUsed()) + "g\n")

            plik.write("\n== vegetables warzywne ============================\n\n")
            for j in vegetables:
                if j.getUsed() > 0:
                    plik.write(j.getName() + " (x" + str(j.getUsed()) + "): " + str(j.getWeight()*j.getUsed()) + "g\n")

            plik.write("\n== vegetables białkowe ============================\n\n")
            for j in proteins:
                if j.getUsed() > 0:
                    plik.write(j.getName() + " (x" + str(j.getUsed()) + "): " + str(j.getWeight()*j.getUsed()) + "g\n")

            plik.write("\n== Składniki sauceu ==============================\n\n")
            for j in sauce:
                if j.getUsed() > 0:
                    plik.write(j.getName() + " (x" + str(j.getUsed()) + "): " + str(j.getWeight()*j.getUsed()) + "g\n")


            plik.write("\n\n\n== Waga i kalorie gotowej sałatki ==============\n\n")
            plik.write("Waga: " + str(round(Salad.getWeight(),2)) + " g\n")
            plik.write("Kalorie: " + str(round(Salad.getKcal100(),2)) +" Kcal\n")

            plik.write("\n\n== Makroskładniki łącznie  =====================\n\n")
            plik.write("Białko: " + str(round(Salad.getProt100(),2)) + "g\n")
            plik.write("Tłuszcz: " + str(round(Salad.getFat100(),2)) + "g\n")
            plik.write("Węglowodany: " + str(round(Salad.getCarb100(),2)) + "g\n")


            if Salad.getWeight() > 0:
                Sprot100 = (Salad.getProt100()/Salad.getWeight())*100
                Sfat100 = (Salad.getFat100()/Salad.getWeight())*100
                Scarb100 = (Salad.getCarb100()/Salad.getWeight())*100
                Skcal100 = (Salad.getKcal100()/Salad.getWeight())*100
            if Salad.getWeight() == 0:
                Sprot100 = 0
                Sfat100 = 0
                Scarb100 = 0
                Skcal100 = 0

            plik.write("\n\n== Podział makroskładników na 100 gram =========\n\n")
            plik.write("Białko: " + str(round(Sprot100,2)) + "g\n")
            plik.write("Tłuszcz: " + str(round(Sfat100,2)) + "g\n")
            plik.write("Węglowodany: " + str(round(Scarb100,2)) + "g\n")
            plik.write("Wartośc energetyczna na 100g: " + str(round(Skcal100,2)) + "Kcal\n")

            plik.write("\n\n== Zawartość witamin i mikroelementów =========\n\n")

            konkat = []
            for i in Salad.getProperties():
                konkat = konkat + i

            for i,j in enumerate(sorted(set(konkat)), start=1):
                if i % 5 == 0:
                    plik.write(j + "\n")
                else:
                    plik.write(j + ", ")
            plik.close()


        if wybor == "9":
            Loop = False
            Salad.preview()

        else:
            print("Wprowadź poprawny numer opcji")
            continue




