class Solution {
    public void sortColors(int[] nums) {
        int zero = 0;
        int one = 0;
        int two = 0;
        int index = 0;
        for(int i=0; i<nums.length; i++)
        {
            if(nums[i] == 0)
            {
                zero ++;
            }
            else if(nums[i] == 1)
            {
                one ++;
            }
            else{
                two ++;
            }
        }
        while(zero > 0)
        {
            nums[index] = 0;
            zero --;
            index ++;
        }
        while(one > 0)
        {
            nums[index] = 1;
            one --;
            index ++;
        }
        while(two > 0)
        {
            nums[index] = 2;
            two --;
            index ++;
        }
    }
}