# 6_4_nge.py
"""
Next Greater Element (NGE) Implementations in Python.
Includes the brute-force O(N^2) approach and the optimal O(N) monotonic stack approach.
"""

def next_greater_element_brute(arr: list) -> list:
    """
    Finds the next greater element for each index using two nested loops.
    Time Complexity: O(N^2)
    Space Complexity: O(1) auxiliary
    """
    n = len(arr)
    result = [-1] * n
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                result[i] = arr[j]
                break
    return result

def next_greater_element_stack(arr: list) -> list:
    """
    Finds the next greater element for each index using a monotonic stack (right-to-left traversal).
    Time Complexity: O(N)
    Space Complexity: O(N) auxiliary
    """
    n = len(arr)
    result = [-1] * n
    stack = []
    
    # Traverse from right to left
    for i in range(n - 1, -1, -1):
        # Pop elements that are smaller than or equal to current element
        while stack and stack[-1] <= arr[i]:
            stack.pop()
            
        # Top of the stack is the NGE (if stack is not empty)
        if stack:
            result[i] = stack[-1]
            
        # Push the current element onto the stack
        stack.append(arr[i])
        
    return result

if __name__ == "__main__":
    # Self-testing assertions
    test_arr = [4, 5, 2, 25]
    expected = [5, 25, 25, -1]
    assert next_greater_element_brute(test_arr) == expected
    assert next_greater_element_stack(test_arr) == expected
    
    test_arr_2 = [13, 7, 6, 12]
    expected_2 = [-1, 12, 12, -1]
    assert next_greater_element_brute(test_arr_2) == expected_2
    assert next_greater_element_stack(test_arr_2) == expected_2
    
    # Decreasing elements test
    assert next_greater_element_stack([5, 4, 3, 2, 1]) == [-1, -1, -1, -1, -1]
    
    # Empty list and single element
    assert next_greater_element_stack([]) == []
    assert next_greater_element_stack([42]) == [-1]
    
    print("6_4_nge.py verified successfully!")
