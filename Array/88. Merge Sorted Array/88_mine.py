# https://leetcode.com/problems/merge-sorted-array/description/
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if all(el == 0 for el in nums1):
            nums1[:] = nums2
        elif n == 0:
            return
        else:
            j = 0
            for i in range(m + n):
                if j == n:
                    break
                if nums2[j] <= nums1[i]:
                    nums1.insert(i, nums2[j])
                    j += 1
                elif all(el == 0 for el in nums1[i:]) and i >= m:
                    nums1[i:] = nums2[j:]
                    break
            nums1[:] = nums1[: m + n]
