class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = 0
        r = len(nums) - 1
        nums.sort()
        # res = []
        mp = {}
        while l < r-1:
            mid = l + 1
            if nums[l] + nums[mid] + nums[r] > 0:
                r -= 1
            r1 = r
            while mid < r1:
                if nums[l] + nums[mid] + nums[r1] == 0:
                    mp[(nums[l], nums[mid], nums[r1])] = 1
                    # res.append([nums[l], nums[mid], nums[r1]])
                    r1 -= 1
                    mid += 1
                    while mid < r1 and nums[mid-1] == nums[mid]:
                        mid += 1
                elif nums[l] + nums[mid] + nums[r1] < 0:
                    mid += 1
                else:
                    r1 -= 1
            l += 1
            while l < r-1 and nums[l-1] == nums[l]:
                l += 1
        # return res
        return list(mp.keys())
        