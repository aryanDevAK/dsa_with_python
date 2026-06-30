# 7_4_verify_greedy.py
"""
Automated test suite verifying the correctness of all Module 7 Greedy algorithms.
Imports modules dynamically to run validation checks.
"""

import sys
import os
import importlib

# Add the parent directory containing the greedy modules to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Dynamically import all the greedy modules
m1 = importlib.import_module("7_1_chef_and_string")
m2 = importlib.import_module("7_2_chopsticks")
m3 = importlib.import_module("7_3_evacuate_to_moon")

if __name__ == "__main__":
    print("Starting automated tests for greedy algorithms...")

    # 1. Verify 7_1_chef_and_string
    assert m1.max_boy_girl_pairs("xyxxy") == 2
    assert m1.max_boy_girl_pairs("xxxx") == 0
    assert m1.max_boy_girl_pairs("yxyxy") == 2
    print("[OK] 7_1_chef_and_string verified.")

    # 2. Verify 7_2_chopsticks
    assert m2.max_chopstick_pairs([1, 3, 3, 9, 4], 2) == 2
    assert m2.max_chopstick_pairs([5, 8, 11, 20], 3) == 1
    assert m2.max_chopstick_pairs([10], 10) == 0
    assert m2.max_chopstick_pairs([], 5) == 0
    print("[OK] 7_2_chopsticks verified.")

    # 3. Verify 7_3_evacuate_to_moon
    assert m3.max_energy_stored([10, 20, 30], [5, 10], 2) == 30
    assert m3.max_energy_stored([10, 15], [20, 15, 5], 1) == 25
    assert m3.max_energy_stored([100], [50], 3) == 100
    assert m3.max_energy_stored([], [10], 5) == 0
    print("[OK] 7_3_evacuate_to_moon verified.")

    print("\nAll greedy algorithms and helper modules verified successfully!")
