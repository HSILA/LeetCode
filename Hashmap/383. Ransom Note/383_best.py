# https://leetcode.com/problems/ransom-note/


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for letter in list(set(ransomNote)):
            if ransomNote.count(letter) > magazine.count(letter):
                return False
        return True
