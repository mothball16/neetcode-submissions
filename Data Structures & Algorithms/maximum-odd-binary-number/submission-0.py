class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count("1")
        not_ones = len(s) - s.count("1")
        return "1" * (ones - 1) + "0" * not_ones + "1"
        