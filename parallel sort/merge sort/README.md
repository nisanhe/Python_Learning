# Merge Sort Performance Comparison: Parallel vs. Sequential

## Overview

This project compares the performance of **Merge Sort** implemented in two ways:
- **Sequential Merge Sort**: The traditional, single-threaded approach.
- **Parallel Merge Sort**: A parallelized version that utilizes multiple CPU cores to speed up the sorting process.

The performance of both algorithms is evaluated by measuring the **execution time**, **CPU usage**, and **memory consumption** while sorting large random arrays.

## Features

- **Merge Sort Algorithm**: A divide-and-conquer algorithm that splits the input array into halves recursively, then merges the sorted subarrays.
  
- **Parallel Merge Sort**: This version of merge sort improves performance by utilizing multiple CPU cores. The array is still split into halves, but the sorting of these halves is done in parallel using the `multiprocessing.Pool` method. This is especially beneficial on multi-core systems.

- **Resource Monitoring**: The `psutil` library is used to track and report CPU usage and memory consumption during the sorting process.

## Requirements

Before running the scripts, ensure you have the following dependencies installed:

- `random` (Standard Python library)
- `time` (Standard Python library)
- `psutil` (For monitoring system resources)
- `multiprocessing` (Standard Python library)

To install `psutil`, run:

```bash
pip install psutil
```

## Usage
To test the sorting methods, follow these steps:
1. Clone or download the repository containing the scripts.
2. Choose the sorting method you wish to test by running either:
* merge_sort_parallel.py for parallel sorting.
* merge_sort_sequential.py for sequential sorting.
Important:
3. Parallel Merge Sort utilizes multiple CPU cores to speed up the sorting process, whereas Sequential Merge Sort runs on a single core.
* The script will generate a random array of integers and begin sorting it. During the sorting process, it will record and display the time taken, as well as track CPU and memory usage.

## Example Output
Time taken to sort the array: 1.234 seconds
Average CPU usage: 75%
Average Memory usage: 60%

## Explanation
### Sequential Merge Sort
- Time Complexity: O(n log n)
- Space Complexity: O(n)

## Performance Metrics
- Time Taken: Measures the total time to sort the array.
- CPU Usage: Average CPU usage during sorting.
- Memory Usage: Average memory usage during execution.

## Conclusion
- Parallel Merge Sort performs better on multi-core machines.
- Sequential Merge Sort is easier and works efficiently for smaller arrays.

