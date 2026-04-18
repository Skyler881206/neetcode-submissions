class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair_parentheses = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for i in range(len(s)):
            if s[i] in ["(", "[", "{"]:
                stack.append(s[i])
                continue

            if s[i] in [")", "]", "}"]:
                if len(stack) == 0:
                    return False
                pop_item = stack.pop()

                if pair_parentheses[s[i]] != pop_item:
                    return False
        if len(stack) != 0:
            return False
        return True
                