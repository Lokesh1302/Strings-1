# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Time Complexity : O(N) where N is length of the input string.
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : Yes.


# Your code here along with comments explaining your approach

# Approach : Two approaches here.
# One approach is having index of the element, and if the same element occurs again, we move our start
# to new position, which either freq[cur] + 1 or start, whichever is maximum.
# We have update our max string length everytime.

# Second approach is by counting the frequency of all the elements, whenever we find the same element
# twice, we move our start and decrement all the frequencies, until the window becomes valid again.
# Time Complexity of this approach is O(2N) as we have to move start and end pointers.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end, size = 0, 0, len(s)
        max_substring = 0
        freq = {}

        for end in range(size):
            cur = s[end]
            if cur in freq:
                start = max(start, freq[cur] + 1)

            freq[cur] = end  # Index at which cur element is present
            max_substring = max(max_substring, end - start + 1)

        return max_substring

    def lengthOfLongestSubstring_frequency_approach(self, s: str) -> int:
        start, end, size = 0, 0, len(s)
        max_substring = 0
        freq = {}

        for end in range(size):
            cur = s[end]
            freq[cur] = freq.get(cur, 0) + 1

            #  Make window valid by moving start
            while freq[cur] > 1 and start <= end:
                prev = s[start]
                freq[prev] -= 1
                start += 1

            max_substring = max(max_substring, end - start + 1)


