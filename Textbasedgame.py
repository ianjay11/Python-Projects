from time import sleep
import random
####stranger danger
def intro():
    print("""
    You woke up tired in unfamiliar room. The last thing you remembered is that you were out partying.
    You were talking to a girl you met at the bar.
    After lots of drinking and talking she ask you if you would like to go somewhere private.
    You went with her and she brought you to an alleyway then you felt someone injected you with something.
    You passed out.
    """)
    sleep(8)
    print("Now you are awake and looking around the room")
    sleep(2)
    print("You have found a note in the table that says:")
    sleep(3)
    print("")
    print("You were chosen as part of our experiment. Your choices will determine your future.")
    print("Right choices can help you escape but wrong choices can get you killed")
    print("Good luck!")
    print("")
    sleep(8)
    room1()

def room1():
    print("Now you are stuck in a big room and there are 3 doors in the room by which you can escape.")
    sleep(3)
    print("")
    print("Each door has a inscription written on it.")
    print("")
    print("1st door has an army of people carrying weapons behind it, which will kill you immediately at first sight.")
    print("2nd door contains lions which are not fed in the last couple of years.")
    print("3rd door leads to falling in the bottomless pit.")
    print("")
    print("Only one door will help you escape. Which room will you choose?")
    print("")
    ###player input
    answer = int(input("Type between 1, 2, or 3.\n>>"))
    if answer == 1:
        print("You opened the door and after several steps you were hit multiple times by bullets. You are dead.")
        sleep(4)
        print("")
        exit ()
    elif answer == 2:
        print("You slowly opened the door, and you saw the lions with only bones remained.")
        print("You have chosen the right door. The lions haven't been fed for a long time and died from hunger.")
        sleep(4)
        print("")
        room2()
        
    elif answer == 3:
        print("You are dead. You fell into the bottomless pit or maybe still falling to eternity.")
        sleep(3)
        print("")
        exit()
    else:
        print("Invalid Answer. Answer only with 1, 2, or 3.")
        sleep(3)
        print("")
        room1()

def room2():
    print("As you walk through the dead lions you found a door that leads to another room.")
    sleep(2)
    print("This room is having one window from which light is coming from but it is too far from your reach.")
    sleep(2)
    print("Again there are three doors to choose from.")
    sleep(2)
    print("")
    print("1st door contains a lens that magnifies sun rays so much that even opening the door will burn you completely.")
    sleep(2)
    print("2nd door contains acid which will burn someone immediately after the door is opened.")
    sleep(2)
    print("3rd door there are wild animals which are alive and someone entering this room will become the food of these wild animals, the moment door is opened.")
    sleep(2)
    print("")
    print("Which door you will choose to escape from this room?")
    ###player input
    answer = int(input("Type between 1, 2, or 3.\n>>"))
    if answer == 1:
        sleep(2)
        print("You saw in the window that it is night-time and sun rays does not work because it has no sun.")
        print("You opened the door and nothing happened.")
        print("You just walked again until you reached another door leading to another room.")
        print("But this time it is a little different room. It has now have only 1 door and have many objects.")
        print("You then check the objects.")
        sleep(8)
        print("")
        menu()
    elif answer == 2:
        print("As soon as you open the door the acid was sprayed and burn you completely.")
        print("")
        exit()
        
    elif answer == 3:
        print("You are dead. Wild animals have eaten you.")
        exit()
    else:
        print("Invalid Answer. Answer only with 1, 2, or 3.")
        room2()

###menu for room 3
def menu():
    for i in objects:
        print(objects.index(i), i)

    answer = int(input("What do you want to check?\n>>"))
    print("")
    if answer == 0:
        door()
    elif answer == 1:
        window()
    elif answer == 2:
        bookshelf()
    elif answer == 3:
        vase()
    elif answer == 4:
        chair()
    elif answer == 5:
        painting()
    elif answer == 6:
        treasurebox()
    elif answer == 7:
        rug()
    elif answer == 8:
        picture_frame()
    elif answer == 9:
        decoder()
    else:
        print("Invalid Input. You should choose between 0-9.")
        sleep(1)
        print("")
        menu()
      

def door():
    print("You walked to the door and found out that you need 4 digit number to unlock it. You enter the code.")
    input_code = (int(input(">> ")))
    if input_code == code:
        print("")
        print("You heared a click and the door opened. Congratulations! You are free for now.")
        print("Thank you for playing the Game!")
        print("")
        exit()
    elif input_code != code:
        print("You tried to open it but to no avail. Your code is incorrect")
        sleep(2)
        print("")
        menu()

def window():
    print("The window is full of dust. There is nothing to see here.")
    sleep(2)
    print("")
    menu()

def bookshelf():
    print("A bookshelf filled with dusty old books.")
    print(f"There are {random_code1} different sets of books found in the bookshelf.")
    print(f"You also saw {random_code1} scrolls that is scattered all around the shelf.")
    sleep(3)
    print("")
    menu()

def vase():
    print("The vase is full of wilting flowers. You empty it and there is nothing inside.")
    sleep(2)
    print("")
    menu()

def chair():
    print("You checked the chair thoroughly and when you turned it upside down")
    print(f"You saw an ingrave number {random_code2} in there.")
    sleep(2)
    print("")
    menu()

def painting():
    print("The painting is a big eye and you always felt like this painting is always looking at you.")
    print(f"You check everywhere as you watch it closely the pupil of the eye has a number {random_code3} on it.")
    sleep(2)
    print("")
    menu()

def treasurebox():
    print("A treasurebox filled with toys not treasures.")
    print("You found a small paper at the very bottom with random letters on it. The words written are:")
    print("Xli svhiv sj gshiw mw mr xli eptlefixmgep svhiv sj sfnigxw sj alivi csy jsyrh xli gshi")
    sleep(2)
    print("")
    menu()
  

def rug():
    print("You found a letter underneath that says:")
    print("When I was one, I had just begun. When I was two, I was nearly new.")
    print("When I was three, I was harldy me. When I was four, I was not much more.")
    print("When I was five, I was just alive. But now I am six,")
    print("I'm as clever as clever. So I think I'll be six now forever and ever.")
    sleep(4)
    print("")
    menu()

def picture_frame():
    print("There is no sign of any codes here.")
    sleep(2)
    print("")
    menu()

def decoder():
    print("Do you have some text to decode? y or n")
    answer = str(input(">> "))
    if answer == "y" or answer == "yes":
        print("What is your text?")
        word = str(input(">> "))
        shift = -4

        for code in word:
            if code.upper() >= 'A' and code.upper() <= 'Z':
                if (code.isupper()):
                    code = chr((ord(code) + shift -65) % 26 + 65)
                    print(code,end= '')

                elif (code.islower()):
                    code = chr((ord(code) + shift -97) % 26 + 97) 
                    print(code,end= '')
                
            else:
                print(code, end='')
        print("")

    elif answer == "n" or answer == "no":
        print("")
        menu()
    
    else:
        print("Invalid Input")
        print("")
        menu()

    sleep(1)
    print("")
    menu()
    
###exit code

def exit():
    print("Would you like to play again? y or n")
    answer = str(input()) ##use .lower
    if answer == "y" or  answer == "Y" or answer == "YES" or answer == "yes":
        intro()
    elif answer == "n" or answer == "N" or answer == "NO" or answer == "no":
        print("Thank you for playing the game!")
    else:
        print("Invalid input")
        exit()

###variable used in door()
objects = ["Door","Window","Bookshelf","Vase","Chair","Painting","Treasurebox","Rug","Picture Frame","Decoder"]

###codes found in objects
random_code1 = random.randint(3,9)
random_code2 = random.randint(1,9)
random_code3 = random.randint(1,9)
code = int(f"{random_code1}{random_code2}{random_code3}{6}") 


intro()
