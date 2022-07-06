import ast
print('введите список из слов и цифр')
lst =input().split() 
print(lst)
lst1=[]
lst2=[]
lst3=[]
n=len(lst)
for i in range(n) :
    
    x = int(lst[i]) if lst[i].isdigit() else float(lst[i]) if lst[i].replace('.', '').isdigit() else lst[i]
    print(type(x))
    if type(x)==str:
        lst2.append(x)
    if type(x)==int:
        lst3.append(x)    
    
print(lst2)
lst2.sort()
lst3.sort(key=float)
lst3.extend(lst2)
print(lst3)