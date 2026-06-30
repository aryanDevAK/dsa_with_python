# 10_5_subarray_k_distinct.py
"""
Variable-size sliding window: Count subarrays with exactly K distinct integers.
Uses the identity: exactly(K) = atMost(K) - atMost(K-1).
(LeetCode 992 / CodeChef Hard)
"""

def _at_most_k_distinct(nums: list, k_limit: int) -> int:
    """Helper: counts subarrays with at most k_limit distinct elements."""
    if k_limit <= 0:
        return 0
    freq = {}
    left = 0
    count = 0
    for right in range(len(nums)):
        num = nums[right]
        freq[num] = freq.get(num, 0) + 1
        while len(freq) > k_limit:
            left_num = nums[left]
            freq[left_num] -= 1
            if freq[left_num] == 0:
                del freq[left_num]
            left += 1
        # All subarrays ending at 'right' with start in [left, right]
        count += right - left + 1
    return count

def subarrays_with_k_distinct(arr: list, k: int) -> int:
    """
    Counts subarrays with exactly K distinct integers.
    Time Complexity: O(N).  Space Complexity: O(K).
    """
    return _at_most_k_distinct(arr, k) - _at_most_k_distinct(arr, k - 1)

if __name__ == "__main__":
    assert subarrays_with_k_distinct([1, 2, 1, 2, 3], 2) == 7
    assert subarrays_with_k_distinct([1, 2, 1, 3, 4], 3) == 3
    assert subarrays_with_k_distinct([1, 1, 1, 1], 1) == 10
    assert subarrays_with_k_distinct([], 1) == 0
    print("10_5_subarray_k_distinct.py verified successfully!")
