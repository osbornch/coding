def uniqueOccur(arr):
    check = dict()
    for i in arr:
        if i in check:
            check[i] += 1
        else:
            check[i] = 1   
    return len(set(check.values())) == len(check.values())


# positive 
print(uniqueOccur([1,2,2,1,1,3]))

# negative
print(uniqueOccur([1,2]))