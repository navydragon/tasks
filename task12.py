def eigth_to_ten (value):
    summ = 0
    arr = list(str(value))
    arr.reverse()
    for idx,val in enumerate(arr):
        summ = summ + int(val)*(8**idx)
    return summ
    
def hex_to_ten (value):
    summ = 0
    arr = list(str(value))
    arr.reverse()
    for idx,val in enumerate(arr):
        if val == 'A': val = 10
        if val == 'B': val = 11
        if val == 'C': val = 12
        if val == 'D': val = 13
        if val == 'E': val = 14
        if val == 'F': val = 15
        summ = summ + int(val)*(16**idx)
    return summ

def UFO (n, data, octal):
    arr = []
    for el in data:
        if octal == False:
            arr.append(hex_to_ten(el))
        else:
            arr.append(eigth_to_ten(el))
    return arr
