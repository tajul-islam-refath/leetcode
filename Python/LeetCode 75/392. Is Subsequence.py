class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        step = 0
        for i in range(len(t)):
            if s[step] == t[i]:
                step += 1
                if step == len(s):
                    return True
        return False
