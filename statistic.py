
from custom_sort import bubleSort,easySort
lst=[]
lst1=[]
lst2=[]
lst3=[]
lst4=[]


f = open('.\\filename.txt','r')
for line in f:
    k = line.strip()
    lst1=k.split(' ')
    lst4.append(lst1)
f.close()
#параметры 
def sorting_value(o):
    for i in range(2):
        if i==0:
            p='time'
        else:
            p='itteration'
        for j in range(4):
            if j==0:
                s='all'
            if j==1:
                s='bubleSort'
            if j==2:
                s='easySort'
            if j==3:
                s='quicksort'
            q=o(lst4,p,s)
            
    return (q)
#максимальное 
def maxparam(lst,param,sorting_type):
    if param == 'time':
        p=3
    if  param == 'itteration':
        p=4
    lst2.clear()
    if sorting_type!= 'all':
        for i in range(len(lst)-1):
            if lst[i][0] ==sorting_type:
                lst2.append(float(lst[i][p]))
    else:
        for i in range(len(lst)-1):
            lst2.append(float(lst[i][p]))
    print('\n Max', param, sorting_type,max(lst2))
    return (max(lst2))


#среднее 
def averageparam(lst,param,sorting_type):  
    if param == 'time':
        p=3
    if  param == 'itteration':
        p=4
    average=0
    summ=0
    lst2.clear()
    if sorting_type!= 'all':
        for i in range(len(lst)-1):
            if lst[i][0] ==sorting_type:
                summ=float(lst[i][4])+summ
                lst2.append(float(lst[i][p]))
    else:
        for i in range(len(lst)-1):
            summ=float(lst[i][4])+summ
            lst2.append(float(lst[i][p]))
    average=summ/len(lst2)
    print('\n  Average ',param, sorting_type, average)
    return (average)


 # медиана 
def medianaparam(lst,param,sorting_type):  
    if param == 'time':
        p=3
    if  param == 'itteration':
        p=4
    lst2.clear()
    if sorting_type!= 'all':
        for i in range(len(lst)-1):
            if lst[i][0] ==sorting_type:
                lst2.append(float(lst[i][p]))
    else:
        for i in range(len(lst)-1):
            lst2.append(float(lst[i][p]))
    lst3,_=easySort(lst2)
    if len(lst3) % 2 == 0:
        m=len(lst3)//2
        mediana=(lst3[m]+lst3[m-1])  / 2
    else:
        m=round(len(lst3)/2)
        mediana=lst3[m-1]
    print('\n Mediana',param,sorting_type,mediana)
    return (mediana)


k=sorting_value(maxparam)
k=sorting_value(medianaparam)
k=sorting_value(averageparam)
