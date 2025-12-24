# stores 10 alien species
# each species has 4 attributes
# user can type a species name and see all info
# command random shows random species
# command add allows a user to create their own species

import random

aliens = {
    "ragnar" : {
        "name" : "Ragnar",
        "power" : 16,
        "intelligence" : 4,
        "dexterity" : 65,
        },
    "blarg" : {
        "name" : "Blarg",
        "power" : 79,
        "intelligence" : 1,
        "dexterity" : 50,
        },
    "gorg" : {
        "name" : "Gorg",
        "power" : 99,
        "intelligence" : 1,
        "dexterity" : 100
        },
    "ferg" : {
        "name" : "Furg",
        "power" : 100,
        "intelligence" : 100,
        "dexterity" : 5,
        },
    "tuzzer" : {
        "name" : "Tuzzer",
        "power" : 76,
        "intelligence" : 84,
        "dexterity" : 76,
        },
}

name = input("Which alien? Ferg, Tuzzer, Gorg, Blarg or Ragnar? Or random, or create: ").strip().lower()

if name in aliens:
    print(f"\nYou selected {name.title()}, here are his statistics: ")

    for stat, value in aliens[name].items():
        print(f"{stat.title()} is {value}")

elif name == "random":
    alien_list = list(aliens.keys())
    pick = random.choice(alien_list)
    
    print(f"\nYou selected {pick.title()}, here are his statistics: ")

    for stat, value in aliens[pick].items():
        print(f"{stat.title()} is {value}")

elif name == "create":
    temporary = {}
    
    name = input("name your Alien: ").strip().lower()
    power = int(input("What is your aliens power: "))
    intelligence = int(input("What is your aliens intelligence: "))
    dexterity = int(input("What is your aliens dexterity: "))

    aliens[name] = {
        "name" : name,
        "power" : power,
        "intelligence" : intelligence,
        "dexterity" : dexterity,
    }

else:
    print("I don't understand, that is not an option")
    
    

