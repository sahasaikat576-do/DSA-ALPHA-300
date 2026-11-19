
class Solution(object):
    def customSortString(self, order, s):
        
        # Step 1: Count frequency
        freq = {}

        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        # Step 2: Create result
        result = ""

        # Step 3: Follow custom order
        for ch in order:
            if ch in freq:
                result += ch * freq[ch]
                freq[ch] = 0

        # Step 4: Add remaining characters
        for ch in freq:
            if freq[ch] > 0:
                result += ch * freq[ch]

        return result


