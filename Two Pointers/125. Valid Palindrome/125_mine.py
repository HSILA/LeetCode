# https://leetcode.com/problems/valid-palindrome/description/


class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for c in s:
            if (ord(c) >= 48 and ord(c) <= 57) or (ord(c) >= 97 and ord(c) <= 122):
                new_s += c
            elif ord(c) >= 65 and ord(c) <= 90:
                new_s += chr(ord(c) + 32)

        mid = len(new_s) // 2

        for i in range(mid):
            if new_s[i] != new_s[len(new_s) - 1 - i]:
                return False

        return True
