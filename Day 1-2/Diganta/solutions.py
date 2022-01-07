class Solution:
def search(self, nums: List[int], target: int) -> int:
    pos = -1
    for i in range(len(nums)):
        if nums[i] == target:
            pos = i

    return pos


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 1,n
        while start <= end:
            mid = start + (end-start)//2
            if isBadVersion(mid): 
                end = mid - 1
            else:
                start = mid + 1
        return start

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        num_abs = [num**2 for num in nums]
        num_abs.sort()
        return num_abs
        
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = nums[k+1:]
        right = nums[:k+1]
        out = [*left, *right]
        nums=out[:]