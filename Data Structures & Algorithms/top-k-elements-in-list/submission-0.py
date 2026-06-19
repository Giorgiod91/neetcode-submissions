class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # need a counter
        # Counter will go through nums and will count how often each element is present
        count = Counter(nums)

        # building empty buckets
        buckets = [[] for _ in range(len(nums) +1)]

        # append the right number into the right bucket
        # will give me the pairs out of the counter
        # num is the number and freq is the frequency
        # for example: (1,3)
        for num , freq in count.items():
            # then I take the frequency and use it as an index and locate the num there
            buckets[freq].append(num)

        # collec them from behind
        result = []

        # backwards through the buckets
        for i in range(len(buckets) -1,0,-1):

            for num in buckets[i]:
                # appending 
                result.append(num)
                # if the length of result is equal to k return it
            if len(result) == k:
                return result

