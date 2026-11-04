class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Edge cases:
        1. All non-alphanumeric
        2. uneven amount of alphanumeric
        3. out of bounds
        4. case-insensitive
        
        Pattern: Two-pointers

        Solution:
        Compare left and right pointers, returning false when they don't match.
        While they haven't crossed!
        Pointers should move up when pointing to non-alphanumeric, BEFORE comparison
        """

        l, r = 0, len(s)-1
        while l<=r:
            while l<len(s) and not s[l].isalnum(): l+=1
            while r>0 and not s[r].isalnum(): r-=1
            if l>r: continue # break out of the loop

            # if l == r: return False # E2

            if s[l].lower() != s[r].lower(): return False
            
            l+=1
            r-=1
        
        return True