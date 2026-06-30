# 5_1_linear_search.py
"""
Linear Search Implementations in Python.
Includes standard linear search for lists, strings, sentinel search optimization, and 2D matrix searches.
"""

def linear_search_array(arr: list, target) -> int:
    """
    Performs standard linear search on a list.
    Time Complexity: O(N)
    Space Complexity: O(1)
    Returns: Index of target if found, else -1.
    """
    for idx in range(len(arr)):
        if arr[idx] == target:
            return idx
    return -1

def linear_search_string(s: str, target: str) -> int:
    """
    Performs standard linear search on a string for a character.
    Time Complexity: O(N)
    Space Complexity: O(1)
    Returns: Index of target character if found, else -1.
    """
    for idx in range(len(s)):
        if s[idx] == target:
            return idx
    return -1

def sentinel_linear_search(arr: list, target) -> int:
    """
    Sentinel Linear Search.
    Eliminates the loop boundary check `idx < len(arr)` at each step,
    reducing constant factor overhead.
    Time Complexity: O(N)
    Space Complexity: O(1)
    Returns: Index of target if found, else -1.
    """
    n = len(arr)
    if n == 0:
        return -1
    
    # Save the last element and replace it with target as the sentinel
    last = arr[n - 1]
    arr[n - 1] = target
    
    idx = 0
    # Boundary check is omitted: loop is guaranteed to terminate
    while arr[idx] != target:
        idx += 1
        
    # Restore the original last element
    arr[n - 1] = last
    
    # Check if the match is actual or just the sentinel
    if idx < n - 1 or arr[n - 1] == target:
        return idx
    return -1

def linear_search_2d(matrix: list, target) -> tuple:
    """
    Performs linear search on a 2D matrix.
    Time Complexity: O(R * C) where R is rows and C is columns.
    Space Complexity: O(1)
    Returns: Tuple (row, col) if found, else (-1, -1).
    """
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == target:
                return (r, c)
    return (-1, -1)


if __name__ == "__main__":
    # Self-testing checks
    test_arr = [4, 2, 7, 1, 9, 3]
    assert linear_search_array(test_arr, 7) == 2
    assert linear_search_array(test_arr, 5) == -1
    
    test_str = "hello dsa"
    assert linear_search_string(test_str, 'o') == 4
    assert linear_search_string(test_str, 'z') == -1
    
    test_sentinel = [4, 2, 7, 1, 9, 3]
    assert sentinel_linear_search(test_sentinel, 7) == 2
    assert sentinel_linear_search(test_sentinel, 3) == 5
    assert sentinel_linear_search(test_sentinel, 5) == -1
    # Check that sentinel modified nothing persistently
    assert test_sentinel == [4, 2, 7, 1, 9, 3]
    
    test_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert linear_search_2d(test_matrix, 6) == (1, 2)
    assert linear_search_2d(test_matrix, 10) == (-1, -1)
    print("5_1_linear_search.py verified successfully!")
