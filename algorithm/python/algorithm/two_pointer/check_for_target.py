def check_for_target(numbers, target):
    left =0
    right = len(numbers)-1
    while left < right:
        curr = numbers[left] + numbers[right]
        if curr == target:
            return True
        if curr > target:
            left += 1
        if curr < target:
            right -= 1
    return False

print(check_for_target([1,2,3,4,5,6,7,8,9], 10))
print(check_for_target([1,2,3,4,5,6,7,8,9], 20))