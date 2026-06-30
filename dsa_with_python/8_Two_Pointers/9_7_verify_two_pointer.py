# 9_7_verify_two_pointer.py
"""
Automated test suite verifying the correctness of all Module 9 Two-Pointer implementations.
Imports modules dynamically to run validation checks.
"""

import sys
import os
import importlib

# Add the parent directory containing the two-pointer modules to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Dynamically import all modules
m1 = importlib.import_module("9_1_remove_duplicates")
m2 = importlib.import_module("9_2_your_name_is_mine")
m3 = importlib.import_module("9_3_sort_array_by_parity")
m4 = importlib.import_module("9_4_difference_pairs")
m5 = importlib.import_module("9_5_chef_and_special_dishes")
m6 = importlib.import_module("9_6_vowel_anxiety")

if __name__ == "__main__":
    print("Starting automated tests for two-pointer algorithms...")

    # 1. Verify 9_1_remove_duplicates
    arr_1 = [1, 1, 2, 2, 3]
    len_1 = m1.remove_duplicates(arr_1)
    assert len_1 == 3
    assert arr_1[:len_1] == [1, 2, 3]
    print("[OK] 9_1_remove_duplicates verified.")

    # 2. Verify 9_2_your_name_is_mine
    assert m2.can_marry("john", "johanna") is True
    assert m2.can_marry("kayla", "lauren") is False
    print("[OK] 9_2_your_name_is_mine verified.")

    # 3. Verify 9_3_sort_array_by_parity
    res_3 = m3.sort_array_by_parity([3, 1, 2, 4])
    assert all(x % 2 == 0 for x in res_3[:2])
    assert all(x % 2 != 0 for x in res_3[2:])
    print("[OK] 9_3_sort_array_by_parity verified.")

    # 4. Verify 9_4_difference_pairs
    assert m4.has_difference_pair([5, 10, 15, 20], 5) is True
    assert m4.has_difference_pair([5, 10, 15, 20], 7) is False
    print("[OK] 9_4_difference_pairs verified.")

    # 5. Verify 9_5_chef_and_special_dishes
    assert m5.is_special_dish("abcdabcd") is True
    assert m5.is_special_dish("abcdxabcd") is True
    assert m5.is_special_dish("abacaba") is True
    assert m5.is_special_dish("abacdab") is False
    print("[OK] 9_5_chef_and_special_dishes verified.")

    # 6. Verify 9_6_vowel_anxiety
    assert m6.solve_vowel_anxiety("abec") == "ebac"
    assert m6.solve_vowel_anxiety("destroye") == "eyedstro"
    print("[OK] 9_6_vowel_anxiety verified.")

    print("\nAll two-pointer algorithms and helper modules verified successfully!")
