class Solution:
    def longestSubstringWithoutRepeatation(self,s:str) -> int :
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        start = 0
        end = 0
        max_len = 0
        charSet = set()
        while end < len(s):
            while s[end] in charSet:
                charSet.remove(s[start])
                start+=1
            charSet.add(s[end])
            max_len = max(max_len,end-start+1)
            end+=1
        return max_len    