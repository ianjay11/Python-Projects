from time import sleep

print("\nWELCOME TO THE PYTHON QUIZ GAME!\n")
sleep(1)
print("What's your name?")
player_name = input()
print("")
print(f"Hello {player_name} Best of luck!\n")
sleep(1)
print("\nTo answer the question put the letter of your choice.\n")
print("-----------------------------\n")
sleep(1.5)

chances = 1
score = 0

#### You make the questions a list

question_1 ="1. What is Python?\n(a) A type of snake\n(b) A programming language\n(c) I don't know\n(d) No one knows"
print(question_1)
answer_1 = "b"

for i in range(chances):
    answer = input("Answer: ")
    if answer.lower() == answer_1:
        print("Correct!")
        score += 1
        break
    else:
        print("Incorrect!")
        print(f"The correct answer is {answer_1}.")

sleep(0.5)
print("-----------------------------")

question_2 = print("1. Who created Python?\n(a) Guido van Rossum\n(b) Nikola Tesla\n(c) Vincent van Gogh\n(d) God")
answer_2 = "a"

for i in range(chances):
    answer = input("Answer: ")
    if answer.lower() == answer_2:
        print("Correct!")
        score += 1
        break
    else:
        print("Incorrect!")
        print(f"The correct answer is {answer_2}.")

sleep(0.5)
print("-----------------------------")

question_3 = print("1. What is a string?\n(a) vibrating element that produces sound\n(b) A long, thin and flexible structure made from threads twisted together\n(c) a sequence of characters contained by single or double quotes\n(d) None of the above")
answer_3 = "c"

for i in range(chances):
    answer = input("Answer: ")
    if answer.lower() == answer_3:
        print("Correct!")
        score += 1
        break
    else:
        print("Incorrect!")
        print(f"The correct answer is {answer_3}.")

sleep(0.5)
print("-----------------------------")

question_4 = print("What year was Python created?\n(a) 1991\n(b) 2000\n(c) 1975\n(d) 2022")
answer_4 = "a"

for i in range(chances):
    answer = input("Answer: ")
    if answer.lower() == answer_4:
        print("Correct!")
        score += 1
        break
    else:
        print("Incorrect!")
        print(f"The correct answer is {answer_4}.")

sleep(0.5)
print("-----------------------------")

question_5 = print("How do you insert COMMENTS in Python code?\n(a) #This is a comment\n(b) //This is a comment\n(c) *This is a comment*\n(d) %This is a comment")
answer_5 = "a"

for i in range(chances):
    answer = input("Answer: ")
    if answer.lower() == answer_5:
        print("Correct!")
        score += 1
        break
    else:
        print("Incorrect!")
        print(f"The correct answer is {answer_5}.")

sleep(0.5)
print("-----------------------------")

while score >= 4:
    print (f"Well done {player_name}! Your score is {score}/5.")
    break

while score == 3:
    print(f"You almost failed there {player_name}, but still great work! Your score is {score}/5.")
    break

while score <=2:
    print(f"Oh no! Your score is {score}/5.\nBetter luck next time!")
    break

sleep(1)
print("")
print("Thank you for playing the Python quiz game!")

