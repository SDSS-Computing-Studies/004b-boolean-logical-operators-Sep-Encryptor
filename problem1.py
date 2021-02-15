"""
Problem 1
Ask the user to enter a number.
The number is considered "frue" if it is
divisible by 6, but not divisible by 8.
State whether the number is "frue" 
(2 marks)

Inputs:
a number

Outputs:
xx is frue
xx is not frue

example:
Enter a number: 48
48 is not frue
"""

#! python3

N=input('input a number: ')
N=int(N)
print(N,end=" ")
if N%6==0 and N%8 !=0:
    print("is frue")
else:
    print('is not frue')