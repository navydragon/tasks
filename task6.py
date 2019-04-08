def WordSearch(length, s, subs):
    arr = []
    words = s.split(" ");
    row = ""
    for word in words:
        if (len(word) > length):
            if row != "":
                arr.append(row)
                row = ""
            for symbol in word:
                row = row + symbol
                if len(row) == length:
                    arr.append(row)
                    row = ""
            continue
        if row != "":
            separator = " "
        else:
            separator = ""
        if (len(row) + len (word) + len(separator)) > length:
            arr.append(row)
            row = ""
            separator = ""
        
        row = row + separator + word
    arr.append(row)
    
    result_arr = []
    for el in arr:
        result = 0
        words = el.split(" ")
        for word in words:
            if word == subs:
                result = 1
                break
        result_arr.append(result)
    return result_arr