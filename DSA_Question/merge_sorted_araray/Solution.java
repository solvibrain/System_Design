package merge_sorted_araray;

public class Solution {
    public void mergeSortedArray(int[] nums1, int m, int[] nums2, int n) {
        int last = m + n - 1;
        while (m > 0 && n > 0) {
            if (nums1[m - 1] > nums2[n - 1]) {
                nums1[last] = nums1[m - 1];
                m--;
            } else {
                nums1[last] = nums2[n - 1];
                n--;
            }
            last--;
        }
        // If elements in nums2 remain even after iterating, we will put all those in nums1
        while (n > 0) {
            nums1[last] = nums2[n - 1];
            n--;
            last--;
        }
    }
} 
