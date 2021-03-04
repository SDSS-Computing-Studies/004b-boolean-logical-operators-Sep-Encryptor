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
L1=(input('enter an integer=>')).strip()
L2=(input('enter an integer=>')).strip()
L3=(input('enter an integer=>')).strip()
L1=int(L1)
L2=int(L2)
L3=int(L3)

a=L1**2
b=L2**2
c=L3**2
if a<b and a < c:
    print(L1,end=",")
    if b < c:
        print(L2,end=",")
        print(L3,end=" ")
    elif c < b:
        print(L3,end=",")
        print(L2,end=" ")
elif b < a and b < c:
    print(L2,end=",")
    if a < c:
        print(L1,end=",")
        print(L3,end=" ")
    if c < a:
        print(L3,end=",")
        print(L1,end=" ")
elif c<b and c<a:
    print(L3,end=",")
    if b < a:
        print(L2,end=",")
        print(L1,end=" ")
    elif a < b:
        print(L1,end=",")
        print(L2,end=" ")
if a+b == c or a+c == b or b+c==a:
    print('form a Pythagorean triple')
else:
    print('do not form a Pythagorean triple')