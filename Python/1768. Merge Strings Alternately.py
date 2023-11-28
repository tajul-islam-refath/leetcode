class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        lw1 = len(word1)
        lw2 = len(word2)
        output = ""
        for i in range(min(lw1, lw2)):
            output += word1[i]
            output += word2[i]

        if lw1 > lw2:
            output += word1[lw2:lw1]
        elif lw2 > lw1:
            output += word2[lw1:lw2]

        return output


word1, word2 = input().split()
solu = Solution()
print(solu.mergeAlternately(word1, word2))
