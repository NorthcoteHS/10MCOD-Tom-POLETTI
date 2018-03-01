
# Answer randomiser
import random
unknown=random.randint(1, 9)

# User input
input('What would you like to ask? I will answer it: ')
print('Interesting question...')
print('')
print('The answer is:')

# Prints answer
if unknown == 1:
    print('Yes')
elif unknown == 2:
    print('No')
elif unknown == 3:
    print('Maybe')
elif unknown == 4:
    print('I am not sure')
elif unknown == 5:
    print('NOOOO')
elif unknown == 6:
    print('Probably')
elif unknown == 7:
    print('Another time')
elif unknown == 8:
    print('Sorry this question does not make sense')
elif unknown == 9:
    print('Yeah mate')

