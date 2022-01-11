class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n_2 = [n*n for n in nums]
        return sorted(n_2)
