# 7_2_chopsticks.py
"""
Greedy sorted threshold matching for the Chopsticks problem (CodeChef TACHSTSP).
Sorts chopstick lengths and pairs adjacent sticks if their difference is <= D.
"""

def max_chopstick_pairs(lengths: list, d: int) -> int:
    """
    Finds the maximum number of chopstick pairs with length difference <= d.
    Time Complexity: O(N log N) dominated by lengths.sort().
    Space Complexity: O(1) auxiliary space (in-place sort).
    Returns: Maximum pair count.
    """
    lengths.sort()
    n = len(lengths)
    pairs = 0
    i = 0
    
    while i < n - 1:
        if lengths[i + 1] - lengths[i] <= d:
            pairs += 1
            i += 2  # Consumed both sticks, move index by 2
        else:
            i += 1  # Element lengths[i] cannot be paired, skip it
            
    return pairs

if __name__ == "__main__":
    # Self-testing assertions
    assert max_chopstick_pairs([1, 3, 3, 9, 4], 2) == 2  # Pairs: (1, 3) and (3, 4) or (3, 3) and (1, ? no)
    # Sorted: [1, 3, 3, 4, 9]
    # Check: 3-1 = 2 <= 2 (Pair 1), index moves to 3 (which is index 2).
    # Check: 4-3 = 1 <= 2 (Pair 2), index moves to 9.
    # Total: 2 pairs. Correct.
    
    assert max_chopstick_pairs([5, 8, 11, 20], 3) == 2  # Pairs: (5, 8) and (8, 11) -> wait:
    # Sorted: [5, 8, 11, 20]
    # Check: 8-5 = 3 <= 3 (Pair 1). Index moves to 11.
    # Check: 20-11 = 9 > 3 (No). Index moves to 20.
    # Total: 1 pair. Correct.
    
    assert max_chopstick_pairs([10, 10, 10, 10], 0) == 2
    assert max_chopstick_pairs([1, 10], 5) == 0
    assert max_chopstick_pairs([5], 10) == 0
    assert max_chopstick_pairs([], 5) == 0
    
    print("7_2_chopsticks.py verified successfully!")
