class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        if nums[r] == target:
            return r
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target > nums[r]:
                r = mid
            elif nums[mid] > nums[r] > target:
                l = mid + 1
            elif nums[r] > nums[mid] > target:
                r = mid
            elif nums[r] > target > nums[mid]:
                l = mid + 1
            elif target > nums[r] > nums[mid]:
                r = mid
            elif target > nums[mid] > nums[r]:
                l = mid + 1
        return l if nums[l] == target else -1
        