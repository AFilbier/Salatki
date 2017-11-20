# -*- coding: utf-8 -*-

from classes.ingredients import ingredient, vegetable, sauce, salad, bcolors
import json
import os
import time


#Initializing some lists and salad object ==============================================================================

flavour = set()
Salad = salad(0, 0, 0, 0, 0, [], [])

#Function that loads json files into class objects =====================================================================
def Load_json(fname):
    objects = []
    try:
        Jfile = open(fname, "r")
        tmp_dict = json.loads(Jfile.read())
        Jfile.close()
    except:
        print("Error loading JSON file:", fname)
        print("Check if the file exists and got proper syntax")
    else:
        for i in tmp_dict:
            #Since 'sauces' file does not have 'type' property the if statement is operating on file names =============
            if os.path.split(fname)[1] == "bases.json":
                object = ingredient(i['name'], i['protein'], i['fat'], i['carb'], i['weight'], i['kcal'], i['type'])
                objects.append(object)
            if os.path.split(fname)[1] == "proteins.json":
                object = ingredient(i['name'], i['protein'], i['fat'], i['carb'], i['weight'], i['kcal'], i['type'])
                objects.append(object)
            if os.path.split(fname)[1] == "vegetables.json":
                object = vegetable(i['name'], i['protein'], i['fat'], i['carb'], i['weight'], i['kcal'], i['type'], i['properties'])
                objects.append(object)
            if os.path.split(fname)[1] == "sauces.json":
                object = sauce(i['name'], i['protein'], i['fat'], i['carb'], i['weight'], i['kcal'], i['flavour'])
                objects.append(object)

    #returns list of class objects of one of the four groups
    return objects

#Functions that adds new ingredient, addNewVegetable is extended by 'properties' parameter =============================
def addNewItem(group, index):
    global Salad
    return Salad.addItem(group[index].getProt(), group[index].getFat(), group[index].getCarb(), \
                           group[index].getWeight(),group[index].getKcal(), group[index].getName())

def addNewVegetable(group, index):
    global Salad
    return Salad.addVegetable(group[index].getProt(), group[index].getFat(), group[index].getCarb(), \
                           group[index].getWeight(),group[index].getKcal(), group[index].getName(), group[index].getProperties())

#Function that increments 'used' parameter. Used for total weight caclulation and text formatting
def itemWasUsed(group, index):
    global Salad
    group[index].wasUsed()



#=======================================================================================================================


bases = Load_json("./bases.json",)
vegetables = Load_json("./vegetables.json")
proteins = Load_json("./proteins.json")
sauces = Load_json("./sauces.json")



Loop = True

while Loop:

    Salad.chooseItem()

    try:
        choice = input("\nChoose action:")
    except:
        print("Type a valid option number")
    else:


#===================================== OPCJE 1-4 DODAWANIE ingredientOW ==================================================

        if choice == "1":
            for i,j in enumerate(bases, start=1):
                if j.getUsed() > 0:
                    print(bcolors.BOLD + bcolors.RED + str(i) + ":", j.getName(), j.getWeight(), "g" + bcolors.ENDC)
                else:
                    print(str(i) + ":", j.getName(), j.getWeight(), "g")
            try:
                addNew = input("\nChoose ingredient:")
                index = int(addNew) -1
            except:
                print("Type a valid option number")
            else:
                print("Choice: ", bases[index].getName(), "\n")
                itemWasUsed(bases,index)
                addNewItem(bases, index)
                continue

        if choice == "2":
            for i,j in enumerate(vegetables, start=1):
                if j.getUsed() > 0:
                    print(bcolors.BOLD + bcolors.RED + str(i) + ":", j.getName(), j.getWeight(), "g" + bcolors.ENDC)
                else:
                    print(str(i) + ":", j.getName(), j.getWeight(), "g")
            try:
                addNew = input("\nChoose ingredient:")
                index = int(addNew) -1
            except:
                print("Type a valid option number")
            else:
                print("Choice: ", vegetables[index].getName(), "\n")
                itemWasUsed(vegetables, index)
                addNewVegetable(vegetables, index)
                continue

        if choice == "3":
            for i,j in enumerate(proteins, start=1):
                if j.getUsed() > 0:
                    print(bcolors.BOLD + bcolors.RED + str(i) + ":", j.getName(), j.getWeight(), "g" + bcolors.ENDC)
                else:
                    print(str(i) + ":", j.getName(), j.getWeight(), "g")
            try:
                addNew = input("\nChoose ingredient:")
                index = int(addNew) -1
            except:
                print("Type a valid option number")
            else:
                print("Wybrano: ", proteins[index].getName(), "\n")
                itemWasUsed(proteins, index)
                addNewItem(proteins, index)
                continue


        if choice == "4":
            for i,j in enumerate(sauces, start=1):
                if j.getUsed() > 0:
                    print(bcolors.BOLD + bcolors.RED + str(i) + ":", j.getName(), j.getWeight(), "g" + bcolors.ENDC)
                else:
                    print(str(i) + ":", j.getName(), j.getWeight(), "g")
                i += 1
            try:
                addNew = input("\nChoose ingredient:")
                index = int(addNew) -1
            except:
                print("Type a valid option number")
            else:
                print("Choice: ", sauces[index].getName(), "\n")
                itemWasUsed(sauces, index)
                addNewItem(sauces, index)
                flavour.add(sauces[index].getFlavour())
                continue


        #============================================ RESET ingredients ================================================
        if choice == "5":
            Salad.reset()
            for j in sauces:
                j.resetUsed()
            for j in proteins:
                j.resetUsed()
            for j in vegetables:
                j.resetUsed()
            for j in bases:
                j.resetUsed()
            flavour.clear()
            continue

        #============================================ Show ingredients and some tips ===================================
        if choice == "6":
            print("\nYour current salad:\n")
            Salad.preview()
            print("")

            #========================================Tips & tricks =====================================================
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

            counter = 0
            for j in bases:
                if j.getUsed() > 0:
                    counter += 1
            if counter == 0:
                print("Sałatka nie ma jeszcze bazowej zieleniny, dodaj np. sałatę czy rukolę\n")

            counter = 0
            for j in vegetables:
                if j.getUsed() > 0:
                    counter += 1
            if counter == 0:
                print("Sałatka nie ma jeszcze żadnych warzyw, dodaj np. kukurydzę pomidory i połówkę awokado\n")

            counter = 0
            for j in proteins:
                if j.getUsed() > 0:
                    counter += 1
            if counter == 0:
                print("Sałatka nie ma jeszcze żadnego białkowego składnika, dodaj np. fileta z kury albo puszkę tuńczyka\n")

            counter = 0
            for j in sauces:
                if j.getUsed() > 0:
                    counter += 1
            if counter == 0:
                print("Sałatka nie ma jeszcze żadnych składników sauceu, addNew np. oliwę, ocet i miód\n")

            if "slodki" not in flavour:
                print("Przy komponowaniu sauceu addNew do niego czegoś słodkiego np. łyżeczkę miodu czy syropu owocowego\n")
            if "kwasny" not in flavour:
                print("Przy komponowaniu sauceu addNew do niego czegoś kwaśnego np. octu czy soku z cytryny\n")
            if "olej" not in flavour:
                print("Przy komponowaniu sauceu addNew do niego dobry olej, np oliwę czy olej z pestek winogron\n")
            continue


        #============================================ Adding custom ingredient =========================================
        if choice == "7":
            Loop2 = True

            while Loop2:
                print("1. Salad's base \n2. Vegetable \n3. Protein \n4. Sauce")

                try:
                    addNew_ingredient = input("Pick igredient group:")
                except:
                    print("Type a valid option number")
                else:
                    if addNew_ingredient == "1":
                        try:
                            print("Type all weights in grams, example: 13.37")
                            cname = input("Type name: ")
                            cprotein = input("Proteins per 100g: ")
                            cfat = input("Fats per 100g: ")
                            ccarb = input("Carb per 100g: ")
                            cweight = input("Weight in grams: ")
                            ckcal = input("Calories per 100g: ")
                            custom_item = ingredient(cname, float(cprotein), float(cfat), float(ccarb), float(cweight), float(ckcal), "base")
                        except:
                            print("Input error, type a valid values.")
                            continue
                        else:
                            print("New item added, it will be visible in choosen category\n")
                            bases.append(custom_item)
                            Loop2 = False


                    if addNew_ingredient == "2":

                        def getCproperties():
                            try:
                                value = input("Type additional nutrition info, example: 'wit. C', empty input to exit: ")
                            except ValueError:
                                value = input("Type a valid property: ")
                            return value
                        try:
                            print("Type all weights in grams, example: 13.37")
                            cname = input("Type name: ")
                            cprotein = input("Proteins per 100g: ")
                            cfat = input("Fats per 100g: ")
                            ccarb = input("Carb per 100g: ")
                            cweight = input("Weight in grams: ")
                            ckcal = input("Calories per 100g: ")
                            properties_list = []
                            cproperties = getCproperties()
                            while cproperties != "":
                                properties_list += [cproperties]
                                cproperties = getCproperties()

                            custom_item = vegetable(cname, float(cprotein), float(cfat), float(ccarb), float(cweight), float(ckcal), "vegetable", properties_list)
                        except:
                            print("Input error, type a valid values.\n")
                            continue
                        else:
                            print("New item added, it will be visible in choosen category\n")
                            vegetables.append(custom_item)
                            Loop2 = False


                    if addNew_ingredient == "3":
                        try:
                            print("Type all weights in grams, example: 13.37")
                            cname = input("Type name: ")
                            cprotein = input("Proteins per 100g: ")
                            cfat = input("Fats per 100g: ")
                            ccarb = input("Carb per 100g: ")
                            cweight = input("Weight in grams: ")
                            ckcal = input("Calories per 100g: ")
                            custom_item = ingredient(cname, float(cprotein), float(cfat), float(ccarb), float(cweight), float(ckcal), "proteins")
                        except:
                            print("Input error, type a valid values.")
                            continue
                        else:
                            print("New item added, it will be visible in choosen category\n")
                            proteins.append(custom_item)
                            Loop2 = False


                    if addNew_ingredient == "4":
                        try:
                            print("Type all weights in grams, example: 13.37")
                            cname = input("Type name: ")
                            cprotein = input("Proteins per 100g: ")
                            cfat = input("Fats per 100g: ")
                            ccarb = input("Carb per 100g: ")
                            cweight = input("Weight in grams: ")
                            ckcal = input("Calories per 100g: ")
                            cflavour = input("Wpisz dominujacy flavour/type (slony, slodki, kwasny, olej): ")
                            custom_item = sauce(cname, float(cprotein), float(cfat), float(ccarb), float(cweight), float(ckcal), cflavour)
                        except:
                            print("Input error, type a valid values.")
                            continue
                        else:
                            print("New item added, it will be visible in choosen category\n")
                            sauces.append(custom_item)
                            Loop2 = False
                        Loop2 = False
                    else:
                        print("Pick a valid option number")
                        continue




        #========================== WRITING TO FILE ====================================================================
        if choice == "8":
            Loop = False
            Salad.preview()

            ts = time.localtime()
            readable_ts = time.strftime("%Y-%m-%d %H:%M:%S", ts)
            new_salad = "Salad_" + time.strftime("%Y-%m-%d_%H;%M;%S", ts) + ".txt"
            print("\nUtworzono nowy outputFile: " + new_salad)
            try:
                outputFile = open(new_salad, "w")
            except IOError:
                print("Error creating output file")

            outputFile.write("====== Sałatka warzywna ========================\n")
            outputFile.write("================================================\n")
            outputFile.write("Utworzono " + readable_ts + "\n\n")

            outputFile.write("\n== Baza sałatki ================================\n\n")
            for j in bases:
                if j.getUsed() > 0:
                    outputFile.write(j.getName() + " (x" + str(j.getUsed()) +"): " + str(j.getWeight()*j.getUsed()) + "g\n")

            outputFile.write("\n== vegetables warzywne ============================\n\n")
            for j in vegetables:
                if j.getUsed() > 0:
                    outputFile.write(j.getName() + " (x" + str(j.getUsed()) + "): " + str(j.getWeight()*j.getUsed()) + "g\n")

            outputFile.write("\n== vegetables białkowe ============================\n\n")
            for j in proteins:
                if j.getUsed() > 0:
                    outputFile.write(j.getName() + " (x" + str(j.getUsed()) + "): " + str(j.getWeight()*j.getUsed()) + "g\n")

            outputFile.write("\n== Składniki sauceu ==============================\n\n")
            for j in sauces:
                if j.getUsed() > 0:
                    outputFile.write(j.getName() + " (x" + str(j.getUsed()) + "): " + str(j.getWeight()*j.getUsed()) + "g\n")

            outputFile.write("\n\n\n== Waga i kalorie gotowej sałatki ==============\n\n")
            outputFile.write("Waga: " + str(round(Salad.getWeight(),2)) + " g\n")
            outputFile.write("Kalorie: " + str(round(Salad.getKcal100(),2)) +" Kcal\n")
            outputFile.write("\n\n== Makroskładniki łącznie  =====================\n\n")
            outputFile.write("Białko: " + str(round(Salad.getProt100(),2)) + "g\n")
            outputFile.write("Tłuszcz: " + str(round(Salad.getFat100(),2)) + "g\n")
            outputFile.write("Węglowodany: " + str(round(Salad.getCarb100(),2)) + "g\n")


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

            outputFile.write("\n\n== Podział makroskładników na 100 gram =========\n\n")
            outputFile.write("Białko: " + str(round(Sprot100,2)) + "g\n")
            outputFile.write("Tłuszcz: " + str(round(Sfat100,2)) + "g\n")
            outputFile.write("Węglowodany: " + str(round(Scarb100,2)) + "g\n")
            outputFile.write("Wartośc energetyczna na 100g: " + str(round(Skcal100,2)) + "Kcal\n")
            outputFile.write("\n\n== Zawartość witamin i mikroelementów =========\n\n")

            concat = []
            for i in Salad.getProperties():
                concat = concat + i

            for i,j in enumerate(sorted(set(concat)), start=1):
                if i % 5 == 0:
                    outputFile.write(j + "\n")
                else:
                    outputFile.write(j + ", ")
            outputFile.close()


        if choice == "9":
            Loop = False
            Salad.preview()

        else:
            print("Type a valid option number")
            continue




