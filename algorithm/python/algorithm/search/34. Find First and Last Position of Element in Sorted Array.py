

def searchLeft(nums, target):
    left = 0
    right = len(nums)-1
    leftBorder = -2
    while left <= right:
        mid = left + (right - left) >> 1
        if (nums[mid] >= target):
            right = mid - 1
            leftBorder = right
        else:
            left = mid + 1
    return leftBorder

def searchRight(nums, target):
    left = 0
    right = len(nums)-1
    rightBorder = -2
    while left <= right:
        mid = left + (right - left) >> 1
        if (nums[mid] > target):
            right = mid - 1
        else:
            left = mid + 1
            rightBorder = left
    return rightBorder


def searchRange(nums, target):
    leftBorder = searchLeft(nums, target)
    rightBorder = searchRight(nums, target)
    if leftBorder == -2 or rightBorder == -2:
        return [-1,-1]
    if rightBorder - leftBorder > 1:
        return [leftBorder+1, rightBorder-1]
    return [-1, -1]

print(searchRange([5,7,7,8,8,10], 8))
print(searchRange([5,7,7,8,8,10], 6))