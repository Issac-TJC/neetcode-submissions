class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # for i in nums1, i+j=(m+n)/2, if (m+n)%2=0 return i/j else i+j/2
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        l = 0
        m, n = len(nums1), len(nums2)
        r = m - 1

        while True:
            i = l + (r - l) // 2
            j = (m + n) // 2 - i - 2

            nums1_left_max = float('-inf') if i < 0 else nums1[i]
            nums1_right_min = float('inf') if (i + 1) >= m else nums1[i + 1]
            
            nums2_left_max = float('-inf') if j < 0 else nums2[j]
            nums2_right_min = float('inf') if (j + 1) >= n else nums2[j + 1]    

            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:   
                if (m + n) % 2:
                    return min(nums1_right_min, nums2_right_min)
                else:
                    return (max(nums1_left_max, nums2_left_max) + 
                            min(nums1_right_min, nums2_right_min)) / 2.0  
            elif nums1_left_max > nums2_right_min:
                r = i - 1
            else:
                l = i + 1
            