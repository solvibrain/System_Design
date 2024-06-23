class Solution:
    def twoSum(self, nums:List[int], target:int) -> List[int]:
        prevMap = {} # val:index
        for i,v in enumerate(nums):
            diff = target -v
            if diff in prevMap:
                return [prevMap[diff],i]
            else:   
                prevMap[v] =i
        return         