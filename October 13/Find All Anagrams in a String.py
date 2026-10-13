
class Solution(object):
    def findAnagrams(self, s, p):
        ans = []

        if len(p) > len(s):
            return ans

        freq1 = [0] * 26
        freq2 = [0] * 26

        for i in range(len(p)):
            freq1[ord(p[i]) - ord('a')] += 1

        left = 0

        for right in range(len(s)):
            freq2[ord(s[right]) - ord('a')] += 1

            while right - left + 1 > len(p):
                freq2[ord(s[left]) - ord('a')] -= 1
                left += 1

            if right - left + 1 == len(p):
                same = True

                for i in range(26):
                    if freq1[i] != freq2[i]:
                        same = False
                        break

                if same:
                    ans.append(left)

        return ans

