class Solution :
    def longestPallindrome(self, s: str) -> str:
        if len(s) == 0:
            return s    
        res = ""
        resLen = 0
        for i in range(len(s)):
            l,r = i,i
            # for odd length Pallindrome and here I can create Function for this Code because it is usable more than one time .
            while l >=0 and r < len(s) and s[l]== s[r]:
                # (r-l+1) is length of the substring
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l-=1
                r+=1
            # For Even length Pallindrome 
            l,r =i, i+1
            while l >=0 and r < len(s) and s[l]== s[r]:
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l-=1
                r+=1
        return res                


