import random


def bubleSort(inputList):
    print("START BUBLE SORT")
    iterationAmount = 0
    listToSort = inputList.copy()
    N = len(listToSort)
    for i in range(N -1 ):
        for j in range(N - 1 - i):
            if listToSort[j] > listToSort[j+1]:
                listToSort[j], listToSort[j+1] = listToSort[j+1], listToSort[j]
            iterationAmount += 1 
    return listToSort, iterationAmount

def easySort(inputList):
    iterationAmount = 0
    listToSort = inputList.copy()
    isSort = True
    N = len(listToSort)
    while (isSort == True):
        isSort = False
        for i in range(N-1) :
            iterationAmount += 1
            if listToSort[i+1] < listToSort[i]:
                b = listToSort[i+1]
                listToSort[i+1] = listToSort[i]
                listToSort[i] = b
                isSort = True
    return listToSort,iterationAmount

def quicksort(listToSort, iterationAmount):
    if len(listToSort) <= 1:
        return listToSort, iterationAmount
    else:
        pivot = random.choice(listToSort)
    l_lst=[]
    r_lst=[]
    m_lst=[]
    for n in listToSort:
        iterationAmount+=1
        if n < pivot:
            l_lst.append(n)
        elif n > pivot:
            r_lst.append(n)
        else:
            m_lst.append(n)
    newLst1, iterationAmount = quicksort(l_lst, iterationAmount)
    newLst2, iterationAmount = quicksort(r_lst, iterationAmount)
 
    return (newLst1 + m_lst + newLst2), iterationAmount