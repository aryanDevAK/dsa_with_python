# 11_15_verify_prefix_suffix.py
"""
Automated test suite verifying all Module 11 Prefix and Suffix Sum implementations.
"""

import sys
import os
import importlib

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

m1 = importlib.import_module("11_1_creating_prefix_array")
m2 = importlib.import_module("11_2_optimization_using_prefix_array")
m3 = importlib.import_module("11_3_counting_pretty_numbers")
m4 = importlib.import_module("11_4_little_chef_and_sums")
m5 = importlib.import_module("11_5_suffix_arrays")
m6 = importlib.import_module("11_6_optimal_denomination")
m7 = importlib.import_module("11_7_good_subarrays")
m8 = importlib.import_module("11_8_good_subarrays_2")
m9 = importlib.import_module("11_9_rectangular_queries")
m11 = importlib.import_module("11_11_binod")
m12 = importlib.import_module("11_12_mystical_numbers")
m13 = importlib.import_module("11_13_segmentation_fault")
m14 = importlib.import_module("11_14_triplets_min")

if __name__ == "__main__":
    print("Starting automated tests for Prefix and Suffix Sum algorithms...\n")

    # 1. Creating Prefix Array
    assert m1.create_prefix_array([3, 1, 4, 1, 5]) == [3, 4, 8, 9, 14]
    print("[OK] 11_1_creating_prefix_array verified.")

    # 2. Optimization Using Prefix Array
    rsq = m2.RangeSumQuery([3, 1, 4, 1, 5])
    assert rsq.get_sum(1, 3) == 6
    assert rsq.get_sum(0, 4) == 14
    print("[OK] 11_2_optimization_using_prefix_array verified.")

    # 3. Counting Pretty Numbers
    counter = m3.PrettyNumberCounter()
    assert counter.count_pretty(1, 10) == 3
    assert counter.count_pretty(11, 33) == 8
    print("[OK] 11_3_counting_pretty_numbers verified.")

    # 4. Little Chef and Sums
    assert m4.find_min_checksum_index([2, 1, 3]) == 2
    assert m4.find_min_checksum_index([1, 1, 1]) == 1
    print("[OK] 11_4_little_chef_and_sums verified.")

    # 5. Suffix Arrays (Suffix Sums)
    assert m5.create_suffix_array([3, 1, 4, 1, 5]) == [14, 11, 10, 6, 5]
    print("[OK] 11_5_suffix_arrays verified.")

    # 6. Optimal Denomination
    assert m6.get_optimal_denomination([2, 2, 4]) == 3
    assert m6.get_optimal_denomination([3, 5, 9]) == 5
    print("[OK] 11_6_optimal_denomination verified.")

    # 7. Good Subarrays (Medium)
    assert m7.count_good_subarrays([1, 1, 1], 2) == 2
    assert m7.count_good_subarrays([1, 2, 3], 3) == 2
    print("[OK] 11_7_good_subarrays verified.")

    # 8. Good Subarrays 2
    assert m8.count_subarrays_divisible_by_n([3, 1, 2]) == 3
    print("[OK] 11_8_good_subarrays_2 verified.")

    # 9. Rectangular Queries
    matrix = [
        [1, 2, 3],
        [3, 2, 1],
        [5, 6, 3]
    ]
    rq = m9.RectangularQueries(matrix)
    assert rq.query_distinct(1, 1, 2, 2) == 3
    assert rq.query_distinct(2, 2, 3, 3) == 4
    print("[OK] 11_9_rectangular_queries verified.")

    # 11. Binod
    arr = [2, 3, 4, 5]
    binod_counter = m11.BinodBitCounter(arr)
    assert binod_counter.get_set_bits_count(0, 3, 0) == 2
    assert binod_counter.get_set_bits_count(1, 3, 2) == 2
    print("[OK] 11_11_binod verified.")

    # 12. Mystical Numbers
    mystic_solver = m12.MysticalNumbersSolver([2, 3, 4, 5])
    assert mystic_solver.query(0, 3, 5) == 2
    print("[OK] 11_12_mystical_numbers verified.")

    # 13. Segmentation Fault
    assert m13.find_thief_suspects(3, [(2, 3), (3, 3), (1, 2)]) == [2, 3]
    print("[OK] 11_13_segmentation_fault verified.")

    # 14. Triplets Min
    triplets_solver = m14.TripletsMinSolver([1, 2, 3, 4])
    assert triplets_solver.query(1) == 1
    assert triplets_solver.query(4) == 2
    print("[OK] 11_14_triplets_min verified.")

    print("\nAll prefix and suffix sum algorithms verified successfully!")
