class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        first = 1
        last = n
        while first < last:
            mid = (first + last) // 2
            if not isBadVersion(mid):
                first = mid + 1
            else:
                last = mid
                
        return first
