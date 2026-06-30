# 11_5_suffix_arrays.py
"""
Suffix Arrays (CodeChef 1200 / Prefix and Suffix Sum Track).
Constructs a suffix sum array and answers suffix queries.
"""

def create_suffix_array(arr: list) -> list:
    """
    Constructs a suffix sum array from a given list.
    Time Complexity: O(N) where N is len(arr).
    Space Complexity: O(N) to store the suffix array.
    """
    if not arr:
        return []
    n = len(arr)
    suffix = [0] * n
    suffix[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] + arr[i]
    return suffix

if __name__ == "__main__":
    # Test cases
    assert create_suffix_array([3, 1, 4, 1, 5]) == [14, 11, 10, 6, 5]
    assert create_suffix_array([10]) == [10]
    assert create_suffix_array([]) == []
    print("11_5_suffix_arrays.py verified successfully!")
