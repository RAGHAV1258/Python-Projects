print('''''
         ~6_.___,`P_,`P_,`P_,`P                                     |
 *  |___)  /^\ /^\ /^\ /^\      *         *   ,     *        \   /
    ='='=`    *                      *        )            --  *   --
                   *           .-----------. ((              /   \
        *                *     )`'`'`'`'`'`( ||     *          |
                              /`'`'`'`'`'`'`\||                     *
    *         *      *       /`'`'`'`'`'`'`'`\| *        *
                    ,,,,,,, /`'`'`'`'`'`'`'`'`\      ,
       *           .-------.`|```````````````|`  .   )       *    *
   *        *     / ,^, ,^, \|  ,^^,   ,^^,  |  / \ ((
                 /  |_| |_|  \  |__|   |__|  | /   \||   *
    *       *   /_____________\ |  |   |  |  |/     \|           *
                 |  __   __  |  '=='   '=='  /.......\     *
  *     *        | (  ) (  ) |  //`_```_`\\  |,^, ,^,|     _    *
   ___,.,___     | |--| |--| |  ||(O)|(O)||  ||_| |_||   _|-|_
  (  (("))  ) *  | |__| |__| |  || " | " ||  ||_| |_|| *  (")       *
   \_('@')_/     |           |  ||   |   ||  |       |  --(_)--  *
 ***/_____\******'==========='==''==='===''=='======='***(___)*****

''''')

print("Welcome to Mystery House.")
print("Your mission is to Escape the House full of dangerous ceratures.")

choice1 = input('You \'re in the room  of a Mystery house. What would you do? Type "find key" or "break the door"\n').lower()

if choice1 == "find key":
    choice2 = input('Now you\'ve  made to the Hallway . There are Traps laid down in the Hallway. What would you do? Type "find a tool" or "crawl on the ground"\n').lower()
    if choice2 == "find a tool":
      choice3 = input('Now You\'re in the basement of the house, There are 3 doors in the basement. What would you do? Type "red" or "blue" or "black"\n').lower()
      if choice3 =="red":
        print("It's a room full of snakes , Game Over.")
      elif choice3 == "blue":
       print("Congratulations, You've Escaped the mystery house successfully.")
      elif choice3 == "black":
       print("It's a room full of Wild Animals , Game over.")

      else:
        print("You chose a door that doesn't exist.") 
    else:
      print("You got Killed, Game Over.")
else:
  print("You got caught by the demon, Game Over.")
  
print("Thanks for Playing.")