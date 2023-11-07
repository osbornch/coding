def minSubArrayLen(nums, target):
    """
    :type target: int
    :type nums: List[int]
    :rtype: int
    """
    l, r = 0, 0
    rsum = 0
    minLength = float('inf')
    for r in range(len(nums)):
        rsum += nums[r]
        while rsum >= target:
            minLength = min(minLength, r-l+1)
            rsum -= nums[l]
            l += 1
    return 0 if minLength == float('inf') else minLength

print(minSubArrayLen([2,3,1,2,4,3], 7))
print(minSubArrayLen([1,1,1,1,1,1,1,1], 11))