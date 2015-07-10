

class Solution:
    ''' 
        merges two sorted list, then return the number in the middle 
        This should take O(m+n), but it somehow passes leetcode's test
    '''

    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        
        nums1 = self.mergeSorted(nums1, nums2)
        
        if len(nums1) % 2 == 0:
            return (nums1[(len(nums1) - 2)/2] + nums1[len(nums1)/2]) / 2.0
        else:
            return nums1[(len(nums1) - 1)/2]
    
    def mergeSorted(self, nums1, nums2):
    
        res = [0] * (len(nums1) + len(nums2))
        i = 0
        j = 0
        c = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                res[c] = nums1[i]
                i += 1
            else:
                res[c] = nums2[j]
                j += 1
            c += 1
        
        while i < len(nums1):
            res[c] = nums1[i]
            i+=1
            c+=1
        while j < len(nums2):
            res[c] = nums2[j]
            j+=1
            c+=1
    
    return res

