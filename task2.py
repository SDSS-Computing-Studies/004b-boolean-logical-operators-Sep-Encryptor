#! python3
# Task2.py

"""
Ask the user to enter a number.
Tell them if the number is both a perfect square and a perfect cube.

Note:  Many languages have a problem when dealing with floating point
decimals, and python is no exception.
Sometimes, when finding the cube root of large numbers, like 729,
you may get 8.9999999999999999999998 instead of 9
To get around this, we can use the round() command
round() accepts 2 parameters, the number to be rounded, and how many decimals
a = round(3.999999999999998, 8) would round at the 8th decimal place, for example.
You don't want to round too early (ie to the nearest whole number) because that
might be too inaccurate.
(2 points) 

Inputs:
number

Outputs:
xx is both a perfect square and a perfect cube.
xx is only a perfect square.
xx is only a perfect cube.

Example:
Enter a number: 8
8 is only a perfect cube.
"""

N=(input('enter an number')).strip()
N=int(N)
print(N,end=" ")
C=N**(1/3)
C = (round(C,9))
import math
if math.sqrt(N)==int(math.sqrt(N)) and C==int(C):
    print('is both a perfect square and a perfect cube.')
elif math.sqrt(N)==int(math.sqrt(N)):
    print('is only a perfect square.')
elif C==int(C):
    print('is only a perfect cube.')