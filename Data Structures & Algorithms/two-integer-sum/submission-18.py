class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Problem restated:

        General case:

        Edge case:

        Pattern: hashmap

        Brute force:
        
        Optimized:
        1. create a map storing {complement -> current index}
        2. check if the current value exists as a saved complement
        Yes -> return the current and complement index, as a sorted array
        No ->  calculate and save a complement, and map it to the current index
        """
        comp = dict()

        for i,v in enumerate(nums):
            if (v) in comp:
                # Grouped as a tuple to allocate less memory
                return sorted( (
                    i,
                    comp[v]
                ) )
            else: comp[target-v]=i