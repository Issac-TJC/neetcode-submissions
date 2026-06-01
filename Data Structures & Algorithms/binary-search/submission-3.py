class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        # while l <= r [l,r]
        while l < r: # [l,r)
            i = (r + l) // 2
            if nums[i] == target:
                return i
            elif nums[i] < target:
                # [l,
                l = i + 1
            else:
                r = i # ,r)
                # r = i - 1 # ,r]
        return -1
        