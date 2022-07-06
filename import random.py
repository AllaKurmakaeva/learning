from urllib.request import Request, urlopen
import random
import time


from custom_sort import bubleSort, quicksort, easySort
def randomint():
    N=50
    unsoredList=[]
    for n in range(N):
        unsoredList.append(random.randint(0, 20))
    return(unsoredList)

def randomfloat():
    N=50
    unsoredList=[]
    for n in range(N):
        unsoredList.append(random.uniform(0, 20))
    return(unsoredList)

def randomword():
    url="https://svnweb.freebsd.org/csrg/share/dict/words?revision=61569&view=co"
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    web_byte = urlopen(req).read()
    webpage = web_byte.decode('utf-8')
    N=50
    first500=[]
    for i in range(N):
        first500.append(random.choice(webpage.split("\n")))
    random.shuffle(first500)
    h=len(first500)
    new_words = []
    for i in first500:
        if i != '':
            new_words.append(i)
    return (new_words)
K=20

for i in range(K):
    start = time.clock()
    sortlist, m=bubleSort(randomint())
    end = time.clock()
    t=str(end-start)
    print('bubleSort','int',len(sortlist),t,m)

for i in range(K):
    start = time.clock()
    sortlist, m=easySort(randomfloat())
    end = time.clock()
    t=str(end-start)
    print('easySort','float',len(sortlist),t,m)
    
for i in range(K):
    l=1
    start = time.clock()
    sortlist, m=quicksort(randomword(),1)
    end = time.clock()
    t=str(end-start)
    print('quicksort','string',len(sortlist),t,m)