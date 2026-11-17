
class Solution(object):
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []

        p_freq = {}
        freq = {}

        for ch in p:
            p_freq[ch] = p_freq.get(ch, 0) + 1

        left = 0
        result = []

        for right in range(len(s)):

            ch = s[right]
            freq[ch] = freq.get(ch, 0) + 1

            if right - left + 1 > len(p):

                left_char = s[left]
                freq[left_char] -= 1

                if freq[left_char] == 0:
                    del freq[left_char]

                left += 1

            if freq == p_freq:
                result.append(left)

        return result
