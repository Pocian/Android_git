import random
options = ["r","p","s"]
score = 0
attempts = 0
while attempts < 5:
  computer_choice = random.choice(options)
  player_choice = input("Enter your choice: for Rock>r, Paper>p, Scissor>s: ")
  if player_choice == computer_choice:
    print("Stalemate! Try again")
  elif player_choice=="r" and computer_choice =="p":
    print("You have lost!")
    attempts+=1
  elif player_choice == "r" and computer_choice=="s":
    print("Won!")
    score+=1
    attempts+=1
  elif player_choice=="s" and computer_choice=="p":
    print("Won")
    score+=1
    attempts+=1
  elif player_choice=="s" and computer_choice=="r":
    print("You have lost!")
    attempts+=1
  elif player_choice =="p" and computer_choice=="r":
    print("Won")
    score+=1
    attempts+=1
  elif player_choice=="p" and computer_choice=="s":
    print("You have lost")
    attempts+=1
  else:
    print("Invalid input,try again")
print(f"Your total score is {score}")
  
  