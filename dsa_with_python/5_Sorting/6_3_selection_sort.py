# 6_3_selection_sort.py
"""
Selection Sort Implementation in Python.
Repeatedly selects the minimum element from the unsorted segment and moves it to the sorted segment.
"""

def selection_sort(arr: list) -> list:
    """
    Performs selection sort on a list in-place.
    Time Complexity: O(N^2) (best, average, worst)
    Space Complexity: O(1)
    """
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # Swap the found minimum element with the first element of unsorted part
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            
    return arr

if __name__ == "__main__":
    # Self-testing assertions
    test_list = [64, 25, 12, 22, 11]
    assert selection_sort(test_list.copy()) == [11, 12, 22, 25, 64]
    
    # Already sorted list
    assert selection_sort([1, 2, 3]) == [1, 2, 3]
    
    # Empty list and single element list
    assert selection_sort([]) == []
    assert selection_sort([99]) == [99]
    
    print("6_3_selection_sort.py verified successfully!")
