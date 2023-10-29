const check_for_target = (nums, target) => {
    let left = 0;
    let right = nums.length - 1;

    while(left < right) { 
      let curr = nums[left] + nums[right];
      if (curr == target){
        return true;
      }

      if (curr > target){
        left++;
      }

      if (curr < target){
        right--;
      }
    }

    return false;

  };
  
  console.log(check_for_target([1,2,3,4,5], 6)); // returns [3, 4, 7, 10, 12]
  console.log(check_for_target([1,2,3,4,5], 10)); // returns [3, 4, 7, 10, 12]