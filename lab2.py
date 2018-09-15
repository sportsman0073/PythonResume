# CS 177 - lab2.py
# Nicholas Koontz
# Triangular Fibonacci Sequence and Running Total


#User Input
print("Number of Rows:")
rows = int(input())

#Variables
columns = 0
num = 0
num_2 = 1
total = 0
full_total = 0

print("The desired Fibonacci sequence is:")
#Nested Loop
for i in range(rows):
    #Making correct columns
    columns = columns + 1
    for k in range(0, columns):
        #Fibonacci Sequence
        total = num + num_2
        print(total, end="\t")
        num = num_2
        num_2 = total
        #Running total
        full_total = full_total + total 
#Print function       
    print("\n")
print("The sum of all the displayed Fibonacci sequence is :", full_total)
