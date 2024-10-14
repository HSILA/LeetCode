# https://leetcode.com/problems/summary-ranges
from typing import List


class Solution:
    def printer(self, track: List[int]):
        if len(track) == 1:
            return str(track[0])
        else:
            return f"{track[0]}->{track[-1]}"

    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return ""
        track = []
        output = []
        for el in nums:
            if not track or el - track[-1] == 1:
                track.append(el)
            else:
                output.append(self.printer(track))
                track = [el]
        output.append(self.printer(track))
        return output
