// Two Sum
// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
//https://leetcode.com/problems/two-sum/description/

const twoSum = (nums, target) => {  
    const map = new Map();
    for(let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];

        if(map.has(complement)) {
            return [map.get(complement), i]
        }
        map.set(nums[i], i);
    }
}

console.log(twoSum())