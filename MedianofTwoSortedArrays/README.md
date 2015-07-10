There are two sorted arrays **nums1** and **nums2** of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

***Not yet done***

#### MedianofTwoSortedArrays-1.py 
Uses Python's built in sort function to sort the concatneted array and then find the median. This is not efficient but code is really clean and easy to implement. 

#### MedianofTwoSortedArrays-2.py
Merges two sorted array into another sorted array, then return the median of the new array. This should take O(m+n)
