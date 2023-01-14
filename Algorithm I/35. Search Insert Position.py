"""
Problem 
Given a sorted array of distinct integers and a target value,
 return the index if the target is found.
  If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

"""

class Solution(object):
    def searchInsert(self, array, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
       # check if target is not present in array
        if target not in array:
                array.append(target)
        # sort the array
        array=sorted(array)
        low = 0
        high = len(array)-1     
        while(low <= high):
                mid=low+(high-low)//2
        
                # check if mid element is equal to target
                if array[mid]==target:
                    return mid
                # if mid element is greater than target
                # then we move to left of mid
                elif array[mid] > target:
                    high = mid -1
                else :
                    # if mid element is less than target
                    # then we move to right of mid
                    low = mid +1
        # if target not found
        return -1