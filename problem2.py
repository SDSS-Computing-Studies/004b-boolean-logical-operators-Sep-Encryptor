#! python3

"""
Problem 2
Factors are positive integers that divide evenly into another integer.
The user will enter in two numbers. Determine if the smaller is a factor of the larger
(2 marks)

inputs:
an integer
an integer

outputs:
xx is a factor of yy
xx is not a factor of yy

examples:
Enter a number: 10
Enter another number: 2
2 is a factor of 10

Enter a number: 4
Enter another number: 25
4 is not a factor of 25
"""

N=input('1st number: ')
F=input('2nd number: ')
N=int(N)
F=int(F)
if N <= F:
    if F%N == 0:
        print(N,end=" ")
        print(' is a factor of',end=" ")
        print(F)
    else:
        print(N,end=" ")
        print('is not a factor of',end=" ")
        print(F)
elif N>F:
    if N%F == 0:
        print(F,end=" ")
        print('is a factor of',end=" ")
        print(N)
    else:
        print(F,end=" ")
        print('is not a factor of',end=" ")
        print(N)
