#! python3
"""
Problem 3
Pythagorean triples are sets of 3 integers such that the squares of the 2 smaller numbers is equal to the square of the third.
Ask the user to enter in 3 numbers, in any order.  Order the numbers from smallest to largest.
Determine if they form a Pythagorean triple. 
(2 marks)

Inputs:
an integer
an integer
an integer

Outpus:
xx,yy,zz form a Pythagorean Triple
xx,yy,zz do not form a Pythagorean Triple

Examples:
Enter an integer=>3
Enter an integer=>5
Enter an integer=>4
3,4,5 form a Pythagorean triple

Enter an integer=>5
Enter an integer=>4
Enter an integer=>2
2,4,5 do not form a Pythagorean triple
"""

import math
a = float(input("Please enter integer "))
b = float(input("Please enter integer "))
c = float(input("Please enter integer "))

if a > b and a > c:
    s1 = b
    s2 = c
    big = a
elif b > a and b > c:
    s1 = a
    s2 = c
    big = b
elif c > a and c> b:
    s1 = a
    s2 = b
    big = c

if (s1**2 + s2**2) == big**2:
    print(str(int(s1)) + "," + str(int(s2)) + "," + str(int(big)) + " form a pythagorean triple")
else:
    print(str(int(s1)) + "," + str(int(s2)) + "," + str(int(big)) + " do not form a pythagorean triple")
    
