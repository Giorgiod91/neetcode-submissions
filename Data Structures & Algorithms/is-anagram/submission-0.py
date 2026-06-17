class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # brute force with sorting the strings
        # then compare if thea are the same
        # if so return True else False
        # not the optimal solution I guess
        if sorted(s) == sorted(t):
            return True
        
        return False
        