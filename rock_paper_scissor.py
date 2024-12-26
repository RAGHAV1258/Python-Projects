import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_symbols = [rock ,paper ,scissors]

user_choice = int(input("Your choice is Type 0 for rock 1 for paper and 2 for scissor.\n"))
if user_choice >=3 or user_choice <0:
    print("You have enter the worng number, You lost")
else:    
    print(game_symbols[user_choice])

    computer_choice = random.randint(0,2)
    print("Computer chose:")
    print(game_symbols[computer_choice])

    if user_choice == 0 and computer_choice ==2:
        print("You Wins")
    elif user_choice == 1 and computer_choice == 0:
        print("You Wins")
    elif user_choice == 2 and computer_choice == 1:
        print("You Wins")
    elif computer_choice == user_choice:
        print("it's a Draw")

    else:
        print("Computer Wins")