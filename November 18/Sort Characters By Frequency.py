
class Solution(object):
    def frequencySort(self, s):
        freq = {}

        # Step 1: Count frequency
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        # Step 2: Extract characters
        chars = list(freq.keys())

        # Step 3: Merge Sort
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2

            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            return merge(left, right)

        def merge(left, right):
            result = []
            i = 0
            j = 0

            while i < len(left) and j < len(right):

                if freq[left[i]] >= freq[right[j]]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            result.extend(left[i:])
            result.extend(right[j:])

            return result

        chars = merge_sort(chars)

        # Step 4: Build result
        result = ""

        for ch in chars:
            result += ch * freq[ch]

        return result


