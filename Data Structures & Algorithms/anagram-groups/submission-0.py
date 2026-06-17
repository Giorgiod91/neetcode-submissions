class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # using defaultdict here cause in the first iteration the key wont exist
        # and would throw an error with normal list
        # the list param will create a new list for the key anytime there is 
        # new one and if with that  we can append after the list is created
        d = defaultdict(list) 
        

        for i in strs:
            # I choose tuple to be the key cause it is hashable that is needed for
            # key
            # key will be the tuple and the sorted word and value will be the element itself
            d[tuple(sorted(i))].append(i)
        
 
        # returning the values that were asked for as a list 
        return list(d.values())

        

        
