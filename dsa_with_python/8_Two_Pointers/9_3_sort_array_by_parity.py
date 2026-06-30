# 9_3_sort_array_by_parity.py
"""
Sort Array by Parity.
Rearranges an array in-place such that all even integers precede all odd integers.
"""

def sort_array_by_parity(arr: list) -> list:
    """
    Sorts array by parity in-place.
    Time Complexity: O(N) where N is len(arr).
    Space Complexity: O(1) auxiliary space.
    Returns: The rearranged list.
    """
    left = 0
    right = len(arr) - 1
    
    while left < right:
        # If left is odd and right is even, swap them
        if arr[left] % 2 > arr[right] % 2:
            arr[left], arr[right] = arr[right], arr[left]
            
        if arr[left] % 2 == 0:
            left += 1
        if arr[right] % 2 != 0:
            right -= 1
            
    return arr

if __name__ == "__main__":
    # Self-testing assertions
    test_1 = [3, 1, 2, 4]
    res_1 = sort_array_by_parity(test_1.copy())
    # Potential results: [4, 2, 1, 3] or similar even-before-odd configuration
    assert all(x % 2 == 0 for x in res_1[:2])
    assert all(x % 2 != 0 for x in res_1[2:])
    
    test_2 = [0]
    assert sort_array_by_parity(test_2.copy()) == [0]
    
    # Already grouped test
    test_3 = [2, 4, 6, 1, 3]
    assert sort_array_by_parity(test_3.copy()) == [2, 4, 6, 1, 3]
    
    print("9_3_sort_array_by_parity.py verified successfully!")
