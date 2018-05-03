inf = 1
for inf in range(1, 10):
    print(inf)
    inf = inf + 1

# Loop from 5 to 7.
for i in range(5,8):
    print(i)    # Displays 5, 6, 7

# Loop from 0 to 4 (note, using just one value loops from 0 by default).
for i in range(5):
    print(i)    # Displays 0, 1, 2, 3, 4

# Loop from 1 to 7 in steps of 2.
for i in range(1,8,2):
    print(i)    # Displays 1, 3, 5, 7

# Loop from 10 to 1 in steps of -1 (counting down).
for i in range(10,0,-1):
    print(i)    # Displays 10, 9, 8, 7, 6, 5, 4, 3, 2, 1

# Loop through each item in a list.
shopping = ['Eggs', 'Bananas', 'Yogurt', 'Cereal', 'Bread', 'Pizza']
for item in shopping:
    print(item)     # Displays Eggs, Bananas, Yogurt, ...

