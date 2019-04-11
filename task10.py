def CoverWithTiles(length):
    if length % 2 == 1 or length <= 0:
        return -1
    if length == 2:
        return 3
    elif length == 4:
        return 11
    else:
        return 4 * CoverWithTiles(length - 2) - CoverWithTiles(length - 4)