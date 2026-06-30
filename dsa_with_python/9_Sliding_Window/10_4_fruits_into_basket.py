# 10_4_fruits_into_basket.py
"""
Variable-size sliding window: Longest subarray with at most 2 distinct elements.
(LeetCode 904 / CodeChef "Put fruits into basket")
"""

def fruits_into_baskets(fruits: list) -> int:
    """
    Finds the maximum number of fruits collectible from a contiguous segment
    using at most 2 baskets (at most 2 distinct fruit types).
    Time Complexity: O(N).  Space Complexity: O(1) (at most 3 keys).
    """
    freq = {}
    left = 0
    max_fruits = 0
    for right in range(len(fruits)):
        fruit = fruits[right]
        freq[fruit] = freq.get(fruit, 0) + 1
        # Shrink while more than 2 distinct fruits
        while len(freq) > 2:
            left_fruit = fruits[left]
            freq[left_fruit] -= 1
            if freq[left_fruit] == 0:
                del freq[left_fruit]
            left += 1
        max_fruits = max(max_fruits, right - left + 1)
    return max_fruits

if __name__ == "__main__":
    assert fruits_into_baskets([1, 2, 1]) == 3
    assert fruits_into_baskets([0, 1, 2, 2]) == 3
    assert fruits_into_baskets([1, 2, 3, 2, 2]) == 4
    assert fruits_into_baskets([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]) == 5
    assert fruits_into_baskets([]) == 0
    print("10_4_fruits_into_basket.py verified successfully!")
