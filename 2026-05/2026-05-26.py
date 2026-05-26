# https://leetcode.com/problems/count-the-number-of-special-characters-i/?envType=daily-question&envId=2026-05-26


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # T: O(n) S:O(26)=>O(1)
        present=[0]*26
        for c in word:
            if c.islower():  # I used 'a'<=c<='z'
                present[ord(c)-ord('a')]|=1
            else:
                present[ord(c)-ord('A')]|=2
        # For lower OR with 1 for upper OR with 2, so if both present answer would be 3
        return sum(v==3 for v in present)