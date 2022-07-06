import random

m=0
def quicksort(lst):
    global m
    m=+1
    if len(lst) <= 1:
        return lst
    else:
        pivot = random.choice(lst)
    l_lst=[]
    r_lst=[]
    m_lst=[]
    for n in lst:
        if n<pivot:
            l_lst.append(n)
            m+=1
        elif n>pivot:
            r_lst.append(n)
        else:
            m_lst.append(n)
            m=+1
    return (quicksort(l_lst) + m_lst + quicksort(r_lst))
N=random.randint(5,20)
unsoredList=[]
for n in range(N):
    unsoredList.append(random.randint(1, 30))
print(unsoredList)
l=1
sortlist=[]
sortlist=quicksort(unsoredList)
print(sortlist,m)