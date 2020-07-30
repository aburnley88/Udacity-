import time
items = []

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(.5)

def intro():
    print_pause("You have just arrived at your new job!")
    print_pause("You are in the elevator.")


def lobby():
    print_pause("You push the button for the 1st floor")
    print_pause("After a few moments, you find yourself in the lobby")
    if "ID Card" in items:
        print_pause("The clerk greets you, but she has already given you your ID card, so there is nothing more to do here.")
        print_pause("Where would you like to go next?")
    else:
        print_pause("The clerk greets you and gives you your ID card.")
        items.append("ID Card")

    choices()

def human_resources():
    print_pause("You push the button for the 2nd floor.")
    print_pause("After a few moments, you find yourself in the Human Resources Department.")
    if "ID Card" in items:
        print_pause("The head of HR greets you.")
        print_pause("He looks at your ID card and then gives you a copy of the employee handbook.")
        items.append("employee handbook")
    else:
        print_pause("The HR folks are busy at their desks. There doesn't seem to be much to do here.")
        print_pause("Where would you like to go next?")
    choices()

def engineering_dept():
    print_pause("You push the button for the 3rd floor.")
    print_pause("After a few moments, you find yourself in the Engineering Department.")
    print_pause("This is where you work.")
    if "ID Card" in items:
        print_pause("You use your ID Card to open the door.")
        print_pause("Your Direcor informs you that you need a handbook to begin working.")
        if "employee handbook" in items:
            print_pause("Good thing you got it already!")
            print_pause("Congrats on your 1st day as the new VP of engineering!!")
        else:
            print_pause("The Director scowls with disguts with your indolence and sends you back to the elevator.")
            print_pause("Where would you like to go next?")
            choices()
    else:
        print_pause("Shoot! The door is locked if only you had a card key to get in...")
        print_pause("With your head hanging low you scuttle back to the elevator.")
        print_pause("Where would you like to go next?")
        choices()

def choices():
    print_pause("Please enter the number for the floor you would like to visit:")
    floor = input("1. Lobby\n" "2. Human resources\n" "3. Engineering department\n")
    if '1' == floor:
        lobby()
    elif '2' == floor:
        human_resources()
    elif '3' == floor:
        engineering_dept()
    else:
        print_pause("Sorry, I don't understand.")
        choices()

def run_game():
    intro()
    choices()

run_game()



