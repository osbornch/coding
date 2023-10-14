def search(nums, target):
    start = 0
    end = len(nums)-1

    while start <= end:
        mid = start + (end-start)//2


        if nums[mid] > target:
            end = mid-1
        elif nums[mid] < target:
            start = mid+1
        else:
            return mid

    return -1


if __name__ == '__main__':
    nums = [2, 12, 15, 17, 27, 29, 45]
    target = 17
    print(search(nums, target))