# 9_1_remove_duplicates.py
"""
In-place duplicate removal from a sorted list using the reader-writer two-pointer pattern.
"""

def remove_duplicates(arr: list) -> int:
    """
    Removes duplicates in-place from a sorted list.
    Time Complexity: O(N) where N is len(arr).
    Space Complexity: O(1) auxiliary space.
    Returns: The new length of the list with unique elements.
    """
    if not arr:
        return 0
        
    write_idx = 1
    for read_idx in range(1, len(arr)):
        # If the current element is different from the last unique element
        if arr[read_idx] != arr[write_idx - 1]:
            arr[write_idx] = arr[read_idx]
            write_idx += 1
            
    return write_idx

if __name__ == "__main__":
    # Self-testing assertions
    test_1 = [1, 1, 2]
    length_1 = remove_duplicates(test_1)
    assert length_1 == 2
    assert test_1[:length_1] == [1, 2]
    
    test_2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    length_2 = remove_duplicates(test_2)
    assert length_2 == 5
    assert test_2[:length_2] == [0, 1, 2, 3, 4]
    
    # Empty and single element list
    assert remove_duplicates([]) == 0
    assert remove_duplicates([42]) == 1
    
    print("9_1_remove_duplicates.py verified successfully!")
