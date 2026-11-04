class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Edge cases:

        Pattern:

        Solution:
        if integer-1 doesn't exist, we're at the min of the consecutive sequence
        if integer+1 doesn't exist, we're at the max of the consecutive sequence
        
        Transform the list to a hashset
        for each iteration of the list, check if the integer is a min, using the hashset
        if yes, using the hashset, count the sequence until you hit the max, keep the max count
        if no, continue to the next iteration

        with this algorithm, you prevent re-counting, because counting is only done at a min
        """
        s, max_count = set(nums), 0
        for integer in nums:
            if integer-1 in s: continue
            count, curr_int = 1, integer
            while curr_int+1 in s:
                count+=1
                curr_int+=1
            max_count = max(max_count,count)
        return max_count