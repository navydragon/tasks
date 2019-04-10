def HowManyTimes (s,s_generic):
    inp = [] 
    count = 0
    for i in s_generic:
        inp.append(i)
    arr = combinations(inp, len(s));
    for el in arr:
        if el == s:
            count = count + 1  
    return count

def combinations(elements, size):
    if len(elements) < size or size == 1:
        return elements
 
    ret = []
    for i, item in enumerate(elements):
        for j in combinations(elements[i + 1:], size - 1):
            ret.append(item + j)
    return ret