# https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/

def minTaps(n, ranges):
    memo = {}
    def recur(ind):
        if ind <= 0: return 0
        if ind in memo: return memo[ind]

        count = float('inf')
        for i in range(ind, -1, -1):
            if ranges[i] > 0 and ranges[i] >= ind - i:
                count = min(count, recur(i-ranges[i]) + 1)
        memo[ind] = count
        return memo[ind]
    
    ans = recur(n)
    return -1 if ans >= float('inf') else ans

# positive 
print(minTaps(5, [3,4,1,1,0,0]))

print(minTaps(3, [0,0,0,0]))

# TC: O(n^2)
# SC: O(n)