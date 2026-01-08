
f = open("score2.txt")

splitted = [line.split() for line in f]
students = {}
topStudents = {}
topStudent = 0

def getStudentsPoints(fName, lName, totalPoints):    
    for student in students:
        if fName + " " + lName == student:
            point = int(students[student]) + int(totalPoints)  
            students[student] = point
            return
    students[fName + " " + lName]= totalPoints

for line in splitted[:]:
    fName = line[2]
    lName = line[3]
    score = line[4]    
    getStudentsPoints(fName, lName, score)

for i in students: 
    print("Student Name: {} student points: {}".format(i,students[i]) )
    if topStudent <= students[i]: 
        topStudent = students[i]

for i in students:
    if students[i]==topStudent:
        topStudents[i] = students[i]

print("Top students")

for i in topStudents:
    print("The winner is: {} with total points : {} ".format(i,topStudents[i]))
