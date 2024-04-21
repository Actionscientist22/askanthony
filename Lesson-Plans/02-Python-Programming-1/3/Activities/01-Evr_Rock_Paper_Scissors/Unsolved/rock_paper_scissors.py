# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Create a continuous loop so the user can play multiple rounds

    # User Selection
    user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

    # Check if the user selected a valid choice from the options list
    
        # Generate the computer selection
        computer_choice = random.choice(options)

        # Create a variable called user_full_choice to hold the text of the 
        # full word for the user's choice by using a conditional
        

        # Run Conditionals to determine the result

        # First check if there is a tie
        
            print(f"You both chose {user_full_choice}!")
            print("A smashing tie!")
        
        # Check if the user picked rock and computer picked paper
        
            print("You chose rock. The computer chose paper.")
            print("Sorry. You lose.")

        # Check if the user picked rock and computer picked scissors
        
            print("You chose rock. The computer chose scissors.")
            print("Yay! You won.")

        # Check if the user picked paper and computer picked scissors
        
            print("You chose paper. The computer chose scissors.")
            print("Sorry. You lose.")

        # Check if the user picked paper and computer picked rock
        
            print("You chose paper. The computer chose rock.")
            print("Yay! You won.")

        # Check if the user picked scissors and computer picked paper
        
            print("You chose scissors. The computer chose paper.")
            print("Yay! You won.")

        # Check if the user picked scissors and computer picked rock
        
            print("You chose scissors. The computer chose rock.")
            print("Sorry. You lose.")

        # Ask the user if they would like to play again and save the answer as 
        # a variable
        

        # If the user's answer is not "y" or "Y", break from the loop
        
    # Print an error if the user didn't select a valid choice
    else:
        print("I don't understand that!")
        print("Next time, choose from 'r', 'p', or 's'.")

# Say goodbye if the loop has been exited
print("Thank you for playing Rock Paper Scissors. See you next time!")