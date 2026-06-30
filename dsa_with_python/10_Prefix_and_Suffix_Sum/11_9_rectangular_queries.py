# 11_9_rectangular_queries.py
"""
Rectangular Queries (CodeChef RECTQUER / 1778).
Given an N x N matrix of values between 1 and 10.
Answer queries (x1, y1) to (x2, y2) asking for distinct element counts.
Uses 2D Prefix Sums on 10 value planes.
"""

class RectangularQueries:
    """
    Builds 2D prefix sums for values 1 to 10.
    Queries count in O(10) -> O(1) time.
    """
    def __init__(self, matrix: list):
        self.n = len(matrix)
        # pref[val][i][j] = count of val in matrix[0...i-1][0...j-1]
        # Using 1-based indexing for prefix sums
        self.pref = [[[0] * (self.n + 1) for _ in range(self.n + 1)] for _ in range(11)]
        
        for val in range(1, 11):
            for i in range(1, self.n + 1):
                for j in range(1, self.n + 1):
                    cell_match = 1 if matrix[i - 1][j - 1] == val else 0
                    self.pref[val][i][j] = (cell_match + 
                                            self.pref[val][i - 1][j] + 
                                            self.pref[val][i][j - 1] - 
                                            self.pref[val][i - 1][j - 1])
                                            
    def query_distinct(self, x1: int, y1: int, x2: int, y2: int) -> int:
        """
        Calculates the count of distinct elements in the submatrix.
        Parameters are 1-based coordinates.
        Time Complexity: O(1) (exactly 10 operations).
        Space Complexity: O(1).
        """
        distinct_count = 0
        for val in range(1, 11):
            count = (self.pref[val][x2][y2] - 
                     self.pref[val][x1 - 1][y2] - 
                     self.pref[val][x2][y1 - 1] + 
                     self.pref[val][x1 - 1][y1 - 1])
            if count > 0:
                distinct_count += 1
        return distinct_count

if __name__ == "__main__":
    # Test cases
    matrix = [
        [1, 2, 3],
        [3, 2, 1],
        [5, 6, 3]
    ]
    rq = RectangularQueries(matrix)
    # Query rectangle (1, 1) to (2, 2) -> [[1, 2], [3, 2]] -> distinct values 1, 2, 3 -> count is 3
    assert rq.query_distinct(1, 1, 2, 2) == 3
    # Query rectangle (2, 2) to (3, 3) -> [[2, 1], [6, 3]] -> distinct values 1, 2, 3, 6 -> count is 4
    assert rq.query_distinct(2, 2, 3, 3) == 4
    print("11_9_rectangular_queries.py verified successfully!")
