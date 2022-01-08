class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % len(nums)
        left = nums[n - k:]
        right = nums[:n - k]
        nums[:] = left[:] + right[:]
