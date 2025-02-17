def specialArray(pos, ranks):
    n = len(pos)
    for i in range(1 << 20):
        if bin(i).count('1') == (n - pos.count(i)):
            return i
    return -1