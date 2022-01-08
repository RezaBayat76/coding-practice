class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """    
        n = len(nums)
        left = 0
        right = n - 1
        index = n - 1
        sorted_list = range(n)
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                sorted_list[index] = nums[left] * nums[left]
                index -= 1
                left += 1
            else:
                sorted_list[index] = nums[right] * nums[right]
                index -= 1
                right -= 1
        return sorted_list
