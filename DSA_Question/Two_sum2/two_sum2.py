class Solution :
    def two_sum2(self, nums : List[int], target:int)-> List[int]:
        # we will take 2 pointer 
        left = 0
        right = len(nums)-1
        
        # Iterating through the array untill l<r
        while(left<right):
            # calculating the sum of two pointers
            sum = nums[left] + nums[right]
            # Criteria Settting 
            if sum > target:
                right -= 1
            elif sum < target :
                left +=1
            else : 
                return [left+1, right+1]        