class Solution:
    def moveZeroes(self, nums: list[int]) -> list[int]:
        slow = 0
        first = 1
        while first < len(nums):
            if nums[slow] == 0 and nums[first] != 0:
                nums[slow], nums[first] = nums[first], nums[slow]
                slow += 1
                first += 1
            else:
                first += 1

        return nums


child = Solution()
print(child.moveZeroes([0, 0, 1]))
