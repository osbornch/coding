// Two Sum
// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
//https://leetcode.com/problems/two-sum/description/

const trap = (heights) => {  
    let left = 0, right = heights.length -1;
    let trappedWater = 0;
    let leftMaxHeight = 0, rightMaxHeight = 0;

    while(left <= right){
        if(heights[left] < heights[right]){
            if(heights[left] > leftMaxHeight){
                leftMaxHeight = heights[left];
            }else{
                trappedWater += leftMaxHeight - heights[left];
            }
            left ++;
        }else{ 
            if(heights[right] > rightMaxHeight){
                rightMaxHeight = heights[right];
            }else{
                trappedWater += rightMaxHeight - heights[right];
            }

            right--;
        }
    }
    return trappedWater
}

console.log(trap([4,2,0,3,2,5])); // returns [3, 4, 7, 10, 12]