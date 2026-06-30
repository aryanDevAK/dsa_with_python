# 5_3_smallest_largest.py
"""
Optimal Min-Max Search.
Finds both smallest and largest numbers in an array with minimal comparisons.
- Standard approach: 2N - 2 comparisons.
- Optimal approach (pairwise comparison): 1.5N - 2 comparisons.
Time Complexity: O(N)
Space Complexity: O(1)
"""

def find_min_max_standard(arr: list) -> tuple:
    """
    Finds (min_val, max_val) using standard search.
    Performs 2N - 2 comparisons in the worst case.
    Time Complexity: O(N)
    Space Complexity: O(1)
    Returns: Tuple (min_val, max_val), or (None, None) if empty.
    """
    n = len(arr)
    if n == 0:
        return (None, None)
    
    min_val = arr[0]
    max_val = arr[0]
    
    # 2 comparisons per iteration
    for i in range(1, n):
        if arr[i] < min_val:
            min_val = arr[i]
        elif arr[i] > max_val:
            max_val = arr[i]
            
    return (min_val, max_val)

def find_min_max_optimal(arr: list) -> tuple:
    """
    Finds (min_val, max_val) using optimal pairwise comparisons.
    Performs 1.5N - 2 (or 1.5N - 1.5) comparisons.
    Time Complexity: O(N)
    Space Complexity: O(1)
    Returns: Tuple (min_val, max_val), or (None, None) if empty.
    """
    n = len(arr)
    if n == 0:
        return (None, None)
    
    # If there is only one element, return it as both min and max
    if n == 1:
        return (arr[0], arr[0])
    
    # Initialize min and max based on the first two elements
    if arr[0] < arr[1]:
        min_val = arr[0]
        max_val = arr[1]
        start_idx = 2
    else:
        min_val = arr[1]
        max_val = arr[0]
        start_idx = 2
        
    # Process elements in pairs
    for i in range(start_idx, n - 1, 2):
        val1, val2 = arr[i], arr[i + 1]
        if val1 < val2:
            # val1 is smaller candidate, val2 is larger candidate
            if val1 < min_val:
                min_val = val1
            if val2 > max_val:
                max_val = val2
        else:
            # val2 is smaller candidate, val1 is larger candidate
            if val2 < min_val:
                min_val = val2
            if val1 > max_val:
                max_val = val1
                
    # If N is odd, compare the last remaining element
    if n % 2 != 0:
        last = arr[n - 1]
        if last < min_val:
            min_val = last
        elif last > max_val:
            max_val = last
            
    return (min_val, max_val)


if __name__ == "__main__":
    # Test cases
    test_even = [6, 4, 9, 2, 8, 1, 7, 5]
    assert find_min_max_standard(test_even) == (1, 9)
    assert find_min_max_optimal(test_even) == (1, 9)
    
    test_odd = [6, 4, 9, 2, 8, 1, 7]
    assert find_min_max_standard(test_odd) == (1, 9)
    assert find_min_max_optimal(test_odd) == (1, 9)
    
    # Single element and empty checks
    assert find_min_max_optimal([42]) == (42, 42)
    assert find_min_max_optimal([]) == (None, None)
    
    print("5_3_smallest_largest.py verified successfully!")
