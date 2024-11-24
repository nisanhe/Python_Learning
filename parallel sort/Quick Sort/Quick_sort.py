import random
import sys
import time
import psutil
from multiprocessing import Pool

# Set recursion limit higher for large arrays
sys.setrecursionlimit(3000)

# Regular Quick Sort with random pivot
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)  # Random pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Parallel Quick Sort
def quick_sort_parallel(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)  # Random pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    with Pool(2) as pool:  # Use 2 parallel processes
        sorted_sublists = pool.map(quick_sort, [left, right])
    left_sorted, right_sorted = sorted_sublists

    return left_sorted + middle + right_sorted

# Measure performance
def measure_performance(sort_function, arr):
    cpu_usage_sum = 0
    memory_usage_sum = 0
    num_measurements = 0

    start_time = time.time()
    sorted_arr = sort_function(arr)
    cpu_usage_sum += psutil.cpu_percent(interval=1)
    memory_usage_sum += psutil.virtual_memory().percent
    num_measurements += 1
    end_time = time.time()

    avg_cpu_usage = cpu_usage_sum / num_measurements
    avg_memory_usage = memory_usage_sum / num_measurements
    time_taken = end_time - start_time
    return time_taken, avg_cpu_usage, avg_memory_usage, sorted_arr

if __name__ == "__main__":
    size = 200000
    arr = [random.randint(1, 100) for _ in range(size)]

    print("Testing Regular Quick Sort...")
    time_taken, avg_cpu, avg_mem, sorted_arr = measure_performance(quick_sort, arr)
    print(f"Time taken: {time_taken:.2f} seconds")
    print(f"Average CPU usage: {avg_cpu:.2f}%")
    print(f"Average Memory usage: {avg_mem:.2f}%\n")

    print("Testing Parallel Quick Sort...")
    time_taken, avg_cpu, avg_mem, sorted_arr = measure_performance(quick_sort_parallel, arr)
    print(f"Time taken: {time_taken:.2f} seconds")
    print(f"Average CPU usage: {avg_cpu:.2f}%")
    print(f"Average Memory usage: {avg_mem:.2f}%")
