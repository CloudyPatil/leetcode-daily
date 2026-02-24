    // 9. Palindrome Number
class Solution {
    public boolean isPalindrome(int x) {
        int reversed = 0; 
       int target = x;
        while(x>0){
           int temp = x % 10;
            x = x / 10;
            reversed = reversed * 10 + temp;
    
        }
       return reversed == target;
    }
}