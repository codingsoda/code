import time
from golomb import golomb_encoding, golomb_decoding
from parallel_golomb import parallel_golomb_encode, parallel_golomb_decode


def measure_performance(numbers, k, chunk_size):
    """
    Measures the performance of original and parallel Golomb coding.
    :param numbers: The list of numbers to encode.
    :param m: The divisor for Golomb coding.
    :return: A tuple containing execution times for original and parallel methods.
    """
    # Measure performance of original Golomb encoding
    start_time = time.time()
    single = golomb_encoding(numbers, k, chunk_size)
    original_encoding_time = time.time() - start_time
    
    print("compression ratio: ", len(numbers) * 32 / len(single))

    # print("length of interger bytes: ", len(numbers) * 4)
    # print("length of bytes: ", len(single)/8)
    # print("compression ratio: ", (len(numbers) * 32) / len(single))

    # Measure performance of parallel Golomb encoding
    start_time = time.time()
    multi = parallel_golomb_encode(numbers, k, chunk_size)
    parallel_encoding_time = time.time() - start_time

    assert single == multi
    assert single.tobytes() == multi.tobytes()

    start_time = time.time()
    single = golomb_decoding(single, k)
    original_decoding_time = time.time() - start_time

    assert tuple(single) == tuple(numbers)

    start_time = time.time()
    multi = parallel_golomb_decode(multi, k)
    parallel_decoding_time = time.time() - start_time

    assert tuple(multi) == tuple(numbers)

    return original_encoding_time, original_decoding_time, parallel_encoding_time, parallel_decoding_time

# Example usage:
# numbers = [9, 14, 28, 35] * 100  # Example list of numbers, repeated to get a significant time difference
# m = 4  # Example divisor
# original_time, parallel_time = measure_performance(numbers, m)
# print(f"Original Golomb coding time: {original_time}")
# print(f"Parallel Golomb coding time: {parallel_time}")
