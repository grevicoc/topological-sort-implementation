def topoSort():
    return

def makeGraph(raw):
    graphDict = {}
    for value in raw:
        arrayOfCourse = value.strip('\n.').split(',')
        keyDict = arrayOfCourse[0]
        del arrayOfCourse[0]
        graphDict[keyDict] = arrayOfCourse
    return graphDict