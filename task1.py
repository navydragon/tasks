def squirrel(n):
    factorial = 1;
    for i in range(1,n+1):
        factorial = factorial * i;
    return int (str (factorial)[0])