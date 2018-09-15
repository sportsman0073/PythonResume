# CS 177 – labprep4a.py
# Nicholas Koontz
# This program takes a string and builds a new string from that string

# User inputs
print("Enter a String:", end='')
x = str(input())
print("Enter number of sub segments:", end='')
y = int(input())
print("Enter the separator:", end='')
z = str(input())

seq = []
t = len(x)//y
for i in range(len(x)//t):
    seq.append(x[i*t:i*t+t])
    q = seq[::-1]
    r = z.join(q)
print(r)

