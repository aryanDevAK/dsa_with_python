# 5_2_kth_character.py
"""
Find K-th Character Position in a string.
Time Complexity: O(N)
Space Complexity: O(1)
"""

def find_kth_character(s: str, target: str, k: int) -> int:
    """
    Finds the 0-indexed position of the k-th occurrence of 'target' in 's'.
    Time Complexity: O(N)
    Space Complexity: O(1)
    Returns: Index of the k-th occurrence if found, else -1.
    """
    if k <= 0 or len(target) != 1:
        return -1
        
    occurrence_count = 0
    for idx in range(len(s)):
        if s[idx] == target:
            occurrence_count += 1
            if occurrence_count == k:
                return idx
    return -1


if __name__ == "__main__":
    test_str = "abracadabra"
    # 'a' occurrences: index 0 (1st), 3 (2nd), 5 (3rd), 7 (4th), 10 (5th)
    assert find_kth_character(test_str, 'a', 1) == 0
    assert find_kth_character(test_str, 'a', 2) == 3
    assert find_kth_character(test_str, 'a', 5) == 10
    assert find_kth_character(test_str, 'a', 6) == -1
    
    # 'b' occurrences: index 1 (1st), 8 (2nd)
    assert find_kth_character(test_str, 'b', 2) == 8
    assert find_kth_character(test_str, 'z', 1) == -1
    
    # Invalid values of k
    assert find_kth_character(test_str, 'a', 0) == -1
    assert find_kth_character(test_str, 'a', -3) == -1
    print("5_2_kth_character.py verified successfully!")
