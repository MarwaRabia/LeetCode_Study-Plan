"""
Problem 
You are a product manager and currently leading a team to develop a new product. 
Unfortunately, the latest version of your product fails the quality check.
 Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad.
 Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low=1  #initialize lower bound of range
        high=n #initialize upper bound of range
        while low <= high:
            mid=(low+high)//2 #calculate middle point of range
            if isBadVersion(mid): #check if middle point is bad version
                if not isBadVersion(mid-1): #check if previous version is not bad
                    return mid #if yes return the middle point
                high=mid-1 # if not move to check lower half
            else:
                low=mid+1 # move to check upper half
        return -1  #if no bad version found return -1