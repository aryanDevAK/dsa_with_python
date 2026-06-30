# 11_12_mystical_numbers.py
"""
Mystical Numbers (CodeChef XORGAND / 1702).
Counts elements A[i] in range [L, R] such that A[i] ^ X < X.
Key Insight: A[i] ^ X < X if and only if the MSB(A[i]) bit is set in X.
Optimized using prefix counts of MSB groups.
"""

class MysticalNumbersSolver:
    """
    Solves Mystical Numbers queries in O(31) -> O(1) time per query.
    """
    def __init__(self, arr: list):
        self.n = len(arr)
        # prefix_counts[i][b] = count of numbers with MSB equal to b up to index i-1
        self.prefix_counts = [[0] * 31 for _ in range(self.n + 1)]
        
        for i in range(self.n):
            msb = self._get_msb(arr[i])
            for b in range(31):
                match = 1 if msb == b else 0
                self.prefix_counts[i + 1][b] = self.prefix_counts[i][b] + match
                
    def _get_msb(self, num: int) -> int:
        """Returns the 0-based bit position of the MSB of num."""
        if num <= 0:
            return -1
        return num.bit_length() - 1
        
    def query(self, l: int, r: int, x: int) -> int:
        """
        Returns the count of elements in range [l, r] (0-based inclusive)
        satisfying A[i] ^ x < x.
        Time Complexity: O(31) -> O(1).
        Space Complexity: O(1).
        """
        if l < 0 or r >= self.n or l > r:
            return 0
            
        count = 0
        for b in range(31):
            if (x >> b) & 1:
                # Add count of elements in range [l, r] whose MSB is b
                count += self.prefix_counts[r + 1][b] - self.prefix_counts[l][b]
        return count

if __name__ == "__main__":
    # Test cases
    # arr = [2, 3, 4, 5]
    # MSBs:
    # 2 (010) -> MSB = 1
    # 3 (011) -> MSB = 1
    # 4 (100) -> MSB = 2
    # 5 (101) -> MSB = 2
    solver = MysticalNumbersSolver([2, 3, 4, 5])
    # Query range [0, 3] with X = 5 (101) -> bits 0 and 2 are set.
    # Elements with MSB 0: none (0)
    # Elements with MSB 2: 4 and 5 (2)
    # Total count = 2. Verified: 2^5=7, 3^5=6, 4^5=1<5, 5^5=0<5. Correct!
    assert solver.query(0, 3, 5) == 2
    print("11_12_mystical_numbers.py verified successfully!")
