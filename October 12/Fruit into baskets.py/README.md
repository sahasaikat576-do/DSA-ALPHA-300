Use a sliding window with a HashMap to track the frequency of each fruit type. Expand the window using right; when more than two fruit types exist, move left until only two remain. Update the maximum window length at each valid step.

Time Complexity: O(n)

Space Complexity: O(1), since the window contains at most two fruit types after adjustment.
