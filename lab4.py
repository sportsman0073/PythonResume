#CS-177
#HeeJoon Rachel Rnoh, Sarah Hermanek, Nicholas Koontz
#lab 4

#This program reads files and creates a new file containing the encypted information

print("This program reads files and creates a new file containing the encrypted information")

#Opening and reading file for coordinates
print("opening coordinates")
file=open('coordinates.txt', 'r')
f = file.read().split("\n")
print("coordinates into list")

#Opening and reading files for indices
print("opening indices")
file1= open('indices.txt', 'r')
f1 = file1.read().split("\n")
print("indices into list")
print("Opening messages")
#Create a new file
file2= open('messages.txt', 'w')
#create a for loop to encrypt
for k in range(len(f1)-1):
    j = int(f1[k])
    i = f[j-1]
    a=i.split(',')
    city = ""
    long = ""
    lat = ""
    citybackwards = a[0][::-1]
    longbackwards = a[1][::-1]
    latbackwards = a[2][::-1]
    for r in range(len(a[0])):
        city += a[0][r] + citybackwards[r]
    for p in range(len(a[1])):
        long += a[1][p] + longbackwards[p]
    for q in range(len(a[2])):
        lat += a[2][q] + a[2][len(a[2])-q-1]
    #print(lat)
    finalstr = lat + city + long
    file2.write(finalstr+'\n')


print("Succesful encryption of message")
#Close files
file2.close()
file.close()
file1.close()
