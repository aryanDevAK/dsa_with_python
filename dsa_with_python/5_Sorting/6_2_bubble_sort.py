# 6_2_bubble_sort.py
"""
Bubble Sort Implementations in Python.
Includes standard bubble sort and an optimized early-termination version.
"""

def bubble_sort_standard(arr: list) -> list:
    """
    Performs standard bubble sort on a list in-place.
    Time Complexity: O(N^2) (best, average, worst)
    Space Complexity: O(1)
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def bubble_sort_optimized(arr: list) -> list:
    """
    Performs optimized bubble sort on a list in-place.
    Uses a 'swapped' flag to terminate early if the array is already sorted.
    Time Complexity: Best O(N), Average O(N^2), Worst O(N^2)
    Space Complexity: O(1)
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no two elements were swapped in inner loop, then list is sorted.
        if not swapped:
            break
    return arr

if __name__ == "__main__":
    # Self-testing assertions
    test_list_1 = [64, 34, 25, 12, 22, 11, 90]
    assert bubble_sort_standard(test_list_1.copy()) == [11, 12, 22, 25, 34, 64, 90]
    
    test_list_2 = [64, 34, 25, 12, 22, 11, 90]
    assert bubble_sort_optimized(test_list_2.copy()) == [11, 12, 22, 25, 34, 64, 90]
    
    # Already sorted test
    sorted_list = [1, 2, 3, 4, 5]
    assert bubble_sort_optimized(sorted_list.copy()) == [1, 2, 3, 4, 5]
    
    # Empty list and single element list
    assert bubble_sort_optimized([]) == []
    assert bubble_sort_optimized([42]) == [42]
    
    print("6_2_bubble_sort.py verified successfully!")
