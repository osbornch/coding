# Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height):
        if len(height) <= 2:
            return 0

        ans = 0

        i = 1
        j = len(height) - 1

        lmax = height[0]
        rmax = height[-1]

        while i<=j:
            if height[i] > lmax:
                lmax = height[i]
            if height[j] > rmax:
                rmax = height[j]

            if lmax <= rmax:
                ans += lmax - height[i]
                i += 1

            else:
                ans += rmax - height[j]
                j -= 1

        return ans
    
print(Solution().trap([4,2,0,3,2,5]))