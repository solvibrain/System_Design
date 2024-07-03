class Solution :
    def permutation(self, nums : List[int]) -> List[List[int]]:
        length = len(nums)
        result = []
        #base Case
        if length == 1 :
            return [nums[:]]
        for i in range(length):
            n = nums.pop(0)
            perms = self.permutation(nums)
            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)

        return result        