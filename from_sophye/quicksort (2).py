import random

def quicksort(lst1):
    k1=1
    def quicksort1(lst,k):
        if len(lst) <= 1:
            return lst, k
        else:
            pivot = random.choice(lst)
        l_lst=[]
        r_lst=[]
        m_lst=[]
        for n in lst:
            k+=1
            print(k)
            if n<pivot:
                l_lst.append(n)
            elif n>pivot:
                r_lst.append(n)
            else:
                m_lst.append(n)
        newLst1,k = quicksort1(l_lst,k)
        newLst2,k = quicksort1(r_lst,k)
        return (newLst1 + m_lst + newLst2), k
    lst1,k1=quicksort1(lst1,k1)
    return lst1,k1

N=random.randint(5,20)
unsoredList=[]
for n in range(N):
    unsoredList.append(random.randint(1, 30))
print(unsoredList)
sortlist = []
sortlist = quicksort(unsoredList)
print(sortlist, K)