# https://leetcode.com/problems/minimum-size-subarray-sum/
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target in nums:
            return 1
        if (len(nums) == 1) and (nums[0] < target):
            return 0

        start = 0
        end = 0
        summ = 0
        min_len = float("inf")

        while end < len(nums):
            summ += nums[end]

            while summ >= target:
                min_len = min(min_len, end - start + 1)
                summ -= nums[start]
                start += 1
            end += 1
        return 0 if min_len == float("inf") else min_len
