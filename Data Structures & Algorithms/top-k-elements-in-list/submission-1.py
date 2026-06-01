class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num,0)

        res = sorted(count.items(), key = lambda x:x[1], reverse = True)
        res1 = []
        for i in range(k):
            res1.append(res[i][0])
        return res1