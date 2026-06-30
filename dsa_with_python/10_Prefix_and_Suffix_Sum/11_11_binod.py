# 11_11_binod.py
"""
Binod (CodeChef BINOD / 1776).
Uses prefix counts of bits (0 to 30) for each position to answer range queries efficiently.
Specifically, count[i][b] stores the number of elements with the b-th bit set up to index i-1.
"""

class BinodBitCounter:
    """
    Tracks set bits at each bit position for prefix segments.
    Enables range set/unset bit queries in O(1) time per bit.
    """
    def __init__(self, arr: list):
        self.n = len(arr)
        # prefix_counts[i][b] = count of numbers with b-th bit set up to index i-1
        self.prefix_counts = [[0] * 31 for _ in range(self.n + 1)]
        for i in range(self.n):
            for b in range(31):
                bit_set = 1 if ((arr[i] >> b) & 1) else 0
                self.prefix_counts[i+1][b] = self.prefix_counts[i][b] + bit_set
                
    def get_set_bits_count(self, l: int, r: int, b: int) -> int:
        """
        Returns the number of elements in the range [l, r] (0-based inclusive)
        that have their b-th bit set.
        Time Complexity: O(1).
        Space Complexity: O(1).
        """
        if l < 0 or r >= self.n or l > r:
            return 0
        return self.prefix_counts[r + 1][b] - self.prefix_counts[l][b]

    def get_unset_bits_count(self, l: int, r: int, b: int) -> int:
        """
        Returns the number of elements in the range [l, r] (0-based inclusive)
        that have their b-th bit unset.
        Time Complexity: O(1).
        Space Complexity: O(1).
        """
        if l < 0 or r >= self.n or l > r:
            return 0
        total_elements = r - l + 1
        return total_elements - self.get_set_bits_count(l, r, b)

if __name__ == "__main__":
    # Test cases
    # 2 = 010 (binary), 3 = 011, 4 = 100, 5 = 101
    arr = [2, 3, 4, 5]
    counter = BinodBitCounter(arr)
    # Check bit 0 (last bit): 3 has it set, 5 has it set. Range [0, 3] should have 2 set bits.
    assert counter.get_set_bits_count(0, 3, 0) == 2
    # Check bit 2 (third bit): 4 has it set, 5 has it set. Range [1, 3] should have 2 set bits.
    assert counter.get_set_bits_count(1, 3, 2) == 2
    # Check unset bits: Range [0, 3] has 4 elements, 2 have bit 0 set, so 2 should have it unset.
    assert counter.get_unset_bits_count(0, 3, 0) == 2
    print("11_11_binod.py verified successfully!")
