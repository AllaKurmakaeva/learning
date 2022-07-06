def orderLists(lst):
    strLst=[]
    digitLst =[]
    for elem in lst:
        x = 0
        if elem.isdigit():
            x = int(elem)
        elif elem.replace('.', '').isdigit():
            x = float(elem)
        else:
            x = elem
        if type(x) == str:
            strLst.append(x)
        elif type(x) == int or type(x) == float:
            digitLst.append(x)

    return strLst, digitLst

if __name__ == '__main__':
    print('введите список из слов и цифр')
    lst = input().split()
    print(lst)
    lst2, lst3 = orderList(lst)
    print(lst2)
    lst2.sort()
    lst3.sort(key=float)
    print(lst2, lst3)