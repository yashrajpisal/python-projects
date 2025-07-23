import random as rd

user_ch = input("Enter your choice.(Rock , Paper or Scissor): ")

list = ["Rock","Paper","Scissor"]

computer_ch = rd.choice(list)


if user_ch == "Rock" and computer_ch == "Paper":
    result = "Computer wins"
elif user_ch == "Rock" and computer_ch == "Scissor":
    result = "User wins"
elif user_ch == "Paper" and computer_ch == "Rock":
    result = "User wins"
elif user_ch == "Paper" and computer_ch == "Scissor":
    result = "Computer wins"
elif user_ch == "Scissor" and computer_ch == "Rock":
    result = "computer wins"
elif user_ch == "Scissor" and computer_ch == "Paper":
    result = "User wins"
else:
    result = "Draw"

print("The computer choice:",computer_ch)
print("The result is:",result)