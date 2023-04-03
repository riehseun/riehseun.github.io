class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        input_string = s

        # Move the end pointer until seeing repeating chars.
        # Move the start pointer until substring has no repeating chars.
        # Keep the max diff between end and start pointer.
        # Scan finished when both start and end pointers reach the end of string.

        start = 0
        max_length = 0
        # Store chracter and its index.
        char_map = {}

        for i,c in enumerate(input_string):

            # If duplicate is found, compute the length using start and the i pointer.
            # The second condition ensures that we are only looking at the substring
            # after the start index.
            if c in char_map and char_map[c] >= start:
                max_length = max(max_length, i-start)
                # Move the start pointer to plus 1 of the index where the duplicate is.
                start = char_map[c] + 1
            char_map[c] = i

        max_length = max(max_length, len(input_string)-start)

        return max_length


    def lengthOfLongestSubstring_v2(self, s):
        """
        :type s: str
        :rtype: int
        """

        input_string = s

        # Move the end pointer until seeing repeating chars.
        # Move the start pointer until substring has no repeating chars.
        # Keep the max diff between end and start pointer.
        # Scan finished when both start and end pointers reach the end of string.

        start = 0
        max_length = 0
        # Store chracter and its index.
        char_map = {}

        for i,c in enumerate(input_string):

            # If a char with two occurance is found, compute the length using start and the i pointer.
            # The third and forth condition ensures that we are only looking at the substring
            # after the start index.
            if c in char_map \
                and len(char_map[c]) == 2 \
                and char_map[c][0] >= start \
                and char_map[c][1] >= start:

                max_length = max(max_length, i-start)
                # Move the start pointer to plus 1 of the index where the duplicate is.
                start = char_map[c][1] + 1

            # Store the indices of first and second occurance.
            if c not in char_map:
                char_map[c] = [i]
            else:
                if len(char_map[c]) == 1:
                    char_map[c].append(i)
                elif len(char_map[c]) == 2:
                    char_map[c][0] = char_map[c][1]
                    char_map[c][1] = i

        max_length = max(max_length, len(input_string)-start)

        return max_length

    print(lengthOfLongestSubstring_v2("", "abcabcbb")) # 6
    print(lengthOfLongestSubstring_v2("", "xyzxyyzzxy")) # 5


