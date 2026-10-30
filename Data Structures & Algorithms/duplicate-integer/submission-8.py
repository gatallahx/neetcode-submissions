class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Problem restated: Given integers, return true if duplicates present
        
        General case: [1,2,3,4]
        
        Edge case: [2,2,2,2], []

        Creating a hashset provides a way of duplicate checking for O(n)
        """

        return len(nums) != len(set(nums))