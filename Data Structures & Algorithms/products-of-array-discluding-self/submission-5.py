class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Edge cases: calculating the first and last output

        Pattern: prefix and suffix pre-calculated products

        Solution:
        in : [1, 2, 4, 6]

        Build the prefix product table O(n)
            built from left to right
            [1, 2, 8, 48]   <- [1, 1*2, 2*4, 2*4*6]
        Build the suffix product table O(n)
            built from right to left
            [48, 48, 24, 6] <- [6*4*2*1, 6*4*2, 6*4, 6]
        Calculate the output table O(n)
            [
                post[1],
                ...
                pre[i-1] * post[i+1]
                ...
                pre[-2]
            ]

        out: [48,24,12,8]
        Trick: make pre/post-fix arrays s.t. pre[i-1] * post[i+1] instead of pre[i] * post[i] 
        """
        n=len(nums)

        pre=[0]*n
        pre[0]=nums[0]
        for i in range(1,n): pre[i] = pre[i-1] * nums[i]

        post=[0]*n
        post[-1]=nums[-1]
        for i in range(n-2,-1,-1): post[i] = post[i+1] * nums[i]

        out=[0]*n
        out[0], out[-1] = post[1], pre[-2]
        for i in range(1, n-1): out[i] = pre[i-1] * post[i+1]
        return out










