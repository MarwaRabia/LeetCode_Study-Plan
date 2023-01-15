"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        #check if k=0 return nums as its
        if k!=0: 
            # check if k > len(nums)
            if k> n:
                    # give me reminder  
                    k=k%n
                    #and check again 
                    if k !=0:
                        nums[:k],nums[k:]=nums[-k:],nums[:-k]
            #if k < len(nums)  make swapping between two parts of array     
            elif k < n :
                nums[:k],nums[k:]=nums[-k:],nums[:-k]
              
