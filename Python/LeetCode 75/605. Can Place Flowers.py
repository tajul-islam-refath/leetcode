# version I
# class Solution:
#     def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#         if len(flowerbed) == 1:
#             if flowerbed[0] == 0 or (flowerbed[0] == 1 and n == 0):
#                 return True
#             else:
#                 return False
#
#
#         for i in range(len(flowerbed)):
#             if i==0:
#                 if flowerbed[i] == 0 and flowerbed[i+1] == 0:
#                     flowerbed[i] = 1
#                     n -= 1
#             elif i == len(flowerbed)-1:
#                  if flowerbed[i] == 0 and flowerbed[i-1] == 0:
#                     flowerbed[i] = 1
#                     n -= 1
#             else:
#                  if flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0:
#                     flowerbed[i] = 1
#                     n -= 1
#         return n <= 0

# version II
class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:

        # Iterate and check left and right
        for i in range(len(flowerbed)):

            # Check if current cell is clear:
            if flowerbed[i] == 0:
                # If so, check neighboring cells
                isLeftEmpty = i == 0 or flowerbed[i - 1] == 0
                isRightEmpty = i == len(flowerbed) - 1 or flowerbed[i + 1] == 0

                # If both left and right empty, decrement n. Return True if n = 0 (its possible)
                flowerbed[i] = 1 if isLeftEmpty and isRightEmpty else 0
                n -= flowerbed[i]
        # If we get here, its not possible
        return n <= 0

l = [1,0,1,0,1,0,1]
n = 0
sol = Solution()
print(sol.canPlaceFlowers(l , n))