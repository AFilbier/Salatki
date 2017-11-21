import time


def save_json_pl(bases, vegetables, proteins, sauces, Salad):
    ts = time.localtime()
    readable_ts = time.strftime("%Y-%m-%d %H:%M:%S", ts)
    new_salad = "Salad_" + time.strftime("%Y-%m-%d_%H;%M;%S", ts) + ".txt"
    print("\nNew output file created: " + new_salad)
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
            outputFile.write(j.getName() + " (x" + str(j.getUsed()) + "): " + str(j.getWeight() * j.getUsed()) + "g\n")

    outputFile.write("\n== Składniki warzywne ============================\n\n")
    for j in vegetables:
        if j.getUsed() > 0:
            outputFile.write(j.getName() + " (x" + str(j.getUsed()) + "): " + str(j.getWeight() * j.getUsed()) + "g\n")

    outputFile.write("\n== Składniki białkowe ============================\n\n")    
    for j in proteins:
        if j.getUsed() > 0:
            outputFile.write(j.getName() + " (x" + str(j.getUsed()) + "): " + str(j.getWeight() * j.getUsed()) + "g\n")

    outputFile.write("\n== Składniki sosu ==============================\n\n")    
    for j in sauces:
        if j.getUsed() > 0:
            outputFile.write(j.getName() + " (x" + str(j.getUsed()) + "): " + str(j.getWeight() * j.getUsed()) + "g\n")

    outputFile.write("\n\n\n== Waga i kalorie gotowej sałatki ==============\n\n")
    outputFile.write("Waga: " + str(round(Salad.getWeight(), 2)) + " g\n")
    outputFile.write("Kalorie: " + str(round(Salad.getKcal100(), 2)) + " Kcal\n")
    outputFile.write("\n\n== Makroskładniki łącznie  =====================\n\n")
    outputFile.write("Białko: " + str(round(Salad.getProt100(), 2)) + "g\n")
    outputFile.write("Tłuszcz: " + str(round(Salad.getFat100(), 2)) + "g\n")
    outputFile.write("Węglowodany: " + str(round(Salad.getCarb100(), 2)) + "g\n")

    if Salad.getWeight() > 0:
        sprot100 = (Salad.getProt100() / Salad.getWeight()) * 100
        sfat100 = (Salad.getFat100() / Salad.getWeight()) * 100
        scarb100 = (Salad.getCarb100() / Salad.getWeight()) * 100
        skcal100 = (Salad.getKcal100() / Salad.getWeight()) * 100
    if Salad.getWeight() == 0:
        sprot100 = 0
        sfat100 = 0
        scarb100 = 0
        skcal100 = 0

    outputFile.write("\n\n== Podział makroskładników na 100 gram =========\n\n")
    outputFile.write("Białko: " + str(round(sprot100, 2)) + "g\n")
    outputFile.write("Tłuszcz: " + str(round(sfat100, 2)) + "g\n")
    outputFile.write("Węglowodany: " + str(round(scarb100, 2)) + "g\n")
    outputFile.write("Wartośc energetyczna na 100g: " + str(round(skcal100, 2)) + "Kcal\n")
    outputFile.write("\n\n== Zawartość witamin i mikroelementów =========\n\n")

    concat = []
    for i in Salad.getProperties():
        concat = concat + i

    for i, j in enumerate(sorted(set(concat)), start=1):
        if i % 5 == 0:
            outputFile.write(j + "\n")
        else:
            outputFile.write(j + ", ")
    outputFile.close()



def save_json_en(bases, vegetables, proteins, sauces, Salad):
    ts = time.localtime()
    readable_ts = time.strftime("%Y-%m-%d %H:%M:%S", ts)
    new_salad = "Salad_" + time.strftime("%Y-%m-%d_%H;%M;%S", ts) + ".txt"
    print("\nNew output file created: " + new_salad)
    try:
        outputFile = open(new_salad, "w")
    except IOError:
        print("Error creating output file")

    outputFile.write("====== Vegetable salad= ========================\n")
    outputFile.write("================================================\n")
    outputFile.write("Created " + readable_ts + "\n\n")

    outputFile.write("\n== Salad's base ================================\n\n")
    for j in bases:
        if j.getUsed() > 0:
            outputFile.write(j.getName() + " (x" + str(j.getUsed()) + "): " + str(j.getWeight() * j.getUsed()) + "g\n")

    outputFile.write("\n== Vegetable ingredients =======================\n\n")
    for j in vegetables:
        if j.getUsed() > 0:
            outputFile.write(j.getName() + " (x" + str(j.getUsed()) + "): " + str(j.getWeight() * j.getUsed()) + "g\n")

    outputFile.write("\n== Protein ingredients =========================\n\n")
    for j in proteins:
        if j.getUsed() > 0:
            outputFile.write(j.getName() + " (x" + str(j.getUsed()) + "): " + str(j.getWeight() * j.getUsed()) + "g\n")

    outputFile.write("\n== Sauce ingredients ===========================\n\n")
    for j in sauces:
        if j.getUsed() > 0:
            outputFile.write(j.getName() + " (x" + str(j.getUsed()) + "): " + str(j.getWeight() * j.getUsed()) + "g\n")

    outputFile.write("\n\n\n== Weight and calories in total ================\n\n")
    outputFile.write("Weight: " + str(round(Salad.getWeight(), 2)) + " g\n")
    outputFile.write("Calories: " + str(round(Salad.getKcal100(), 2)) + " Kcal\n")
    outputFile.write("\n\n== Macrolemenets in total  =====================\n\n")
    outputFile.write("Proteins: " + str(round(Salad.getProt100(), 2)) + "g\n")
    outputFile.write("Fats: " + str(round(Salad.getFat100(), 2)) + "g\n")
    outputFile.write("Carbohydrates: " + str(round(Salad.getCarb100(), 2)) + "g\n")

    if Salad.getWeight() > 0:
        sprot100 = (Salad.getProt100() / Salad.getWeight()) * 100
        sfat100 = (Salad.getFat100() / Salad.getWeight()) * 100
        scarb100 = (Salad.getCarb100() / Salad.getWeight()) * 100
        skcal100 = (Salad.getKcal100() / Salad.getWeight()) * 100
    if Salad.getWeight() == 0:
        sprot100 = 0
        sfat100 = 0
        scarb100 = 0
        skcal100 = 0

    outputFile.write("\n\n== Macroelements per 100g ======================\n\n")
    outputFile.write("Proteins: " + str(round(sprot100, 2)) + "g\n")
    outputFile.write("Fats: " + str(round(sfat100, 2)) + "g\n")
    outputFile.write("Carbohydrates: " + str(round(scarb100, 2)) + "g\n")
    outputFile.write("Calories: " + str(round(skcal100, 2)) + "Kcal\n")
    outputFile.write("\n\n== Vitamins and microelements ==================\n\n")

    concat = []
    for i in Salad.getProperties():
        concat = concat + i

    for i, j in enumerate(sorted(set(concat)), start=1):
        if i % 5 == 0:
            outputFile.write(j + "\n")
        else:
            outputFile.write(j + ", ")
    outputFile.close()