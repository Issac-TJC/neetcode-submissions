class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        # need = 0
        def dfs(i, need):
            # if i == len(nums):
            if need == 0:
                res.append(cur.copy())
                return
            elif need < 0 or i == len(nums):
                return
            cur.append(nums[i])
            dfs(i, need - nums[i])
            cur.pop()
            dfs(i + 1, need)
        dfs(0, target)
        return res
        