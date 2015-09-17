import simplegui
import random

# Functions that compute RPSLS
def name_to_number(name):
    if (name=="rock"):
        return 0;
    elif (name=="Spock"):
        return 1;
    elif (name=="paper"):
        return 2;
    elif (name=="lizard"):
        return 3;
    elif (name=="scissors"):
        return 4;
    else:
        return 100;

def number_to_name(number):
    if (number==0):
        return "rock";
    elif (number==1):
        return "Spock";
    elif (number==2):
        return "paper";
    elif (number==3):
        return "lizard";
    elif (number==4):
        return "scissors";
    else:
        return number


def rpsls(guess):  
    print
    player_number=name_to_number(guess) 
    comp_number = random.randint(0,5)
    comp_choice=number_to_name(comp_number);
    if (player_number==100):
        return "Bad input "+guess+" to rpsls"
    
    print "Player chooses",guess
    print "Computer chooses ",comp_choice
    if ((player_number-comp_number)%5==1) or ((player_number-comp_number)%5==2):
        return "Player wins!"
    elif ((player_number-comp_number)%5==3) or ((player_number-comp_number)%5==4):
        return "Computer wins!"
    elif ((player_number-comp_number)%5==0): 
        return "Player and computer tie!"

    
# Handler for input field
def get_guess(guess):
    print rpsls(guess)
    

    


# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("GUI-based RPSLS", 200, 200)
frame.add_input("Enter guess for RPSLS", get_guess, 200)


# Start the frame animation
frame.start()


