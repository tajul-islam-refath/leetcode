class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        def checkAsteroid(value:int):
            if len(ans) == 0:
                ans.append(value)
            elif value > 0 and ans[-1] > 0:
                ans.append(value)
            elif value < 0 and ans[-1] < 0:
                ans.append(value)
            elif value < 0:
                if abs(value) == abs(ans[-1]):
                    ans.pop()
                elif abs(ans[-1]) < abs(value):
                    ans.pop()
                    checkAsteroid(value)
            else:
                ans.append(value)

        for value in asteroids:
            checkAsteroid(value)
        return ans