# 6_9_radix_sort.py
"""
Radix Sort Implementation in Python.
Sorts non-negative integers digit-by-digit from Least Significant Digit (LSD)
to Most Significant Digit (MSD) using Counting Sort as a stable helper subroutine.
"""

def radix_sort(arr: list) -> list:
    """
    Performs Radix Sort on a list of non-negative integers in-place.
    Time Complexity: O(d * (N + B)) where d is max digits, B is base (10)
    Space Complexity: O(N + B)
    """
    if not arr:
        return arr
        
    max_val = max(arr)
    # Loop for every digit. exp is 10^i where i is current digit position.
    exp = 1
    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    return arr

def counting_sort_for_radix(arr: list, exp: int):
    """
    A stable counting sort subroutine used to sort numbers based on the digit at position 'exp'.
    """
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # Base 10 digits (0-9)
    
    # 1. Count occurrences of digits at current position
    for i in range(n):
        digit = (arr[i] // exp) % 10
        count[digit] += 1
        
    # 2. Accumulate count array (Prefix Sums)
    for i in range(1, 10):
        count[i] += count[i - 1]
        
    # 3. Build output array in reverse order to maintain stability
    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        position = count[digit] - 1
        output[position] = arr[i]
        count[digit] -= 1
        
    # 4. Copy sorted output back to the original array
    for i in range(n):
        arr[i] = output[i]

if __name__ == "__main__":
    # Self-testing assertions
    test_arr = [170, 45, 75, 90, 802, 24, 2, 66]
    assert radix_sort(test_arr.copy()) == [2, 24, 45, 66, 75, 90, 170, 802]
    
    # Already sorted list
    assert radix_sort([1, 2, 3]) == [1, 2, 3]
    
    # Empty list and single element
    assert radix_sort([]) == []
    assert radix_sort([42]) == [42]
    
    print("6_9_radix_sort.py verified successfully!")
