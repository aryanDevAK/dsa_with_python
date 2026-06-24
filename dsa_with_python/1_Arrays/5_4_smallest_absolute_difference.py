# 5_4_smallest_absolute_difference.py
"""
Smallest Absolute Difference.
Finds the minimum absolute difference between any two elements in an array.
- Brute Force: O(N^2) time.
- Sorted Array: O(N) time (checking adjacent elements).
- Unsorted Array: O(N log N) time (sorting + checking adjacent elements).
"""

def smallest_abs_diff_brute(arr: list) -> int:
    """
    Finds smallest absolute difference by checking all pairs.
    Time Complexity: O(N^2)
    Space Complexity: O(1)
    Returns: Minimum absolute difference, or float('inf') if less than 2 elements.
    """
    n = len(arr)
    if n < 2:
        return float('inf')
        
    min_diff = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            diff = abs(arr[i] - arr[j])
            if diff < min_diff:
                min_diff = diff
    return min_diff

def smallest_abs_diff_sorted(sorted_arr: list) -> int:
    """
    Finds smallest absolute difference in a pre-sorted array.
    Time Complexity: O(N)
    Space Complexity: O(1)
    Returns: Minimum absolute difference, or float('inf') if less than 2 elements.
    """
    n = len(sorted_arr)
    if n < 2:
        return float('inf')
        
    min_diff = float('inf')
    for i in range(1, n):
        diff = sorted_arr[i] - sorted_arr[i - 1]
        if diff < min_diff:
            min_diff = diff
    return min_diff

def smallest_abs_diff_unsorted(arr: list) -> int:
    """
    Finds smallest absolute difference in an unsorted array.
    Sorts the array first, then does a linear check of adjacent elements.
    Time Complexity: O(N log N)
    Space Complexity: O(1) auxiliary (if sorting in-place)
    Returns: Minimum absolute difference, or float('inf') if less than 2 elements.
    """
    n = len(arr)
    if n < 2:
        return float('inf')
        
    # Sort in-place
    arr.sort()
    return smallest_abs_diff_sorted(arr)


if __name__ == "__main__":
    # Test cases
    test_unsorted = [1, 9, 5, 23, 18, 12, 100]
    # Pairs and differences:
    # 5 - 1 = 4, 9 - 5 = 4, 12 - 9 = 3, 18 - 12 = 6, 23 - 18 = 5
    # Min is 3 (between 9 and 12)
    assert smallest_abs_diff_brute(test_unsorted.copy()) == 3
    assert smallest_abs_diff_unsorted(test_unsorted.copy()) == 3
    
    test_sorted = [1, 5, 9, 12, 18, 23, 100]
    assert smallest_abs_diff_sorted(test_sorted) == 3
    
    # Boundary checks
    assert smallest_abs_diff_unsorted([10]) == float('inf')
    assert smallest_abs_diff_unsorted([]) == float('inf')
    print("5_4_smallest_absolute_difference.py verified successfully!")
