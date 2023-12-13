class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxWater = 0
        for i in range(len(height) - 1):
            water = 0
            for j in range(i + 1, len(height)):
                water = max(min(height[i], height[j]) * (j - i), water)
            maxWater = max(maxWater, water)
        return maxWater

    def maxAreaTwoPointer(self, height: list[int]) -> int:
        maxWater = 0
        left = 0
        right = len(height) - 1
        while left < right:
            water = min(height[left], height[right]) * (right - left)
            maxWater = max(maxWater, water)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return maxWater


child = Solution()
print(child.maxAreaTwoPointer(([1,8,6,2,5,4,8,3,7])))
