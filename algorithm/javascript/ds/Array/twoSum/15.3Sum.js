// Two Sum
// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
//https://leetcode.com/problems/two-sum/description/
const threeSum = (nums, target) => {  

    nums.sort((a,b) => a - b);
    const result = [];

    for(let i = 0; i < nums.length; i++) {
        if(i>0 && nums[i-1] === nums[i]) continue;
        let left = i+1
        let right = nums.length - 1;
        while(left < right){
            const sum = nums[i] + nums[left] + nums[right]
            if(sum < target){
                left++;
            }else if(sum > target){
                right--;    
            }else{
                result.push([nums[i], nums[left], nums[right]]);
                left++;
                while(nums[left] === nums[left-1]){
                    left++;
                }   
                right--;
                while(nums[right] === nums[left+1]){
                    right--;
                }
            }
        }
    }
    return result;
}

console.log(threeSum([-1,0,1,2,-1,-4], 0)); // returns [3, 4, 7, 10, 12]