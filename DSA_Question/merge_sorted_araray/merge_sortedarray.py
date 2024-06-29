class Solution :
    def merge_sorted_array(self,nums1: List[int],m : int ,  nums2 : List[int], n : int) -> None:
        last = m+n-1
        while m>0 and n>0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums[m-1]
                m-=1
            else :
                nums1[last] = nums2[n-1]    
                n-=1
            last-=1
        # If element in the nums2 remains even after iterating , we will put all those in nums1
        while n >0:
            nums1[last]= nums2[n-1]
            n,last = n-1,last-1
            
