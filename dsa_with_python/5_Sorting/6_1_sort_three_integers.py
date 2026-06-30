# 6_1_sort_three_integers.py
"""
Optimal sorting of exactly three integers using raw comparisons and swaps.
Avoids loop instructions or temporary array allocations to maintain O(1) performance.
"""

def sort_three_integers(a: int, b: int, c: int) -> tuple:
    """
    Sorts three integers using at most 3 comparisons.
    Time Complexity: O(1)
    Space Complexity: O(1)
    Returns: Tuple (min, mid, max) in sorted ascending order.
    """
    # Comparison 1: Ensure a <= b
    if a > b:
        a, b = b, a
        
    # Comparison 2: Ensure b <= c
    if b > c:
        b, c = c, b
        
        # Comparison 3: Since c was swapped into b, check if new b is smaller than a
        if a > b:
            a, b = b, a
            
    return (a, b, c)

if __name__ == "__main__":
    # Self-testing assertions
    assert sort_three_integers(3, 2, 1) == (1, 2, 3)
    assert sort_three_integers(1, 2, 3) == (1, 2, 3)
    assert sort_three_integers(1, 3, 2) == (1, 2, 3)
    assert sort_three_integers(2, 1, 3) == (1, 2, 3)
    assert sort_three_integers(2, 3, 1) == (1, 2, 3)
    assert sort_three_integers(3, 1, 2) == (1, 2, 3)
    assert sort_three_integers(5, 5, 2) == (2, 5, 5)
    assert sort_three_integers(-1, -10, 0) == (-10, -1, 0)
    print("6_1_sort_three_integers.py verified successfully!")
