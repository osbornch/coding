// Two Sum
// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
//https://leetcode.com/problems/two-sum/description/

const spiralOrder = (matrix) => {  
    const m = matrix.length;
    const n = matrix[0].length;

    let top = 0
    let bottom = m-1
    let left = 0
    let right = n-1

    const result = []
    while(top<= bottom && left <= right) {
        for(let j=left; j<=right; j++){
            result.push(matrix[top][j])
        }  
        top++;

        for(let i=top; i<=bottom; i++){
            result.push(matrix[i][right])
        }   

        right--;

        if(top<=bottom){
            for(let j=right; j>=left; j--){
                result.push(matrix[bottom][j])
            }   
            bottom--;
        }

        if(left <= right){
            for(let i=bottom; i>=top; i--){
                result.push(matrix[i][left])
            }
            left ++;
        }
    }
    return result;
}

console.log(spiralOrder([[1,2,3],[4,5,6],[7,8,9]])); // returns [3, 4, 7, 10, 12]