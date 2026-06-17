class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # using two loops one normal one the other one starts at  i+1
        # then checking if those two add together at some point and if so
        # returning the pair of indices
        for i in range(len(nums)):
            # inner looop starts one ahead
            for j in range(i+1, len(nums)):
                # if those two add together equals the target
                if nums[i] + nums[j] == target:
                    # return indices
                    return [i,j]
        