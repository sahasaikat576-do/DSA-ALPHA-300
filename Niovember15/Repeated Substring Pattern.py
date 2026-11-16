
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)

        for i in range(1, n // 2 + 1):

            if n % i == 0:
                sub = s[:i]
                count = n // i

                if sub * count == s:
                    return True

        return False
