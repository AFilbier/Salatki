#Base ingredient class with most used methods

class ingredient:
    def __init__(self, name, protein, fat, carb, weight, kcal, type):
        self.name = name
        self.protein = protein
        self.fat = fat
        self.carb = carb
        self.weight = weight
        self.kcal = kcal
        self.type = type
        self.used = 0

    def getName(self):
        return self.name

    def getProt(self):
        return (self.protein/100) * self.weight

    def getFat(self):
        return (self.fat/100) * self.weight

    def getCarb(self):
        return (self.carb/100) * self.weight

    def getWeight(self):
        return self.weight

    def getKcal(self):
        return (self.kcal/100) * self.weight

    #Do note that actual macros weight is dufferent than per 100g weight - thus 2 method types were needed
    def getProt100(self):
        return self.protein

    def getFat100(self):
        return self.fat

    def getCarb100(self):
        return self.carb

    def getKcal100(self):
        return self.kcal

    def getType(self):
        return self.type

    def getUsed(self):
        return self.used

    def wasUsed(self):
        self.used += 1
        return self.used

    def resetUsed(self):
        self.used = 0
        return self.used


#Class vegetable with additional parameter to store properties like vitamins, etc ======================================

class vegetable(ingredient):
    def __init__(self, name, protein, fat, carb, weight, kcal, type, properties):
        ingredient.__init__(self, name, protein, fat, carb, weight, kcal, type)
        self.properties = properties

    def getProperties(self):
        return self.properties


#Class sauce with flavour parameter - uset to compose a balanced sauce =================================================

class sauce(ingredient):
    def __init__(self, name, protein, fat, carb, weight, kcal, flavour):
        ingredient.__init__(self, name, protein, fat, carb, weight, kcal, "sauce")
        self.flavour = flavour

    def getFlavour(self):
        return self.flavour


#Class salad is a final product with list of used ingredients, calories and macros =====================================

class salad(ingredient):
    def __init__(self, protein, fat, carb, weight, kcal, ingredients, properties):
        ingredient.__init__(self, "Vegetable salad", protein, fat, carb, weight, kcal, "salad")
        self.groups = ["Base", "Vegetables", "Proteins", "Sauce", "Start from scratch", "Preview + tips&tricks", \
                       "Add custom ingredient", "End and save to a file", "End without saving"]
        self.ingredients = ingredients
        self.properties = properties

    def getIngredients(self):
        return self.ingredients

    def getProperties(self):
        return self.properties

    def chooseItem(self):
        for i, item in enumerate(self.groups, start=1):
            print(str(i) + ":", item)

    def addItem(self, itemProtein, itemFat, itemCarb, itemWeight, itemKcal, itemName):
        self.protein += itemProtein
        self.fat += itemFat
        self.carb += itemCarb
        self.weight += itemWeight
        self.kcal += itemKcal
        self.ingredients.append(itemName)

    def addVegetable(self, itemProtein, itemFat, itemCarb, itemWeight, itemKcal, itemName, itemproperties):
        self.protein += itemProtein
        self.fat += itemFat
        self.carb += itemCarb
        self.weight += itemWeight
        self.kcal += itemKcal
        self.ingredients.append(itemName)
        self.properties.append(itemproperties)

    def reset(self):
        self.protein = 0
        self.fat = 0
        self.carb = 0
        self.weight = 0
        self.kcal = 0
        self.ingredients = []

    def preview(self):        
        self.getIngredients().sort()

        #2D list into 1D list then into set to get rid of duplicates
        concat = []
        for i in self.getProperties():
            concat=concat+i

        if len(set(concat)) == 0:
            print("Weight: ", format(self.getWeight(),'.2f'), "g, " \
                  "Calories:", format(self.getKcal100(),'.2f'),"Kcal, " \
                  "\nMacros: Proteins:", format(self.getProt100(),'.2f'), "g, " \
                  "Fats:", format(self.getFat100(),'.2f'), "g, "\
                  "Carbs:", format(self.getCarb100(),'.2f'), "g, "\
                  "\nIngredients:", self.getIngredients())

        else:
            print("Weight:", format(self.getWeight(),'.2f'), "g, " \
                  "Calories:", format(self.getKcal100(),'.2f'),"Kcal, " \
                  "\nMacros: Proteins:", format(self.getProt100(),'.2f'), "g, " \
                  "Fats:", format(self.getFat100(),'.2f'), "g, "\
                  "Carbs:", format(self.getCarb100(),'.2f'), "g, "\
                  "\nIngredients:", self.getIngredients(), \
                  "\nContains:", set(concat))


#Text formatting class =================================================================================================
class bcolors:
    GREEN = '\33[94m'
    RED = '\33[91m'
    ENDC = '\33[0m'
    BOLD = '\33[1m'
