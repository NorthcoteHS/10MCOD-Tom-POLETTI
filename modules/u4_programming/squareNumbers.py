"""
Prog:   squareNumbers.py
Name:   Tom Poletti
Date:   2018/05/03
Desc:   This program will use a for loop for the numbers 1 - 10. Each number should be squared and the result added to a new list called squares. Print the list at the end of the file.
"""

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = []

for num in range (11):
    squares.append(num**2)
    num = num+1

print(squares)
