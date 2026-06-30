# 11_1_creating_prefix_array.py
"""
Creates a prefix sum array from a given list.
Each element prefix_sum[i] stores the sum of all elements up to index i.
"""

def create_prefix_array(arr: list) -> list:
    """
    Constructs a prefix sum array from a given list.
    Time Complexity: O(N) where N is len(arr).
    Space Complexity: O(N) to store the prefix array.
    """
    if not arr:
        return []
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]
    for i in range(1, n):
        prefix[i] = prefix[i - 1] + arr[i]
    return prefix

if __name__ == "__main__":
    # Test cases
    assert create_prefix_array([3, 1, 4, 1, 5]) == [3, 4, 8, 9, 14]
    assert create_prefix_array([10]) == [10]
    assert create_prefix_array([]) == []
    print("11_1_creating_prefix_array.py verified successfully!")
