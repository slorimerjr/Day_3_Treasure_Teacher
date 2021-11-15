print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice1 = input('You\'re at a crossroads, where do you want to go? Type "right" or "left".\n').lower()

if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat, type "swim" to swim across.\n').lower()
  if choice2 == "wait":
    choice3 = input('You\'ve arrived at the island unharmed. You see 3 doors, one "red", one "blue", and one "yellow". Which do you choose?\n').lower()
    if choice3 == "red":
      print("It\'s a room full of fire. Game over.")
    elif choice3 == "yellow":
      print("You\'ve found the treasure, you win!!!")
    elif choice3 == "blue":
      print("It\'s a room full of beasts. Game over.")
    else:
      print("You chose a door that doesn\'t exist. Game over.")
  else:
    print("You got attacked by an angry trout. Game over.")
else:
  print("You fell into a hole, game over.")

# same issue I had previously. 