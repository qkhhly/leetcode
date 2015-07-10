There are two sorted arrays **nums1** and **nums2** of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

***Not yet done***

#### MedianofTwoSortedArrays-1.py 
Uses Python's built in sort function to sort the concatneted array and then find the median. This is not efficient but code is really clean and easy to implement. 

#### MedianofTwoSortedArrays-2.py
Merges two sorted array into another sorted array, then return the median of the new array. This should take O(m+n). This algorithm can be improved by only merging to the (m+n)/2-th element. In general, if we are to find the k-th smallest element in two sorted array, this (improved) algorithm will take O(k). If k is a constant (not functions of m and/or n), then this could be faster than O(log(m+n))

#### MedianofTwoSortedArrays-3.py
Uses a divide and conqure algorithm to find the median of two sorted array. A generaliaztion of this algorithm is in ```findKth.py```.

### findKth.py
Find the k-th smallest element in two sorted array. This is used to solve this "find median" problem.
