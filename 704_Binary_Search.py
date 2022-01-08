class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def check(nums, left_index, right_index, target):
            if left_index <= right_index:
                middle = (left_index + right_index) // 2
                
                if nums[middle] == target:
                    return middle
                
                elif nums[middle] > target:
                    return check(nums, left_index, middle - 1, target)
                
                elif nums[middle] < target:
                    return check(nums, middle + 1, right_index, target)
            
            else:
                return -1
        
        return check(nums, 0, len(nums) - 1, target)
