#hardest question on review way to figure it out with some help
#You Rock you are going to ace this exam
import math
#input values
print("value for A")
A = eval(input())
print("how many values in range")
X = int(input())
print("start")
z = eval(input())
print("step")
y = eval(input())
#get value for def
end = int(X*y+z)
#step for range
def frange(z, end, y):
           tmp = z
           while(tmp < end):
               yield tmp
               tmp += y
#range and proper printing               
for i in frange(z, int(X*y+z), y):
    p = A * math.log(i)
    print(i, end='\t')
    print("*"*int((round(p,0))))
