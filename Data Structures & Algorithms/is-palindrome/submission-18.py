class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Edge cases:
        1. All non-alphanumeric
        2. out of bounds
        3. case-insensitive
        
        Pattern: Two-pointers

        Solution:
        Compare left and right pointer values, returning false when they don't match.
        """

        l, r = 0, len(s)-1
        while l<=r:
            if not s[l].isalnum(): 
                l+=1
                continue
            if not s[r].isalnum(): 
                r-=1
                continue

            if s[l].lower() != s[r].lower(): return False
            
            l+=1
            r-=1
        
        return True