# 6_6_merge_sort.py
"""
Merge Sort Implementation in Python.
Uses the Divide and Conquer design paradigm to recursively split and merge lists.
"""

def merge_sort(arr: list) -> list:
    """
    Performs merge sort on a list.
    Time Complexity: O(N log N) (best, average, worst)
    Space Complexity: O(N)
    Returns: A new sorted list.
    """
    if len(arr) <= 1:
        return arr
        
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    return merge_sorted_arrays(left_half, right_half)

def merge_sorted_arrays(left: list, right: list) -> list:
    """
    Helper function to merge two sorted lists in O(N) time.
    Preserves stability.
    """
    merged = []
    i = j = 0
    
    # Merge sorted lists in order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # '<=' maintains stability
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            
    # Append remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

if __name__ == "__main__":
    # Self-testing assertions
    test_list = [38, 27, 43, 3, 9, 82, 10]
    assert merge_sort(test_list) == [3, 9, 10, 27, 38, 43, 82]
    
    # Check that original list is unchanged (since merge sort returns new list)
    assert test_list == [38, 27, 43, 3, 9, 82, 10]
    
    # Already sorted list
    assert merge_sort([1, 2, 3]) == [1, 2, 3]
    
    # Empty list and single element list
    assert merge_sort([]) == []
    assert merge_sort([42]) == [42]
    
    print("6_6_merge_sort.py verified successfully!")
