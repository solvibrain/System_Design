# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
First Intuition was to use three loop after sorting the array to remove duplicacy and we can use other operations also to remove first duplicay, but when we will use three loops it will give 0(n3)
# Approach
<!-- Describe your approach to solving the problem. -->
So , using first sorting algorithm and then using first loop to get first element for the combination and then for remaining two we will simply use algorithm that is getting use for two sum 2. Using loop and two pointer , first is pointing to starting index and other is pointing to last index and then summing up and checking and then updating according to criteria that is used in code.
# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
0(n2)
- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
o(1) and sometimes if sorting algorithm is taking space then o(n)
# Code
```
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()

        for i , e in enumerate(nums):
            if i> 0 and e == nums[i-1]:
                continue
            l, r = i +1, len(nums)-1
            while l<r:
                threeSum = e + nums[l]+nums[r]

                if threeSum > 0:
                    r-=1
                elif threeSum < 0:
                    l+=1
                else:
                    res.append([e,nums[l],nums[r]])        
                    # updating the pointer for further getting other combination 
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        return res                

```