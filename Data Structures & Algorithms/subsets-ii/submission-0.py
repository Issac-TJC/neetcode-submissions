class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        cur = []

        def backtrack(i):
            if i == len(nums):
                res.append(cur.copy())
                return
            cur.append(nums[i])
            backtrack(i + 1)
            cur.pop()
            while i < len(nums) - 1 and nums[i + 1] == nums[i]:
                i += 1
                continue
            backtrack(i + 1)
        
        backtrack(0)
        return res
        