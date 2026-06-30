# 11_13_segmentation_fault.py
"""
Segmentation Fault (CodeChef SEGFAULT / 1815).
Exactly one person is the thief and lies; others are honest and tell the truth.
Each person i claims the thief is in [L_i, R_i].
A suspect x is a valid thief if:
1. Exactly N - 1 people claim x is the thief.
2. Person x does not claim themselves as the thief (i.e., x is not in [L_x, R_x]).
Uses a Difference Array to count claims covering each person.
"""

def find_thief_suspects(n: int, ranges: list) -> list:
    """
    Finds all valid suspects for the thief.
    ranges is a 0-based list of tuples (L_i, R_i) representing claims of person i+1.
    Time Complexity: O(N) where N is the number of people.
    Space Complexity: O(N) to store counts and difference array.
    """
    # 1-based index setup
    diff = [0] * (n + 2)
    for i in range(n):
        l, r = ranges[i]
        diff[l] += 1
        diff[r + 1] -= 1
        
    # Compute running prefix sum to get cover counts
    cover_counts = [0] * (n + 1)
    current = 0
    for i in range(1, n + 1):
        current += diff[i]
        cover_counts[i] = current
        
    suspects = []
    for i in range(1, n + 1):
        l, r = ranges[i - 1]
        # Condition 1: Exactly N - 1 people claim i is the thief
        # Condition 2: i does not claim themselves (i.e., i < l or i > r)
        if cover_counts[i] == n - 1 and (i < l or i > r):
            suspects.append(i)
            
    return suspects

if __name__ == "__main__":
    # Test cases
    # N = 3
    # Person 1 says thief in [2, 3] (does not include 1)
    # Person 2 says thief in [3, 3] (does not include 2)
    # Person 3 says thief in [1, 2] (does not include 3)
    # Cover counts:
    # 1 is covered by range [1, 2] (Person 3) -> count = 1
    # 2 is covered by range [2, 3] (Person 1), [1, 2] (Person 3) -> count = 2 (N-1)
    # 3 is covered by range [2, 3] (Person 1), [3, 3] (Person 2) -> count = 2 (N-1)
    # Let's check suspects:
    # 2: count is 2 (N-1). Range of 2 is [3, 3], which doesn't include 2. Suspect!
    # 3: count is 2 (N-1). Range of 3 is [1, 2], which doesn't include 3. Suspect!
    # Suspects = [2, 3]
    assert find_thief_suspects(3, [(2, 3), (3, 3), (1, 2)]) == [2, 3]
    print("11_13_segmentation_fault.py verified successfully!")
