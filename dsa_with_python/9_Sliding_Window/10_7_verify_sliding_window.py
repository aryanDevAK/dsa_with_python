# 10_7_verify_sliding_window.py
"""
Automated test suite verifying all Module 10 Sliding Window implementations.
"""

import sys
import os
import importlib

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

m1 = importlib.import_module("10_1_max_sum_k")
m2 = importlib.import_module("10_2_min_sum_k")
m3 = importlib.import_module("10_3_longest_substring_no_repeat")
m4 = importlib.import_module("10_4_fruits_into_basket")
m5 = importlib.import_module("10_5_subarray_k_distinct")
m6 = importlib.import_module("10_6_max_unique_segment")

if __name__ == "__main__":
    print("Starting automated tests for sliding window algorithms...")

    # 1. Max Sum of K
    assert m1.max_sum_of_k([2, 1, 5, 1, 3, 2], 3) == 9
    assert m1.max_sum_of_k([2, 3, 4, 1, 5], 2) == 7
    assert m1.max_sum_of_k([], 3) == 0
    print("[OK] 10_1_max_sum_k verified.")

    # 2. Min Sum of K
    assert m2.min_sum_of_k([2, 1, 5, 1, 3, 2], 3) == 6
    assert m2.min_sum_of_k([10, 4, 2, 5, 6], 2) == 6
    assert m2.min_sum_of_k([], 2) == 0
    print("[OK] 10_2_min_sum_k verified.")

    # 3. Longest Substring No Repeat
    assert m3.longest_substring_no_repeat("abcabcbb") == 3
    assert m3.longest_substring_no_repeat("bbbbb") == 1
    assert m3.longest_substring_no_repeat("pwwkew") == 3
    assert m3.longest_substring_no_repeat("") == 0
    print("[OK] 10_3_longest_substring_no_repeat verified.")

    # 4. Fruits Into Basket
    assert m4.fruits_into_baskets([1, 2, 1]) == 3
    assert m4.fruits_into_baskets([0, 1, 2, 2]) == 3
    assert m4.fruits_into_baskets([1, 2, 3, 2, 2]) == 4
    assert m4.fruits_into_baskets([]) == 0
    print("[OK] 10_4_fruits_into_basket verified.")

    # 5. Subarray with K Distinct
    assert m5.subarrays_with_k_distinct([1, 2, 1, 2, 3], 2) == 7
    assert m5.subarrays_with_k_distinct([1, 2, 1, 3, 4], 3) == 3
    assert m5.subarrays_with_k_distinct([1, 1, 1, 1], 1) == 10
    print("[OK] 10_5_subarray_k_distinct verified.")

    # 6. Max Unique Segment
    assert m6.max_unique_segment([1, 2, 3, 1, 2, 3]) == 3
    assert m6.max_unique_segment([1, 2, 3, 4, 5]) == 5
    assert m6.max_unique_segment([5, 5, 5, 5]) == 1
    assert m6.max_unique_segment([]) == 0
    print("[OK] 10_6_max_unique_segment verified.")

    print("\nAll sliding window algorithms verified successfully!")
