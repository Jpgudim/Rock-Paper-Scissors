import random

computer_list = ["rock", "paper", "scissors"]

print ("Welcome to Rock, Paper, Scissors!")

choice = input("type rock, paper, or scissors: ")
choice = choice.lower()

while choice not in computer_list:
    choice = input("Please enter a valid input: ") 
    choice = choice.lower()

c_choice = random.choice(computer_list)

def user_wins():
    print ("You chose %s and the computer chose %s. You win!" % (choice, c_choice))

def computer_wins():
    print ("You chose %s and the computer chose %s. The computer wins." % (choice, c_choice))

if c_choice == choice:
    print ("You both chose %s, that's a draw!" % choice)

if c_choice == "rock" and choice =="scissors":
    print ()
    computer_wins()
if c_choice == "rock" and choice == "paper":
    print ()
    user_wins()
if c_choice == "scissors" and choice == "paper":
    print ()
    computer_wins()
if c_choice == "scissors" and choice == "rock":
    print ()
    user_wins()
if c_choice == "paper" and choice == "rock":
    print ()
    computer_wins()
if c_choice == "paper" and choice == "scissors":
    print 
    user_wins()