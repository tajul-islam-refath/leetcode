class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        if len(nums) < 3:
            return False

        i = float('inf')
        j = float('inf')
        for num in nums:
            if num <= i:
                i = num
            elif num <= j:
                j = num
            else:
                return True
        return False


obj = Solution()
print(obj.increasingTriplet(([1,2,1,3])))
