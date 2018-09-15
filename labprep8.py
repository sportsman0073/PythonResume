# CS 177 - labprep7.py
# Nicholas Koontz
# Reads Two Files Inputted by the user and then puts them into three dictionaries

def student(students):
    sid = []
    name = []
    newdict = {}
    
    file = open(students, 'r')
    f = file.read()
    y = f.split('\n')
    file.close()
    
    for i in y:
        x = i.split(' | ')
        sid.append(x[0].replace('sid=s',''))
        name.append(x[1].replace('name=',''))
        
    #Make into a dictionary    
    for k in range(len(sid)):
        newdict.update({sid[k]:name[k]})
        
    return newdict, y

def score(grades, names):
    sids = {}
    
    file = open(grades, 'r')
    f = file.read()
    y = f.split('\n')
    file.close()
    
    for i in y:
        x = i.split(' | ')
        sid = x[0].replace('sid=s','')
        grade = int(x[2].replace('grade=',''))
        name = names[sid]
        
        #Make into dictionary
        sids[name] = sids.get(name,0) + grade
    return sids
            
def count(lines):
    gender = {}
    states = {}
    count_m = 0
    count_f = 0
    
    for i in lines:
        x = i.split(' | ')
        state = x[3].replace('state=','')
        #If x[2] is a gender
        if x[2].replace('gender=','') == 'Male':
            male = x[2].replace('gender=','')
            count_m += 1
        else:
            female = x[2].replace('gender=','')
            count_f += 1
         #Make into Dictionary   
        states[state] = states.get(state, 0) + 1
    #Dictionary for male and female long ways
    gender[female] = gender.get(female, 0) + int(count_f)
    gender[male] = gender.get(male, 0) + int(count_m)
    
    return gender, states
        
        
    


def main():
    #User input
    print("Enter students filename:", end=' ')
    students = input()
    print("Enter grades filename:", end=' ')
    grades = input()
    #Call functions
    
    names,lines = student(students)
    
    score(grades, names)

    count(lines)
    
    #Print formating
    print('States Dictionary:')
    print('\n')
    print(count(lines)[1])
    print('\n')
    print('Gender Dictionary:')
    print('\n')
    print(count(lines)[0])
    print('\n')
    print('Grades Dictionary:')
    print('\n')
    print(score(grades, names))
    
main()
