# 11_2_optimization_using_prefix_array.py
"""
Range Sum Queries optimization using prefix sum arrays.
Calculates the sum of elements within a range [L, R] in O(1) time after O(N) preprocessing.
"""

class RangeSumQuery:
    """
    Handles range sum queries in O(1) time after O(N) preprocessing.
    """
    def __init__(self, arr: list):
        # Using a 1-based prefix sum array simplifies boundary checks (L = 0)
        self.prefix = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            self.prefix[i + 1] = self.prefix[i] + arr[i]
            
    def get_sum(self, left: int, right: int) -> int:
        """
        Returns the sum of elements from index left to right (inclusive).
        Time Complexity: O(1).
        Space Complexity: O(1).
        """
        if left < 0 or right >= len(self.prefix) - 1 or left > right:
            return 0
        return self.prefix[right + 1] - self.prefix[left]

if __name__ == "__main__":
    # Test cases
    rsq = RangeSumQuery([3, 1, 4, 1, 5])
    assert rsq.get_sum(1, 3) == 6 # 1 + 4 + 1 = 6
    assert rsq.get_sum(0, 4) == 14 # 3 + 1 + 4 + 1 + 5 = 14
    assert rsq.get_sum(2, 2) == 4 # 4
    print("11_2_optimization_using_prefix_array.py verified successfully!")
