package Two_sum;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
public class Twosum {
    
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> prevMap = new HashMap<>(); // val:index
        for (int i = 0; i < nums.length; i++) {
            int diff = target - nums[i];
            if (prevMap.containsKey(diff)) {
                return new int[] { prevMap.get(diff), i };
            } else {
                prevMap.put(nums[i], i);
            }
        }
        return new int[] {}; // or throw an exception if no solution is found
    }
}

