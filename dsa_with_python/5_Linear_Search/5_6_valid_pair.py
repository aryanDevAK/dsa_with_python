# 5_6_valid_pair.py
"""
Valid Difference Pair.
Given an array and a target difference D, finds a pair (arr[i], arr[j])
such that |arr[i] - arr[j]| = D.
- Hashing Approach (Unsorted Array): O(N) time, O(N) space.
- Two-Pointer Approach (Sorted Array): O(N) time, O(1) space.
"""

def find_valid_pair_unordered(arr: list, target_diff: int) -> tuple:
    """
    Finds a pair with absolute difference equal to target_diff using a hash set.
    Works on unsorted arrays.
    Time Complexity: O(N)
    Space Complexity: O(N)
    Returns: Tuple (x, y) such that |x - y| = target_diff, or None if no such pair exists.
    """
    if target_diff < 0:
        target_diff = abs(target_diff)
        
    seen = set()
    for num in arr:
        # Check if we have seen the complement numbers that satisfy the difference
        # num - x = target_diff -> x = num - target_diff
        # x - num = target_diff -> x = num + target_diff
        if (num - target_diff) in seen:
            return (num - target_diff, num)
        if (num + target_diff) in seen:
            return (num + target_diff, num)
        seen.add(num)
        
    return None

def find_valid_pair_sorted(sorted_arr: list, target_diff: int) -> tuple:
    """
    Finds a pair with absolute difference equal to target_diff using two pointers.
    Requires a sorted array.
    Time Complexity: O(N)
    Space Complexity: O(1)
    Returns: Tuple (x, y) such that y - x = target_diff, or None if no such pair exists.
    """
    if target_diff < 0:
        target_diff = abs(target_diff)
        
    n = len(sorted_arr)
    if n < 2:
        return None
        
    left = 0
    right = 1
    
    while left < n and right < n:
        if left == right:
            right += 1
            continue
            
        diff = sorted_arr[right] - sorted_arr[left]
        
        if diff == target_diff:
            return (sorted_arr[left], sorted_arr[right])
        elif diff < target_diff:
            # Increase the difference by moving the right pointer
            right += 1
        else:
            # Decrease the difference by moving the left pointer
            left += 1
            
    return None


if __name__ == "__main__":
    # Test cases for unsorted array
    test_unsorted = [5, 20, 3, 2, 50, 80]
    # Target diff 78: 80 - 2 = 78
    assert find_valid_pair_unordered(test_unsorted, 78) == (2, 80)
    # Target diff 17: 20 - 3 = 17
    assert find_valid_pair_unordered(test_unsorted, 17) in [(3, 20), (20, 3)]
    assert find_valid_pair_unordered(test_unsorted, 99) is None
    
    # Test cases for sorted array
    test_sorted = [2, 3, 5, 20, 50, 80]
    assert find_valid_pair_sorted(test_sorted, 78) == (2, 80)
    assert find_valid_pair_sorted(test_sorted, 17) == (3, 20)
    assert find_valid_pair_sorted(test_sorted, 99) is None
    
    # Check boundary: target_diff = 0 (finding duplicates)
    test_dups = [1, 3, 5, 5, 8]
    assert find_valid_pair_sorted(test_dups, 0) == (5, 5)
    
    print("5_6_valid_pair.py verified successfully!")
