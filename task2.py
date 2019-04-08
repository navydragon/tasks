def odometer (oksana):
    prev_hour = None;
    summ = 0;
    for i in range(len(oksana)-1):
        if i % 2 == 1:
            continue
        if prev_hour == None:
            summ = summ + oksana[i] * oksana[i+1]
            prev_hour = oksana[i+1];
        else:
            summ = summ + oksana[i] * (oksana[i+1] - prev_hour)
            prev_hour = oksana[i+1];
    return summ