import random 

gameOptions = ["Rock", "Paper", "Scissors"]

def game():

   user_action = int(input("Would you like to play a game of Rock-Paper-Scissors? \n 1.(Yes) \n 2.(No) \n "))
   
   if user_action == 1:
       print("Welcome")
       in_game()
   elif user_action == 2:
       exit()
   else:
       print("Invalid Choice. Try Again.")
       game()

def in_game():
    while True:

        user_choice = input("Enter your choice: \n R for rock \n P for paper \n S for scissors  \n")
        if user_choice in ("R", "P", "S"):
            if user_choice == "R":
                user = gameOptions[0]
            if user_choice == "P":
                user = gameOptions[1]
            if user_choice == "S":
                user = gameOptions[2]
            possible_choices = ["R", "P", "S"]
            computer_choice = random.choice(possible_choices)
            if computer_choice in ("R", "P", "S"):
                if computer_choice == "R":
                    computer = gameOptions[0]
                if computer_choice == "P":
                    computer = gameOptions[1]
                if computer_choice == "S":
                    computer = gameOptions[2]
                print("Player(%s): Computer(%s)" % (user, computer))
            
            if user_choice == computer_choice:
                print("It's a tie! Play Again.")
                in_game()
            elif user_choice == "R":
                if computer_choice == "S":
                    print("Rock beats scissors! You win!")
                else:
                    print("Paper beats rock! You lose.")
            elif user_choice == "P":
                if computer_choice == "R":
                    print("Paper beats rock! You win!")
                else:
                    print("Scissors beats paper! You lose.")
            elif user_choice == "S":
                if computer_choice == "P":
                    print("Scissors beats paper! You win!")
                else:
                    print("Rock beats scissors! You lose.")

            play_again = input("Do you want to play again? (yes/no): \n")
            if play_again == "yes":
                pass
            if play_again == "no":
                print("Thanks for playing. Hope to see you soon.")
                exit() 
        else:
            print("Invalid Input. Try Again.")


game()