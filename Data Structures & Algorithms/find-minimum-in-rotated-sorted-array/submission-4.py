class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)
        m = nums[0]
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < m:
                m = nums[mid]
                r = mid
            else:
                l = mid + 1
        return m
        