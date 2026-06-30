# 6_5_insertion_sort.py
"""
Insertion Sort Implementation in Python.
Builds the sorted array one element at a time by shifting elements to insert the key.
"""

def insertion_sort(arr: list) -> list:
    """
    Performs insertion sort on a list in-place.
    Time Complexity: Best O(N) when already sorted, Average/Worst O(N^2)
    Space Complexity: O(1)
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Shift elements of arr[0..i-1] that are greater than key to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

if __name__ == "__main__":
    # Self-testing assertions
    test_list = [12, 11, 13, 5, 6]
    assert insertion_sort(test_list.copy()) == [5, 6, 11, 12, 13]
    
    # Already sorted list
    assert insertion_sort([1, 2, 3]) == [1, 2, 3]
    
    # Empty list and single element list
    assert insertion_sort([]) == []
    assert insertion_sort([42]) == [42]
    
    print("6_5_insertion_sort.py verified successfully!")
