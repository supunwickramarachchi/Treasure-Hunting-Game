print('''
*******************************************************************************
|---------|-------------------|------------------|---------------------|-------
|_________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
|_________|_____________________:=._o "=._."_.-="'"=.__________________|_______
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
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************      
''')

print()

print("<<<*>>> Welcome to the Treasure Island <<<*>>>")

print()

print("<!> Your mission is to find the treasure <!>")

player_name = input("What is your name buddy: ").title()

print(f"""
    You are entered to the unknown mystery island {player_name}.
    You walked into the forest...
    
    Oh you found a two roads one for left and other for right.
    
    You have to take a decision now to choose a path,
    """)

select_road = input("What is your choosing path (left or right): \n").lower()

if select_road == 'left':
    print(f"""
        Well done, {player_name}!
        
        You are walking alone. No one here this forest, but you are brave enough to walk alone.
        
        'What is this, I never saw this kind of dark watering hall'
        You found a mysterious watering hall in the forest.
        
        Now you have to take a discussion. Swim or walk around the watering hall
        """)

    passing_river = input("How you think to continue your journey (swim or walk): \n").lower()
    if passing_river == 'walk':
        print(f"""
              Well done, {player_name}!\n
              you pass the dangerous watering hall in the forest,
              There are lots of monsters in that watering's hall.

              You are continue your journey. You walk and walk so long...
              
              'Ah.. I am hungry...'
              
              You eat some food you brought when you came... 'Now all is good'
              You started to walk again!

              You find another two roads one for left and other for right
              """)

        select_road_2 = input("What is your choosing path (left or right):\n ").lower()
        if select_road_2 == 'right':
            print(f'''
                  Well done, {player_name}!, you are marvellous. 

                  You bravely came a long way into the forest {player_name}. 
                  
                  You hered some many worst sounds from different animals.
                  You feel those sounds are like monsters.

                  Suddenly you saw something! 'Oh there is cave in the forest'.

                  You need to get a decision to enter the cave or avoid and continue!
                  ''')

            treasure_cave = input("Do you enter to the case(enter or avoid): \n").lower()
            if treasure_cave == 'enter':
                print(f"""
                      Well done, {player_name}!, your entered the mystery cave.

                      you continued your journey. Drank some water and walk and walk into the cave. 

                      Suddenly you saw something, 'Oh that's a light, where it's come from?'.
                      You asked from yourself...

                      You ran to that light you saw and you find another small cave fill with fireflies.
                      'Wow how beautiful is this.'
                      Those fireflies became lights to the cave.
                      
                      You walked into the small cave you found that filled with fireflies.

                      'What is that?'... You saw something.
                      
                      There are 3 boxes in the corner of the cave. All those boxes are gold plated.
                      Those boxes marked with some colors.
                      Like... Green --> |_____| Yellow --> |______| Blue --> |_____|.
                      
                      You saw there is a message in the stone near the boxes,
                      |----------------------------------------|
                      | Only one chase...                      | 
                      | Three boxes, select one                |
                      | If you select right one                |
                      | You will leave this cave with fortune  |
                      | If you select wrong one                |
                      | You will stuck here for lifetime...    |
                      | It is your choice, things are waiting..|
                      |----------------------------------------|
                      
                      You understand that there is one chance to look a box. If something wrong the cave close. 
                      
                      So this is the your chance... 
                      Be carefully open...
                      """)
                treasure_box = input("Which box do you open (green or yellow or blue): ").lower()
                if treasure_box == 'yellow':
                    print(f"""
                          * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                          *                                                             *
                          *  Eureka...! Eureka...! Eureka...!                           *
                          *  You win the game!!!!                                       *
                          *  You found the treasure of the jungle {player_name}.        *
                          *                                                             *
                          *  Congratulations... Your Treasure Yellow Box --> |_______|  *
                          *                                                             *
                          *  Well Done!!! Bring your treasure to your home!             *
                          *                                                             *
                          * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
                          """)

                elif treasure_box == 'green':
                    print('Start a fire in the cave. Gave Over')
                    print(f"""
                          Oh God...! You choose the wrong one.. It's not {treasure_box}
                          Suddenly start a fire in the cave... And closed the cave door!
                          
                          <- You lose the Game -> 
                          """)
                elif treasure_box == 'blue':
                    print(f"""
                          Oh God...! You choose the wrong one.. It's not {treasure_box} 
                          You wake up the monster inside the cave... 
                          
                          Grraaaauuuu! Grraaaauuuu! Grraaaauuuu!
                          
                          Closed the cave door!
                          <- You lose the Game -> 
                          """)
                else:
                    print("""
                          You lose the way in final step. Mission failed!...
                          Try another day.. Bye!
                          """)
            else:
                print("""
                      You lose the way in soon to find the treasure. Mission failed!...
                      Try another day.. Bye!
                      """)
        else:
            print("""
                  You lose the way in the middle. Mission failed!...
                  Try another day.. Bye!
                  """)
    else:
        print("""
              You lose the way in the beginning. Mission failed!...
              Try another day.. Bye!
              """)

else:
    print("""
          You lose the way too early. Mission failed!...
          Try another day.. Bye!\n
          """)

print('******** Thank you for played the Game! *********')
