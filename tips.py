def showTipsPL(Salad,flavour, bases, vegetables, proteins, sauces):
    if "Pomidory" in Salad.getIngredients():
        if "Ogorek" in Salad.getIngredients():
            print("Nie łącz ogórka z pomidorem - zniszczysz wit. C\n")
        if "Awokado (polowka)" not in Salad.getIngredients():
            if "olej" not in flavour:
                print(
                    "Do pomidorów dobrze dodać awokado czy olej - tłuszcz poprawia przyswajanie likopenu z pomidorów\n")
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
        print("Sałatka nie ma jeszcze żadnych składników sosu, dodaj np. oliwę, ocet i miód\n")

    if "slodki" not in flavour:
        print("Przy komponowaniu sosu dodaj do niego czegoś słodkiego np. łyżeczkę miodu czy syropu owocowego\n")
    if "kwasny" not in flavour:
        print("Przy komponowaniu sosu dodaj do niego czegoś kwaśnego np. octu czy soku z cytryny\n")
    if "olej" not in flavour:
        print("Przy komponowaniu sosu dodaj do niego dobry olej, np oliwę czy olej z pestek winogron\n")

def showTipsEN(Salad,flavour, bases, vegetables, proteins, sauces):
    if "Tomatoes" in Salad.getIngredients():
        if "Cucumber" in Salad.getIngredients():
            print("Do NOT mix tomatoes with cucumbers - you'll destroy vit. C\n")
        if "Avocado (half)" not in Salad.getIngredients():
            if "oil" not in flavour:
                print(
                    "It's advisable to add avocado or oil to tomatoes - fats helps your body to absorb lycopene from tomatoes\n")
    if "Avocado (half)" in Salad.getIngredients():
        if "Tomatoes" not in Salad.getIngredients():
            print("Try adding tomatoes to avocado - fats from avocado helps your body to absorb lycopene from tomatoes\n")
    if "Pepper" in Salad.getIngredients():
        if "Cucumber" in Salad.getIngredients():
            print("It's advisable not to mix peppers with cucumbers - you'll destroy vit. C from peppers\n")

    counter = 0
    for j in bases:
        if j.getUsed() > 0:
            counter += 1
    if counter == 0:
        print("There is no base vegetable yet, add some kale or lettuce\n")

    counter = 0
    for j in vegetables:
        if j.getUsed() > 0:
            counter += 1
    if counter == 0:
        print("There are no veggies yet, add some corn, tomatoes or avocado\n")

    counter = 0
    for j in proteins:
        if j.getUsed() > 0:
            counter += 1
    if counter == 0:
        print("There are no proteins yet, add some chicken breast or tuna\n")

    counter = 0
    for j in sauces:
        if j.getUsed() > 0:
            counter += 1
    if counter == 0:
        print("There are no sauce ingredients yet, add some olive, honey and vinegar\n")

    if "sweet" not in flavour:
        print("Add something sweet to your sauce to balance its taste - like honey or sugar\n")
    if "sour" not in flavour:
        print("Add something sour to your sauce to balance its taste - like lemon juice or vinegar\n")
    if "oil" not in flavour:
        print("Add some oil to your sauce to balance its taste - like olive oil or grapeseed oil\n")