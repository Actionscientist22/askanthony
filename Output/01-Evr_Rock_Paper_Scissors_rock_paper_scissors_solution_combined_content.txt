# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Create a continuous loop so the user can play multiple rounds
while True:
    # User Selection
    user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

    # Check if the user selected a valid choice from the options list
    if user_choice in options:
        # Generate the computer selection
        computer_choice = random.choice(options)

        # Create a variable called user_full_choice to hold the text of the 
        # full word for the user's choice by using a conditional
        if user_choice == 'r':
            user_full_choice = 'rock'
        elif user_choice == 'p':
            user_full_choice = 'paper'
        else:
            user_full_choice = 'scissors'

        # Run Conditionals

        # First check if there is a tie
        if user_choice == computer_choice:
            print(f"You both chose {user_full_choice}!")
            print("A smashing tie!")
        
        # Check if the user picked rock and computer picked paper
        elif (user_choice == "r" and computer_choice == "p"):
            print("You chose rock. The computer chose paper.")
            print("Sorry. You lose.")

        # Check if the user picked rock and computer picked scissors
        elif (user_choice == "r" and computer_choice == "s"):
            print("You chose rock. The computer chose scissors.")
            print("Yay! You won.")

        # Check if the user picked paper and computer picked scissors
        elif (user_choice == "p" and computer_choice == "s"):
            print("You chose paper. The computer chose scissors.")
            print("Sorry. You lose.")

        # Check if the user picked paper and computer picked rock
        elif (user_choice == "p" and computer_choice == "r"):
            print("You chose paper. The computer chose rock.")
            print("Yay! You won.")

        # Check if the user picked scissors and computer picked paper
        elif (user_choice == "s" and computer_choice == "p"):
            print("You chose scissors. The computer chose paper.")
            print("Yay! You won.")

        # Check if the user picked scissors and computer picked rock
        elif (user_choice == "s" and computer_choice == "r"):
            print("You chose scissors. The computer chose rock.")
            print("Sorry. You lose.")

        # Ask the user if they would like to play again and save the answer as 
        # a variable
        print("Would you like to play again?")
        play_again = input("Type (y) to continue or anything else to exit. ")

        # If the user's answer is not "y" or "Y", break from the loop
        if play_again.lower() != "y":
            break
    # Print an error if the user didn't select a valid choice
    else:
        print("I don't understand that!")
        print("Next time, choose from 'r', 'p', or 's'.")

# Say goodbye if the loop has been exited
print("Thank you for playing Rock Paper Scissors. See you next time!")