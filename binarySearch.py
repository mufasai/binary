import time
import matplotlib.pyplot as plt
import numpy as np

# Recursive Binary Search
def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)

# Iterative Binary Search
def binary_search_iterative(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Generate database with 10,000 entries
def generate_database():
    sorted_data = np.sort(np.random.randint(100000, 999999, 5000))  # 5,000 sorted NIMs
    unsorted_data = np.random.randint(100000, 999999, 5000)  # 5,000 unsorted NIMs
    return np.concatenate((sorted_data, unsorted_data))

# Measure execution time
def measure_execution_time(function, arr, target, is_recursive):
    start_time = time.time()
    if is_recursive:
        function(arr, target, 0, len(arr) - 1)
    else:
        function(arr, target)
    return time.time() - start_time

# Main analysis
def analyze_performance(database, sizes):
    recursive_sorted_times = []
    recursive_unsorted_times = []
    iterative_sorted_times = []
    iterative_unsorted_times = []

    for size in sizes:
        data_sorted = database[:size // 2]  # First half (sorted)
        data_unsorted = database[size // 2:size]  # Second half (unsorted)
        target = data_sorted[len(data_sorted) // 2]  # Target from sorted portion

        # Recursive Binary Search
        recursive_sorted_times.append(
            measure_execution_time(binary_search_recursive, data_sorted, target, True)
        )
        recursive_unsorted_times.append(
            measure_execution_time(binary_search_recursive, data_unsorted, target, True)
        )

        # Iterative Binary Search
        iterative_sorted_times.append(
            measure_execution_time(binary_search_iterative, data_sorted, target, False)
        )
        iterative_unsorted_times.append(
            measure_execution_time(binary_search_iterative, data_unsorted, target, False)
        )

    return (recursive_sorted_times, recursive_unsorted_times, iterative_sorted_times, iterative_unsorted_times)

# Plot performance
def plot_performance(sizes, recursive_sorted, recursive_unsorted, iterative_sorted, iterative_unsorted):
    plt.figure(figsize=(10, 6))

    plt.plot(sizes, recursive_sorted, label='Recursive Sorted', marker='o')
    plt.plot(sizes, recursive_unsorted, label='Recursive Unsorted', linestyle='--', marker='o')
    plt.plot(sizes, iterative_sorted, label='Iterative Sorted', marker='s')
    plt.plot(sizes, iterative_unsorted, label='Iterative Unsorted', linestyle='--', marker='s')

    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Size of Dataset')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Performance Comparison of Recursive and Iterative Binary Search')
    plt.legend()
    plt.grid(which='both', linestyle='--', linewidth=0.5)
    plt.show()

# Execute the analysis
if __name__ == "__main__":
    database = generate_database()
    sizes = [100, 500, 1000, 5000, 10000]
    results = analyze_performance(database, sizes)
    plot_performance(sizes, *results)
