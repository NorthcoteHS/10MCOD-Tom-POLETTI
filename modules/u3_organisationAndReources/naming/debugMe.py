"""
Prog:   yesNoProgram.py
Name:   Tom Poletti
Date:   2018/04/18
Desc:   Answers yes or no to any question.
"""

# Ask the user for a question.
question = input('Ask me anything!')

# Check for special input.
if  question == 'Quit':
    print('Goodbye.')
elif question == 'Hi' or 'Hello':
    print("What's up?")

# Answer yes or no randomly.
else:
    import random
    num = random.randint(0,4);
    if num == 1:
        print("Yes!")
    if num == 2:
        print("No")
break
