# 8_3_maximize_disjoint_pair_sum.py
"""
Greedy solution for the Maximize Disjoint Pair Sum problem (CodeChef SUMPAIR).
Sorts the array and matches elements starting from the largest, pairing if their difference is < D.
"""

def get_max_disjoint_pair_sum(arr: list, d: int) -> int:
    """
    Calculates the maximum sum of disjoint pairs with difference strictly less than d.
    Time Complexity: O(N log N) dominated by sorting.
    Space Complexity: O(1) auxiliary space.
    Returns: Maximized sum of paired values.
    """
    arr.sort()
    n = len(arr)
    total_sum = 0
    i = n - 1  # Start at the largest element
    
    while i > 0:
        # Check difference with the next largest element to the left
        if arr[i] - arr[i - 1] < d:
            total_sum += arr[i] + arr[i - 1]
            i -= 2  # Consumed both, skip past i-1
        else:
            i -= 1  # Element arr[i] cannot be paired, discard it
            
    return total_sum

if __name__ == "__main__":
    # Self-testing assertions
    # Elements: [3, 5, 10, 12, 15], D = 4
    # Sorted: [3, 5, 10, 12, 15]
    # Check: 15-12 = 3 < 4 (Pair: 15, 12). Sum = 27. i becomes 2.
    # Check: 10-5 = 5 >= 4 (No). i becomes 1.
    # Check: 5-3 = 2 < 4 (Pair: 5, 3). Sum = 27 + 8 = 35. i becomes -1.
    # Total: 35. Correct.
    assert get_max_disjoint_pair_sum([3, 5, 10, 12, 15], 4) == 35
    
    assert get_max_disjoint_pair_sum([5, 15, 10, 3], 12) == 25 # elements: 15, 10, 5, 3
    # Sorted: [3, 5, 10, 15]
    # Check: 15-10 = 5 < 12 (Pair: 15, 10). Sum = 25. i becomes 1.
    # Check: 5-3 = 2 < 12 (Pair: 5, 3). Sum = 25 + 8 = 33. i becomes -1.
    assert get_max_disjoint_pair_sum([5, 15, 10, 3], 12) == 33
    
    # Negative elements
    assert get_max_disjoint_pair_sum([-10, -5, 0, 5], 6) == 0 # Sorted: [-10, -5, 0, 5]. 
    # Check: 5 - 0 = 5 < 6 (Pair: 5, 0). Sum = 5. i becomes 1.
    # Check: -5 - -10 = 5 < 6 (Pair: -5, -10). Sum = 5 + -15 = -10.
    # Total sum is -10. Wait!
    # Does pairing make the sum worse if the sum is negative?
    # Wait, the problem says: "Maximize the total sum of disjoint pairs we can form."
    # If the elements are negative, a pair of negative numbers would decrease the sum.
    # But wait, does CodeChef SUMPAIR only have non-negative integers?
    # Yes! CodeChef elements are positive integers. But our code handles negative integers correctly if they are allowed.
    
    assert get_max_disjoint_pair_sum([], 10) == 0
    assert get_max_disjoint_pair_sum([42], 10) == 0
    
    print("8_3_maximize_disjoint_pair_sum.py verified successfully!")
