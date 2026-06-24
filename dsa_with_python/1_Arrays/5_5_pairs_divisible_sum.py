# 5_5_pairs_divisible_sum.py
"""
Pairs Divisible Sum.
Given an array and an integer K, finds the count of pairs (i, j) with i < j
such that (arr[i] + arr[j]) % K == 0.
- Brute Force: O(N^2) time.
- Optimized: O(N + K) time using remainder frequency map.
"""

def count_pairs_divisible_brute(arr: list, k: int) -> int:
    """
    Counts pairs with sum divisible by K using brute force.
    Time Complexity: O(N^2)
    Space Complexity: O(1)
    Returns: Number of pairs.
    """
    if k <= 0:
        return 0
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] + arr[j]) % k == 0:
                count += 1
    return count

def count_pairs_divisible_optimized(arr: list, k: int) -> int:
    """
    Counts pairs with sum divisible by K using remainder frequencies.
    Formula:
    If (A + B) % k == 0, then:
      - If A % k == 0, then B % k must be 0.
      - If A % k == r (where r > 0), then B % k must be k - r.
    Time Complexity: O(N + K)
    Space Complexity: O(K) for remainder array
    Returns: Number of pairs.
    """
    if k <= 0:
        return 0
    
    # Frequency table for remainders
    # remainder_freq[r] stores the number of elements with arr[i] % k == r
    remainder_freq = [0] * k
    for num in arr:
        rem = num % k
        # Handle negative numbers in Python: num % k is already in [0, k-1] range
        remainder_freq[rem] += 1
        
    pair_count = 0
    
    # 1. Elements that are divisible by K (remainder 0)
    # Pairs can only be formed among themselves: choose 2 from remainder_freq[0]
    freq0 = remainder_freq[0]
    pair_count += (freq0 * (freq0 - 1)) // 2
    
    # 2. Elements with remainder r and complement remainder k - r
    # Run loop from 1 to k // 2
    for r in range(1, (k // 2) + 1):
        # Avoid double-counting the midpoint if K is even
        if r == k - r:
            freq_mid = remainder_freq[r]
            pair_count += (freq_mid * (freq_mid - 1)) // 2
        else:
            pair_count += remainder_freq[r] * remainder_freq[k - r]
            
    return pair_count


if __name__ == "__main__":
    # Test cases
    test_arr = [1, 2, 3, 4, 5, 6]
    test_k = 3
    # Pairs divisible by 3:
    # (1, 2) -> 3
    # (1, 5) -> 6
    # (2, 4) -> 6
    # (3, 6) -> 9
    # (4, 5) -> 9
    # Total = 5 pairs
    assert count_pairs_divisible_brute(test_arr, test_k) == 5
    assert count_pairs_divisible_optimized(test_arr, test_k) == 5
    
    test_arr2 = [2, 2, 1, 7, 5, 3]
    test_k2 = 4
    # Remainder 0: None
    # Remainder 1: 1, 5 (complement: Remainder 3)
    # Remainder 2: 2, 2 (complement: Remainder 2 - mid)
    # Remainder 3: 7, 3 (complement: Remainder 1)
    # Pairs:
    # (2, 2) -> 4
    # (1, 7) -> 8
    # (1, 3) -> 4
    # (5, 7) -> 12
    # (5, 3) -> 8
    # Total = 5 pairs
    assert count_pairs_divisible_brute(test_arr2, test_k2) == 5
    assert count_pairs_divisible_optimized(test_arr2, test_k2) == 5
    
    # Handle empty list
    assert count_pairs_divisible_optimized([], 4) == 0
    print("5_5_pairs_divisible_sum.py verified successfully!")
