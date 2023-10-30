// Two Sum
// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
//https://leetcode.com/problems/two-sum/description/

const searchInsert = (nums, target) => {  
    let left = 0, right = nums.length;
    while(left <= right){
        let mid = left + right >> 1;
        if(nums[mid] == target) return mid
        if(nums[mid] < target)
            left = mid + 1;
        else
            right = mid - 1;
        
    }
    return left;
}

console.log(searchInsert([1,3,5,6], 5)); // returns [3, 4, 7, 10, 12]