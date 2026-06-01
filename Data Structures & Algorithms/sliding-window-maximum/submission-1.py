class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        l = 0
        res = []

        for i in range(k):
            if nums[l] < nums[i]:
                l = i
        res.append(nums[l])

        for r in range(k, len(nums)):
            if r - l < k:
                if nums[r] >= nums[l]:
                    l = r
                res.append(nums[l])
            else:
                l = r
                for i in range(k):
                    if nums[r-i] > nums[l]:
                        l = r-i
                res.append(nums[l])
        return res
        