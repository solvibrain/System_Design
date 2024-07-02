class Solution :

    def rob(self, nums : list[int]) -> int:
        # n=len(nums)
        # if n == 1 :
        #     return nums[0]
        # if n==2:
        #     return max(nums[0],nums[1])
        if len(nums) == 1:
            return nums[0]
        rob1 , rob2 = 0,0
        #[rob1,rob2,num, num+1 ......]
        for num in nums:
            temp = max(rob1+num,rob2)
            rob1 = rob2
            rob2 = temp
        return rob2    
        # return max(nums[0]+ self.rob(nums[2:n]), self.rob(nums[1:n]))
            

        