import java.util.Arrays;

public class Solution {
    public int[] twoSum(int[] nums, int target) {
        // we will take 2 pointer 
        int left = 0;
        int right = nums.length - 1;
        
        // Iterating through the array until l < r
        while (left < right) {
            // calculating the sum of two pointers
            int sum = nums[left] + nums[right];
            // Criteria Setting 
            if (sum > target) {
                right -= 1;
            } else if (sum < target) {
                left += 1;
            } else {
                return new int[]{left + 1, right + 1};
            }
        }
        return new int[]{}; // return empty array if no solution is found
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums = {2, 7, 11, 15};
        int target = 9;
        int[] result = solution.twoSum(nums, target);
        System.out.println(Arrays.toString(result));
    }
}