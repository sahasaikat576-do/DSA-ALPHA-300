# Folder Contents & Summary

| Type | File | Approach | Time | Space |
|---|---|---|---|---|
| Primary | [Fruit into basket.py](./Fruit%20into%20basket.py) | Sliding window + HashMap; maintain at most two fruit types and maximize the window length. | O(n) | O(1) |
| Primary | [Minimum_Size_Subarray_Sum.py](./Minimum_Size_Subarray_Sum.py) | Sliding window; expand until the sum reaches the target, then shrink from the left. | O(n) | O(1) |
| Primary | [Subarray Sum Equals K.py](./Subarray%20Sum%20Equals%20K.py) | Prefix sum + HashMap; count previous prefix sums equal to the current sum minus k. | O(n) | O(n) |

## Edge Cases

- **Fruit Into Baskets:** Remove a fruit type when its frequency becomes zero.
- **Minimum Size Subarray Sum:** Return 0 if no subarray reaches the target.
- **Subarray Sum Equals K:** Initialize the HashMap with `{0: 1}` to count subarrays starting at index 0.
