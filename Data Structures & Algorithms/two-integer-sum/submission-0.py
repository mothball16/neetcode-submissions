class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        matches = {}
        for i, num in enumerate(nums):
            match = matches.get(target - num)
            if not match is None:
                return [match, i]
            matches[num] = i
        # impossible to reach
        return []

