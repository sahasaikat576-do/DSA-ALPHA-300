
class Solution(object):
    def vowelQueries(self, s, queries):
        vowels = "aeiou"

        prefix = [0]

        for ch in s:
            if ch in vowels:
                prefix.append(prefix[-1] + 1)
            else:
                prefix.append(prefix[-1])

        result = []

        for left, right in queries:
            count = prefix[right + 1] - prefix[left]
            result.append(count)

        return result
