class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Edge cases:

        Solution:
        Count integers with a hashmap
        Have a frequency array holding a list
        Insert the integer into the frequency array by integer count (key of the hashmap)
        Iterate the frequency array backwards and count the integers within the lists while k>0
        """
        from collections import defaultdict

        count=defaultdict(int)
        for integer in nums: count[integer]+=1

        f=[ [] for _ in range(len(nums)+1) ]

        for integer in count: f[ count[integer] ].append(integer)

        output=[]
        for i in range(len(f)-1,-1,-1):
            if not f[i]: continue
            for integer in f[i]:
                output.append(integer)
                k-=1
                if k<=0: return output