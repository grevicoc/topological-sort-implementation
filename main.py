import topoSort as ts

def main():
    file = open('courses.txt','r')
    
    #membuat graph
    graphDict = {}
    
    #semua line disimpan mentah
    reader = file.readlines()
    
    #1 line dibagi2 melalui delimiter dan disimpan menjadi array
    graphDict = ts.makeGraph(reader)
        
    print(graphDict)
    input()

if __name__ == "__main__":
    main()