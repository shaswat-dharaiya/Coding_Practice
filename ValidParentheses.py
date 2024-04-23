class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        pair = {")":"(", "]":"[", "}":"{"}

        for ch in s:
            if ch in ["(", "{", "["]:
                stack.append(ch)
            else:
                if len(stack) == 0 and ch in pair.keys():
                    return False
                if pair[ch] == stack[len(stack)-1]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

                