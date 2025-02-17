def snail(matrix):
    if not matrix:
        return []

    result = []
    while matrix:
        result += matrix.pop(0)
        if matrix and matrix[0]:
            matrix = [row.pop() for row in matrix]
        if matrix:
            result += [row[-1] for row in matrix][::-1]
        if matrix:
            matrix.reverse()
    return result