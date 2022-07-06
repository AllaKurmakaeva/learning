import random
def quicksort(lst,k):
    if len(lst) <= 1:
        return lst
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
    return (quicksort(l_lst,k) + m_lst + quicksort(r_lst,k)),k
N=random.randint(5,20)
unsoredList=[]
for n in range(N):
    unsoredList.append(random.randint(1, 30))
print(unsoredList)
l=1
m=0
sortlist=[]
sortlist,m=quicksort(unsoredList,l)
print(sortlist,m)