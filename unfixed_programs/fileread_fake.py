lst=[]
f = open('C:\\Users\\unnamed\\Desktop\\прога\\examp.txt','r')
lst =[line.strip() for line in f]
f.close()
print(lst)
lst2=[]
lst3=[]
n=len(lst)
for i in range(n) :
    x = int(lst[i]) if lst[i].isdigit() else float(lst[i]) if lst[i].replace('.', '').isdigit() else lst[i]
    if type(x)==str:
        lst2.append(x)
    if type(x)==int:
        lst3.append(x)
def f2(a):
    i = 0
    n=len(a)
    while i < n - 1:
        j = 0
        while j < n - 1 - i:
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
            j += 1 
        i += 1
    return a
lst2=f2(lst2)
lst3=f2(lst3)
lst3.extend(lst2)
print(lst3)
f4=open('C:\\Users\\unnamed\\Desktop\\прога\\examp2.txt','w')
f4.write('')
f4.close()
i=0
n=len(lst3)
for i in range(n):
    f3=open('C:\\Users\\unnamed\\Desktop\\прога\\examp2.txt','a')
    f3.write(str(lst3[i])+'\n')
    f3.close()
f = open('C:\\Users\\unnamed\\Desktop\\прога\\examp2.txt','r')
lst =[line.strip() for line in f]
f.close()
print(lst)