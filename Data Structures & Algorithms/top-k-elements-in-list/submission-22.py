class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Problem restated: return k of the most frequent integers

        Edge case: all of nums is the same integer

        Pattern: hashmap

        Solution 1:
            count with a hashmap O(n)
            sort the hashmap O(nlogn)
            pick the top k

        Solution 3:
            count with a hashmap O(n)
            insert all into a max-heap, then heapify O(n)
            pop-append to a list, k times O(klogn)

        Solution 4: O(n)
        count with a hashmap
        place each value in a frequency array (size = nums length)
        frequency array holds lists, in case of integers with the same count
        extract k elements, starting from the back of the list
        account for empty cells and multi-value cells
        
        trick: 
        while k>0 keep extracting
        [[] for _ in range(n)] to an array of empty lists

        at worst, every integer occurs once, O(n) to find them + O(n) to extract, NOT O(n^2)
        """
        from collections import defaultdict
        count = defaultdict(int)
        for n in nums: count[n]+=1

        # nums = [2, 2]
        #           0  1  2
        # f_arr = [ 0, 0, 2] len(nums)+1
        f_arr= [ [] for _ in range( len(nums)+1 ) ]
        for integer in count: f_arr[ count[integer] ].append(integer)

        res=[]
        i = len(f_arr)-1 # back of the list
        while k>0:
            if not f_arr[i]:
                i-=1
                continue # skip empty cell
            for num in f_arr[i]:
                if k>0:
                    res.append(num)
                    k-=1
                else: return res
            i-=1
        return res

