#Forgotten Artifacts

#Introduction

import time
from idlelib.sidebar import temp_enable_text_widget
from random import choice


#from random import random


#Shows text by the character
def text_print(text, delay=0.00):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

#Prologue
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
# #Loop unitl correct choice is made
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
#
# #Dungeon 1 Pyramid
#
#Inventory
inventory = ["Torch"]

#shows inventory
def inv():
    if inventory:
        print("You have: ")
        #iteratese over inventory and returns index i and the items.
        for i, item in enumerate(inventory, start=1):
            print(f"{i}. {item}")
    else:
        print("You don't have any items")

# #Walking through the Pyramid
# text_print("Narrator - You walk through the entrance corridor")
# text_print("It's getting quite dark")
# text_print("Narrator - You look into the the backpack that you took with you")
# text_print("Narrator - type inv to show inventory")
# openinv = input("> ").lower
#
# #Using torch
# if openinv == "inv":
#     inv()
#
# text_print("Would you like to use an item? (yes/no): ")
# while True:
#     useitem = input("> ").lower()
#     if useitem == "yes":
#         text_print("Narrator - You decide to use the Torch.")
#         text_print("Just want I needed a torch.")
#         text_print("Narrator - You use the torch, the corridor was lit up")
#         text_print("Narrator - You see a pressure plate and managed to avoid it")
#         text_print("Good thing I saw that. That could have been bad.")
#         break
#     elif useitem == "no":
#         text_print("You decide not to use the Torch.")
#         text_print("You keep travelling the corridor and step on a pressure plate")
#         text_print("You fall to your death.")
#         text_print("Game over, Please try again.")
#     else:
#         text_print("Invalid input please try again.")
#
# #Entering the kings chamber
# text_print("Narrator - you keep walking whilst avoiding obstacles.")
# text_print("A door, and it is sealed. Hmmmm, how do I open it?")
# text_print("Narrator - you look to right of the door and see 4 familiar symbols.")
# text_print("Those look like hieroglyphics. I wonder if I can use those to activate the door.")
# text_print("Narrator - you put your hands on the symbols and managed to press it.")
# text_print("Narrator - it made a sound")
# text_print("Did that do it?")
# text_print("Narrator - you try to open the door but to no avail.")
# text_print("Guess I might need to press it in an order.")
#
# #Puzzle 1 Kings chamber door.
# correct_order = ["sun", "bird", "tree", "river"]
#
# #Check if sequence is correct
# def check_sequence(player_sequence):
#     return player_sequence == correct_order
#
# #Loop
# text_print("Narrator - you take a close look at the hieroglyphics.")
# text_print("These symbols they look like something.")
# text_print("The 4 hieroglyphics are 'tree, sun, river, bird'")
# text_print("And a clue. 'From the Heaven to the Earth and sea'")
# text_print("What should the order be? ")
#
#
# #Player keeps entering input unitl correct number of entries
# while True:
#     text_print("What should the order be? ")
# #Reset player's sequence
#     player_sequence = []
# #Input the sequence
#     while len(player_sequence) < len(correct_order):
# # New line for each input
#         doorchoice = input("\nEnter your choice (tree/sun/river/bird): ").lower()
#
#         if doorchoice in ["sun", "bird", "tree", "river"]:
#             player_sequence.append(doorchoice)
#             text_print(f"You pressed the {doorchoice} hieroglyphic.")
#         else:
#             text_print("Invalid choice. Please try again.")
#
#     if check_sequence(player_sequence):
#         text_print("Narrator - The door opens as the symbols light up.")
#         break
#     else:
#         text_print("Narrator - The sequence is incorrect. And the hieroglyphics reset. Try again.")
#
# #Enter the King Chamber
# text_print("Narrator - You open the door and see a sarcophagus")
# text_print("This must be the King's chamber")
# text_print("Time to grab the artifact.")
# text_print("Narrator - You remember the words of the hooded man at the entrance warning you to not go in")
#
# #Getting the map
# while True:
#     pickupitem = input("Do you open the sarcophagus? (yes/no): ").lower()
#     if pickupitem == "yes":
#         text_print("Narrator - You open the sarcophagus")
#         break
#     elif pickupitem == "no":
#         text_print("Narrator - You step away from the sarcophagus")
#         text_print("I have a bad feeling about this")
#         text_print("Narrator - As you step back the door behind you closes but the door opposite to the room opens")
#         text_print("What could that be?")
#         text_print("Narrator - As the door opens a stone creature emerges and lunges to attack you")
#         text_print("Narrator - You Died")
#         exit()
#     else:
#         text_print("Invalid input please try again.")
# #Looking at the mummy?
# text_print("Narrator - You look inside the sarcophagus")
# text_print("Narrator - As you open it a large amount of dust spewed out")
# text_print("There is no artifact here, where could it be?")
# text_print("Narrator - You take a deeper look into the sarcophagus and see a skeleton holding a map")
# text_print("Narrator - You think to yourself for a second")
# text_print("Wait a second this is a skeleton not a mummy, this isn't the kings room this is a fake room.")
# text_print("Narrator - As you ponder on the thought you hear the door behind you close. But the opposite of the room opens")
# text_print("What could that be?")
# text_print("Narrator - As the door opens a stone creature emerges")
# #Hide
# while True:
#     hide1 = input("Do you hide in the sarcophagus? (yes/no): ").lower()
#     if hide1 == "yes":
#         text_print("Narrator - You jump in the sarcophagus next to the mummy")
#         break
#     elif hide1 == "no":
#         text_print("Narrator - You step away from the sarcophagus")
#         text_print("Narrator - The stone creature attacks you")
#         text_print("Narrator - You Died")
#         exit()
#     else:
#         text_print("Invalid input please try again.")
#
#Getting to the new area
# text_print("Narrator - As you jump in the bottom of the sarcophagus breaks and you and the skeleton fall.")
# text_print("Ahh my head. Where am I now?")
# text_print("Narrator - You move your hand and notice the map next to you.")
# text_print("Narrator - You picked it up.")
#
# while True:
#     pickupmap = input("Do you read the map? (yes/no): ").lower()
#     if pickupmap == "yes":
#         text_print("Narrator - You opened the map and see that you are just underneath the false King's chamber")
#         text_print("There is another King's chamber here.")
#         text_print("Narrator - You put the map away, and picked yourself up.")
#         inventory.append("Map")
#         text_print("Narrator - You picked up a map.")
#         break
#     elif pickupmap == "no":
#         text_print("Narrator - You put the map away, and picked yourself up.")
#         inventory.append("Map")
#         text_print("Narrator - You picked up a map.")
#         break
#     else:
#         text_print("Invalid input please try again.")
#
# #Corridor
# text_print("Narrator - You walk down the corridor and spot familiar looking symbols on the tile.")
# text_print("More hieroglyphics")
# text_print("Narrator - You pick up a piece of bone from the skeleton and throw it at a tile.")
# text_print("Narrator - The tile drops and along with the bone into a spikey pit")
# text_print("Guess I got to stand on the right symbols.")

# #Floor puzzle
# floor_sequence = ["snowflake", "bee", "sun", "leaf"]
# #Check for player sequence
# def check_sequence(player_sequence):
#     return player_sequence == floor_sequence
# #Loop for puzzle
# text_print("Narrator - The corridor is made up of a 4x4 grid tile")
# text_print("Narrator - The symbols are:")
# text_print("Leaf, Bee, Sun, Snowflake")
# text_print("There is a clue it reads")
# text_print("Clue: The cycle of the year, from the cold till the heat and back again.")
#
# while True:
#     #Reset choice if incorrect
#     player_sequence = []
#
#     #Player choice in sequence
#     #Loop will iterate 4 times
#     for s in range(len(floor_sequence)):
#         #formatted string to not show {s + 1} but 2,3,4
#         floorsteps = input(f"Step {s + 1}: Choose a symbol (Leaf, Bee, Sun, Snowflake): ").lower()
#         #Check for valid symbols
#         if floorsteps in ["leaf", "bee", "sun", "snowflake"]:
#             player_sequence.append(floorsteps)
#         else:
#             print("Invalid input please try again.")
#             break
#     if check_sequence(player_sequence):
#         text_print("Narrator - You slowly step on each tile with each one lighting up underneath you.")
#         text_print("Narrator - You made it pass the trap.")
#         break
#     else:
#         text_print("Narrator - You step onto the tiles but it collapse under you and you fall into the spikes.")
#         text_print("Narrator - Try again.")

# Onto the kitchen


# while True:
#     text_print("Narrator - You progress down the corridor and enter a fork, what will you do?")
#     choice1 = input("Do you want to (1) Open your inventory or (2) Chose a direction? > ")
#     if choice1 == "1":
#         inv()
#         #Remove whitespace
#         itemchoice = input("Select an item to use. (1) or (2) > ").strip()
#
#         #Checks if choice is a digit
#         if itemchoice.isdigit():
#             #0 based index
#             item_index = int(itemchoice) - 1
#             #Checks if the index is valid
#             if 0 <= item_index < len(inventory):
#                 select_item = inventory[item_index]
#                 #Used the map
#                 if select_item == "Map":
#                     text_print("Narrator - You opened the map.")
#                     text_print("If I go left there is a kitchen. I might find something useful there.")
#                     text_print("Narrator - You put the map away.")
#                 #Used the torch
#                 elif select_item == "Torch":
#                     text_print("Narrator - it did nothing")
#                 else:
#                     text_print("Narrator - Invalid choice please try again.")
#
#
#     elif choice1 == "2":
#         text_print("Narrator - You chose a direction to head to")
#         fork = input("Do you want to go (1) Left, (2) Straight ahead or (3) Right? > ")
#         if fork == "1":
#             text_print("Narrator - You entered to main kitchen.")
#             break
#         elif fork == "2":
#             text_print("Narrator - Head straight on which lead to a locked door.")
#             text_print("There must be a key nearby.")
#         elif fork == "3":
#             text_print("Narrator - You turned right and it lead to a dead end")
#             text_print("Narrator - You turned back around")
#         else:
#             text_print("Invalid input please try again.")
#     else:
#         text_print("Invalid input please try again.")


# import random
#
# def kitchen():
#     storages = {
#         "Cupboards": ["Key"],
#         "Drawer": ["Health Potion", "Nothing"],
#         "Dining Table": ["Health Potion", "Nothing"],
#         "Counter": ["Health Potion", "Nothing", "Nothing"],
#
#     }
#     while storages:
#         #Shows storage locations
#         text_print("Narrator - You look around the kitchen for items. Where do you want to look?")
#         for i, area in enumerate(storages.keys(), start=1):
#             print(f"{i}. {area}")
#             #Player look choice
#         looklocation = input("Where do you want to look: (1,2,3 or 4) > ").strip()
#
#         if looklocation.isdigit():
#             looklocation = int(looklocation)
#             if 1 <= looklocation <= len(storages): #Checks for valid choices
#                 selected_area = list(storages.keys())[looklocation - 1]
#                 text_print(f"Narrator - You searched the {selected_area.lower()}...")
#
#                 #Random selects items from chosen locations
#                 found_item = random.choice(storages[selected_area])
#                 if found_item == "Nothing":
#                         text_print("You found nothing useful.")
#                 else:
#                         text_print(f"You found {found_item}.")
#                         inventory.append(found_item)
#                 #Removes searched locations
#                 del storages[selected_area]
#                 text_print(f"Narrator - You can no longer search the {selected_area.lower()}.")
#             else:
#                     text_print("Narrator - Invalid input.")
#         else:
#                 text_print("Narrator - Invalid input.")
#     #No more places to search
#     if not storages:
#         text_print("Narrator - The kitchen is empty.")
#         text_print("Narrator - You left the kitchen.")
#     #Display inventory
#     text_print("Narrator - You have these items in your inventory: ")
#     for item in inventory:
#         text_print(f"- {item}")
#
#
#
# kitchen()
#
# text_print("I got some good items in the kitchen.")
# text_print("Where to next?")
# text_print("Narrator - You open the map and see that there is a staircase next to you.")
# text_print("Narrator - You decide to head there.")
# text_print("A door. And it's lock as well.")
# text_print("I must have got an item to open this door")
#
# def use_key():
#     if "Key" in inventory:
#         text_print("Narrator - You used the key to unlock the door")
#         inventory.remove("Key")
#
# while True:
#     text_print("Narrator - Do you want to (1) Search your inventory or (2) Find another way in?")
#     keydoor = input("> ").strip()
#
#     if keydoor == "1":
#         #Call the function of using the key
#         use_key()
#         break
#     elif keydoor == "2":
#         text_print("Narrator - You deside to use force to open the door but to avail.")
#
# text_print("Narrator - Your current inventory:")
# if inventory:
#     for item in inventory:
#         text_print(f"- {item}")
# else:
#     text_print("Your inventory is empty.")


def treasure_room():
    weapons = ["Sword", "Bow", "Axe", "Dagger"]
    text_print("Narrator - You go down the stairs and enter the treasure room")
    text_print("Wow look at all this gold.")
    text_print("There are even some weapons and armour. The person here must be a leader for wars.")
    text_print("Narrator - You decide to take some armour to wear but cannot decide on what weapon to take with you.")
    text_print("There are:")

    #Shows available weapons
    for i, weapon in enumerate(weapons, start=1):
        print(f"{i}. {weapon}")

    while True:
        weapon_choice = input("Which one should I take: (1,2,3 or 4): >  ").strip()

        if weapon_choice.isdigit():
            weapon_choice = int(weapon_choice)
            if 1 <= weapon_choice <= len(weapons):
                selected_weapon = weapons[weapon_choice - 1]
                text_print(f"Narrator - You picked up the {selected_weapon}. For some reason it fits your hand perfectly.")
                #Adds weapon to inventory
                inventory.append(selected_weapon)
                text_print(f"Narrator - The {selected_weapon} is now in your inventory.")
                break
            else:
                text_print("Narrator - Invalid input.")
        else:
            text_print("Narrator - Invalid input.")

    text_print("Narrator - Your current inventory:")
    if inventory:
        for item in inventory:
            text_print(f"- {item}")

treasure_room()

#Real King's Chamber
text_print("Narrator - Whilst you admire your new equipment, you notice a grand door at the end of the room.")
text_print("That must be it right, the real King's Chamber.")
text_print("Narrator - As you approach it the door automatically opens as if it was waiting for you.")
text_print("That's a bit creepy but whats inside?")
text_print("Narrator - You look inside of the room and see a mummy sitting on a throne at the end of the room.")
text_print("Narrator - The mummy was wearing a golden mask and holding an amulet.")
text_print("That must be it. That is the King wearing his crown and what he is holding there is the artifact.")









