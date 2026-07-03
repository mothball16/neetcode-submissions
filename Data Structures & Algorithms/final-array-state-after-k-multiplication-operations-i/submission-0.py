class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            min = math.inf
            minIdx = 0
            for i, value in enumerate(nums):
                if min > value:
                    minIdx = i
                    min = value
            nums[minIdx] *= multiplier

        return nums