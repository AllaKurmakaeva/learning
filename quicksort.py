import random
K = 1
def quicksort(lst):
    global K
    if len(lst) <= 1:
        return lst
    else:
        pivot = random.choice(lst)
    l_lst=[]
    r_lst=[]
    m_lst=[]
    for n in lst:
        K+=1
        if n<pivot:
            l_lst.append(n)
        elif n>pivot:
            r_lst.append(n)
        else:
            m_lst.append(n)
    newLst1 = quicksort(l_lst)
    newLst2 = quicksort(r_lst)
    return (newLst1 + m_lst + newLst2)
N=random.randint(5,20)
unsoredList=[]
for n in range(N):
    unsoredList.append(random.randint(1, 30))
print(unsoredList)
sortlist = []
sortlist = quicksort(unsoredList)
print(sortlist, K)