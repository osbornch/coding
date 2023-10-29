const check_for_target = (s) => {
    let left = 0;
    let right = s.length - 1;

    while(left < right) { 
      if (s[left] != s[right]){
        return false;
      }
      left ++;
      right --;
    }

    return true;
  };
  
  console.log(check_for_target("abba")); 
  console.log(check_for_target("abbaa")); 