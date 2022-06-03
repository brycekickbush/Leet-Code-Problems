//Faster than 100% of java submissions
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] valid = new int[2];
        for(int x = 0; x < nums.length; x++)
        {
            for(int y = 0; y < nums.length; y++)
            {
                if((nums[x]+nums[y]) == target && x != y)
                {
                    valid[0] = x;
                    valid[1] = y;
                    return valid;
                }
                    
            }
        }
        return valid;
    }
}
