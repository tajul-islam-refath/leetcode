class Solution:
    # time complexity -> O(n^2)
    # space complexity -> O(n)
    def increasingTriplet(self, nums: list[int]) -> int:
        ans = []
        ans.append(float("inf"))
        for num in nums:
            flag = False
            for i in range(len(ans)):
                if num <= ans[i]:
                    ans[i] = num
                    flag = True
                    break
            if not flag:
                ans.append(num)
        return len(ans)

    def increasingTripletBS(self, nums: list[int]) -> int:
        ans = [float("inf")]
        for num in nums:
            self.bs(0, len(ans)-1, num, ans)
        return len(ans)

    def bs(self, l: int, r: int, num: int, ans):
        #print(f"left-{l}, right-{r}, num-{num}, ans-{ans}")
        if r == l:
            if num <= ans[l]:
                ans[l] = num
            else:
                ans.append(num)
            return
        mid = (r + l) // 2
        if ans[mid] == num:
            ans[mid] = num
            return
        if ans[mid] > num:
            self.bs(l, mid-1, num , ans)
        else:
            self.bs(mid+1, r, num , ans)


obj = Solution()
print(obj.increasingTripletBS([10,9,2,5,3,7,101,18]))
