class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s) - 1

        def isVowel(w):
            return w == 'a' or w == 'e' or w == 'i' or w == 'o' or w == 'u'

        while left < right:
            if isVowel(s[left]) and isVowel(s[right]):
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            if not isVowel(s[left]):
                left += 1
            if not isVowel(s[right]):
                right -= 1
        return s

child = Solution()
print(child.reverseVowels("leetcode"))