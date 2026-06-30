# verify_linear_search.py
import sys
import os

# Add the workspace directory containing python modules to sys.path
sys.path.append(r"d:\study\dsa_with_python\1_Arrays")

import importlib

# Let's import all modules dynamically using importlib
m1 = importlib.import_module("5_1_linear_search")
m2 = importlib.import_module("5_2_kth_character")
m3 = importlib.import_module("5_3_smallest_largest")
m4 = importlib.import_module("5_4_smallest_absolute_difference")
m5 = importlib.import_module("5_5_pairs_divisible_sum")
m6 = importlib.import_module("5_6_valid_pair")

if __name__ == "__main__":
    print("Starting automated tests for searching algorithms...")
    
    # 1. Test 5_1_linear_search
    arr = [10, 20, 30, 40, 50]
    assert m1.linear_search_array(arr, 30) == 2
    assert m1.linear_search_array(arr, 99) == -1
    
    s = "hello python"
    assert m1.linear_search_string(s, 'p') == 6
    assert m1.linear_search_string(s, 'x') == -1
    
    # Sentinel search
    arr_sentinel = [10, 20, 30, 40, 50]
    assert m1.sentinel_linear_search(arr_sentinel, 30) == 2
    assert m1.sentinel_linear_search(arr_sentinel, 50) == 4
    assert m1.sentinel_linear_search(arr_sentinel, 99) == -1
    assert arr_sentinel == [10, 20, 30, 40, 50] # Check it restored correctly
    
    # 2D Array search
    matrix = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]
    assert m1.linear_search_2d(matrix, 4) == (1, 1)
    assert m1.linear_search_2d(matrix, 7) == (-1, -1)
    
    # 2. Test 5_2_kth_character
    test_str = "banana"
    # 'a' at index 1, 3, 5
    assert m2.find_kth_character(test_str, 'a', 1) == 1
    assert m2.find_kth_character(test_str, 'a', 2) == 3
    assert m2.find_kth_character(test_str, 'a', 3) == 5
    assert m2.find_kth_character(test_str, 'a', 4) == -1
    assert m2.find_kth_character(test_str, 'n', 2) == 4
    
    # 3. Test 5_3_smallest_largest
    mix_arr = [12, 3, 5, 7, 19, 1, 15, 2, 8]
    assert m3.find_min_max_standard(mix_arr) == (1, 19)
    assert m3.find_min_max_optimal(mix_arr) == (1, 19)
    
    # 4. Test 5_4_smallest_absolute_difference
    diff_arr = [1, 19, 7, 25, 10, 31]
    # Sorted: 1, 7, 10, 19, 25, 31
    # Adjacent differences: 6, 3, 9, 6, 6 -> Min is 3 (between 7 and 10)
    assert m4.smallest_abs_diff_brute(diff_arr) == 3
    assert m4.smallest_abs_diff_unsorted(diff_arr.copy()) == 3
    assert m4.smallest_abs_diff_sorted([1, 7, 10, 19, 25, 31]) == 3
    
    # 5. Test 5_5_pairs_divisible_sum
    pair_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Divisible by 5:
    # (1,4), (1,9), (2,3), (2,8), (3,7), (4,6), (5,10), (6,9), (7,8)
    # Total = 9 pairs
    assert m5.count_pairs_divisible_brute(pair_arr, 5) == 9
    assert m5.count_pairs_divisible_optimized(pair_arr, 5) == 9
    
    # 6. Test 5_6_valid_pair
    val_arr = [10, 50, 4, 80, 20]
    # target difference 46: 50 - 4 = 46
    assert tuple(sorted(m6.find_valid_pair_unordered(val_arr, 46))) == (4, 50)
    assert tuple(sorted(m6.find_valid_pair_sorted(sorted(val_arr), 46))) == (4, 50)
    assert m6.find_valid_pair_sorted(sorted(val_arr), 99) is None
    
    print("All tests passed! Modules verified successfully!")
