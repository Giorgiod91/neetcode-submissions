class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # creating set for unique elements
        try_with_set = set()
        # loop through the list
        for i in nums:
            # if current element already in the set return true
            # that means we found a duplicate
            # else add the current element to the set
            if i in try_with_set:
                return True
            else:

                try_with_set.add(i)
                
        
        return False
        

        
        