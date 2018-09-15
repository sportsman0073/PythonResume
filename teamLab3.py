#team lab 3
#Nicholas Koontz, Sarah Hermanek, Heejoon Rachel Rnoh
#This program Log(1+x) terms and approx and diff

import math

#inform user of program function
print ("This program approximates the value of log(1+x) for any x value between -1 and 1")
print("More terms increase the accuracy")

#promt user to enter the number of terms
x = eval(input("Enter number th value of x: "))
term = eval(input("Enter the nuber of terms in the calculation: "))
total = 0

#calculate approximate value of log(x+1)
for i in range(1, term+1):
    ans= ((x**i)/i) * ((-1)**(i+1))
    total = total+ans

#Print and diff
print("Approximate value of log(x+1): ", total)
print("Exact value of log(x+1): ", math.log(x+1))
print("The difference = ", (abs(total-(math.log(x+1)))))
