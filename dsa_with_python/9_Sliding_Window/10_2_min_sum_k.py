# 10_2_min_sum_k.py
"""
Fixed-size sliding window: Minimum sum of K consecutive elements.
"""

def min_sum_of_k(arr: list, k: int) -> int:
    """
    Finds the minimum sum of any contiguous subarray of size K.
    Time Complexity: O(N).  Space Complexity: O(1).
    """
    n = len(arr)
    if n < k or k <= 0:
        return 0
    current_sum = sum(arr[:k])
    min_sum = current_sum
    for i in range(k, n):
        current_sum += arr[i] - arr[i - k]
        min_sum = min(min_sum, current_sum)
    return min_sum

if __name__ == "__main__":
    assert min_sum_of_k([2, 1, 5, 1, 3, 2], 3) == 6
    assert min_sum_of_k([10, 4, 2, 5, 6], 2) == 6
    assert min_sum_of_k([3], 1) == 3
    assert min_sum_of_k([], 2) == 0
    print("10_2_min_sum_k.py verified successfully!")
