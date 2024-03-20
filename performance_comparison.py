import time
from golomb import golomb_encoding, golomb_decoding
from parallel_golomb import parallel_golomb_encode


def measure_performance(numbers, m):
    """
    Measures the performance of original and parallel Golomb coding.
    :param numbers: The list of numbers to encode.
    :param m: The divisor for Golomb coding.
    :return: A tuple containing execution times for original and parallel methods.
    """
    # Measure performance of original Golomb encoding
    start_time = time.time()
    single = golomb_encoding(numbers, m)
    original_encoding_time = time.time() - start_time
    
    print("compression ratio: ", len(numbers) * 32 / len(single))

    # Measure performance of parallel Golomb encoding
    start_time = time.time()
    multi = parallel_golomb_encode(numbers, m)
    parallel_encoding_time = time.time() - start_time

    assert single == multi
    assert single.tobytes() == multi.tobytes()
    assert tuple(golomb_decoding(single, m)) == tuple(numbers)

    return original_encoding_time, parallel_encoding_time

# Example usage:
# numbers = [9, 14, 28, 35] * 100  # Example list of numbers, repeated to get a significant time difference
# m = 4  # Example divisor
# original_time, parallel_time = measure_performance(numbers, m)
# print(f"Original Golomb coding time: {original_time}")
# print(f"Parallel Golomb coding time: {parallel_time}")
