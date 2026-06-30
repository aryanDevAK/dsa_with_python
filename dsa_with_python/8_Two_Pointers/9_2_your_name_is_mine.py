# 9_2_your_name_is_mine.py
"""
Subsequence check for the Your Name is Mine problem (CodeChef NAME2).
Verifies if one string is a subsequence of another using two pointers.
"""

def is_subsequence(s1: str, s2: str) -> bool:
    """
    Checks if s1 is a subsequence of s2.
    Time Complexity: O(len(s2))
    Space Complexity: O(1) auxiliary space.
    """
    p1 = 0
    p2 = 0
    
    while p1 < len(s1) and p2 < len(s2):
        if s1[p1] == s2[p2]:
            p1 += 1
        p2 += 1
        
    return p1 == len(s1)

def can_marry(m: str, w: str) -> bool:
    """
    Determines if man M and woman W can marry.
    True if M is a subsequence of W or vice-versa.
    """
    return is_subsequence(m, w) or is_subsequence(w, m)

if __name__ == "__main__":
    # Self-testing assertions
    assert can_marry("john", "johanna") is True
    assert can_marry("ira", "ira") is True
    assert can_marry("kayla", "lauren") is False
    assert can_marry("a", "b") is False
    assert can_marry("", "anything") is True
    
    print("9_2_your_name_is_mine.py verified successfully!")
