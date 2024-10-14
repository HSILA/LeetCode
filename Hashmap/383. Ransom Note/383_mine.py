# https://leetcode.com/problems/ransom-note/


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_hash = {}
        for c in magazine:
            mag_hash[c] = mag_hash[c] + 1 if c in mag_hash else 1
        rans_hash = {}
        for c in ransomNote:
            rans_hash[c] = rans_hash[c] + 1 if c in rans_hash else 1

        for k in rans_hash.keys():
            if k not in mag_hash:
                return False
            elif rans_hash[k] > mag_hash[k]:
                return False

        return True
