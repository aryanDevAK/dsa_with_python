# 11_6_optimal_denomination.py
"""
Optimal Denomination (CodeChef OPTDENOM / 1759).
Maximize the overall GCD by changing exactly one element to minimize the sum divided by the GCD.
Uses prefix and suffix GCD arrays.
"""

import math

def get_optimal_denomination(arr: list) -> int:
    """
    Finds the minimum value of (sum(arr) - A[i] + new_A[i]) / new_GCD
    by replacing exactly one element.
    Time Complexity: O(N log(max_val)) where log(max_val) is for the Euclidean GCD algorithm.
    Space Complexity: O(N) to store prefix and suffix GCDs.
    """
    n = len(arr)
    if n == 1:
        return 1
        
    # prefix GCDs: pref_gcd[i] = gcd(arr[0...i])
    pref_gcd = [0] * n
    pref_gcd[0] = arr[0]
    for i in range(1, n):
        pref_gcd[i] = math.gcd(pref_gcd[i - 1], arr[i])
        
    # suffix GCDs: suff_gcd[i] = gcd(arr[i...n-1])
    suff_gcd = [0] * n
    suff_gcd[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        suff_gcd[i] = math.gcd(suff_gcd[i + 1], arr[i])
        
    total_sum = sum(arr)
    min_cost = float('inf')
    
    for i in range(n):
        if i == 0:
            current_gcd = suff_gcd[1]
        elif i == n - 1:
            current_gcd = pref_gcd[n - 2]
        else:
            current_gcd = math.gcd(pref_gcd[i - 1], suff_gcd[i + 1])
            
        new_sum = total_sum - arr[i] + current_gcd
        cost = new_sum // current_gcd
        min_cost = min(min_cost, cost)
        
    return min_cost

if __name__ == "__main__":
    # Test cases
    assert get_optimal_denomination([2, 2, 4]) == 3 # change 4 to 2, new array: [2, 2, 2], gcd=2, sum=6, cost=6/2=3
    assert get_optimal_denomination([3, 5, 9]) == 5 # change 5 to 3, new array: [3, 3, 9], gcd=3, sum=15, cost=15/3=5
    print("11_6_optimal_denomination.py verified successfully!")
