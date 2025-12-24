# RPG inventory system controlled by a dict
# can add items, remove them, use them, and check their price

inventory_system = {
    "sword" : {
        "damage" : 10,
        "value" : 50,
        },
    "potion" : {
        "healing" : 100,
        "value" : 5,
        },          
}

choice = input("You can add items with 'add', remove them with 'remove', use them with 'use', or check prices with 'price': ").strip().lower()
if choice == "add":
    temporary = {}

    item = input("What item do you want to add? Examples inlude 'sword' and 'potion': ")
    stats = int(input("How many stats do you want to add? I would advise having at least a price: "))

    for number in range(stats):
        ability = input("The statistic you want to add. Examples: 'power', 'healing': ").strip().lower()
        value = input("The value of the ability you just chose. Examples: '10', '50': ")
        temporary[ability] = value
    inventory_system[item] = temporary
    print(inventory_system)

elif choice == "remove":
    removed = input("Which item do you want to remove: ").strip().lower()
    del inventory_system[removed]

elif choice == "use":
    picked = input("which item do you want to use: ")
    print(f"\nThe item you have selected is {picked.title()}. Here are it's statistics: ")
    for desired, info in inventory_system[picked].items():
        print(f"{desired.title()} has a magnitude of {info}")