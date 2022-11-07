import random
from words import wordlist
import time

###hangman visual
hangman_display = [
"""
 +----+
      |
      |
      |
      |
      |
     ===""", """
 +----+
 |    |
 O    |
      |
      |
      |
     ===""", """
 +----+
 |    |
 O    |
 |    |
      |
      |
     ===""", """
 +----+
 |    |
 O    |
/|    |
      |
      |
     ===""", """    
 +----+
 |    |
 O    |
/|\   |
      |
      |
     ===""", """
 +----+
 |    |
 O    |
/|\   |
 |    |
/     |
     ===""", """
 +----+
 |    |
 O    |
/|\   |
 |    |
/ \   |
     ===""", """
 
"""
]

def intro():
    print("Welcome to Hangman!\n")
    name = input("Enter your name: ")
    print()
    print(f"Hello {name}! Best of Luck!")
    time.sleep(2)
    print("The game is about to start!\nLet's play Hangman!\n")
    time.sleep(2)
    game()

##main body of game
def game():
    secret_word = wordlist
    word = random.choice(secret_word).lower()
    guessed_correctly = []
    guessed_incorrectly = []
    guesses = 7
    hangman_count = -1

    while guesses > 0:
        output = ''
        for letter in word:
            if letter in guessed_correctly:
                output += letter
            else:
                output += '_ '
        if output == word:
            break

        print("Guess the word: ",output)
        print(f"{guesses} chances left")
        guess = input().lower()
        ###output
        if guess in guessed_correctly or guess in guessed_incorrectly:
            print("Already guessed", guess)
        elif guess in word:
            print("Good job! You guessed the correct letter!")
            guessed_correctly.append(guess)
        else:
            print("Sorry! You have guessed a wrong letter!")
            hangman_count += 1
            guesses -= 1
            guessed_incorrectly.append(guess)
            print(hangman_display[hangman_count])

    if guesses > 0:
        print(f"You guessed it! the word is {word}")
        
    else:
        print(f"Ooooops you are hanged. The word is {word}.\nBetter luck next time!")
        
    exit()

def exit():
    print("Would you like to play again? y or n")
    answer = str(input())
    if answer == "y" or  answer == "Y" or answer == "YES" or answer == "yes":
        print("")
        game()
    elif answer == "n" or answer == "N" or answer == "NO" or answer == "no":
        print("")
        print("Thank you for playing the game!")

intro()