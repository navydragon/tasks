def time_to_wait (cur_time,red_time,green_time):
    cycle = red_time + green_time
    if (cur_time % cycle) < red_time:
        return red_time - (cur_time % cycle)
    else:
        return 0
        
        
def Unmanned (L,N, arr):
    summ = 0
    for i in range(L):
        svt = 0
        for j in range(N):
            if arr[j][0] == i:
                summ = summ + time_to_wait (summ,arr[j][1],arr[j][2])
                svt = 1
        summ = summ  + 1
    return summ
