from urllib.request import Request, urlopen
import random
from custom_sort import bubleSort, quicksort, easySort
def randomint():
    N=random.randint(5,20)
    unsoredList=[]
    for n in range(N):
        unsoredList.append(random.randint(0, 20))
    return(unsoredList)
def randomfloat():
    N=random.randint(5, 20)
    unsoredList=[]
    for n in range(N):
        unsoredList.append(random.uniform(0, 20))
    return(unsoredList)
def randomword():
    url="https://svnweb.freebsd.org/csrg/share/dict/words?revision=61569&view=co"
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    web_byte = urlopen(req).read()
    webpage = web_byte.decode('utf-8')
    l=random.randint(1,2000)
    r=random.randint(100,500)
    first500 = webpage[l::r].split("\n")
    random.shuffle(first500)
    h=len(first500)
    new_words = []
    for i in first500:
        if i != '':
            new_words.append(i)
    return (new_words)
random_choce=random.randint(1,3)
random_choce =3

if random_choce == 1:
    unsortlist=randomint()
    print(unsortlist)
    
if random_choce == 2:
    unsortlist=randomfloat()
    print(unsortlist)
    
if random_choce == 3:
    unsortlist=randomword()
    print(unsortlist)

if type(unsortlist[1])==int:
    sortelist, m=bubleSort(unsortlist)
    print(sortelist, m)
elif type(unsortlist[1])==float:    
    sortlist, m=easySort(unsortlist)
    print(sortlist, m)
elif type(unsortlist[1])==str:    
    l=1
    sortlist, m=quicksort(unsortlist,l)
    print(sortlist, m)
else:
    print('введенные данные некоректны',)
import sys
sys.stdout=open("out.txt","w")
print ("hello")
sys.stdout.close()