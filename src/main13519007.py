import header13519007 as ts

def main():

    #Membaca file dan menyimpannya dalam graphDict dalam bentuk dictionary graph
    file = open('../test/ASSIGN_HERE.txt','r')
    graphDict = {}
    reader = file.readlines()
    graphDict = ts.makeGraph(reader)

    #Pensortiran graphDict dan disimpan oleh finalArray
    finalArray = []
    ts.topoSort(finalArray,graphDict,0)
    
    #Menuliskan susunan yang telah fix (finalArray) ke stdout
    for i in range (len(finalArray)):
        print("Semester %d: "%(i+1),end="")
        print(*finalArray[i],sep=", ")
    
    print("")
    print("")
    print("")
    input("Tekan enter untuk menyudahi program.")

if __name__ == "__main__":
    main()