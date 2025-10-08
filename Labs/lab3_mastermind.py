## Mastermind Game

import random

# Rules
turns = 12
t = 1
code_length = 4
open_circle = '\u25CB'      # white circle (wrong position)
filled_circle = '\u25CF'    # black circle (correct position)
print(f"Welcome to Mastermind! You have {turns} turns to guess the correct sequence of {code_length} numbers between 1 and 6 (inclusive). \n"
      f"After each guess, you'll receive feedback in the form of circles: \n"
      f"{filled_circle} for correct numbers in the correct position \n"
      f"{open_circle} for correct numbers in the wrong position.")


# Sequence Generation
random.seed()
sequence = []
for i in range(code_length):
    sequence.append(random.randint(1,6))

# Game Loop
while True:
    guess = []
    while len(guess) != code_length:
        print(f"Turn {t} of {turns}: Enter {code_length} numbers between 1 and 6 (inclusive) : ")
        guess = [input()]
        guess = [int(x) for x in guess[0] if x.isdigit()]
        if len(guess) != code_length or any(x < 1 or x > 6 for x in guess):
            print('Invalid input : must enter a 4 digit code')
            guess = []

    temp_code = sequence.copy()
    temp_guess = guess.copy()

    result = []
    # Perfect matches
    for i in range(code_length):
        if temp_guess[i] == temp_code[i]:
            result.append(filled_circle)
            temp_code[i] = 0
            temp_guess[i] = -1
    # Misplaced matches
    for i in range(code_length):
        for j in range(code_length):
            if temp_guess[i] == temp_code[j] and i != j:
                result.append(open_circle)
                temp_code[j] = 0
                break
    print(' '.join(result))

    # Win/Loss checks
    if guess == sequence:
        print(f"Congratulations! You've cracked the code in {t} turns.")
        break
    if t > turns:
        print(f"Sorry, you've used all your turns. The correct sequence was: {' '.join(sequence)}")
        break
    t += 1      # turn counter