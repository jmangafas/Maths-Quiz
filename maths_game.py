import random
import pyinputplus

num1 = None
num2 = None
correct = 0
incorrect = 0
counter = 0
name = input('\n''Hi, welcome to the Maths quiz, please type in your name: ')

def additiongame(num1, num2):

    num1 = random.randrange(1,10)
    num2 = random.randrange(1,10)
    global correct
    global incorrect

    answer = pyinputplus.inputNum('\n'f'{num1} + {num2} = ')
    x = num1 + num2

    if answer == x:
        print('Correct!')
        correct = correct + 1
    else:
        print(f'The answer was {x}')
        incorrect = incorrect + 1

while counter < 5:
    additiongame(num1, num2)
    counter += 1

if correct >= 4:
    print('\n'f'{name} you have answered {correct} correctly, and {incorrect} incorrectly, time for some treats.')
else:
    print('\n'f'{name} you need more practice, you have answered {correct} correctly, and {incorrect} incorrectly.')
