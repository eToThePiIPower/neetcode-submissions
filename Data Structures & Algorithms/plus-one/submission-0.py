class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [0] + digits
        ans = [0] * (len(digits))
        carry = 1
        for idx in range(len(digits) - 1, -1, -1):
            ans[idx] = (digits[idx] + carry) % 10
            carry = (digits[idx] + carry) // 10
        if ans[0] != 0:
            return ans
        else:
            return ans[1:]


