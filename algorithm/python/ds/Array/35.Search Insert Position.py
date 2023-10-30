# https://leetcode.com/problems/spiral-matrix/description/


def searchInsert(nums, target):
    i = 0
    j = len(nums)

    if target <= nums[0]:
        return 0
    elif target > nums[-1]:
        return j
    
    while i < j:
        mid = (i + j) // 2
        if nums[mid] >= target and nums[mid-1] < target:
            break
        elif nums[mid] < target:
            j = mid
        else: 
            i = mid + 1
    return mid




# positive 
print(searchInsert([1,3,5,6], 5))

