# https://leetcode.com/problems/custom-sort-string/

# Time Complexity : O(N) where N is length of the input string.
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : Yes


# Your code here along with comments explaining your approach

# Approach : We just first calculate frequency of all the elements. Then we start creating the second
# string using the order string.

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = {}
        for cur in s:
            freq[cur] = freq.get(cur, 0) + 1

        result = []
        for cur in order:
            if cur in freq:
                cur_str = [cur] * freq[cur]
                result.append(''.join(cur_str))
                freq[cur] = 0

        for key, val in freq.items():
            if val != 0:
                cur_str = [key] * val
                result.append(''.join(cur_str))

        return ''.join(result)

