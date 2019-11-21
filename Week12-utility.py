#Samuel Potter
#CSCI 102 - Section E
#Week 12 - Part A
#-----------------------------------------------------------------------

def PrintOutput(word):
    
    print("OUTPUT", word)

def LoadFile(nameFile):
    
    doc = open(nameFile, "r")
    readLines = doc.readlines()
    readLines = list(map(lambda x:x.strip(),readLines))
    
    return readLines

def UpdateString(org,sec,Num):

    newList = list(org)
    otherList = []

    for i in range(len(newList)):

        if i == Num:
            otherList.append(sec)

        else:
            otherList.append(newList[i])

    print("OUTPUT", ''.join(otherList))

def FindWordCount(List,String):

    count = 0
    
    List = (''.join(List))
    List = List.split()

    print(List)

    for word in List:

        if word == String:

            count += 1

    return count

def ScoreFinder(List_1,List_2,String):

    if String in List_1:
        loc = List_1.index(String)
        score = List_2[loc]
        
        print("OUTPUT", String, "got a score of", score)

    else:
        print("OUTPUT Player not found")

def Union(List_1,List_2):

    UpdatedList = List_1 + List_2

    return UpdatedList

def Intersection(List_1,List_2):

    UpdatedList = []

    for word in List_1:

        if word in List_2:

            UpdatedList.append(word)

    return UpdatedList

def NotIn(List_1,List_2):

    UpdatedList = []

    for word in List_1:

        if word not in List_2:

            UpdatedList.append(word)

    return UpdatedList

    

    

    

