class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Edge case:

        Pattern:

        Solution:
        count integer occurance with a hashmap
        create a frequency table where index==occurence and value==integer
        frequency table has lists in case there's many integers with same occurence count
        look the table backwards and collect integers until you have k in the result array
        """
        from collections import defaultdict
        count = defaultdict(int)
        for n in nums: count[n]+=1

        f=[ [] for _ in range(len(nums)+1) ]
        for integer in count: f[ count[integer] ].append(integer)

        res=[]
        i=len(f)-1
        while i>0:
            if not f[i]: # skips empty cell
                i-=1
                continue
            for integer in f[i]:
                k-=1
                res.append(integer)
                if k<=0: return res
            i-=1