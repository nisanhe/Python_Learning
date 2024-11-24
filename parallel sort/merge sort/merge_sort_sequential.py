import random
import time
import psutil

# Function to perform sequential merge sort on an array
def merge_sort(arr):
    # Base case: If the array has one or zero elements, it is already sorted
    if len(arr) <= 1:
        return arr

    # Split the array into two halves
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]

    # Recursively sort each half
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    # Merge the two sorted halves
    return merge(left_sorted, right_sorted)

# Merge function to combine two sorted lists into one
def merge(left, right):
    sorted_list = []
    while left and right:
        if left[0] < right[0]:  # Compare the first elements of each list
            sorted_list.append(left.pop(0))  # Pop the smallest element
        else:
            sorted_list.append(right.pop(0))  # Pop the smallest element
    # Append any remaining elements from both lists
    sorted_list.extend(left)
    sorted_list.extend(right)
    return sorted_list

if __name__ == "__main__":
    size = 200000  # Size of the array to be sorted
    arr = [random.randint(1, 100) for _ in range(size)]  # Generate a random array of integers

    # Variables to track CPU and memory usage
    cpu_usage_sum = 0
    memory_usage_sum = 0
    num_measurements = 0

    # Measure the time it takes to sort the array using sequential merge sort
    start_time = time.time()
    
    # Start the sequential sorting process
    sorted_arr = merge_sort(arr)
    
    # Track CPU and memory usage during sorting
    cpu_usage_sum += psutil.cpu_percent(interval=1)
    memory_usage_sum += psutil.virtual_memory().percent
    num_measurements += 1

    # End time for sorting
    end_time = time.time()

    # Calculate average CPU and memory usage
    avg_cpu_usage = cpu_usage_sum / num_measurements
    avg_memory_usage = memory_usage_sum / num_measurements

    # Print the results
    time_taken = end_time - start_time
    print(f"Time taken to sort the array: {time_taken} seconds")
    print(f"Average CPU usage: {avg_cpu_usage}%")
    print(f"Average Memory usage: {avg_memory_usage}%")
