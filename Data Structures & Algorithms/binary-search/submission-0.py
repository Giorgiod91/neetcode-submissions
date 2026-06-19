class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # first defing left and right
        left = 0
        right = len(nums) -1
        # while loop that goes until left is below or equal to right
        while left <= right:
            # defining the mid
            mid = (left + right ) // 2
            # if the mid equsls the target I just return the target
            if nums[mid] == target:
                return mid
            # elif because if the target is in the right side of the list that means
            # bigger then nums[mid] then we have to redefine left to mid +1
            # because then we know the target cant be on the current left side so we cut it off
            # and define the left new to be the old mit +1 so we concentrate on the right side of the list
            elif target>nums[mid]:
                left = mid +1
            #  same goes for the left side if we know the target hast to be on the left side of the list
            # we just say that the right is the mid -1
            else:
                right = mid -1

        return -1
        