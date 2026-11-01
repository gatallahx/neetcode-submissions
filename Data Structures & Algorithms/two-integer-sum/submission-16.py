class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Problem restated:

        General case:

        Edge case:

        Pattern: hashmap

        Brute force:
        
        Use a map to track the sum complement. { curr_val , comp_i }
        Optimized:
        1. see if key target - nums[i] exists in the map
        YES? return the current index and the one at key= target - nums[i]
        NO?  add to the map { target - nums[i] , i }
        """

        from collections import defaultdict

        comp = dict()

        for i,v in enumerate(nums):
            if (v) in comp:
                return sorted( ( 
                    i,
                    comp[v]
                ) )
            else: comp[target-v]=i