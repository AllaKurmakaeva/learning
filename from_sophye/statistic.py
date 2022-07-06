
from custom_sort import bubleSort, easySort

#параметры 
def sorting_value(statisticOperation, allData):
    for i in range(2):
        if i==0:
            p='time'
        else:
            p='itteration'

        statisticOperation(allData, p, 'all')
        statisticOperation(allData, p, 'bubleSort')
        statisticOperation(allData, p, 'easySort')
        statisticOperation(allData, p, 'quicksort')


#максимальное 
def maxparam(allData, param, sorting_type):
    if param == 'time':
        p=3
    if  param == 'itteration':
        p=4
    result = []
    if sorting_type!= 'all':
        result = [float(line[p]) for line in allData if line[0] == sorting_type]
    else:
        result = [float(line[p]) for line in allData]

    # TODO: use formatted string print(f'\n Max {param:4} {sorting_type} {max(result)}')
    # TODO: change it to have see like table 
    print('\n Max', param, sorting_type,max(result))

#среднее 
def averageparam(lst,param,sorting_type):  
    if param == 'time':
        p=3
    if  param == 'itteration':
        p=4
    average = 0
    summ = 0
    result = []
    if sorting_type!= 'all':
        # TODO:  create list comprehention 
        # TODO:  calculate sum on list with build in function
        for i in range(len(lst)-1):
            if lst[i][0] ==sorting_type:
                summ=float(lst[i][4])+summ
                result.append(float(lst[i][p]))
    else:
        for i in range(len(lst)-1):
            summ=float(lst[i][4])+summ
            result.append(float(lst[i][p]))
    average=summ/len(result)
    # TODO:  formated string
    print('\n  Average ',param, sorting_type, average)

 # медиана 
def medianaparam(lst,param,sorting_type):  
    if param == 'time':
        p=3
    if  param == 'itteration':
        p=4
    result = []
    if sorting_type!= 'all':
        for i in range(len(lst)-1):
            if lst[i][0] ==sorting_type:
                result.append(float(lst[i][p]))
    else:
        for i in range(len(lst)-1):
            result.append(float(lst[i][p]))
    # TODO:  use Math or smth like that to calc mediana
    lst3,_=easySort(result)
    if len(lst3) % 2 == 0:
        m=len(lst3)//2
        mediana=(lst3[m]+lst3[m-1])  / 2
    else:
        m=round(len(lst3)/2)
        mediana=lst3[m-1]
    # TODO:  formated string
    print('\n Mediana',param,sorting_type,mediana)
    return (mediana)


lst=[]
allData=[]

f = open('.\\filename.txt','r')
for line in f:
    k = line.strip()
    lst1 = k.split(' ')
    allData.append(lst1)
f.close()


# TODO: allData make as dict
# dict()
# {
#     'sort_type': [
#         {'type': , '...': ...}
#     ],

# }

k=sorting_value(maxparam, allData)
k=sorting_value(medianaparam, allData)
k=sorting_value(averageparam, allData)
