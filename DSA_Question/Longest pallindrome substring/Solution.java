public class Solution {
    public String longestPalindrome(String s) {
        if (s.length() == 0) {
            return s;
        }
        String res = "";
        int resLen = 0;
        for (int i = 0; i < s.length(); i++) {
            int l = i, r = i;
            // for odd length Palindrome
            while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {
                // (r-l+1) is length of the substring
                if (r - l + 1 > resLen) {
                    res = s.substring(l, r + 1);
                    resLen = r - l + 1;
                }
                l--;
                r++;
            }
            // For Even length Palindrome
            l = i;
            r = i + 1;
            while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {
                if (r - l + 1 > resLen) {
                    res = s.substring(l, r + 1);
                    resLen = r - l + 1;
                }
                l--;
                r++;
            }
        }
        return res;
    }
}