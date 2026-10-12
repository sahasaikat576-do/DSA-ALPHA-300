class Solution(object):
    def subarraySum(self, nums, k):

        prefix_sum = 0
        count = 0
        hashmap = {0: 1}

        for i in range(len(nums)):
            prefix_sum += nums[i]

            remaining = prefix_sum - k

            if remaining in hashmap:
                count += hashmap[remaining]

            hashmap[prefix_sum] = hashmap.get(prefix_sum, 0) + 1

        return count
