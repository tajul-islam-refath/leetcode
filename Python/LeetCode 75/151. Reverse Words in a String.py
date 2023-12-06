class Solution:
    # solution one
    def reverseWordsTwo(self, s: str) -> str:
        words = s.split()
        return " ".join(words[::-1])
    # better solution
    def reverseWords(self, s: str) -> str:
        words = []
        word = ""
        for w in s:
            if w != " ":
                word += w
            elif word != "":
                words.append(word)
                word = ""
        if word != "":
            words.append(word)

        return " ".join(words[::-1])


child = Solution()
print(child.reverseWords("  hello world  "))
