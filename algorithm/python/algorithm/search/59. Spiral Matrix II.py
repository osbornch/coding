def generateMatrix(n):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    r1 = 0
    r2 = n-1
    c1 = 0
    c2 = n-1

    res = [[0]*n for _ in range(n)]

    num = 1
    while r1 <= r2 and c1 <= c2:
        for c in range(c1, c2+1):
            res[r1][c] = num
            num += 1
        for r in range(r1+1, r2+1):
            res[r][c2] = num
            num += 1
        if r1 < r2 and c1 < c2:
            for c in range(c2-1, c1, -1):
                res[r2][c] = num
                num += 1
            for r in range(r2, r1, -1):
                res[r][c1] = num
                num += 1
        r1 += 1
        r2 -= 1
        c1 += 1
        c2 -= 1
    return res


print(generateMatrix(3))
print(generateMatrix(1))