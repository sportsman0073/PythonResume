# Program to add up the ASCII values in your name
name = input("Enter your name: ")       # Prompt the user for their name
score = 0                               # Initialize the score variable
for char in name:                       # Setup a loop to step through characters
    score += ord(char)                  # Add the ASCII value of each character
print('Your name has an ASCII score of:',score) # Display the result when done
