
class Solution(object):
    def characterReplacement(self, s, k):
        freq = {}
        left = 0
        max_freq = 0
        max_length = 0

        for right in range(len(s)):

            ch = s[right]

            freq[ch] = freq.get(ch, 0) + 1

            max_freq = max(max_freq, freq[ch])

            while (right - left + 1) - max_freq > k:

                left_char = s[left]
                freq[left_char] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
