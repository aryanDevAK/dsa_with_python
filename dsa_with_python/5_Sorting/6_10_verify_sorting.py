# 6_10_verify_sorting.py
"""
Automated test suite verifying the correctness of all Module 6 sorting and searching algorithms.
Imports modules dynamically to run a series of validation checks.
"""

import sys
import os
import importlib

# Add the parent directory containing the sorting modules to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Dynamically import all the sorting modules
m1 = importlib.import_module("6_1_sort_three_integers")
m2 = importlib.import_module("6_2_bubble_sort")
m3 = importlib.import_module("6_3_selection_sort")
m4 = importlib.import_module("6_4_nge")
m5 = importlib.import_module("6_5_insertion_sort")
m6 = importlib.import_module("6_6_merge_sort")
m7 = importlib.import_module("6_7_quick_sort")
m8 = importlib.import_module("6_8_counting_sort")
m9 = importlib.import_module("6_9_radix_sort")

if __name__ == "__main__":
    print("Starting automated tests for sorting and NGE algorithms...")

    # 1. Verify 6_1_sort_three_integers
    assert m1.sort_three_integers(10, 5, 20) == (5, 10, 20)
    assert m1.sort_three_integers(3, 3, 1) == (1, 3, 3)
    assert m1.sort_three_integers(-1, -5, -2) == (-5, -2, -1)
    print("[OK] 6_1_sort_three_integers verified.")

    # 2. Verify 6_2_bubble_sort
    arr = [5, 2, 9, 1, 5, 6]
    assert m2.bubble_sort_standard(arr.copy()) == [1, 2, 5, 5, 6, 9]
    assert m2.bubble_sort_optimized(arr.copy()) == [1, 2, 5, 5, 6, 9]
    print("[OK] 6_2_bubble_sort (standard & optimized) verified.")

    # 3. Verify 6_3_selection_sort
    arr = [5, 2, 9, 1, 5, 6]
    assert m3.selection_sort(arr.copy()) == [1, 2, 5, 5, 6, 9]
    print("[OK] 6_3_selection_sort verified.")

    # 4. Verify 6_4_nge
    nge_test = [3, 10, 4, 2, 1, 2, 6, 1, 7, 2, 9]
    expected_nge = [10, -1, 6, 6, 2, 6, 7, 7, 9, 9, -1]
    assert m4.next_greater_element_brute(nge_test) == expected_nge
    assert m4.next_greater_element_stack(nge_test) == expected_nge
    print("[OK] 6_4_nge (brute & stack) verified.")

    # 5. Verify 6_5_insertion_sort
    arr = [5, 2, 9, 1, 5, 6]
    assert m5.insertion_sort(arr.copy()) == [1, 2, 5, 5, 6, 9]
    print("[OK] 6_5_insertion_sort verified.")

    # 6. Verify 6_6_merge_sort
    arr = [5, 2, 9, 1, 5, 6]
    assert m6.merge_sort(arr) == [1, 2, 5, 5, 6, 9]
    print("[OK] 6_6_merge_sort verified.")

    # 7. Verify 6_7_quick_sort
    # Lomuto
    arr_lomuto = [5, 2, 9, 1, 5, 6]
    m7.quick_sort_lomuto(arr_lomuto, 0, len(arr_lomuto) - 1)
    assert arr_lomuto == [1, 2, 5, 5, 6, 9]
    # Hoare
    arr_hoare = [5, 2, 9, 1, 5, 6]
    m7.quick_sort_hoare(arr_hoare, 0, len(arr_hoare) - 1)
    assert arr_hoare == [1, 2, 5, 5, 6, 9]
    print("[OK] 6_7_quick_sort (Lomuto & Hoare) verified.")

    # 8. Verify 6_8_counting_sort
    arr_count = [5, 2, 9, 1, 5, 6]
    assert m8.counting_sort_unstable(arr_count.copy()) == [1, 2, 5, 5, 6, 9]
    assert m8.counting_sort_stable(arr_count) == [1, 2, 5, 5, 6, 9]
    # Support for negatives in stable counting sort
    arr_neg = [-3, 5, -1, 0, 5, -3]
    assert m8.counting_sort_stable(arr_neg) == [-3, -3, -1, 0, 5, 5]
    print("[OK] 6_8_counting_sort (stable & unstable) verified.")

    # 9. Verify 6_9_radix_sort
    arr_radix = [170, 45, 75, 90, 802, 24, 2, 66]
    assert m9.radix_sort(arr_radix.copy()) == [2, 24, 45, 66, 75, 90, 170, 802]
    print("[OK] 6_9_radix_sort verified.")

    print("\nAll sorting algorithms and helper modules verified successfully!")
