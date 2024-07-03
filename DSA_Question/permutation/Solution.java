package permutation;

import java.util.ArrayList;
import java.util.List;

public class Solution {
    public List<List<Integer>> permutation(int[] nums) {
        int length = nums.length;
        List<List<Integer>> result = new ArrayList<>();
        
        // Base Case
        if (length == 1) {
            List<Integer> singleElementList = new ArrayList<>();
            singleElementList.add(nums[0]);
            result.add(singleElementList);
            return result;
        }
        
        for (int i = 0; i < length; i++) {
            int n = nums[i];
            int[] remainingNums = new int[length - 1];
            System.arraycopy(nums, 0, remainingNums, 0, i);
            System.arraycopy(nums, i + 1, remainingNums, i, length - i - 1);
            
            List<List<Integer>> perms = permutation(remainingNums);
            for (List<Integer> perm : perms) {
                perm.add(n);
            }
            result.addAll(perms);
        }
        
        return result;
    }
}