class Solution:
    def kidsWithCandies(self, candies, extraCandies: int) -> list[bool]:
        maxValue = max(candies)
        ansList = []
        for v in candies:
            if v + extraCandies >= maxValue:
                ansList.append(True)
            else:
                ansList.append(False)
        return ansList
