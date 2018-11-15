# Rock-paper-scissors-lizard-Spock template

import random

def name_to_number(name):
    if name == "rock":
         return 0
    elif name == "Spock":
         return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return -1
        
def number_to_name(number):
 if number == 0:
       return "rock"
 elif number == 1:
       return  "Spock"
 elif number == 2:
       return  "paper"
 elif number == 3:
       return  "lizard"
 elif number == 4:
       return  "scissors"
 else:
       return "ERROR " + str(number) + " is not a valid option."


def rpsls(player_choice): 
    print
    print "Player chooses " + player_choice
    player_number = name_to_number(player_choice)
    
    if player_number < 0:
        print "ERROR invalid player choice '" + player_choice + "'"
        break
    computer_choice = random.randrange(0,5)
    print "Computer chooses " + number_to_name(computer_choice)
    result = (player_number - computer_choice) %5
    if result == 0:
        print "Tie Game"
    if result == 1 or result == 2:
        print "Player wins!"
    if result == 3 or result == 4:
        print "Computer wins!"

    # use if/elif/else to determine winner, print winner message

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
rpsls("test error")
# always remember to check your completed program against the grading rubric


