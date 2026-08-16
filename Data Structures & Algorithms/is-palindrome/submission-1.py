class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([i.lower() for i in s if i.isalnum()])

        for idx in range((len(s)+1)//2):
            if s[idx] != s[-1-idx]:
                return False
        return True