class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        size = 0
        maxs = 0

        for num in nums:
            if (num-1) not in s:
                size = 1
                while (num+size) in s:
                    size += 1
                maxs = max(size,maxs)
        
        return maxs
        