def findContentChildren(g, s):
    g.sort()
    s.sort()
    a = len(g) - 1
    b = len(s) - 1
    maxs = 0

    while a >= 0 and b >= 0:
        if s[b] >= g[a]:
            maxs += 1
            b -= 1
            a -= 1
        else:
            a -= 1

    return maxs

print(findContentChildren([1,2,3], [1,1]))
print(findContentChildren([1,2], [1,2,3]))
