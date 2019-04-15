def ShopOLAP (N, items):
    newList = []
    for item in items:
        elem = item.split(" ")
        newList.append([elem[0],elem[1]])
    newList = sorted (newList)
    
    arr = []
    s_name = ""; s_kol = 0
    for el in newList:
        if el[0] != s_name:
            arr.append([s_name,s_kol])
            s_name = el[0]
            s_kol = int(el[1])
        else:
            s_kol = s_kol + int(el[1])
    arr.append([s_name,s_kol])
    del arr[0]
    arr.sort(key=lambda x: x[1], reverse=True)
    
    arr2 = []
    for elem in arr:
        arr2.append(elem[0]+" "+str(elem[1]))
    
    return arr2