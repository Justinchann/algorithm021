class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return []
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1
            digits[i] = digits[i] % 10
            if digits[i] != 0:
                return digits
        digits = [0] * (len(digits) + 1)
        digits[0] = 1

        return digits