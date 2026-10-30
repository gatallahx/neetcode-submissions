class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Problem restated: Return false if two strings have different char counts
        
        General case:
        
        Edge case: s and t are different sizes
        
        Pattern: frequency array OR hashmap

        Brute force:

        Optimized: 
        1.  Create a letter frequency array O(26)
        2.  Increment the array with s O(n)
        3.  Decrement the array with t O(n)
        3.1 If the frequency falls below zero, return false
        4.  Return false if any letter frequence is not zero (edge case) O(26)
        5.  Return true (it's an anagram)
        """

        f=[0]*26

        for c in s: f[ ord(c)-97 ]+=1

        for c in t:
            f[ ord(c)-97 ]-=1
            if f[ ord(c)-97 ] < 0: return False 

        for count in f: 
            if count!=0: return False

        return True

