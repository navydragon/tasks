def symbol_weight (symbol):
    arr = [
        {"s": " ", "w": 0},{"s": "!", "w": 9},{"s": "\"", "w": 6},{"s": "#", "w": 24},{"s": "$", "w": 29},{"s": "%", "w": 22},
        {"s": "&", "w": 24},{"s": "'", "w": 3},{"s": "(", "w": 12},{"s": ")", "w": 12},{"s": "*", "w": 17},{"s": "+", "w": 13},
        {"s": ",", "w": 7},{"s": "-", "w": 7},{"s": ".", "w": 4},{"s": "/", "w": 10},{"s": "0", "w": 22},{"s": "1", "w": 19},
        {"s": "2", "w": 22},{"s": "3", "w": 23},{"s": "4", "w": 21},{"s": "5", "w": 27},{"s": "6", "w": 26},{"s": "7", "w": 16},
        {"s": "8", "w": 23},{"s": "9", "w": 26},{"s": ":", "w": 8},{"s": ";", "w": 11},{"s": "<", "w": 10},{"s": "=", "w": 14},
        {"s": ">", "w": 10},{"s": "?", "w": 15},{"s": "@", "w": 32},{"s": "A", "w": 24},{"s": "B", "w": 29},{"s": "C", "w": 20},
        {"s": "D", "w": 26},{"s": "E", "w": 26},{"s": "F", "w": 20},{"s": "G", "w": 25},{"s": "H", "w": 25},{"s": "I", "w": 18},
        {"s": "J", "w": 18},{"s": "K", "w": 21},{"s": "L", "w": 16},{"s": "M", "w": 28},{"s": "N", "w": 25},{"s": "O", "w": 26},
        {"s": "P", "w": 23},{"s": "Q", "w": 31},{"s": "R", "w": 28},{"s": "S", "w": 25},{"s": "T", "w": 16},{"s": "U", "w": 23},
        {"s": "V", "w": 19},{"s": "W", "w": 26},{"s": "X", "w": 18},{"s": "Y", "w": 14},{"s": "Z", "w": 22},{"s": "[", "w": 18},
        {"s": "\\", "w": 10},{"s": "]", "w": 18},{"s": "^", "w": 7},{"s": "_", "w": 8},{"s": "`", "w": 3},{"s": "a", "w": 23},
        {"s": "b", "w": 25},{"s": "c", "w": 17},{"s": "d", "w": 25},{"s": "e", "w": 23},{"s": "f", "w": 18},{"s": "g", "w": 30},
        {"s": "h", "w": 21},{"s": "i", "w": 15},{"s": "j", "w": 20},{"s": "k", "w": 21},{"s": "l", "w": 16},{"s": "m", "w": 22},
        {"s": "n", "w": 18},{"s": "o", "w": 20},{"s": "p", "w": 25},{"s": "q", "w": 25},{"s": "r", "w": 13},{"s": "s", "w": 21},
        {"s": "t", "w": 17},{"s": "u", "w": 17},{"s": "v", "w": 13},{"s": "w", "w": 19},{"s": "x", "w": 13},{"s": "y", "w": 24},
        {"s": "z", "w": 19},{"s": "{", "w": 18},{"s": "|", "w": 12},{"s": "}", "w": 18},{"s": "~", "w": 9}
        ]
    for el in arr:
        if el["s"] == symbol:
            return el["w"]
    return 23

def PrintingCosts (line):
    summ = 0
    line = list(line)
    for letter in line:
        summ = summ + symbol_weight (letter)
    return summ