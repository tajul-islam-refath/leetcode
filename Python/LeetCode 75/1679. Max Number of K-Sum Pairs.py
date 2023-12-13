class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        cnt = 0
        for i in range(len(nums) - 1):
            if nums[i] != -1:
                num = k - nums[i]
                for j in range(i + 1, len(nums)):
                    if nums[j] == num and nums[j] != -1:
                        nums[i] = nums[j] = -1
                        cnt += 1
                        break
        return cnt

    def maxOperationsTwoPointer(self, nums: list[int], k: int) -> int:
        cnt = 0
        left = 0
        right = len(nums) - 1
        nums.sort()
        while left < right:
            if nums[left] + nums[right] == k:
                cnt += 1
                left += 1
                right -= 1
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                right -= 1
        return cnt


child = Solution()
print(child.maxOperationsTwoPointer([4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4], 2))
