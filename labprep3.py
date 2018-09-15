# CS 177 – labprep3.py
# Nicholas Koontz
# This program prompts the user for the number of columns to display and then displays a table of calculations for each one

import math

#Inputs

print('What is the starting value?')
x = eval(input())
print('What is the endding value?')
y = eval(input())
print('What is the step of the values?')
step = eval(input())
print('How many columns should there be?')
columns = eval(input())
print()
#Variables
j1 = 0
k1 = 0
l1 = 0
m1 = 0
n1 = 0
o1 = 0
p1 = 0
q1 = 0

#Print basic information
print("This program displays math tables for multiples of", step)
print("How many columns should be displayed:", columns)
print()
#for loops
print("Num:", end='\t')
for i in range(x,y + 1, step):
    print(i, end='\t')
print()
print("=====================================")
print("Sqr", end='\t')
for j in range(x,y + 1, step):
    j1 = j ** 2
    print(j1, end='\t')
print()
print("SqRt", end='\t')
for k in range(x,y + 1, step):
    k1 = math.sqrt(k)
    k2 = round(k1, 2)
    print(k2, end='\t')
print()
print("Sin", end='\t')
for l in range(x,y + 1, step):
    l1 = math.sin(math.radians(l))
    l2 = round(l1, 2)
    print(l2, end='\t')
print()
print("Cos", end='\t')
for m in range(x,y + 1, step):
    m1 = math.cos(math.radians(m))
    m2 = round(m1, 2)
    print(m2, end='\t')
print()
print("Tan", end='\t')
for n in range(x,y + 1, step):
    n1 = math.tan(math.radians(n))
    n2 = round(n1, 2)
    print(n2, end='\t')
print()
print("Log", end='\t')
for p in range(x,y + 1, step):
    p1 = math.log(p)
    p2 = round(p1, 2)
    print(p2, end='\t')
print()
print("Log10", end='\t')
for q in range(x,y + 1, step):
    q1 = math.log10(q)
    q2 = round(q1, 2)
    print(q2, end='\t')
print()
