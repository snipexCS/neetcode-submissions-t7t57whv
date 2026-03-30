class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        last = n + m - 1 
        leftLast = m - 1 
        rightLast = n - 1 
        while rightLast >= 0:
            if leftLast >= 0 and nums1[leftLast] > nums2[rightLast]:
                nums1[last] = nums1[leftLast]
                leftLast-=1
            else:
                nums1[last] = nums2[rightLast]
                rightLast-=1
            last -= 1