import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)
word_list = ['apple', 'mango' , 'pineapple' , 'grapes' , 'peach' ]

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(f"hint : {word_length}")

end_of_game = False
lives = 6

display = []
for _ in range (word_length):
    display += "_"

while not end_of_game:
   guess = input("Guess the letter: ").lower()
# Check weather the guessed letter in the chosen word if true then place it in the position in the and remove the blank space.
   for position in range(word_length):
       letter = chosen_word[position]

       if letter == guess:
           display[position] = letter
#check weather the guessed letter present in chosen word.
   if guess not in chosen_word:
       print(f"You guessed {guess}, thats not present in chosen word,you lose life.")

       lives -= 1
       if lives == 0:
           end_of_game = True
           print("You lose, Game over.")

   if "_" not in display:
       end_of_game = True
       print("You Win, Game Over")

print(f"{' '.join(display)}")         
print(stages[lives])





       