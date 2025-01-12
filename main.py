#Forgotten Artifacts

#Introduction

import time


#Shows text by the character
def text_print(text, delay=0.00):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

#Prologue
text_print("Are you ready for the experiment Agennt?")
text_print("As ready as I'll every be doctor")
text_print("Firing up the machine")
text_print("Power is at 10%, How are you feeling?")
text_print("Nothing abnormal")
text_print("Good we will keep going. Power is at 50%")
text_print("Still good")
text_print("Power is at 80%")
text_print("Somthing feels off, I'm going numb")
text_print("Just a little more Agent")
text_print("I don' think my body can take anymore of this")
text_print("Power is at 95%, just 5% more")
text_print("Power is at 100%")
text_print("UHHHHHH.....")

#Act 1
text_print("ACT 1")
text_print("Where am I? Who am I?")
#Enter name
name = input("What is your name? ")
text_print("I remember my name is " + name)
text_print("Now where am I?")
text_print("Narrator - you look towards your surroundings and see a looming desert")
#Where are you
text_print("Oh this place must me...")
text_print("1. Ancient Egypt")
text_print("2. The beach")
text_print("3. Mars")

#Loop unitl correct choice is made
while True:
    choice = input("Enter 1, 2, or 3: ")
    if choice == "1":
        text_print("Ahh yes this was the place the doctor mentioned")
        break #Correct choice and ends the loop
    elif choice == "2":
        text_print("No, I don't think that was quite what the doctor said")
    elif choice == "3":
        text_print("No, I don't think that was quite what the doctor said")
    else:
        text_print("Invalid input, Please enter 1, 2 or 3.")
#Travel to the pyramid
text_print("Narrator - you picked yourself up and started to walk ")
text_print("Narrator you dont know where to go so you decided on a random direction ")

#Direction
text_print("Do you go:")
text_print("1. North")
text_print("2. East")
text_print("3. West")
text_print("4. South")
#Chosing the direction
while True:
    choice = input("Enter 1, 2, 3 or 4: ")
    if choice == "1":
        text_print("Narrator - You travel North for a while but you see nothing in the distance.")
        text_print("I think I should chose another direction.")
    elif choice == "2":
        text_print("Narrator - You travel East and come across an oasis, you take a break.")
        text_print("I think I should chose another direction.")
    elif choice == "3":
        text_print("Narrator - You travel West and come across a small settlement.")
        text_print("Narrator - you speak to one of the villages")
        text_print("Do you know where the Pyramids are?")
        text_print("Narrator - The villager points South")
        text_print("Guess I'll head south")
    elif choice == "4":
        text_print("Narrator - You travel South and after a while you spot a Pyramid, just over the horizon.")
        text_print("I found it!")
        text_print("Narrator - The Pyramid stands tall, looking like it was built not long ago, the blocks have not been worn by time")
        text_print("The time machine worked, I am really back in the past.")
        break
    else:
        text_print("Invalid input, please try again")
#Hodded man
text_print("Narrator - You make your way over to the Pyramid")
text_print("Narrator - As you stand at the entrance a hooded man walks up to you")
text_print("You don't look like you are from here are you")
text_print(name +" - No I am just a traveller")
text_print("Hooded man - Is that so. Anyways, what brings you here.")
text_print(name +" - Just some sight seeing.")
text_print("Hooded man - We both no that is a lie. You are really here for the treasure")
text_print(name +" - ....")
text_print("Hooded man - Your silence tells me time right. I am not going to stop you but you best be careful")
text_print(name +" - Why is that?")
text_print("Hooded man - You didn't know about the rumors? The ones about the curse they put inside the Pyramid")
text_print("Hooded man - It was to stop people like you from getting in")
text_print(name +" - Well too far to back off now")
text_print("Hooded man - Be my guess")
text_print("Narrator - You look back into the dark entrance of the Pyramid and when you looked back to bid the man farewell he was gone")
text_print("Narrator - You entered the Pyramid")

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
correct_order = ["sun", "bird", "tree", "river"]

#Check if sequence is correct
def check_sequence(player_sequence):
    return player_sequence == correct_order

#Loop
text_print("Narrator - you take a close look at the hieroglyphics.")
text_print("These symbols they look like something.")
text_print("The 4 hieroglyphics are 'tree, sun, river, bird'")
text_print("And a clue. 'From the Heaven to the Earth and sea'")
text_print("What should the order be? ")


#Player keeps entering input unitl correct number of entries
while True:
    text_print("What should the order be? ")
#Reset player's sequence
    player_sequence = []
#Input the sequence
    while len(player_sequence) < len(correct_order):
# New line for each input
        doorchoice = input("\nEnter your choice (tree/sun/river/bird): ").lower()

        if doorchoice in ["sun", "bird", "tree", "river"]:
            player_sequence.append(doorchoice)
            text_print(f"You pressed the {doorchoice} hieroglyphic.")
        else:
            text_print("Invalid choice. Please try again.")

    if check_sequence(player_sequence):
        text_print("Narrator - The door opens as the symbols light up.")
        break
    else:
        text_print("Narrator - The sequence is incorrect. And the hieroglyphics reset. Try again.")

#Enter the King Chamber
text_print("Narrator - You open the door and see a sarcophagus")
text_print("This must be the King's chamber")
text_print("Time to grab the artifact.")
text_print("Narrator - You remember the words of the hooded man at the entrance warning you to not go in")

#Getting the map
while True:
    pickupitem = input("Do you open the sarcophagus? (yes/no): ").lower()
    if pickupitem == "yes":
        text_print("Narrator - You open the sarcophagus")
        break
    elif pickupitem == "no":
        text_print("Narrator - You step away from the sarcophagus")
        text_print("I have a bad feeling about this")
        text_print("Narrator - As you step back the door behind you closes but the door opposite to the room opens")
        text_print("What could that be?")
        text_print("Narrator - As the door opens a stone creature emerges and lunges to attack you")
        text_print("Narrator - You Died")
        exit()
    else:
        text_print("Invalid input please try again.")
#Looking at the mummy?
text_print("Narrator - You look inside of the sarcophagus")
text_print("Narrator - As you open it a large amount of dust spewed out")
text_print("There is no artifact here, where could it be?")
text_print("Narrator - You take a deeper look into the sarcophagus and see a skeleton holding a map")
text_print("Narrator - You think to yourself for a second")
text_print("Wait a second this is a skeleton not a mummy, this isn't the kings room this is a fake room.")
text_print("Narrator - As you ponder on the thought you hear the door behind you close. But the opposite of the room opens")
text_print("What could that be?")
text_print("Narrator - As the door opens a stone creature emerges")
#Hide
while True:
    hide1 = input("Do you hide in the sarcophagus? (yes/no): ").lower()
    if hide1 == "yes":
        text_print("Narrator - You jump in the sarcophagus next to the mummy")
        break
    elif hide1 == "no":
        text_print("Narrator - You step away from the sarcophagus")
        text_print("Narrator - The stone creature attacks you")
        text_print("Narrator - You Died")
        exit()
    else:
        text_print("Invalid input please try again.")

#Getting to the new area
text_print("Narrator - As you jump in the bottom of the sarcophagus breaks and you and the skeleton fall.")
text_print("Ahh my head. Where am I now?")

