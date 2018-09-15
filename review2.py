print("Mezza step")
x = int(input())
print("value for n")
n = int(input())
total = 0
sign = 1
for i in range(0,n*x, x):
    index = i * sign
    sign = sign * -1
    total += index
print(total)
