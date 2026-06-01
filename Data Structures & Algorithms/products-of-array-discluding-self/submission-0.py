class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul = {}
        zero_idx = 0
        num_zero = 0
        p = 1

        for i in range(len(nums)):
            if nums[i] == 0:
                if num_zero == 0:
                    num_zero += 1
                    zero_idx = i
                else:
                    num_zero += 1
                    res = [0]*len(nums)
                    return res
            else:
                p *= nums[i]
        
        if num_zero:
            res = [0]*len(nums)
            res[zero_idx] = p
            return res
        
        res = []

        for i in range(len(nums)):
            if nums[i] in mul:
                res.append(mul[nums[i]])
            else:
                num = p // nums[i]
                res.append(num)
                mul[nums[i]] = num
            
        return res
