# 11_4_little_chef_and_sums.py
"""
Little Chef and Sums (CodeChef CHEFSUM).
Finds the 1-based index i that minimizes prefix_sum[i] + suffix_sum[i].
Since prefix_sum[i] + suffix_sum[i] = total_sum + arr[i], this is equivalent
to finding the minimum value in the array.
"""

def find_min_checksum_index(arr: list) -> int:
    """
    Finds the 1-based index that minimizes prefix_sum[i] + suffix_sum[i].
    Time Complexity: O(N) where N is len(arr).
    Space Complexity: O(1) auxiliary space.
    Returns: The 1-based index of the minimum element.
    """
    if not arr:
        return -1
    min_val = float('inf')
    min_idx = -1
    for idx, val in enumerate(arr):
        if val < min_val:
            min_val = val
            min_idx = idx
    return min_idx + 1

if __name__ == "__main__":
    # Test cases
    assert find_min_checksum_index([2, 1, 3]) == 2 # Minimum is 1 at index 1 (1-based index 2)
    assert find_min_checksum_index([1, 1, 1]) == 1 # choosing the first smallest index
    print("11_4_little_chef_and_sums.py verified successfully!")
