#Fungsi untuk membuat graph dari raw file reader
def makeGraph(raw):
    graphDict = {}
    for value in raw:
        arrayOfCourse = value.strip('\n.').split(',')
        keyDict = arrayOfCourse[0]
        del arrayOfCourse[0]
        graphDict[keyDict] = arrayOfCourse
    return graphDict

#Fungsi untuk menghapus edge yang verticenya telah dihapus
def deleteEdges(verticeDeleted,rawGraph):
    counter = 0
    verticeWillDeleted = []
    
    for unit in rawGraph:
        if (verticeDeleted in rawGraph.get(unit)):
            indexToBeDeleted = rawGraph.get(unit).index(verticeDeleted)
            del rawGraph[unit][indexToBeDeleted]      
        
#Fungsi yang mencari vertice dengan edge kosong dan vertice tersebut akan dihapus. Begitu juga edge-edge yang terhubung dengan vertice yang dihapus
def findNull(rawGraph):
    
    returnArray = []
    counter=0

    for unit in rawGraph:
        if (len(rawGraph.get(unit))==0):
            returnArray = returnArray + [unit]
            counter+=1

    #del vertice
    for i in range(counter):
        del rawGraph[returnArray[i]]

    #del edge
    for i in range(counter):
        deleteEdges(returnArray[i],rawGraph)

    #return nilai vertice yang kosong
    return returnArray

    

#Membuat topo sort dari rawGraph dan hasilnya akan disimpan dalam array sorted. Limit adalah penanda apakah topoSort dicukupkan atau tidak (8 semester maks).
def topoSort(sorted,rawGraph,limit):
    if (limit==7):
        sorted.append(findNull(rawGraph))
    else:
        if (len(rawGraph)!=0):
            sorted.append(findNull(rawGraph))
            topoSort(sorted,rawGraph,limit+1)

    


