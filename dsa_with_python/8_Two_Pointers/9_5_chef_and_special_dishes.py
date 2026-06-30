# 9_5_chef_and_special_dishes.py
"""
Chef And Special Dishes (CodeChef CHEFSPL).
Determines if a string can be formed by doubling a string T (T+T) with at most one insert.
"""

def match_with_one_skip(short_str: str, long_str: str) -> bool:
    """
    Checks if short_str matches long_str with at most 1 character skipped in long_str.
    Time Complexity: O(len(short_str))
    Space Complexity: O(1) auxiliary space.
    """
    p_short = 0
    p_long = 0
    skips = 0
    
    while p_short < len(short_str) and p_long < len(long_str):
        if short_str[p_short] == long_str[p_long]:
            p_short += 1
            p_long += 1
        else:
            p_long += 1  # Skip character in long_str
            skips += 1
            if skips > 1:
                return False
                
    return p_short == len(short_str)

def is_special_dish(s: str) -> bool:
    """
    Checks if the string S is special.
    Time Complexity: O(N) where N is len(s).
    Space Complexity: O(1) auxiliary space (or O(N) for slices).
    """
    n = len(s)
    if n < 2:
        return False
        
    if n % 2 == 0:
        mid = n // 2
        return s[:mid] == s[mid:]
        
    mid = n // 2
    # Case 1: First half is shorter (extra character in second half)
    # Compare s[0:mid] with s[mid:n]
    if match_with_one_skip(s[:mid], s[mid:]):
        return True
        
    # Case 2: First half is longer (extra character in first half)
    # Compare s[mid+1:n] with s[0:mid+1]
    if match_with_one_skip(s[mid+1:], s[:mid+1]):
        return True
        
    return False

if __name__ == "__main__":
    # Self-testing assertions
    assert is_special_dish("aba") is True  # "ab" vs "a" or "a" vs "ba", "a" matches "ba" with 1 skip.
    assert is_special_dish("abacaba") is False
    assert is_special_dish("abcdabcd") is True  # Even string exactly equal
    assert is_special_dish("abcdxabcd") is True # Odd string with 'x' inserted in middle
    assert is_special_dish("abcxdabcd") is True # Odd string with 'x' inserted inside first half
    
    print("9_5_chef_and_special_dishes.py verified successfully!")
