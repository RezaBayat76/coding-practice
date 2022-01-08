class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left <= right:
            tmp = s[right]
            s[right] = s[left]
            s[left]= tmp
            left += 1
            right -= 1
