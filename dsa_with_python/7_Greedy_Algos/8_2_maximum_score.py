# 8_2_maximum_score.py
"""
Greedy reverse search solution for the Maximum Score problem (CodeChef MAXSC).
Sorts matrix rows and selects the largest valid element strictly less than the successor's selection.
"""

def get_maximum_score_matrix(matrix: list) -> int:
    """
    Finds the maximum sum of a strictly increasing sequence from matrix rows.
    Time Complexity: O(N^2 log N) to sort each row.
    Space Complexity: O(1) in-place.
    Returns: Maximized sum, or -1 if impossible.
    """
    n = len(matrix)
    if n == 0:
        return 0
        
    # Sort each row in ascending order
    for row in matrix:
        row.sort()
        
    total_sum = 0
    current_limit = float('inf')
    
    # Iterate backwards from row n-1 down to 0
    for i in range(n - 1, -1, -1):
        chosen_element = -1
        # Scan from right (largest) to left (smallest)
        for j in range(n - 1, -1, -1):
            if matrix[i][j] < current_limit:
                chosen_element = matrix[i][j]
                break
                
        # If no valid element found, strictly increasing sequence is impossible
        if chosen_element == -1:
            return -1
            
        total_sum += chosen_element
        current_limit = chosen_element
        
    return total_sum

if __name__ == "__main__":
    # Self-testing assertions
    test_matrix = [
        [10, 20, 30],
        [5, 15, 25],
        [12, 14, 18]
    ]
    # Optimal selections:
    # Row 2: 18 (limit becomes 18)
    # Row 1: 15 (limit becomes 15)
    # Row 0: 10 (limit becomes 10)
    # Total: 18 + 15 + 10 = 43
    assert get_maximum_score_matrix(test_matrix) == 43
    
    # Impossible case
    impossible_matrix = [
        [10, 20, 30],
        [1, 2, 3],
        [2, 4, 6]
    ]
    # Row 2: 6
    # Row 1: 3
    # Row 0: no element < 3 exists (options: 10, 20, 30) -> Return -1
    assert get_maximum_score_matrix(impossible_matrix) == -1
    
    # Single element row matrix
    assert get_maximum_score_matrix([[42]]) == 42
    
    print("8_2_maximum_score.py verified successfully!")
