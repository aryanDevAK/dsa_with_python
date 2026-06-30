# 7_1_chef_and_string.py
"""
Greedy solution for the Chef and String problem (CodeChef XYSTR).
Maximizes the number of adjacent boy-girl ('x'-'y' or 'y'-'x') pairs in a string row.
"""

def max_boy_girl_pairs(s: str) -> int:
    """
    Finds the maximum number of adjacent boy-girl pairs.
    Time Complexity: O(N) where N is the length of the string.
    Space Complexity: O(1) auxiliary space.
    Returns: Maximum pair count.
    """
    n = len(s)
    pairs = 0
    i = 0
    
    while i < n - 1:
        # If adjacent characters are different, they can form a boy-girl pair
        if s[i] != s[i + 1]:
            pairs += 1
            i += 2  # Consume both characters by stepping index forward by 2
        else:
            i += 1  # Standard step forward by 1
            
    return pairs

if __name__ == "__main__":
    # Self-testing assertions
    assert max_boy_girl_pairs("xy") == 1
    assert max_boy_girl_pairs("xyxxy") == 2
    assert max_boy_girl_pairs("yy") == 0
    assert max_boy_girl_pairs("xxxx") == 0
    assert max_boy_girl_pairs("xyxyxy") == 3
    assert max_boy_girl_pairs("yxyx") == 2
    assert max_boy_girl_pairs("x") == 0
    assert max_boy_girl_pairs("") == 0
    
    print("7_1_chef_and_string.py verified successfully!")
