class Solution(object):
    def minSubArrayLen(self, target, nums):

        left = 0
        minlength = float('inf')
        total = 0

        for right in range(len(nums)):
            total += nums[right]

            while total >= target:
                minlength = min(minlength, right - left + 1)

                total -= nums[left]
                left += 1

        if minlength == float('inf'):
            return 0

        return minlength
