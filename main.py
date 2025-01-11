#Forgotten Artifacts

#Introduction

import time

#Shows text by the character
def text_print(text, delay=0.00):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# #Prologue
# text_print("Are you ready for the experiment Agennt?")
# text_print("As ready as I'll every be doctor")
# text_print("Firing up the machine")
# text_print("Power is at 10%, How are you feeling?")
# text_print("Nothing abnormal")
# text_print("Good we will keep going. Power is at 50%")
# text_print("Still good")
# text_print("Power is at 80%")
# text_print("Somthing feels off, I'm going numb")
# text_print("Just a little more Agent")
# text_print("I don' think my body can take anymore of this")
# text_print("Power is at 95%, just 5% more")
# text_print("Power is at 100%")
# text_print("UHHHHHH.....")
#
# #Act 1
# text_print("ACT 1")
# text_print("Where am I? Who am I?")
# #Enter name
# name = input("What is your name? ")
# text_print("I remember my name is " + name)
# text_print("Now where am I?")
# text_print("Narrator - you look towards your surroundings and see a looming desert")
# #Where are you
# text_print("Oh this place must me...")
# text_print("1. Ancient Egypt")
# text_print("2. The beach")
# text_print("3. Mars")
#
#Loop unitl correct choice is made
# while True:
#     choice = input("Enter 1, 2, or 3: ")
#     if choice == "1":
#         text_print("Ahh yes this was the place the doctor mentioned")
#         break #Correct choice and ends the loop
#     elif choice == "2":
#         text_print("No, I don't think that was quite what the doctor said")
#     elif choice == "3":
#         text_print("No, I don't think that was quite what the doctor said")
#     else:
#         text_print("Invalid input, Please enter 1, 2 or 3.")
# #Travel to the pyramid
# text_print("Narrator - you picked yourself up and started to walk ")
# text_print("Narrator you dont know where to go so you decided on a random direction ")
#
# #Direction
# text_print("Do you go:")
# text_print("1. North")
# text_print("2. East")
# text_print("3. West")
# text_print("4. South")
# #Chosing the direction
# while True:
#     choice = input("Enter 1, 2, 3 or 4: ")
#     if choice == "1":
#         text_print("Narrator - You travel North for a while but you see nothing in the distance.")
#         text_print("I think I should chose another direction.")
#     elif choice == "2":
#         text_print("Narrator - You travel East and come across an oasis, you take a break.")
#         text_print("I think I should chose another direction.")
#     elif choice == "3":
#         text_print("Narrator - You travel West and come across a small settlement.")
#         text_print("Narrator - you speak to one of the villages")
#         text_print("Do you know where the Pyramids are?")
#         text_print("Narrator - The villager points South")
#         text_print("Guess I'll head south")
#     elif choice == "4":
#         text_print("Narrator - You travel South and after a while you spot a Pyramid, just over the horizon.")
#         text_print("I found it!")
#         text_print("Narrator - The Pyramid stands tall, looking like it was built not long ago, the blocks have not been worn by time")
#         text_print("The time machine worked, I am really back in the past.")
#         break
#     else:
#         text_print("Invalid input, please try again")
# #Hodded man
# text_print("Narrator - You make your way over to the Pyramid")
# text_print("Narrator - As you stand at the entrance a hooded man walks up to you")
# text_print("You don't look like you are from here are you")
# text_print(name +" - No I am just a traveller")
# text_print("Hooded man - Is that so. Anyways, what brings you here.")
# text_print(name +" - Just some sight seeing.")
# text_print("Hooded man - We both no that is a lie. You are really here for the treasure")
# text_print(name +" - ....")
# text_print("Hooded man - Your silence tells me time right. I am not going to stop you but you best be careful")
# text_print(name +" - Why is that?")
# text_print("Hooded man - You didn't know about the rumors? The ones about the curse they put inside the Pyramid")
# text_print("Hooded man - It was to stop people like you from getting in")
# text_print(name +" - Well too far to back off now")
# text_print("Hooded man - Be my guess")
# text_print("Narrator - You look back into the dark entrance of the Pyramid and when you looked back to bid the man farewell he was gone")
# text_print("Narrator - You entered the Pyramid")

#Dungeon 1 Pyramid

#Inventory
inventory = ["Torch"]

#shows inventory
def inv():
    if inventory:
        print("You have: ")
        for item in inventory:
            print(f"- {item}")
    else:
        print("You don't have any items")

#Walking through the Pyramid
text_print("Narrator - You walk through the entrance corridor")
text_print("It's getting quite dark")
text_print("Narrator - You look into the the backpack that you took with you")
text_print("Narrator - type inv to show inventory")
openinv = input("> ").lower

#Using torch
if openinv == "inv":
    inv()

text_print("Would you like to use an item? (yes/no): ")
while True:
    useitem = input("> ").lower()
    if useitem == "yes":
        text_print("Narrator - You decide to use the Torch.")
        text_print("Just want I needed a torch.")
        text_print("Narrator - You use the torch, the corridor was lit up")
        text_print("Narrator - You see a pressure plate and managed to avoid it")
        text_print("Good thing I saw that. That could have been bad.")
        break
    elif useitem == "no":
        text_print("You decide not to use the Torch.")
        text_print("You keep travelling the corridor and step on a pressure plate")
        text_print("You fall to your death.")
        text_print("Game over, Please try again.")
    else:
        text_print("Invalid input please try again.")

#Entering the kings chamber
text_print("Narrator - you keep walking whilst avoiding obstacles.")
text_print("A door, and it is sealed. Hmmmm, how do I open it?")
text_print("Narrator - you look to right of the door and see 4 familiar symbols.")
text_print("Those look like hieroglyphics. I wonder if I can use those to activate the door.")
text_print("Narrator - you put your hands on the symbols and managed to press it.")
text_print("Narrator - it made a sound")
text_print("Did that do it?")
text_print("Narrator - you try to open the door but to no avail.")
text_print("Guess I might need to press it in an order.")

#Puzzle 1 Kings chamber door.
def check_sequence(player_sequence):
    return player_sequence == correct_order

#loop
text_print("Narrator - you take a close look at the hieroglyphics.")
text_print("These symbols they look like something.")
text_print("The 4 hieroglyphics are 'tree, sun, river, bird'")
text_print("What order should I press these in")
text_print("The first one is:")

while True:
    pressbutton = input("> ").lower()
    if pressbutton == "sun":









