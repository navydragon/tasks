def ShopOLAP (N, items):
    newList = sorted (items)
    arr = []
    s_name = ""; s_kol = 0
    for el in newList:
        if el[0] != s_name:
            arr.append([s_name,s_kol])
            s_name = el[0]
            s_kol = el[1]
        else:
            s_kol = s_kol + el[1]
    arr.append([s_name,s_kol])
    del arr[0]
    arr.sort(key=lambda x: x[1], reverse=True)
    return arr