#! python3
"""
Ask the user to enter a number. 
Tell them if the number is a positive integer
(2 points) 

inputs:
a number of any type

outputs:
xx is a positive integer.
xx is not a positive integer

example:
Enter a number: -3
-3 is not a positive integer
"""
N=input('enter an number')
N=float(N)
print(N,end=" ")
if N==int(N) and N > 0:
    print('is a positive integer.')
else:
    print('is not a positive integer')