from custom_sort import bubleSort, quicksort, easySort
import random



N = random.randint(5,20)
unsoredList=[]
for n in range(N):
    unsoredList.append(random.randint(1, 30))

print(unsoredList)
soredList, m = bubleSort(unsoredList)
print (soredList, m)

print(unsoredList)
soredList, m = easySort(unsoredList)
print(soredList, m)

print(unsoredList)
l=1
soredList, m= quicksort(unsoredList, l)
print(soredList,m)

