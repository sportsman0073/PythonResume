# CS 177 – mylab3.py
# Nicholas Koontz
#Log(1 + x) terms and approx and diff print based on the term

import math

#Inputs from the User
print("Starting Number of elements:", end='')
start = eval(input())
print("Ending Number of elements:", end='')
last = eval(input())
print("step:", end='')
step = eval(input())
print("Precision:", end='')
precision = eval(input())
print("Enter the value of x:", end='')
x = eval(input())
total = 0
diff = 0

#Exact Value
print("#terms", end='\t')
print("approx", end='\t')
print("diff")      
#For loop for approximation
for i in range(start, last + 1, step):
    print(i, end='\t')
    total = 0
    for k in range(1, i+1):
        ans = ((x**k)/k) * ((-1)**(k+1))
        total = total + ans
    print(round(total,precision), end='\t')
    diff = abs(total - math.log(x+1))
    print(round(diff, precision))


