# 6_8_counting_sort.py
"""
Counting Sort Implementations in Python.
Includes the simple unstable overwrite method and the optimal stable prefix-sum placement method.
"""

def counting_sort_unstable(arr: list) -> list:
    """
    Performs counting sort by counting frequencies and overwriting the array.
    This version is unstable and only works directly on integers.
    Time Complexity: O(N + K) where K is range of values (max - min + 1)
    Space Complexity: O(K) for count array
    """
    if not arr:
        return arr
        
    min_val = min(arr)
    max_val = max(arr)
    range_of_elements = max_val - min_val + 1
    
    count = [0] * range_of_elements
    for num in arr:
        count[num - min_val] += 1
        
    idx = 0
    for val_offset, freq in enumerate(count):
        actual_val = val_offset + min_val
        for _ in range(freq):
            arr[idx] = actual_val
            idx += 1
            
    return arr

def counting_sort_stable(arr: list) -> list:
    """
    Performs stable counting sort on an integer list.
    Uses prefix sum cumulative counts and right-to-left output construction.
    Time Complexity: O(N + K)
    Space Complexity: O(N + K)
    Returns: A new sorted list.
    """
    if not arr:
        return arr
        
    min_val = min(arr)
    max_val = max(arr)
    range_of_elements = max_val - min_val + 1
    
    count = [0] * range_of_elements
    output = [0] * len(arr)
    
    # 1. Store count of each element
    for num in arr:
        count[num - min_val] += 1
        
    # 2. Accumulate count array (Prefix Sums)
    for i in range(1, len(count)):
        count[i] += count[i - 1]
        
    # 3. Build output array in reverse order to maintain stability
    for i in range(len(arr) - 1, -1, -1):
        num = arr[i]
        position = count[num - min_val] - 1
        output[position] = num
        count[num - min_val] -= 1
        
    return output

if __name__ == "__main__":
    # Self-testing assertions
    test_arr = [4, 2, 2, 8, 3, 3, 1]
    assert counting_sort_stable(test_arr) == [1, 2, 2, 3, 3, 4, 8]
    
    test_arr_unstable = [4, 2, 2, 8, 3, 3, 1]
    assert counting_sort_unstable(test_arr_unstable.copy()) == [1, 2, 2, 3, 3, 4, 8]
    
    # Negative number support
    neg_arr = [-5, -2, 0, -2, 5, 2]
    assert counting_sort_stable(neg_arr) == [-5, -2, -2, 0, 2, 5]
    
    # Empty list and single element
    assert counting_sort_stable([]) == []
    assert counting_sort_stable([42]) == [42]
    
    print("6_8_counting_sort.py verified successfully!")
