class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Problem restated: anagram check, then add to a collection.

        General case:

        Edge case: empty string, duplicates

        Pattern: hashmap

        Solution:
        Have a hashmap holding lists
        Use a string's sorted state as a key to a hashmap.
        This filters and groups for anagrams.
        The string is appended to the anagram list.

        Trick:
        sorted here returns an array of chars, so you join them with a string func
        dictionary.values() excludes the keys
        """

        from collections import defaultdict
        grams = defaultdict(list)

        for s in strs: grams[ "".join( sorted(s) ) ].append(s)

        return list( grams.values() )