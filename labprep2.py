# CS 177 - labprep2.py
# Nicholas Koontz
# Prompts the user for a starting integer and number of columns and rows then displays a number grid

#User inputs
print("Input a starting integer")

num = int(input())

print("Input the number of rows")

rows = int(input())

print("Input the number of columns")

columns = int(input())

#Nested for loop
for i in range(rows):
    for k in range(columns):
        num = num + 1
        #Print function
        print(num-1, end="\t")
    print("\n")
