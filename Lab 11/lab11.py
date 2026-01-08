import sqlite3

print('\n\n')

with open("score2.txt") as myFile:
    theRows = myFile.read()

def splitTheList(listType):
    tempList = []
    for element in listType:
        splitElement = element.split()
        tempList.append(splitElement)
    return tempList

listInList = splitTheList(theRows.splitlines())
#print(listInList) #print out the whole list


def getPersonWithScoreList(listType):
    tempList = []
    personScoreList = []
    for person in listType:
        if person[2] + " " + person[3] not in tempList:
            tempList.append(person[2]+ " " + person[3])
            indexOfNewPerson = tempList.index(person[2]+ " " + person[3])
            #print(indexOfNewPerson, tempList[indexOfNewPerson])
        personScoreList.append((tempList.index(person[2]+ " " + person[3])+1, tempList[tempList.index(person[2] + " " + person[3])], person[1], person[4]))
        #print(dataP.index(p[2]+ " " + p[3])+1, p[1], p[2]+' '+ p[3], p[4]) 
        # #98 persons list

    return personScoreList
#dataPersonScore = getPersonWithScoreList(listInList)
#print ('Score is (idPerson, task, score)', dataPersonScore)
# List of idPerson, task and score 


## task 2

def dbfunc(dataInput):
    conn = sqlite3.connect('lab11.db')
    cur = conn.cursor()

    #cur.execute("DROP TABLE Persons")
    #cur.execute("DROP TABLE Scores")

    #cur.execute('''CREATE TABLE IF NOT EXISTS Persons(id INTEGER UNIQUE,name1 TEXT NOT NULL, UNIQUE(name1))''')
    #cur.execute('''CREATE TABLE IF NOT EXISTS Scores(idPerson INTEGER NOT NULL,Task INTEGER NOT NULL,Score INTEGER NOT NULL)''')

    sData = []
    pData = []
    for d in dataInput:
        sData.append((d[0], d[2], d[3]))
        pData.append((d[0], d[1]))
    cur.executemany('INSERT INTO Scores VALUES (?,?,?)', sData)
    cur.executemany('INSERT OR IGNORE INTO Persons VALUES (?,?)', pData)

    print("========= persons below ####################")
    #for row in cur.execute("SELECT * FROM Persons"):# 1,a 
     #   print(row)
    print("========== scores below #################")
    #for row in cur.execute("SELECT  * FROM Scores"):
       #print(row)

    for row in cur.execute(''' SELECT p.name1, SUM(s.Score) FROM Persons as p JOIN Scores AS s ON p.id = s.idPerson 
                            GROUP BY p.name1 ORDER BY SUM(s.Score) DESC LIMIT 10'''): 
        print(row)
    #for row in cur.execute('''SELECT s.Task, SUM(s.Score) FROM Scores AS s GROUP BY s.Task ORDER BY SUM(s.Score) ASC LIMIT 10'''):
        #print(row)


    conn.close()

dbfunc(getPersonWithScoreList(listInList))

print('\n')

#2a
"""('Maria Johansson', 37)
('Kristina Larsson', 37)
('Margareta Eriksson', 36)
('Nils Johansson', 33)
('Karl Eriksson', 33)
('Maria Eriksson', 32)
('Karin Eriksson', 31)
('Eva Eriksson', 31)
('Erik Johansson', 31)
('Sven Nilsson', 30)"""
# 2b
"""(5, 8)
(51, 8)
(33, 10)
(38, 11)
(39, 13)
(47, 13)
(85, 13)
(87, 13)
(3, 14)
(40, 14)"""