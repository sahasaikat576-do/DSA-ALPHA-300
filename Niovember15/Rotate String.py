class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s) != len(goal):
            return False

        new_s = s + s

        n = len(new_s)
        m = len(goal)

        for i in range(n - m + 1):
            j = 0

            while j < m and new_s[i + j] == goal[j]:
                j += 1

            if j == m:
                return True

        return False
