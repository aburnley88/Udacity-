import time
import random
items = ["useless q-tip", "useless q-tip", "useless q-tip"]
elf_gift = ["Golden Key", "Silver Key", "Silver Key", "Silver Key",
            "Silver Key", "Silver Key"]
monsters = ["Psycho Dragon", "Armed Robber", "Sewer Monster"]
imp_gift = ["Bad advice", "Photo of his ex", "Christmas list",
            "tax bill", "connect 4", "dragon dung", "Silver Key", "Golden Key"]


def play_again():
    response = input("Would you like to play again; yes or no?\n")
    if response == 'yes':
        print_pause("Awesome, let's do it!")
        run_game()
    elif response == 'no':
        print_pause("Thank you for playing.")
    else:
        ("You're harshing my vibes, dude.")
        play_again()


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro():
    print_pause("You are a wandering adventurer looking for treasure.")
    print_pause("You are walking along a path and come to a fork in the path.")
    print_pause("There is an old wooden signpost pointing East and West.")
    direction()


def direction():
    print_pause("Towards the East is the Crystal Cave, and to the West is the "
                "Tower of Mysteries.")
    direction = input("Will you go East or West?\n").lower()
    if 'east' == direction:
        print_pause("Off to the caves you go!")
        East()
    elif 'west' == direction:
        print_pause("With a heart full of courage you head towards the tower.")
        West()
    else:
        print_pause("No one speaks gibberish but you! Try again!")
        intro()


def East_alt():
    if 'Reflector Shield' in items:
        print_pause("Strange... the cave and elf have disappeared.")
        print_pause("You head back to the signpost.")
        direction()


def East():
    East_alt()
    print_pause("Near the mouth of the cave you find a large-eared elf.")
    print_pause("The elf asks you your name.")
    print_pause("You tell her but she can't hear you, and explains her ears "
                "are very dirty.")
    print_pause('You check your pouch and find a "useless q-tip"')
    answer = input('"Will you give her your "useless q-tip"; yes or no?"\n')
    if 'yes' == answer:
        items.remove('useless q-tip')
        print_pause('"useless q-tip" removed from pouch')
        print_pause('The elf squeals "you\'re my hero! Thank you!"')
        name = input('Once again she asks, "What\'s your name traveler?"\n')
        print_pause(f'"Thank you, {name}!"')
        print_pause('"Please, take this gift."')
        gift = random.choice(elf_gift)
        items.append(random.choice(elf_gift))
        print_pause(f"{items} are in your pouch.")
        crystal_cave()
    elif 'no' == answer:
        print_pause('The elf says, "Your selfishness will get you nowhere."')
        crystal_cave()
    else:
        print_pause("...huh?")
        East()


def crystal_cave():
    print_pause("You approach the cave and see it is sealed by a large "
                "rainbow door radiating magical energy.")
    print_pause("looks like you need a key to get in.")
    if 'Golden Key' in items:
        print_pause("You open the door to heaps of gold and the "
                    "Diamond crown!")
        print_pause("Congratulations, you beat the game violence free!")
        items.append("Diamond Crown")
        print_pause('"Diamond Crown" added to pouch.')
        play_again()
    elif 'Silver Key' in items:
        print_pause("You use your key to open the door.")
        print_pause("The walls are encrusted with gems of various shapes "
                    "and sizes.")
        print_pause("A silver haired lad appears.")
        print_pause('"Hello, traveler. If you answer my question I\'ll '
                    'give you a prize."')
        print_pause('"I wax I wane and dance upon a celestial plane."')
        print_pause('"Who am I?"')
        answer = input("Type your answer, traveler.\n").lower()
        if 'moon' in answer:
            print_pause('"By Her light we feel!"')
            items.append("Reflector Shield")
            print_pause('"Reflector Shield" added to items')
            print_pause("The lunar boy teleports you back to the signpost.")
            direction()
        else:
            print_pause("...goodbye.")
            print_pause("Your life force slips away...")
            items.remove('Silver Key')
            play_again()
    else:
        print_pause("The door is locked to the greedy.")
        print_pause("You head back to the path")
        direction()


def West():
    print_pause("You head West in search of fabled treasure.")
    print_pause("However, a fickle imp stands in your way.")
    print_pause(' The imp asks, "Are yee a pants of smarty?"')
    reply = input("Yes or no traveler...\n")
    if reply == 'no':
        print_pause("THEN AWAY WITH YEE!")
        print_pause("You suffer a mysterious death.")
        play_again()
    elif 'yes' == reply:
        print_pause('"Great, I have a riddle."')
        print_pause('"You\'ll never see me at midnight, but at noon I\'m '
                    'impossible to miss."')
        print_pause('"Who am I?"')
        answer = input("Type your answer, traveler.\n").lower()
        if 'sun' in answer:
            print_pause('"By His light we live!"')
            gift = random.choice(imp_gift)
            items.append(random.choice(imp_gift))
            print_pause(f"Look at you inventory!{items}")
            print_pause("You continue onwards to the tower.")
            tower()
        else:
            print_pause("...goodbye.")
            West()
    else:
        print_pause("No one speaks gibberish but you! Try again!")
        West()


def tower():
    print_pause("You finally make it to the tower.")
    print_pause("Looks like you need a key to get in.")
    if 'Silver Key' in items:
        villain = random.choice(monsters)
        print_pause(f"You unlock the door and out pops a {villain}.")
        if 'Reflector Shield' not in items:
            print_pause("The monster destroys you in an instant!")
            print_pause("unforgiveable...")
            items.remove('Silver Key')
            play_again()
        print_pause('It fires at you, but you have your "Reflector Shield."')
        print_pause("You raise the shield just in time reflecting the attack "
                    "right back at the monster.")
        print_pause("The monster explodes...whats that inside it's body?")
        answer = input("Will you reach in and grab it? yes or no?\n")
        if 'yes' in answer:
            items.append("Diamond Crown")
            print_pause('"The Diamond Crown" has been added to items.')
            print_pause("Congratulations, traveler this is the most prized "
                        "treasure in the land!")
            items.remove('Silver Key')
            play_again()
        else:
            print_pause("DIE A COWARD!")
            play_again()
    elif 'Golden Key' in items:
        villain = random.choice('monsters')
        print_pause(f"You unlock the door and out pops a(n) {villain}.")
        print_pause('He says, "ah, the Golden Key."')
        print_pause("In that case...")
        items.append("Diamond Crown")
        print_pause('"The Diamond Crown" has been added to items.')
        print_pause("Congratulations, you beat the game violence free!")
        play_again()
    else:
        print_pause("You need a key, butthead!")
        print_pause("You head back to the signpost.")
        direction()


def run_game():
    intro()


run_game()
