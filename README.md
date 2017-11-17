# Vegetable salad builder
Written in Python 3.6.2.
Language - PL


## How to use it

Upon launching the main.py you'll be given a brief description and a menu.
You will navigate the app by typing option numbers and pressing enter.
Ingredients are split into four groups: Salad's base, vegetables, protein sources, sauce ingredients.
You can also add any amount of custom items you'd like to use in your own salad.
When you use something and enter the same ingredients group later - the stuff already used will be highlighted in red.
At any time in main menu you can use option 5 to get rid of whatever ingredients you've already added 
or use option 6 to preview the current state of your salad including macroelements, weight and calories.
When you're done you can save the final product into a text file. The file will have every ingredient used, its weight,
it will also calculate macroelements and calories for your convenience.
Enjoy and have fun!


## How it works

Data about ingredients is kept in JSON files. Standard JSON library was used to handle coding/decoding the files.
During runtime every ingredient from JSON files is used to create a corresponding class object 
which is then loaded into a list. As a result 4 lists of objects are created (one per JSON file).

Main class is called skladniki and a few child classes inherits from it.
Salatki is a special kind of class - there is only one object created from it 
and it is used to store info about all added ingredients.
Most notable class methods are the ones responsible for returning a given parameter, add item to a Salatka object
or print a preview of currently used ingredients.
There is one support class responsible for text formatting.

During runtime user operates on a main menu (while loop) which leads to submenus with lists of available ingredients 
or additional functionality (reset, preview, end and save to a file).
When an ingredient is used its 'used' parameter is incremented.
'used' value is used to format text, and to calculate final weight of used item.
All values are floats that are rounded in preview/save mode to prevent values such as 6.000000001 grams of olive etc.
For displaying and saving a summary of vitaming/microelements sets were used to ensure no duplicates are present.


