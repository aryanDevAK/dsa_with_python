# 9_6_vowel_anxiety.py
"""
Vowel Anxiety (CodeChef VOWANX).
Constructs the final string where substrings are toggled on vowels in O(N) linear time.
"""

from collections import deque

def solve_vowel_anxiety(s: str) -> str:
    """
    Simulates string reversals on vowels in O(N) time.
    Separates characters into odd and even groups based on the number of vowels
    to their right (which determines their total number of reversals).
    Time Complexity: O(N) where N is len(s).
    Space Complexity: O(N) to store groups.
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    n = len(s)
    
    # Step 1: Precalculate suffix vowel counts
    vowels_right = [0] * n
    count = 0
    for i in range(n - 1, -1, -1):
        if s[i] in vowels:
            count += 1
        vowels_right[i] = count
        
    # Step 2: Separate into odd and even groups
    odd_chars = []
    even_chars = []
    for i in range(n):
        if vowels_right[i] % 2 == 1:
            odd_chars.append(s[i])
        else:
            even_chars.append(s[i])
            
    # Step 3: Odd group has been reversed an odd number of times, so reverse its relative order
    odd_chars.reverse()
    
    return "".join(odd_chars) + "".join(even_chars)

if __name__ == "__main__":
    # Self-testing assertions
    # Input: "abc" -> vowel at 0 ('a').
    # Naive trace: "a" -> "a". "ab" -> "ab". "abc" -> "abc". Winner: "abc"
    assert solve_vowel_anxiety("abc") == "abc"
    
    # Input: "abec" -> vowel at 0 ('a'), 2 ('e')
    # Naive trace:
    # 'a': "a" (vowel -> reversed "a")
    # 'b': "ab"
    # 'e': "abe" (vowel -> reversed "eba")
    # 'c': "ebac"
    assert solve_vowel_anxiety("abec") == "ebac"
    
    # Input: "destroye"
    # Naive trace:
    # 'd': "d"
    # 'e': "de" (vowel -> "ed")
    # 's': "eds"
    # 't': "edst"
    # 'r': "edstr"
    # 'o': "edstro" (vowel -> "ortsde")
    # 'y': "ortsdey"
    # 'e': "ortsdeye" (vowel -> "eyedstro")
    assert solve_vowel_anxiety("destroye") == "eyedstro"
    
    print("9_6_vowel_anxiety.py verified successfully!")
