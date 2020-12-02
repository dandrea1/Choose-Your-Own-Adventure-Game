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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

first_question = input("You are walking and come to a fork in the road. Will you go left or right?\n").lower()

if first_question == 'left':
  print("Nice job! You avoided the cliff.")
  second_question = input("You come to the bank of a river. Will you swim or wait? Type swim or wait.\n").lower()  
  if second_question =='wait':
    print("Lucky you! A boat arrived to take you across.")
    third_question = input("""Across the river you find 3 houses. 
  Will you enter the one with the red, blue, or yellow door? Type R, B or Y\n""").lower()
    if third_question == 'r':
      print("Sorry, the wolf was waiting for little red riding hood, but ate you instead!")
    elif third_question == 'b':
      print("Sorry, the witch from Hanzel and Gretal cooks you in a bowl of soup!")
    elif third_question == 'y':
      print("Success! You found the treasure; you never have to work again!")
    else:
      print("Congrats! You figured out that thinking outside the box is the greatest treasure of all!")
  else:
    print("\nSorry game over, you drowned in the river!")
else:
  print("\nSorry game over, you fell off the cliff!")
  

