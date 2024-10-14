# https://leetcode.com/problems/ransom-note/
# https://leetcode.com/problems/ransom-note/solutions/5644265/easiest-faster-lesser-c-python3-java-c-python-c-explained-beats

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for letter in list(set(ransomNote)):
            if ransomNote.count(letter) > magazine.count(letter):
                return False
        return True
