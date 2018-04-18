"""
Prog:   rectCalc.py
Name:   Tom Poletti
Date:   2018/04/18
Desc:   Calculates the area and perimeter of a rectangle.
"""

#print welcome message
print('Welcome to the Circle Calculator!')

#takes user input
r = input('Enter a radius: ')
r = int(r)

#calculates and prints area
area = 3.14 * r * r
print('The area is', area)

#calculates and prints perimeter
perimeter = 3.14 * r * 2
print('The perimeter is', perimeter)
