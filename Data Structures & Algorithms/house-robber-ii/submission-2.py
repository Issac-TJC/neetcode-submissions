class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        dp1 = [0] * n
        dp2 = [0] * n
        dp1[0] = nums[0]
        dp2[0] = 0
        dp1[1] = max(nums[0], nums[1])
        dp2[1] = nums[1]
        for i in range(2, n):
            if i == n - 1:
                dp1[i] = max(dp1[i-1], dp2[i-2] + nums[i])
            else:
                dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i])
            dp2[i] = max(dp2[i-1], dp2[i-2] + nums[i])
        return dp1[n - 1]
        