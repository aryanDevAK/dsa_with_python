# 11_7_good_subarrays.py
"""
Good Subarrays (Medium).
Counts contiguous subarrays whose sum equals K.
Uses Prefix Sum + HashMap (Dictionary) logic.
"""

def count_good_subarrays(arr: list, k: int) -> int:
    """
    Counts contiguous subarrays with sum equal to k.
    Time Complexity: O(N) where N is len(arr).
    Space Complexity: O(N) to store prefix sum frequencies.
    """
    prefix_sums = {0: 1} # Base case
    current_sum = 0
    count = 0
    
    for val in arr:
        current_sum += val
        if current_sum - k in prefix_sums:
            count += prefix_sums[current_sum - k]
        prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
        
    return count

if __name__ == "__main__":
    # Test cases
    assert count_good_subarrays([1, 1, 1], 2) == 2 # [1, 1] at start and end
    assert count_good_subarrays([1, 2, 3], 3) == 2 # [1, 2] and [3]
    assert count_good_subarrays([1, -1, 0], 0) == 3 # [1, -1], [0], [1, -1, 0]
    print("11_7_good_subarrays.py verified successfully!")
