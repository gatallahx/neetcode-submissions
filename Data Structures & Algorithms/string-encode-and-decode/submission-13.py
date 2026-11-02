class Solution:
    """
    Problem restated: create an algo to deliminate strings. Can't use non-ASCII
    
    Edge case inputs:
    - []
    - [""]
    - [ "x" , ""  , "y" ]
    - [ ""  , "x" , "y" ]
    - [ "x" , "y" , ""  ]
    - [ ""  , ""  , ""  ]

    Pattern:

    Solution:
    - Encode: Merge the strings with its length + delimiter + contents, for every string
    - Decode:
        1. Get the length by reading until delimiter
        2. Append the string, from delimeter+1 to delimeter+1+length
        3. Adjust iteration index
    """

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs: res=f"{res}{len(s)}#{s}"
        return res

    def decode(self, s: str) -> List[str]:
        # s="0#2#aa0#"
        res, i, length = [], 0, 0
        while i<len(s):
            j=i
            while s[j]!="#": j+=1
            length = int( s[i:j] )
            res.append( s[ j+1 : j+1+length ] )
            i = j+1+length
        return res


