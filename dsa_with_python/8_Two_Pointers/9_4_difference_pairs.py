# 9_4_difference_pairs.py
"""
Difference Pairs (CodeChef 1000).
Checks if there exists a pair with difference K in a sorted array using same-direction pointers.
"""

def has_difference_pair(arr: list, k: int) -> bool:
    """
    Finds if there exists a pair with difference K in the sorted array.
    Time Complexity: O(N) where N is len(arr).
    Space Complexity: O(1) auxiliary space.
    Returns: True if pair exists, else False.
    """
    k = abs(k)
    n = len(arr)
    left = 0
    right = 1
    
    while left < n and right < n:
        if left == right:
            right += 1
            continue
            
        diff = arr[right] - arr[left]
        if diff == k:
            return True
        elif diff < k:
            right += 1
        else:
            left += 1
            
    return False

if __name__ == "__main__":
    # Self-testing assertions
    # Sorted: [5, 10, 15, 20], K = 5 -> (10, 5) exists.
    assert has_difference_pair([5, 10, 15, 20], 5) is True
    assert has_difference_pair([5, 10, 15, 20], 10) is True
    assert has_difference_pair([5, 10, 15, 20], 7) is False
    assert has_difference_pair([1, 2], 0) is False # difference 0 must be disjoint elements
    
    print("9_4_difference_pairs.py verified successfully!")
