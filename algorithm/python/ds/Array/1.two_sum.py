# Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums, target):
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
        return []
    
print(Solution().twoSum([2,7,11,15], 9))