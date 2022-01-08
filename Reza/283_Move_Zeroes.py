class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        current_zero_index = -1
        current_index = 0
        while current_index != len(nums):
            if current_zero_index == -1 and nums[current_index] == 0:
                current_zero_index = current_index
            elif nums[current_index] != 0 and current_zero_index != -1:
                nums[current_zero_index] = nums[current_index]
                nums[current_index] = 0
                current_zero_index +=1
            current_index += 1
