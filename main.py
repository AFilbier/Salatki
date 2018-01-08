# -*- coding: utf-8 -*-

from classes.ingredients import ingredient, vegetable, sauce, salad, bcolors
import jsonfileload as jload
import txtfilesave as tsave
import tips



#Initializing some stuff needed later ==================================================================================

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

#Function that increments 'used' parameter. Used for total weight caclulation and text formatting ======================
def itemWasUsed(group, index):
    global Salad
    group[index].wasUsed()

#Function that displays ingredients list from a given group and lets you choose one ====================================
def pickNewIngredient(list, choice):
    for i, j in enumerate(list, start=1):
        if j.getUsed() > 0:
            print(bcolors.BOLD + bcolors.RED + str(i) + ":", j.getName(), j.getWeight(), "g" + bcolors.ENDC)
        else:
            print(str(i) + ":", j.getName(), j.getWeight(), "g")
    try:
        addNew = input("\nChoose ingredient:")
        index = int(addNew) - 1
    except:
        print("Type a valid option number")
    else:
        print("Choice: ", list[index].getName(), "\n")
        itemWasUsed(list, index)
        if choice == "2":
            addNewVegetable(list, index)
        else:
            addNewItem(list, index)
            if choice == "4":
                flavour.add(list[index].getFlavour())


def addCustomItem(list,choice):
    try:
        print("Type all weights in grams, example: 13.37")
        cname = input("Type name: ")
        cprotein = input("Proteins per 100g: ")
        cfat = input("Fats per 100g: ")
        ccarb = input("Carb per 100g: ")
        cweight = input("Weight in grams: ")
        ckcal = input("Calories per 100g: ")

        # using a vegetable class constructor
        if choice == "2":
            properties_list = []
            cproperties = getCproperties()
            while cproperties != "":
                properties_list += [cproperties]
                cproperties = getCproperties()
            custom_item = vegetable(cname, round(float(cprotein), 2), round(float(cfat), 2), round(float(ccarb), 2), round(float(cweight), 2), round(float(ckcal), 2),"vegetable", properties_list)

        #using an ingredient class constructor for bases or proteins
        elif choice == "1" or choice == "3": #
            custom_item = ingredient(cname, round(float(cprotein), 2), round(float(cfat), 2), round(float(ccarb), 2), round(float(cweight), 2), round(float(ckcal), 2),"base")

        #using a sauces class constructor
        elif choice == "4":
            cflavour = input("Dominating flavour/type (slony/salty, slodki/sweet, kwasny/sour, olej/oil): ")
            custom_item = sauce(cname, round(float(cprotein), 2), round(float(cfat), 2), round(float(ccarb), 2), round(float(cweight), 2), round(float(ckcal), 2),cflavour)
    except:
        print("Input error, type a valid values.")
        return -1
    else:
        print("New item added, it will be visible in choosen category\n")
        list.append(custom_item)
        return 0

def getCproperties():
    try:
        value = input("Type additional nutrition info, example: 'wit. C', empty input to exit: ")
    except ValueError:
        value = input("Type a valid property: ")
    return value



def main():
    #==============================Loading json files into list of class objects =======================================
    bases = jload.load_json("./bases.json",)
    vegetables = jload.load_json("./vegetables.json")
    proteins = jload.load_json("./proteins.json")
    sauces = jload.load_json("./sauces.json")

    Loop = True
    while Loop:

        Salad.chooseItem()
        choice = input("\nChoose action:")

        #===================================== OPTIONS 1-4 FOR ADDING INGREDIENTS ======================================
        if choice == "1":
            #Picking salad's base
            pickNewIngredient(bases, choice)

        elif choice == "2":
            #Picking veggies
            pickNewIngredient(vegetables, choice)

        elif choice == "3":
            #Picking meat etc
            pickNewIngredient(proteins, choice)

        elif choice == "4":
            #Picking sauce ingredients
            pickNewIngredient(sauces, choice)

        #============================================ RESET ingredients ================================================
        elif choice == "5":
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

        #============================================ Show ingredients and some tips ===================================
        elif choice == "6":
            print("\nYour current salad:\n")
            Salad.preview()
            print("")
            tips.showTipsPL(Salad, flavour, bases, vegetables, proteins, sauces)

        #============================================ Adding custom ingredient =========================================
        elif choice == "7":
            Loop2 = True
            while Loop2:
                print("1. Salad's base \n2. Vegetable \n3. Protein \n4. Sauce")
                addNew_ingredient = input("Pick igredient group:")

                if addNew_ingredient == "1":
                    if addCustomItem(bases,addNew_ingredient) != -1:
                        Loop2 = False
                if addNew_ingredient == "2":
                    if addCustomItem(vegetables, addNew_ingredient) != -1:
                        Loop2 = False
                if addNew_ingredient == "3":
                    if addCustomItem(proteins, addNew_ingredient) != -1:
                        Loop2 = False
                if addNew_ingredient == "4":
                    if addCustomItem(sauces, addNew_ingredient) != -1:
                        Loop2 = False
                else:
                    print("Pick proper group number")

        #========================== Writing output to file =================================================================
        elif choice == "8":
            Loop = False
            Salad.preview()
            tsave.save_txt_pl(bases, vegetables, proteins, sauces, Salad)

        #Exit app without saving to file ===================================================================================
        elif choice == "9":
            Loop = False
            Salad.preview()

        else:
            print("Type a valid option number")


if __name__ == "__main__" :
    main()
