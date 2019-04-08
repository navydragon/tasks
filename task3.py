def ConquestCampaign (N, M, L, battalion):
    square = N * M
    conquered = False
    days = 0
    area = []
    for i in range (N):
        for j in range (M):
            area.append({'x' : i+1, 'y' : j+1, 'conquered' : False})
    while conquered == False:
        days = days + 1
        a = 0
        c = 0
        for i in range(len(battalion)-1):
            if i % 2 == 0:
                for row in area:
                    if row['x'] == battalion[i] and row['y'] == battalion[i+1] and row['conquered'] == False:
                        row['conquered'] = True
                        c = c + 1;
                if (battalion[i]+1) <= N: 
                    battalion.append(battalion[i]+1)
                    battalion.append(battalion[i+1])
                if (battalion[i]-1) >= 1: 
                    battalion.append(battalion[i]-1)
                    battalion.append(battalion[i+1])
                if (battalion[i+1]+1) <= M: 
                    battalion.append(battalion[i])
                    battalion.append(battalion[i+1]+1)
                if (battalion[i+1]-1) >= 1: 
                    battalion.append(battalion[i])
                    battalion.append(battalion[i+1]-1)
        conquered = True
        for row in area:
            if row['conquered'] == False:
                conquered = False;
                break
    return days