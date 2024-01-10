class Solution:
    def removeStars(self, s: str) -> str:
        ans_stack = []
        for c in s:
            if c == '*':
                if len(ans_stack) != 0:
                    ans_stack.pop()
            else:
                ans_stack.append(c)
        print(ans_stack)
        return "".join(ans_stack)