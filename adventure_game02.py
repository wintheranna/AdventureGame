import time
import random


def print_pause(message):
    print(message)
    time.sleep(2)


# game introduction
def intro():
    print_pause("You find yourself standing in a dark forest, "
                "filled with tall trees and fern covering the damp ground.")
    print_pause("Rumor has it that a " + enemy + " is attacking humans, "
                "and has been terrifying people in the area.")
    print_pause("In front of you is a tiny crooked house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty "
                "(but not very effective) dagger.\n")


# game starting point, decide where to go
def forest():
    location = input("Enter 1 to knock on the door of the old house.\n"
                     "Enter 2 to peer into the dark cave.\n"
                     "What would you like to do?\n"
                     "(Please enter 1 or 2.)\n")
    if location == "1":
        house()
    elif location == "2":
        cave()
    else:
        forest()


# game location
def house():
    print_pause("You approach the door of the tiny house.")
    print_pause("You are about to knock when the door suddenly opens "
                "and out steps a " + enemy + ".")
    print_pause("Eep! This is the " + enemy + "'s house!")
    if weapon in items:
        print_pause("The " + enemy + " attacks you!")
    else:
        print_pause("The " + enemy + " attacks you!")
        print_pause("You feel a bit under-prepared for this, "
                    "what with only having a tiny unsharp dagger.")
    take_action()


# action to take when in "house"
def take_action():
    action = input("Would you like to (1) fight or (2) run away?\n")
    if action == "1":
        if weapon in items:
            print_pause("As the " + enemy + " moves to attack, "
                        "you unsheath your new " + weapon + ".")
            print_pause("The " + weapon + " shines brightly in your "
                        "hand as you brace yourself for the attack.")
            print_pause("But the " + enemy + " takes one look at your "
                        "shiny new weapon and runs away!")
            print_pause("You have rid the town of the "
                        "torturous " + enemy + ". "
                        "You have won the battle!")
            start_over()
        else:
            print_pause("You do your very best...")
            print_pause("but your dagger is no match for the " + enemy + ".")
            print_pause("You have been defeated!")
            start_over()
    elif action == "2":
        print_pause("You run back into the forest. Luckily, "
                    "you don't seem to have been followed "
                    "by the " + enemy + ".\n")
        forest()
    else:
        take_action()


# game location
def cave():
    print_pause("You peer cautiously into the cave.")
    if weapon in items:
        print_pause("You've been here before, and gotten all "
                    "the good stuff. It's just an empty cave now.")
    else:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical " + weapon + "!")
        print_pause("You discard your silly old dagger and "
                    "take the weapon with you.")
        items.append(weapon)

    print_pause("You walk back out to the forest.\n")
    forest()


# choose whether to exit or play again
def start_over():
    play_again = input("Would you like to play again? (y/n)\n")
    if play_again == "y":
        print_pause("Excellent! Restarting the game ...")
        play_game()
    elif play_again == "n":
        print_pause("Thanks for playing! See you next time.")
    else:
        start_over()


# final game function, plays entire game
def play_game():
    global weapon
    weapons = ["sword of Ogoroth", "crossbow of Aranos",
               "spear of Torenai", "battle axe of Silithus"]
    weapon = random.choice(weapons)
    global enemy
    enemies = ["pirate", "troll", "gorgon", "wicked fairie"]
    enemy = random.choice(enemies)
    global items
    items = []
    intro()
    forest()


# call function
play_game()
