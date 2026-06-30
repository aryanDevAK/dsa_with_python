# 10_3_longest_substring_no_repeat.py
"""
Variable-size sliding window: Longest substring without repeating characters.
(CodeChef 932 / LeetCode 3)
"""

def longest_substring_no_repeat(s: str) -> int:
    """
    Finds the length of the longest substring with all unique characters.
    Time Complexity: O(N) amortized.  Space Complexity: O(min(N, |alphabet|)).
    """
    char_set = set()
    left = 0
    max_length = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length

if __name__ == "__main__":
    assert longest_substring_no_repeat("abcabcbb") == 3
    assert longest_substring_no_repeat("bbbbb") == 1
    assert longest_substring_no_repeat("pwwkew") == 3
    assert longest_substring_no_repeat("") == 0
    assert longest_substring_no_repeat("abcdef") == 6
    print("10_3_longest_substring_no_repeat.py verified successfully!")
