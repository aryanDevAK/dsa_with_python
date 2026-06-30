# 8_4_verify_greedy_applications.py
"""
Automated test suite verifying the correctness of all Module 8 Greedy applications.
Imports modules dynamically to run validation checks.
"""

import sys
import os
import importlib

# Add the parent directory containing the greedy modules to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Dynamically import all the advanced greedy modules
m1 = importlib.import_module("8_1_snake_mongoose")
m2 = importlib.import_module("8_2_maximum_score")
m3 = importlib.import_module("8_3_maximize_disjoint_pair_sum")

if __name__ == "__main__":
    print("Starting automated tests for advanced greedy applications...")

    # 1. Verify 8_1_snake_mongoose
    assert m1.check_election_winner("smssm") == "mongooses"
    assert m1.check_election_winner("s") == "snakes"
    assert m1.check_election_winner("m") == "mongooses"
    assert m1.check_election_winner("sms") == "tie"
    assert m1.check_election_winner("mms") == "mongooses"
    print("[OK] 8_1_snake_mongoose verified.")

    # 2. Verify 8_2_maximum_score
    test_matrix = [
        [10, 20, 30],
        [5, 15, 25],
        [12, 14, 18]
    ]
    assert m2.get_maximum_score_matrix(test_matrix) == 43

    impossible_matrix = [
        [10, 20, 30],
        [1, 2, 3],
        [2, 4, 6]
    ]
    assert m2.get_maximum_score_matrix(impossible_matrix) == -1
    assert m2.get_maximum_score_matrix([[99]]) == 99
    print("[OK] 8_2_maximum_score verified.")

    # 3. Verify 8_3_maximize_disjoint_pair_sum
    assert m3.get_max_disjoint_pair_sum([3, 5, 10, 12, 15], 4) == 35
    assert m3.get_max_disjoint_pair_sum([5, 15, 10, 3], 12) == 33
    assert m3.get_max_disjoint_pair_sum([1, 100], 50) == 0
    assert m3.get_max_disjoint_pair_sum([], 10) == 0
    print("[OK] 8_3_maximize_disjoint_pair_sum verified.")

    print("\nAll advanced greedy applications and helper modules verified successfully!")
