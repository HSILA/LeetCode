# https://leetcode.com/problems/minimum-size-subarray-sum/
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target in nums:
            return 1
        if (len(nums) == 1) and (target not in nums):
            return 0

        i = 0
        j = 1
        lens = []

        while i + j <= len(nums):
            window = nums[i : i + j]
            if sum(window) >= target:
                i += 1
                j -= 1
                lens.append(len(window))
            else:
                j += 1
        return min(lens) if lens else 0
