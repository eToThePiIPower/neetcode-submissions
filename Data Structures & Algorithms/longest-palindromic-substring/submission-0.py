class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, resLen = "", 0
        for i in range(len(s)):
            # check odd-length palindromes
            for n in range(min(i, len(s) - i - 1) + 1):
                string = s[i-n:i+n+1]
                if string != string[::-1]: break
                elif len(string) <= resLen: continue
                else:
                    res = string
                    resLen = len(string)

            # check even-length palindromes
            for n in range(min(i, len(s) - i - 2) + 1):
                string = s[i-n:i+n+2]
                if string != string[::-1]: break
                elif len(string) <= resLen: continue
                else:
                    res = string
                    resLen = len(string)
        return res

        
