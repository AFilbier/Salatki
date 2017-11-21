from classes.ingredients import ingredient, vegetable, sauce
import json
import os

def load_json(fname):
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