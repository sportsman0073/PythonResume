# CS 177 – labprep4.py
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
print("")

#Open a file read its continents and print a new Purdue email address for every name
print("This program opens a file reads the file and creates a new Purdue email from the names in the file")

#User input

print("Type what file you would like to open:", end = '')
infile = str(input())
k = []
b = []
email = []

#open file and read
file = open(infile, 'r')

#creating a list of names
b = file

#Open file and write in list of email addresses 
h = open("emails.txt", 'w')

#Create email addresses
for i in file.readlines():
    k = i.lower()
    p = k[0]#First Letter of the name
    #Need the first 7 of the last name
    a = k.split(' ')[1]
    a = a[0:len(a)-1 if len(a) <= 7 else 7]
    email = (p + a + "@purdue.edu")
    h.write(email + '\n')
    
#close the file
file.close()  
#Close the file with the emails
h.close()
