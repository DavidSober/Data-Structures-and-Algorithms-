# beats 72% in time and 35% in space

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(curr, i):
            if len(curr) == k:
                ans.append(curr[:])
                return 
            
            for num in range(i, n + 1):
                curr.append(num)
                backtrack(curr, num + 1)
                curr.pop()
        backtrack([], 1)
        return ans

