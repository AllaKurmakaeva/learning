from input_sorting import orderLists
from random_sorting import bubleSort

lst=[]
f = open('.\\examp.txt','r')
#  list comprehantion
lst = [line.strip() for line in f]
f.close()
print(lst)
lst2, lst3 = orderLists(lst)
n=len(lst)

lst2, _ = bubleSort(lst2)
lst3, _ = bubleSort(lst3)
lst3.extend(lst2)
print(lst3)
f4=open('.\\examp2.txt','w')
for elem in lst3:
    f4.write(str(elem)+'\n')
f4.close()

f = open('.\\examp2.txt','r')
lst =[line.strip() for line in f]
f.close()
print(lst)