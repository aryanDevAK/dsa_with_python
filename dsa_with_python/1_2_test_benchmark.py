import sys
import array
import time

try:
    import numpy as np
except ImportError:
    np = None

def run_benchmarks():
    size = 1_000_000
    print(f"Creating arrays of size: {size:,}\n")

    # 1. Python List
    start_time = time.time()
    py_list = list(range(size))
    list_time = time.time() - start_time
    
    # Calculate list memory footprint (references array size + size of individual integer objects)
    list_ref_size = sys.getsizeof(py_list)
    # Estimate total size including standard integer object overhead (28 bytes per int in 64-bit Python)
    list_total_size = list_ref_size + sum(sys.getsizeof(x) for x in py_list)

    # 2. Python Array Module
    start_time = time.time()
    py_array = array.array('i', range(size))
    array_time = time.time() - start_time
    array_total_size = sys.getsizeof(py_array)

    # 3. NumPy Array (if available)
    if np is not None:
        start_time = time.time()
        np_arr = np.arange(size, dtype=np.int32)
        np_time = time.time() - start_time
        np_total_size = np_arr.nbytes
    else:
        np_time = "N/A"
        np_total_size = "N/A"

    # Display Results
    print(f"{'Structure':<15} | {'Creation Time (s)':<18} | {'Estimated Memory Size':<25}")
    print("-" * 65)
    print(f"{'Python List':<15} | {list_time:<18.5f} | {list_total_size / (1024*1024):.2f} MB")
    print(f"{'Array Module':<15} | {array_time:<18.5f} | {array_total_size / (1024*1024):.2f} MB")
    if np is not None:
        print(f"{'NumPy Array':<15} | {np_time:<18.5f} | {np_total_size / (1024*1024):.2f} MB")
    else:
        print(f"{'NumPy Array':<15} | {'Not Installed':<18} | {'N/A':<25}")
        
    print("\n[Analysis]")
    print("* The standard Python list has significant memory overhead because it allocates pointers and individual PyObject structures on the heap.")
    print("* The typed array module stores values contiguously in C-style memory, reducing memory overhead.")

if __name__ == "__main__":
    run_benchmarks()
