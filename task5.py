def length (num1,num2):
    arr = [
        {"x" : 0, "y" : 0},
        {"x" : 2, "y" : 1},
        {"x" : 2, "y" : 2},
        {"x" : 2, "y" : 3},
        {"x" : 1, "y" : 3},
        {"x" : 1, "y" : 2},
        {"x" : 1, "y" : 1},
        {"x" : 3, "y" : 3},
        {"x" : 3, "y" : 2},
        {"x" : 3, "y" : 1},
    ]
    
    if arr[num1]["x"] == arr[num2]["x"] or arr[num1]["y"] == arr[num2]["y"]:
        return 1
    else:
        return 2**0.5
        
def PatternUnlock(N, hits):
    summ = 0;
    for i in range(N-1):
        summ = summ + length (int(hits[i]),int(hits[i+1]))
    summ = str(summ)
    if summ.find(".") == -1:
       return  summ.replace("0","")
    
    summ = summ.split(".");
    s1 = summ[0].replace("0","")
    if len(summ[1]) >= 5:
        s2 = summ[1][0:5].replace("0","");
    else:
        s2 = summ[1][0:len(summ[1])].replace("0","");
    return s1+s2