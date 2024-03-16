import time
from golomb import golomb_encode
from parallel_golomb import parallel_golomb_encode


def measure_performance(numbers, m):
    """
    Measures the performance of original and parallel Golomb coding.
    :param numbers: The list of numbers to encode.
    :param m: The divisor for Golomb coding.
    :return: A tuple containing execution times for original and parallel methods.
    """
    # Measure performance of original Golomb coding
    start_time = time.time()
    for n in numbers:
        golomb_encode(n, m)
    original_time = time.time() - start_time

    # Measure performance of parallel Golomb coding
    start_time = time.time()
    parallel_golomb_encode(numbers, m)
    parallel_time = time.time() - start_time

    return original_time, parallel_time

# Example usage:
# numbers = [9, 14, 28, 35] * 100  # Example list of numbers, repeated to get a significant time difference
# m = 4  # Example divisor
# original_time, parallel_time = measure_performance(numbers, m)
# print(f"Original Golomb coding time: {original_time}")
# print(f"Parallel Golomb coding time: {parallel_time}")
