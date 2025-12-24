objects = []

name = input("What is your name User? Mine is narrator. ")
print(f"Well then, hello {name.title()}")
print("Listen, I have been pondering ferociously... if you could make a top 5 list, what would it be?")

def list():
    for i in range(5):
        item = input(f"Item number {i + 1} is: ")
        objects.append(item)

items_chosen = list()
print(objects)

desired = input(f"Yes or no {name.title()}? ").lower().strip()
if desired == "yes":
    print("Miraculuos! Let us continue. Onwards I say!")
elif desired == "no":
    while True:
        objects = []
        items_chosen = list()
        print(objects)
        happy = input(f"Happy now? Say 'yes' if so, if you don't this will take a while {name}: ").lower().strip()
        if happy == "yes":
            break

print(sorted(objects))
print("Now your list is in alaphebitical order!")
objects.sort()

middle_list = input("But your middle term is utterly impalpable. Send me an item to add to the middle of the list:  ").strip().lower()
objects.insert(2, middle_list)
print(objects)
print("Sorry, am I a joke to you? Let's have a look at what you put here shall we?")
print(f"'{objects[-4]}'!", end = "")
print(" Hilarious! Utterly hilarious!")

del objects[-4]
print(objects)
print(f"See your item? I don't. Now we have {len(objects)} items. Though something is missing...")

print("You know what, I'll fix the problem and lighten the mood. Watch this-")
average_item = objects.pop(0)
objects.insert(0, "Narrator")
print(f"here is your new list: {objects}")
print(f"I am afraid '{average_item}' gave it's place to {objects[0]}.")

ending = input(f"Fortunately, it seems am I first in your list! (Suddenly, {name} recieves a hint from a remarkable computational developer to type 'reverse') ").strip().lower()
if ending == "reverse":
    objects.reverse()
    print(objects)
    print(f"Damn you {name}! Till we meet again!")
else:
    print("A flying unicorn jumps out the bushes. Are you happy with your decision?")






