def LineAnalysis (line):
    arr = []
    first_dot = 0
    for i in range (len(line)):
        if line[i] == ".":
            first_dot = i
            break
    if first_dot == 0: return True
    sep = "";
    for i in range(first_dot):
        sep = sep + "*"
    arr = line.split(sep)
    is_right = True
    length = -1
    for el in arr:
        if (len(el) != 0):
            if (len(el) != length and length > -1):
                is_right = False
            length = len(el)
    length = -1
    arr = line.split(".");
    for el in arr:
        if (len(el) != 0):
            if (len(el) != length and length > -1):
                is_right = False
            length = len(el)
    return is_right