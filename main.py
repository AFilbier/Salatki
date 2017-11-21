# -*- coding: utf-8 -*-

from classes.ingredients import ingredient, vegetable, sauce, salad, bcolors
import jsonfileload as jload
import jsonfilesave as jsave



#Initializing some lists and salad object ==============================================================================

flavour = set()
Salad = salad(0, 0, 0, 0, 0, [], [])

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


bases = jload.load_json("./bases.json",)
vegetables = jload.load_json("./vegetables.json")
proteins = jload.load_json("./proteins.json")
sauces = jload.load_json("./sauces.json")



Loop = True

while Loop:

    Salad.chooseItem()

    try:
        choice = input("\nChoose action:")
    except:
        print("Type a valid option number")
    else:


        #===================================== OPTIONS 1-4 FOR ADDING INGREDIENTS ======================================
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

            jsave.save_json_en(bases, vegetables, proteins, sauces, Salad)
            #jsave.save_json_pl(bases, vegetables, proteins, sauces, Salad)

        if choice == "9":
            Loop = False
            Salad.preview()

        else:
            print("Type a valid option number")
            continue


