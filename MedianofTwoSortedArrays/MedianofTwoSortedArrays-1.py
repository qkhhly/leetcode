class Solution:
    ''' 
        This uses Python's built in sort function, which is timsort. 
        Timsort should take O(m+n) in the best case, but this somehow passes
        leetcode's test, and it is one of the faster Python solution comparing 
        to other Python solutions...
    '''

    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        nums1 = sorted(nums1)
        
        if len(nums1) % 2 == 0:
            return (nums1[(len(nums1) - 2)/2] + nums1[len(nums1)/2]) / 2.0
        else:
            return nums1[(len(nums1) - 1)/2]