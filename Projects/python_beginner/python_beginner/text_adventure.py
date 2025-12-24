# Plot: Character attempts to learn python but is stopped by a futuristic intelligence agency

# notes:
# make a function that defines 'he' or 'she'

inventory = {}

def add_item(item):
    #add an item to the players inventory
    print("Not finished yet, here so code works...")

def choice_2(option_1, option_2):
    # quickly simulate a choice with 2 options, could go crazy and make it any number of options in future
    while True:
        choice = input(f"{option_1} or {option_2}? ").strip().lower()
        if choice == option_1:
            return True
        elif choice == option_2:
            return False
        else:
            continue
       
while True:
    name = input("Welcome, what is your name: ").lower().strip().title()
    print(f"Hello {name.title()}!")
    if choice_2("yes", "no"):
        break

print(f"On christmas day in Nottingham, {name} is cooped up in his bedroom.")
print(f"It is dark and moody. \n{name} is just finishing up his glass of orange juice when he spots a glint under his bed. ")
if choice_2("investigate", "ignore"):
    print(f"{name} picks up the mysterious object- ")
    print(f"He narrows his eyes as he adjusts to the darkness- ")
    print(f"'What the hell?' {name} exclaims 'It's a python book!'")
else:
    print("boring")



