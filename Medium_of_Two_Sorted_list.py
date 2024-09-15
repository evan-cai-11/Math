class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        index1 = 0
        index2 = 0
        total = len(nums1) + len(nums2)
        merged = [0] * total
        curr = 0

        while index1 < len(nums1) and index2 < len(nums2):
            if nums1[index1] >= nums2[index2]:
                merged[curr] = nums2[index2]
                index2 += 1
                curr += 1
            else:
                merged[curr] = nums1[index1]
                index1 += 1
                curr += 1
        
        remaining = None
        index_remain = 0
        if index1 >= len(nums1):
            remaining = nums2
            index_remain = index2
        else:
            remaining = nums1
            index_remain = index1

        for i in range(index_remain, len(remaining)):
            merged[curr] = remaining[i]
            curr += 1

        if total == 0:
            return None
        elif total % 2 == 1:        
            return merged[int(total / 2)]
        else:
            return (merged[int(total / 2) - 1] + merged[int(total / 2)]) / 2 