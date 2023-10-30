// Two Sum
// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
// https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/solutions/

const minTaps = function(n, ranges) {  
    const arr = new Array(n+1).fill(0);
    for(let i=0; i<ranges.length; i++){
        if(ranges[i] === 0) continue;
        const left = Math.max(0, i-ranges[i]);
        arr[left] = Math.max(arr[left], i+ranges[i]);
    }

    let end = 0, far_can_reach = 0, count = 0;
    for(let i=0; i<=n; i++){
        if(i>end){
            if(far_can_reach === end) return -1;
            end = far_can_reach;
            count++;
        }
        far_can_reach = Math.max(far_can_reach, arr[i]);

    }
    return count + (end <n? 1:0);

}

console.log(minTaps(5,  [3,4,1,1,0,0])); // returns [3, 4, 7, 10, 12]
console.log(minTaps(3,  [0,0,0,0])); // returns [3, 4, 7, 10, 12]

// TC: O(N~2)
// SC: O(N)