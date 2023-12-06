class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        s_list = list(s.lowercase())  # Convert the string to a list

        def isVowel(w):
            return w in "AEIOUaeiou"

        while left < right:
            if isVowel(s_list[left]) and isVowel(s_list[right]):
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
            if not isVowel(s_list[left]):
                left += 1
            if not isVowel(s_list[right]):
                right -= 1

        return ''.join(s_list)  # Convert the list back to a string


child = Solution()
print(child.reverseVowels("leetcode"))
