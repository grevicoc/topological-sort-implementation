import header as ts

def main():
    file = open('courses.txt','r')
    
    #membuat graph
    graphDict = {}
    
    #semua line disimpan mentah
    reader = file.readlines()
    
    #1 line dibagi2 melalui delimiter dan disimpan menjadi array
    graphDict = ts.makeGraph(reader)

    array = []
    # ts.deleteEdges("C3",graphDict)
    # print(array)
    # print(graphDict)
    nullArray = []
    ts.topoSort(nullArray,graphDict,0)
    print(nullArray)

    
    # print(graphDict)
    # input()

if __name__ == "__main__":
    main()