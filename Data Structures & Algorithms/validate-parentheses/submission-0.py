class Solution:
    def isValid(self, s: str) -> bool:
        pair = {')': '(', '}': '{', ']': '['}
        stack =[]
        for i in s:
            if i in '([{':
                stack.append(i)
            else:
                if not stack or stack[-1] != pair.get(i):
                    return False
                stack.pop()

        return not stack

