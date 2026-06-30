# 6_7_quick_sort.py
"""
Quick Sort Implementations in Python.
Includes the standard Lomuto partition scheme and the Hoare partition scheme.
"""

def quick_sort_lomuto(arr: list, low: int, high: int):
    """
    Performs quick sort in-place using Lomuto partitioning.
    Time Complexity: Best/Average O(N log N), Worst O(N^2)
    Space Complexity: O(log N) stack frames
    """
    if low < high:
        p_idx = partition_lomuto(arr, low, high)
        quick_sort_lomuto(arr, low, p_idx - 1)
        quick_sort_lomuto(arr, p_idx + 1, high)

def partition_lomuto(arr: list, low: int, high: int) -> int:
    """
    Lomuto partition scheme.
    Uses the last element as the pivot.
    """
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    # Swap pivot element with element at i+1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort_hoare(arr: list, low: int, high: int):
    """
    Performs quick sort in-place using Hoare partitioning.
    Time Complexity: Best/Average O(N log N), Worst O(N^2)
    Space Complexity: O(log N) stack frames
    """
    if low < high:
        p_idx = partition_hoare(arr, low, high)
        quick_sort_hoare(arr, low, p_idx)
        quick_sort_hoare(arr, p_idx + 1, high)

def partition_hoare(arr: list, low: int, high: int) -> int:
    """
    Hoare partition scheme.
    Uses the first element as the pivot.
    """
    pivot = arr[low]
    i = low - 1
    j = high + 1
    
    while True:
        # Move right pointer left until finding element <= pivot
        j -= 1
        while arr[j] > pivot:
            j -= 1
            
        # Move left pointer right until finding element >= pivot
        i += 1
        while arr[i] < pivot:
            i += 1
            
        if i >= j:
            return j
            
        arr[i], arr[j] = arr[j], arr[i]

if __name__ == "__main__":
    # Self-testing assertions for Lomuto Quick Sort
    test_lomuto = [10, 7, 8, 9, 1, 5]
    quick_sort_lomuto(test_lomuto, 0, len(test_lomuto) - 1)
    assert test_lomuto == [1, 5, 7, 8, 9, 10]
    
    # Self-testing assertions for Hoare Quick Sort
    test_hoare = [10, 7, 8, 9, 1, 5]
    quick_sort_hoare(test_hoare, 0, len(test_hoare) - 1)
    assert test_hoare == [1, 5, 7, 8, 9, 10]
    
    # Edge cases
    empty_list = []
    quick_sort_lomuto(empty_list, 0, -1)
    assert empty_list == []
    
    single_list = [42]
    quick_sort_hoare(single_list, 0, 0)
    assert single_list == [42]
    
    print("6_7_quick_sort.py verified successfully!")
