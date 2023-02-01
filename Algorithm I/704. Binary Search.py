class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # Iterative Binary Search Function
        # It returns index of x in given array arr if present,
        # else returns -1
        low=0
        high=len(nums)-1
        mid=0
        while low <= high:
            mid=(low+high)//2
            # means x is present at mid
            if target==nums[mid]:
                return mid
            # If x is greater, ignore left half
            elif target>nums[mid]:
                low=mid+1
            # If x is smaller, ignore right half
            elif target<nums[mid]:
                high=mid-1
        # If we reach here, then the element was not present
        return -1
    
    
    
        
