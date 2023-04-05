class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # In count_s, we will store the count of only the characters
        # that exist in t.
        count_s = {}
        count_t = {}

        min_length = len(s) + 1
        min_substring = ""

        for c in t:
            if c not in count_t:
                count_t[c] = 0
            count_t[c] += 1

        start = 0
        end = 0

        while start <= end and end <= len(s):

            is_valid_substring = True
            for k,v in count_t.items():
                if k not in count_s \
                    or (k in count_s and count_s[k] < count_t[k]):
                    is_valid_substring = False

            if is_valid_substring:

                if end - start < min_length:
                    min_length = end - start
                    min_substring = s[start:end]

                # Whenever "start" pointer moves forward, must remove
                # the previous chracter from count_s set.
                # This block must come before incrementing the start pointer!
                if s[start] in count_t:
                    if count_s[s[start]] > 1:
                        count_s[s[start]] -= 1
                    else:
                        del count_s[s[start]]

                start += 1

            else:
                # If covered the last character in s,
                # increment the start pointer until it reaches the end.
                if end == len(s):
                    start += 1
                else:
                    # Update count_s dictionary each time "end" pointer moves.
                    # This block must come before incrementing the end pointer!
                    if s[end] in count_t:
                        if s[end] not in count_s:
                            count_s[s[end]] = 0
                        count_s[s[end]] += 1

                    end += 1

        return min_substring