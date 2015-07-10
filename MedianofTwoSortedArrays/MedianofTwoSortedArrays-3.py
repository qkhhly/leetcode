

def findMedianSortedArraysOdd(n1, n2, n1s, n1e, half):

    mid = (n1s + n1e)/2
    if n1[mid] >= n2[half - mid - 1] and n1[mid] < n2[half - mid]:
        return n1[mid]
    elif n1s == n1e:
        return findMedianSortedArraysOdd(n2, n1, 0, len(n2), half)
    elif n1[mid] < n2[half - mid]:
        return findMedianSortedArraysOdd(n1, n2, mid, n1e, half)
    else:
        return findMedianSortedArraysOdd(n1, n2, n1s, mid, half)


def findMedianSortedArraysEven(n1, n2, n1s, n1e, half):

    mid = (n1s + n1e) / 2
    if n1[mid] == n2[half - mid] or n1[mid] == n2[half - mid + 1]:
        return n1[mid]
    elif n1[mid] > n2[half - mid] and n1[mid] < n2[half - mid + 1]:
        return (n1[mid] + min(n2[half - mid + 1], n1[mid+1])) / 2.0
    elif n1s == n1e:
        return findMedianSortedArraysEven(n2, n1, 0, len(n2), half)
    elif n1[mid] < n2[half - mid]:
        return findMedianSortedArraysEven(n1, n2, mid, n1e, half)
    else:
        return findMedianSortedArraysEven(n1, n2, 0, mid, half)

def median_of(nums):
    n = len(nums)
    if n % 2 == 1:
        return nums[n/2]  
    else:
        return (nums[n/2 - 1] + nums[n/2]) / 2.0

class Solution:
    ''' 
        merges two sorted list, then return the number in the middle 
        This should take O(m+n), but it somehow passes leetcode's test
    '''

    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        
        ''' if nums1[i] is the median, then it must be larger than (m+n)/2 - i numbers in nums2, because it is alreay larger than i numbers in nums1

            if m+n is even, then the median is the average of (m+n-2)/2 and (m+n)/2

            if m+n is odd, then the median is the (m+n-1)/2

            find the middle number nums1[m/2], check if it is larger than nums2[ n/2 ] and less than nums2[n/2 + 1], if yes then it's the median. If not, if it's less than nums2[n/2] then the median should be larger than nums1[m/2]; if it's larger than nums2[n/2] then the median is smaller than nums1[m/2]. Then search the correspoinding half of the array.

            If can't find the median in nums1, do the same on nums2. The complexitiy should be O(log(m) + log(n))
        '''
        m = len(nums1)
        n = len(nums2)

        if m == 0:
            return median_of(nums2)
        if n == 0:
            return median_of(nums1)


        if (m + n) % 2 == 0:
            return findMedianSortedArraysEven(nums1,nums2,0,m - 1, (m+n - 2)/2)
        else:
            return findMedianSortedArraysOdd(nums1, nums2, 0, m-1, (m+n - 1)/2)


