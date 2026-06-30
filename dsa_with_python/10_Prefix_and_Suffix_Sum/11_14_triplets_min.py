# 11_14_triplets_min.py
"""
Triplets Min (CodeChef 1868 / Starters 97).
Finds the K-th smallest element in the triplet minimums array.
Each sorted element A[i] is the minimum for C(N - 1 - i, 2) triplets.
Uses prefix sums of combinatorics counts + binary search (bisect) for queries.
"""

import bisect

class TripletsMinSolver:
    """
    Precomputes cumulative triplet min counts.
    Answers rank queries in O(log N) time.
    """
    def __init__(self, arr: list):
        self.arr = sorted(arr)
        self.n = len(self.arr)
        
        self.counts = []
        for i in range(self.n - 2):
            rem = self.n - 1 - i
            triplets_count = rem * (rem - 1) // 2
            self.counts.append(triplets_count)
            
        # Compute prefix sums of counts
        self.pref = []
        current_sum = 0
        for count in self.counts:
            current_sum += count
            self.pref.append(current_sum)
            
    def query(self, k: int) -> int:
        """
        Returns the K-th smallest triplet minimum (1-based rank).
        Time Complexity: O(log N).
        Space Complexity: O(1).
        """
        # Find the first index where prefix sum >= k
        idx = bisect.bisect_left(self.pref, k)
        if idx < len(self.arr):
            return self.arr[idx]
        return -1

if __name__ == "__main__":
    # Test cases
    # arr = [1, 2, 3, 4]
    # Sorted: [1, 2, 3, 4]
    # Triplets: (1,2,3)->1, (1,2,4)->1, (1,3,4)->1, (2,3,4)->2
    # Triplet min counts:
    # 1 is minimum in 3 triplets (indices 1, 2, 3) -> comb(3, 2) = 3
    # 2 is minimum in 1 triplet (index 3) -> comb(2, 2) = 1
    # prefix sums: [3, 4]
    solver = TripletsMinSolver([1, 2, 3, 4])
    assert solver.query(1) == 1
    assert solver.query(2) == 1
    assert solver.query(3) == 1
    assert solver.query(4) == 2
    print("11_14_triplets_min.py verified successfully!")
