
class Solution(object):
    def frequencySort(self, nums):
        freq = {}

        # Step 1: Count frequency
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Step 2: Selection sort
        n = len(nums)

        for i in range(n):
            min_idx = i

            for j in range(i + 1, n):
                # Smaller frequency comes first
                if freq[nums[j]] < freq[nums[min_idx]]:
                    min_idx = j

                # If frequencies are equal,
                # larger number comes first
                elif (freq[nums[j]] == freq[nums[min_idx]]
                      and nums[j] > nums[min_idx]):
                    min_idx = j

            # Swap elements
            nums[i], nums[min_idx] = nums[min_idx], nums[i]

        return nums
