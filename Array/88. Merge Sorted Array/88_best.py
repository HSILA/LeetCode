# https://leetcode.com/problems/merge-sorted-array/description/
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        pm, pn, p = m-1, n-1, m+n-1

        while pm >= 0 and pn >= 0:
            if nums1[pm] > nums2[pn]:
                nums1[p] = nums1[pm]
                pm -= 1
            else:
                nums1[p] = nums2[pn]
                pn -= 1
            p -= 1

        while pn >= 0:
            nums1[p] = nums2[pn]
            pn -= 1
            p -= 1
