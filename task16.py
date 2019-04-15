def ShopOLAP (N, items):
    arr = items.split(" ")
    newList = []
    for i in range (len(arr)):
        if i % 2 == 1:
            newList.append([arr[i-1],arr[i]]) 
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
    return arr