import random

class Rock_paper_scissors:
    def __init__(self,total_rounds):
        self.total_rounds=total_rounds
        self.user_wins=0
        self.computer_wins=0
    def get_computer_choice(self):
        return random.choice(["rock", "paper", "scissors"])
    def determine_winner(self,user_choice,computer_choice):
        if user_choice == computer_choice:
            return "tie"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            return "user"
        else:
            return "computer"
    def play_round(self,user_choice):
        computer_choice=self.get_computer_choice()
        winner=self.determine_winner(user_choice,computer_choice)
        if winner=='user':
            self.user_wins+=1
        elif winner=='computer':
            self.computer_wins+=1
        return winner,computer_choice
            
game=Rock_paper_scissors(3)
for i in range(game.total_rounds):
    user_choice=input("enter your choice(rock,paper,scissors):")
    winner,computer_choice=game.play_round(user_choice)
    print(f"computer choose:{computer_choice}")
    print(f"{winner} wins the round" if winner!="tie" else "it is a tie")
print(f"User wins: {game.user_wins}, Computer wins: {game.computer_wins}")    
if game.user_wins > game.computer_wins:
    print("User wins the game!")
elif game.computer_wins > game.user_wins:
    print("Computer wins the game!")
else:
    print("The game is a tie!")    
        
