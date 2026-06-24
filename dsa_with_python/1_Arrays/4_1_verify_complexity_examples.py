# verify_complexity_examples.py
import time
import sys
import collections

# 1. Binary Search
def logarithmic_time_example(sorted_arr: list, target: int) -> int:
    low, high = 0, len(sorted_arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_arr[mid] == target:
            return mid
        elif sorted_arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# 2. Primality test (O(sqrt(N)))
def check_prime(n: int) -> bool:
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

# 3. Harmonic loop demonstration
def harmonic_loop(n: int) -> int:
    count = 0
    for i in range(1, n):
        for j in range(i, n, i):
            count += 1
    return count

# 4. Recursion with Memoization
def fib_naive(n: int) -> int:
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)

def fib_memoized(n: int, memo: dict = None) -> int:
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memoized(n - 1, memo) + fib_memoized(n - 2, memo)
    return memo[n]

# 5. Tail Recursion emulation using a Trampoline (Generator-based)
def trampoline(f):
    def wrapped(*args, **kwargs):
        g = f(*args, **kwargs)
        while isinstance(g, tuple) and len(g) > 0 and callable(g[0]):
            g = g[0](*g[1], **g[2])
        return g
    return wrapped

# Let's write recursive factorial that runs in O(N) time but O(1) space with trampoline
def factorial_trampolined(n: int):
    def step(curr_n, acc):
        if curr_n <= 1:
            return acc
        return step, (curr_n - 1, acc * curr_n), {}
    
    # We can run this with the trampoline
    return trampoline(step)(n, 1)

# 6. Space Complexity: In-place vs Out-of-place
def reverse_in_place(arr: list) -> None:
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left, right = left + 1, right - 1

def reverse_out_of_place(arr: list) -> list:
    new_arr = []
    for i in range(len(arr) - 1, -1, -1):
        new_arr.append(arr[i])
    return new_arr

# 7. Time-Space Tradeoffs
def has_duplicate_bad(arr: list) -> bool:
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False

def has_duplicate_good(arr: list) -> bool:
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False

# 8. Real-world Caching (Spatial Locality) demonstration
def benchmark_spatial_locality():
    size = 1000
    matrix = [[1] * size for _ in range(size)]
    
    # Row-major traversal (fast due to spatial locality)
    start = time.perf_counter()
    row_sum = 0
    for r in range(size):
        for c in range(size):
            row_sum += matrix[r][c]
    row_time = time.perf_counter() - start
    
    # Column-major traversal (slower due to cache line jumps)
    start = time.perf_counter()
    col_sum = 0
    for c in range(size):
        for r in range(size):
            col_sum += matrix[r][c]
    col_time = time.perf_counter() - start
    
    return row_time, col_time

# 9. String Concatenation Trap
def benchmark_string_concat():
    iterations = 20000
    
    # Naive += (O(N^2))
    start = time.perf_counter()
    s = ""
    for i in range(iterations):
        s += "a"
    naive_time = time.perf_counter() - start
    
    # Optimized .join() (O(N))
    start = time.perf_counter()
    lst = []
    for i in range(iterations):
        lst.append("a")
    res = "".join(lst)
    join_time = time.perf_counter() - start
    
    return naive_time, join_time

# 10. Generator for O(1) space data streaming
def generate_squares(n: int):
    for i in range(n):
        yield i * i

if __name__ == "__main__":
    print("Verifying correctness of algorithms...")
    # Assertions
    assert logarithmic_time_example([1, 2, 3, 4, 5], 3) == 2
    assert check_prime(17) is True
    assert check_prime(15) is False
    assert harmonic_loop(10) > 0
    assert fib_memoized(10) == 55
    assert factorial_trampolined(5) == 120
    
    arr1 = [1, 2, 3]
    reverse_in_place(arr1)
    assert arr1 == [3, 2, 1]
    assert reverse_out_of_place([1, 2, 3]) == [3, 2, 1]
    
    assert has_duplicate_bad([1, 2, 3, 2]) is True
    assert has_duplicate_good([1, 2, 3, 2]) is True
    assert has_duplicate_good([1, 2, 3]) is False
    
    print("All functional checks passed! Running benchmarks...")
    row_t, col_t = benchmark_spatial_locality()
    print(f"Spatial Locality: Row-major={row_t:.5f}s, Column-major={col_t:.5f}s (Ratio: {col_t/row_t:.2f}x)")
    
    naive_str_t, join_str_t = benchmark_string_concat()
    print(f"String Concatenation: Naive +=={naive_str_t:.5f}s, Join={join_str_t:.5f}s (Ratio: {naive_str_t/join_str_t:.2f}x)")
    
    squares = generate_squares(100)
    assert next(squares) == 0
    assert next(squares) == 1
    print("Generators verified.")
    print("Verification script runs successfully!")
