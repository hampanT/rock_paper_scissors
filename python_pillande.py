#Hampans hemkok av spaghettikod, endast lagad med de finaste kodstrukturerna och de finaste variablerna.
from operator import contains
import random


#rock papper scissors
def rock_paper_scissors(): #move : str
    
    def check_if_valid_move(user_move):
        if not ((user_move == "rock") or (user_move == "paper") or (user_move == "scissor")):
            print("Invalid input, input must be: rock, paper or scissor")
            return False
        return True
     
    
    
    print("Welcome to rock - paper - scissors :D")

    user_score = 0
    computer_score = 0

    previous_move = ""
    

  
    while ((user_score <= 3) or (computer_score <= 3)):
        

        previous_move = ""
        user_move = str(input("Choose your next move: ")).lower()
        computer_move = random.choice(["rock", "paper", "scissor"])  

        #print("User move: ", user_move)
        #print("Computer move: ", computer_move)
        def computer_logic():
            
            previous_move = user_move

            if user_move == "rock" and previous_move == user_move:
                computer_move = "paper"
                print("Hello 2 rocks :DDD")
            elif user_move == "paper" and previous_move == user_move:
                computer_move = "scissor"
                print("SCISSOOOOOOR")
            elif user_move == "scissor" and previous_move == user_move:
                computer_move = "rock"
                print("ROOOOOOOOOOOOOKKK")



        

        if check_if_valid_move(user_move):

            computer_logic()
            if user_move == computer_move:
                print("Player move: ", user_move)
                print("Computer move: ", computer_move)
                print("It's a draw!!!!")
                print(f"User score is: {user_score}, computer score is: {computer_score}")

            elif (user_move == "rock") and (computer_move == "scissor"):
                print("Player move: ", user_move)
                print("Computer move: ", computer_move)
                print("Rock beats scissor, player won this round")
                user_score += 1
                print(f"User score is: {user_score}, computer score is: {computer_score}")

            elif (user_move == "paper") and (computer_move == "rock"):
                print("Player move: ", user_move)
                print("Computer move: ", computer_move)
                print("Paper beats rock, player won this round")
                user_score += 1

                print(f"User score is: {user_score}, computer score is: {computer_score}")

            elif (user_move == "scissor") and (computer_move == "paper"):
                print("Player move: ", user_move)
                print("Computer move: ", computer_move)
                print("Scissor beats paper, player won this round")
                user_score += 1
                
                print(f"User score is: {user_score}, computer score is: {computer_score}")


            elif (computer_move == "rock") and (user_move == "scissor"):
                print("Player move: ", user_move)
                print("Computer move: ", computer_move)
                print("Rock beats scissor, computer won this round")
                computer_score += 1

                print(f"User score is: {user_score}, computer score is: {computer_score}")

            elif (computer_move == "paper") and (user_move == "rock"):
                print("Player move: ", user_move)
                print("Computer move: ", computer_move)
                print("Paper beats rock, computer won this round")
                computer_score += 1

                print(f"User score is: {user_score}, computer score is: {computer_score}")

            elif (computer_move == "scissor") and (user_move == "paper"):
                print("Player move: ", user_move)
                print("Computer move: ", computer_move)
                computer_score += 1
                print("Scissor beats paper, computer won this round")
                print(f"User score is: {user_score}, computer score is: {computer_score}")
            



            if (user_score == 3) or (computer_score == 3):
                print("Game over!")
                if user_score == 3:
                    print("The player has won!")
                elif computer_score == 3:
                    print("Computer has won!")
                break

rock_paper_scissors()

