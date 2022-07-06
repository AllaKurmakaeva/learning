from random import randint

def bubleSort(listToSort):
    iterationAmount = 0
    N = len(listToSort)
    for i in range(N -1 ):
        for j in range(N - 1 - i):
            if listToSort[j] > listToSort[j+1]:
                listToSort[j], listToSort[j+1] = listToSort[j+1], listToSort[j]
            iterationAmount += 1
    return listToSort, iterationAmount

def easySort(listToSort):
    k = 1
    m = 0 
    N = len(listToSort)
    while (k>=1):
        k = 0
        for i in range(N-1) :
            if listToSort[i+1] < listToSort[i]:
                b = listToSort[i+1]
                listToSort[i+1] = listToSort[i]
                listToSort[i] = b
                k+=1
                m+=1
    return listToSort,m

if __name__ == '__main__':
    N = randint(1, 30)
    unsoredList = []
    for i in range(N):
        unsoredList.append(randint(1, 99))
    print(unsoredList)

    easySortedList, easyIterationAmount = easySort(unsoredList)
    print(easySortedList)
    print(easyIterationAmount)

    bubleSortedList, bubleIterationAmount = bubleSort(unsoredList)
    print(bubleSortedList)
    print(bubleIterationAmount)