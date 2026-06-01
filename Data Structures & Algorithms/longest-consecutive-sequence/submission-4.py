class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        prev = -1
        length = 0
        maxlen = 0
        for i in range(len(nums)):
            if nums[i] == prev and i != 0:
                continue
            if nums[i] != prev + 1:
                if length > maxlen:
                    maxlen = length
                length = 1
            else:
                length += 1
            prev = nums[i]
        if length > maxlen:
            maxlen = length
        return maxlen
