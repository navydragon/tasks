def MassVote (n, arr):
    max_votes = max (arr)
    winners = 0
    for i in arr:
        if i == max_votes:
            winners = winners + 1
    if winners > 1:
        return "no winner"
    else:
        summ = sum (arr)
        winner = arr.index(max_votes) + 1
        if (max_votes / summ) > 0.5:
            return "majority winner "+str(winner)
        else:
            return "minority winner "+str(winner)