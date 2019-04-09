def SumOfThe (N, data):
    work = []
    for el in data:
        work.append(el)
    for el in data:
        work.remove(el)
        if sum(work) == el:
            return el
        work.append(el)
    return None