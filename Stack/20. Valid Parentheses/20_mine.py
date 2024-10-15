# https://leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for char in s:
            if char in mapping:
                stack.append(char)
            else:
                if not stack:
                    return False
                last = stack.pop()
                if mapping[last] != char:
                    return False

        return not stack
