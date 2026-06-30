# 10_1_max_sum_k.py
"""
Fixed-size sliding window: Maximum sum of K consecutive elements.
"""

def max_sum_of_k(arr: list, k: int) -> int:
    """
    Finds the maximum sum of any contiguous subarray of size K.
    Time Complexity: O(N).  Space Complexity: O(1).
    """
    n = len(arr)
    if n < k or k <= 0:
        return 0
    current_sum = sum(arr[:k])
    max_sum = current_sum
    for i in range(k, n):
        current_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, current_sum)
    return max_sum

if __name__ == "__main__":
    assert max_sum_of_k([2, 1, 5, 1, 3, 2], 3) == 9
    assert max_sum_of_k([2, 3, 4, 1, 5], 2) == 7
    assert max_sum_of_k([1], 1) == 1
    assert max_sum_of_k([], 3) == 0
    print("10_1_max_sum_k.py verified successfully!")
