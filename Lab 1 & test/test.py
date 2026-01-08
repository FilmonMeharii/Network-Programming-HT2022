#print('hello')
#animal = ["dog", "cat", "elefant"]
#for a in animal:
 #   print(a)

""""
a = range(99)
for n in a:
    print(n)

words = ['cat', 'window', 'different']
for w in words:
    print(w, len(w))


list(range(6,18))


a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
"""


f=open("score2.txt", 'r')

students = {}
topStudents={}
topStudent = 0

splitted = [line.split() for line in f]

def getStudentsPoints(fName, lName, totalPoints):
    for student in students:
        if fName + " " + lName == students:
            point = int(students[student]) + int(totalPoints)  
            students[student] = point
            return
        students[fName + " " + lName]= totalPoints

for line in splitted[:]:
    fName = line[2]
    lName = line[3]
    score = line[4]

    getStudentsPoints(fName, lName, score)
