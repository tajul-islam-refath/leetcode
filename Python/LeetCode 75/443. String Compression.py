class Solution:
    def compress(self, chars: list[str]) -> int:
        s = ""
        charPairs = []
        ans = []
        for c in chars:
            if c in s:
                s += c
            else:
                if s != "":
                    charPairs.append([s[0], len(s)])
                    s = ""
                if s == "":
                    s += c
        if s != "":
            charPairs.append([s[0], len(s)])

        for pair in charPairs:
            ans.append(pair[0])
            if pair[1] != 1:
                for i in str(pair[1]):
                    ans.append(i)

        chars.clear()
        chars.extend(ans)
        return len(ans)


child = Solution()
print(child.compress(["a", "a", "a", "b", "b", "a", "a"]))
