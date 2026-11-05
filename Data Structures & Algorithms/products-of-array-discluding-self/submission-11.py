class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Edge cases:

        Solution:
        [ 2       , 3     , 5   , 7     ] -> [105, 70, 42, 30]

        [ 1       , 1*2   , 2*3 , 2*3*5 ] prefix of nums[i]
        [ 3*5*7*1 , 5*7*1 , 7*1 , 1     ] postfix of nums[i]

        setup these tables then multiply them to get the output in O(n)
        """        
        n=len(nums)
        pre=[1]*n
        for i in range(1,n): pre[i] = pre[i-1] * nums[i-1]

        post=[1]*n
        for i in range(n-2,-1,-1): post[i] = post[i+1] * nums[i+1]

        #  newlist = [expression for item in iterable if condition == True] 
        return [ pre[i]*post[i] for i in range(n) ]