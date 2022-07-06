from random import randint
N = 10
l = []
for i in range(N):
    l.append(randint(1, 99))
print(l)
z=[]

def f1(a):
    k = 1 
    b = 0
    m=0 
    while (k>=1):
        k = 0
        for i in range(N-1) :
            if a[i+1] < a[i] :
                b=a[i+1]
                a[i+1]=a[i]
                a[i]=b
                k+=1
                m+=1
    return a,m            
z,c = f1(l)
print(z)
print(c)
def f2(a):
    i = 0
    m=0
    while i < N - 1:
        j = 0
        while j < N - 1 - i:
            if a[j] > a[j+1]:
                a[j], ac[j+1] = a[j+1], a[j]
            j += 1 
            m+=1
        i += 1
    return a,m
z,c = f2(l)
print(z)
print(c)