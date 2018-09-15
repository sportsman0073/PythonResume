# CS 177 - labprep7.py
# Nicholas Koontz
# Looks for the words in a file and say what line they are on

#Words Function
def words(x):
    n = []
    file = open(x,'r')
    f = file.read().split('\n')
    #Loop for the words
    for i in range(len(f)-1):
        k = f[i]
        #Makes the words lowercase and in a list
        n.append(k.lower())
    #Close File
    file.close()
    #Returns a list
    return n

#Search function
def search(y,n):
    j = []
    t = [n[0]]
    p = [n[1]]
    o = [n[2]]
    z = [n[3]]
    x = [n[4]]
    v = [n[5]]
    file = open(y,'r')
    f = file.read().split('\n')
    for i in range(len(f)-1):
        k = f[i]
        #Make lines without puntuation and all lowercase
        j.append(k.lower().strip(',').strip('.').replace('"',"").strip('?').replace("'","").strip('`').strip().split(' '))
        #Checks and adds to a list with the proper line number of the words
        if n[0] in j[i]:
            t.append(i+1)
        if n[1] in j[i]:
            p.append(i+1)
        if n[2] in j[i]:
            o.append(i+1)
        if n[3] in j[i]:
            z.append(i+1)
        if n[4] in j[i]:
            x.append(i+1)
        if n[5] in j[i]:
            v.append(i+1)
    #Close File
    file.close()
    #Returns the list as one list
    return [t, p, o, z, x, v]

#Main FUnction
def main():
    #User inputs
    print("Enter the words filename:", end=' ')
    x = str(input())
    print("Enter the search filename:", end=' ')
    y = str(input())
    words(x)
    search(y,words(x))
    print(search(y,words(x)))
    #Returns the list of the words with their line numbers
    return search(y,words(x))
#Calls main function to start the program
main()
