def equalPairs(rows, cols):
    count = {}
    for i in range(len(rows)):
        for j in range(len(cols[i])):
            pair = (rows[i], cols[i][j])
            if pair not in count:
                count[pair] = 0
            count[pair] += 1
    return list(count.values())