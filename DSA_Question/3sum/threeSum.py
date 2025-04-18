class Solution :
    def threeSum(self, nums : list[int]) -> list[list[int]]:
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
                    l+1
                else:
                    res.append([e,nums[l],nums[r]])        
                    # updating the pointer for further getting other combination 
                    l+=1
                    while nums[l] == nums[l-1] and l<r :
                        l+=1
        return res                
