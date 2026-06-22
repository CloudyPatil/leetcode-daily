class Solution {
    public int[] sortArrayByParity(int[] nums) {
        int[] ans = new int[nums.length];
        int insert = 0;
        for(int i=0; i<nums.length; i++)
        {
            if(nums[i] % 2 == 0)
            {
                ans[insert] = nums[i];
                insert ++;
            }
        }
        for(int i=0; i<nums.length; i++)
        {
            if(nums[i] % 2 != 0)
            {
                ans[insert] = nums[i];
                insert ++;
            }
        }
        return ans;
    }
}