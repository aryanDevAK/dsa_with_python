# 10_6_max_unique_segment.py
"""
Variable-size sliding window: Longest contiguous subarray with all unique elements.
(CodeChef MAXUNSEG 1791)
"""

def max_unique_segment(arr: list) -> int:
    """
    Finds the length of the longest subarray where all elements are unique.
    Time Complexity: O(N) amortized.  Space Complexity: O(N).
    """
    seen = set()
    left = 0
    max_len = 0
    for right in range(len(arr)):
        while arr[right] in seen:
            seen.remove(arr[left])
            left += 1
        seen.add(arr[right])
        max_len = max(max_len, right - left + 1)
    return max_len

if __name__ == "__main__":
    assert max_unique_segment([1, 2, 3, 1, 2, 3]) == 3
    assert max_unique_segment([1, 2, 3, 4, 5]) == 5
    assert max_unique_segment([5, 5, 5, 5]) == 1
    assert max_unique_segment([1]) == 1
    assert max_unique_segment([]) == 0
    print("10_6_max_unique_segment.py verified successfully!")
