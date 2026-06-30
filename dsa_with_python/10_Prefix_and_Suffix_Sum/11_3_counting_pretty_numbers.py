# 11_3_counting_pretty_numbers.py
"""
Counting Pretty Numbers (CodeChef NUM239).
Counts how many numbers in a range [L, R] have their last digit as 2, 3, or 9.
Optimized using a prefix sum array.
"""

class PrettyNumberCounter:
    """
    Precomputes the count of pretty numbers up to a specified limit.
    Allows range queries in O(1) time.
    """
    def __init__(self, limit: int = 100000):
        self.pref = [0] * (limit + 1)
        for i in range(1, limit + 1):
            is_pretty = 1 if (i % 10 in {2, 3, 9}) else 0
            self.pref[i] = self.pref[i - 1] + is_pretty
            
    def count_pretty(self, l: int, r: int) -> int:
        """
        Returns the number of pretty numbers in the range [l, r].
        Time Complexity: O(1).
        Space Complexity: O(1).
        """
        if l > r or l < 1:
            return 0
        return self.pref[r] - self.pref[l - 1]

if __name__ == "__main__":
    # Test cases
    counter = PrettyNumberCounter()
    assert counter.count_pretty(1, 10) == 3 # 2, 3, 9
    assert counter.count_pretty(11, 33) == 8 # 12, 13, 19, 22, 23, 29, 32, 33
    print("11_3_counting_pretty_numbers.py verified successfully!")
