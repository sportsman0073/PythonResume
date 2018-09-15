#CS - 177 project1.py
#Nicholas Koontz
# The program then loops through each characters in the plaintext to complete the encryption

#Input and print functions
x = list()
t = list()
print("This program uses a Ceasar Cipher to encrypt a plaintext message using the encryption key you provide.")
print("Enter the message to be encrypted:")
mystr = str(input())
print("Enter the integer for an encryption key:")
y = str(input())

#Chatacters to uppercase
mystr = mystr.upper()
y = y * len(mystr)
#Start of the print functions
print("This is a bar graph of the encrypted message:")
print("="*45)
enc=""
dec=""
#Loop for encryption
for character in mystr:
#Change to Ascii number
    x.append(ord(character))
for i in range(len(x)):
    #key char you'll add to the x item at index i = (i % len(y))
    x[i] += int(y[i])
    num = x[i]
    enc += chr(x[i])
    print("[",num,"]", end='\t')
    print("*"*(num//2))

for i in range(len(x)):
    x[i] -= int(y[i])
    dec += chr(x[i])   
print("The fully encoded message is:", enc, end="\n")
print("The reverse (decoded) message is:", dec, end="")
