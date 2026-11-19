
class Solution(object):
    def reorganizeString(self, s):
        n = len(s)

        # Step 1: Count frequency
        freq = {}

        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        # Step 2: Find maximum frequency
        max_freq = 0
        max_char = ""

        for ch in freq:
            if freq[ch] > max_freq:
                max_freq = freq[ch]
                max_char = ch

        # Step 3: Check possibility
        if max_freq > (n + 1) // 2:
            return ""

        # Step 4: Create result array
        result = [""] * n
        index = 0

        # Step 5: Place most frequent character
        for _ in range(max_freq):
            result[index] = max_char
            index += 2

        # Step 6: Place remaining characters
        for ch in freq:
            if ch == max_char:
                continue

            count = freq[ch]

            for _ in range(count):
                if index >= n:
                    index = 1

                result[index] = ch
                index += 2

        # Step 7: Return string
        return "".join(result)


# Example
s = "aaabbc"
obj = Solution()
print(obj.reorganizeString(s))
