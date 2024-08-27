# +++++++++++++++++++++++++++++++++++++++++
#   Search for the Smurfs Village game
# +++++++++++++++++++++++++++++++++++++++++

import time
import random


# Function to print a message and sleep for a specified time
def print_sleep(message, wait_time=1):
    print(message)
    time.sleep(wait_time)


# Global variables
map_found = False
key_found = False
protection = 0


# Function for the cave exploration
def cave():
    global map_found, key_found, protection
    print_sleep(" |You are now inside the ancient cave of Malmö, "
                "and this cave contains a lot of mysteries,\n"
                "so you will have several possibilities presented to "
                "you, and you will have to choose between them.|")
    print_sleep("-----------------------------------")
    print_sleep("1 Find a box ")
    print_sleep("2 Find the key to an old house ")
    print_sleep("3 Get a meal")
    print_sleep("4 Get protection")
    print_sleep("5 Return to the forest")
    print_sleep("-----------------------------------")

    choice = ''
    while choice not in ['1', '2', '3', '4', '5']:
        choice = input("(Please enter 1, 2, 3, 4, or 5.)\n")

    if choice == '1':
        find_box()
    elif choice == '2':
        find_key()
    elif choice == '3':
        get_meal()
    elif choice == '4':
        get_protection()
    elif choice == '5':
        print_return_forest()
        return_to_forest()


# function print return to the forest word
def print_return_forest():
    print_sleep(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print_sleep("|You are back in the forest.|")


# Function for finding a box with a map
def find_box():
    global map_found
    print_sleep("|You find a box inside which there is a map.|")
    print_sleep("|This map explains the way to reach the Smurfs village "
                "by walking through the trees and following a safe path.|")
    map_found = True
    print_return_forest()
    return_to_forest()


# Function for finding a key to an old house
def find_key():
    global key_found
    print_sleep("|You have found the key to an old house.|")
    print_sleep("|This key belongs to the Smurfs' grandfather and will "
                "help you find the secret Smurf village.|")
    key_found = True
    print_return_forest()
    return_to_forest()


# Function for getting a meal
def get_meal():
    global protection
    meals = ['cranberries', 'coconut', 'Malmo meal', 'cane meal', 'sumo meal']
    food = random.choice(meals)
    print_sleep(f"You got a meal of {food}.")

    choice = ''
    while choice not in ['1', '2']:
        print_sleep("Do you want to eat it or throw it away? "
                    "(1 for eat, 2 for throw)")
        choice = input()

        if choice == '1':
            if food in ['cranberries', 'sumo meal']:
                if protection > 0:
                    print_sleep("This food is poisonous, "
                                "but you have been protected from harm.")
                else:
                    print_sleep("This food is poisonous"
                                " and you have been eliminated.")
                    play_again()
            else:
                print_sleep(f"The meal of {food} is"
                            "nutritious and full of energy.")
            print_return_forest()
            return_to_forest()
        elif choice == '2':
            print_sleep("You threw the food away. Returning to the forest.")
            print_return_forest()
            return_to_forest()


# Function for obtaining protection
def get_protection():
    global protection
    if protection == 0:
        protection += 1
        print_sleep("|Well done :) , a wonderful choice. \n"
                    "You have obtained a means of "
                    "protection from something harmful or dangerous"
                    " that may appear in front of you later.|")
    else:
        print_sleep("You already have protection."
                    "You cannot obtain it again in this game.")
    print_return_forest()
    return_to_forest()


# Function for exploring the house
def house():
    global key_found

    print_sleep("|Welcome to Grandfather Smurf's house.|\n"
                "|This house belongs to Papa Smurf's father."
                " It is the origin of "
                "the Smurf village in a secret place in the forest.|\n"
                "|This house was abandoned after his death.|")

    while True:
        print_sleep("|You can now enter the house or explore the garden.|")
        print_sleep("-----------------------------------")
        print_sleep("1 Check out the garden")
        print_sleep("2 Enter the house")
        print_sleep("-----------------------------------")

        choice = input("(Please enter 1 or 2.)\n")

        if choice == '1':
            garden()
            break
        elif choice == '2':
            if key_found:
                enter_house()
                break
            else:
                print_sleep("|This is Grandpa Smurf’s house,"
                            " and it is the origin of "
                            "the Smurf village in the forest,\n"
                            "but you do not have the key to the house."
                            " You cannot enter:(")
                print_sleep("|You can either >>> |")
                print_sleep("-----------------------------------")
                print_sleep("1 Return to the forest")
                print_sleep("2 Check out the garden")
                print_sleep("-----------------------------------")

                while True:
                    choice = input("(Please enter 1 or 2.)\n")

                    if choice == '1':
                        print_return_forest()
                        return_to_forest()
                        break
                    elif choice == '2':
                        garden()
                        break
                    else:
                        print_sleep("Invalid choice. Please enter 1 or 2.")
        else:
            print_sleep("Invalid choice. Please enter 1 or 2.")


# Function for exploring the garden
def garden():
    global key_found
    print_sleep("|This is the garden of Grandpa Smurf’s house."
                " There are two options: |")
    print_sleep("-----------------------------------")
    print_sleep("1) Enter the wooden house")
    print_sleep("2) Sit on the old chair\n")
    print_sleep("-----------------------------------")

    choice = ''
    while choice not in ['1', '2']:
        choice = input("(Please enter 1 or 2.)\n")

    if choice == '1':
        enter_wooden_house()
    elif choice == '2':
        sit_on_chair()


# Function for entering the wooden house
def enter_wooden_house():
    global protection
    print_sleep("|You enter the wooden house and find a"
                " predatory animal inside. It attacks you -_- ")
    print_sleep("Do you want to 1) Return or 2) Attack? |")
    print_sleep("-----------------------------------")

    choice = ''
    while choice not in ['1', '2']:
        choice = input("(Please enter 1 or 2.)\n")

    if choice == '1':
        print_return_forest()
        return_to_forest()
    elif choice == '2':
        if protection > 0:
            print_sleep("You fight off the predatory animal with"
                        " your protection and return to the forest.")
            print_return_forest()
            return_to_forest()
        else:
            print_sleep("You do not have protection or a powerful weapon."
                        " You have been eliminated by the predatory animal.")
            play_again()


# Function for sitting on the old chair
def sit_on_chair():
    global key_found
    if not key_found:
        print_sleep("Great choice. Grandpa Smurf has hidden a key"
                    " to his house in the left hand of the wooden chair."
                    " You have found the key.")
        key_found = True
    else:
        print_sleep("Here Grandpa Smurf hides a copy of the key,"
                    " but you already have the key to the house.")
    print_return_forest()
    return_to_forest()


# Function for entering the house
def enter_house():
    global protection
    print_sleep("|You are now inside Grandpa Smurf’s house"
                " because you have a key.\n "
                "There are the following options: |")
    print_sleep("-----------------------------------")
    print_sleep("1) Enter Grandpa Smurf's bedroom")
    print_sleep("2) Obtain Grandpa Smurf's secret box")
    print_sleep("3) Return to the forest")
    print_sleep("-----------------------------------")

    choice = ''
    while choice not in ['1', '2', '3']:
        choice = input("(Please enter 1, 2, or 3.)\n")

    if choice == '1':
        enter_bedroom()
    elif choice == '2':
        secret_box()
    elif choice == '3':
        print_return_forest()
        return_to_forest()


# Function for entering Grandpa Smurf's bedroom
def enter_bedroom():
    global protection
    print_sleep("|You are in Grandpa Smurf's bedroom.\n"
                "There is a secret door that leads to a tunnel. |")

    # Randomly choose between 1 and 2
    destination = random.choice(['1', '2'])

    if destination == '1':
        print_sleep("|Congratulations!:) \n"
                    "|You have reached your destination and found the "
                    "Smurfs’ secret village in the forest.|\n"
                    "|You have won the game :> |")
        play_again()
    elif destination == '2':
        if protection > 0:
            print_sleep("|The tunnel leads to Gargamel's house :< \n"
                        "but because you have protection,\n"
                        "you will defeat him and gain a"
                        " new protection value of +1.|")
            protection += 1
            return_to_house()
        else:
            print_sleep("|The tunnel leads to Gargamel's house :(.|\n"
                        "|You faced Gargamel, and without protection,|\n"
                        "|you were eliminated :( |")
            play_again()


# Function for returning to the house after the tunnel
def return_to_house():
    print_sleep("You leave the house and return to the forest.")
    print_return_forest()
    return_to_forest()


# Function for obtaining Grandpa Smurf's secret box
def secret_box():
    global protection
    items = ['a means of protection', 'nothing']
    item = random.choice(items)

    if item == 'a means of protection':
        protection += 1
        print_sleep("|You have obtained Grandpa Smurf's secret box.\n"
                    " Inside it is a means of protection,\n"
                    " |increasing your protection counter by 1.|")
    else:
        print_sleep("|You have obtained Grandpa Smurf's secret box, "
                    "but it is empty.|")

    print_sleep("|Do you want to stay in the house or return to "
                "the forest? |")
    print_sleep("-----------------------------------")
    print_sleep("1) Stay in the house")
    print_sleep("2) Return to the forest")
    print_sleep("-----------------------------------")

    choice = ''
    while choice not in ['1', '2']:
        choice = input("(Please enter 1 or 2.)\n")

    if choice == '1':
        enter_house()
    elif choice == '2':
        print_return_forest()
        return_to_forest()


# Function for returning to the forest
def return_to_forest():
    print_sleep("|You can now choose to explore the cave,"
                " the house, or the road full of trees.|")
    print_sleep("-----------------------------------")
    print_sleep("1 Enter the cave")
    print_sleep("2 Enter the house")
    print_sleep("3 Take the road full of trees")
    print_sleep("-----------------------------------")

    choice = ''
    while choice not in ['1', '2', '3']:
        choice = input("(Please enter 1, 2, or 3.)\n")

    if choice == '1':
        cave()
    elif choice == '2':
        house()
    elif choice == '3':
        road_of_trees()


# Function for taking the road full of trees
def road_of_trees():
    global map_found
    print_sleep("You are now on a forest road full of dense trees.")
    if map_found:
        print_sleep("You have a map that will guide you to a short, easy, "
                    "and safe route to the secret Smurf "
                    "village in the forest.")
        print_sleep("Congratulations! You have reached your destination and "
                    "found the Smurf village. You have won the game!")
        play_again()
    else:
        print_sleep("|You do not have a map.|\n |Do you want to continue "
                    "walking on the forest path or return to the forest from "
                    "the starting point?|")
        print_sleep("-----------------------------------")
        print_sleep("1 Continue walking")
        print_sleep("2 Return to the forest")
        print_sleep("-----------------------------------")

        choice = ''
        while choice not in ['1', '2']:
            choice = input("(Please enter 1 or 2.)\n")

        if choice == '1':
            predator_encounter()
        elif choice == '2':
            print_return_forest()
            return_to_forest()


# A function to explain what happens
# when you meet a monster
# on a forest path full of trees
def predator_encounter():
    global protection
    predators = ['a dinosaur', 'a dragon', 'a giant tiger',
                 'a wild bear', 'a large poisonous snake']
    predator = random.choice(predators)
    print_sleep(f"A predator has appeared in front of you: {predator}.")
    print_sleep("Do you want to 1) Confront it or 2) Return to the forest?")
    choice = ''
    while choice not in ['1', '2']:
        choice = input("(Please enter 1 or 2.)\n")
    if choice == '1':
        if protection > 0:
            print_sleep(f"You confront the {predator} and successfully "
                        "defeat it with your protection. You return to "
                        "the forest.")
            print_return_forest()
            return_to_forest()
        else:
            print_sleep(f"You do not have protection. The {predator} "
                        "eliminates you. You have been eliminated.")
            play_again()
    elif choice == '2':
        print_sleep("You decide to return to the forest.")
        print_return_forest()
        return_to_forest()


# Function for replaying the game
def play_again():
    print_sleep("-----------------------------------")
    print_sleep("Would you like to play again? (y/n)")
    choice = input().lower()
    if choice == 'y':
        start_game()
    else:
        print_sleep("Thank you for playing! Goodbye!")
        exit()


# Function for starting the game
def start_game():
    global map_found, key_found, protection
    map_found = False
    key_found = False
    protection = 0

    print_sleep("-----------------------------------")
    print_sleep("Welcome to the Search for the Smurfs Village!")
    print_sleep("-----------------------------------")
    print_sleep("You are in a forest full of mysteries and adventures.")
    print_sleep("Your mission is to find the secret Smurf village.")
    return_to_forest()


# Starting the game
start_game()
