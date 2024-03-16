import multiprocessing
from multiprocessing import Pool
from golomb import golomb_encode


def parallel_golomb_encode_worker(args):
    """
    Worker function to encode a single number using Golomb coding.
    This is a helper function for multiprocessing to unpack the arguments.
    """
    return golomb_encode(*args)


def parallel_golomb_encode(numbers, m):
    """
    Encodes a list of numbers using Golomb coding in parallel using processes.
    :param numbers: The list of numbers to encode.
    :param m: The divisor for Golomb coding.
    :return: List of Golomb coded strings.
    """
    args = [(n, m) for n in numbers]
    with Pool(processes=multiprocessing.cpu_count()) as pool:
        return pool.map(parallel_golomb_encode_worker, args)

# Example usage:
# numbers = [9, 14, 28, 35]  # Example list of numbers
# m = 4  # Example divisor
# encoded_numbers = parallel_golomb_encode(numbers, m)
# print(encoded_numbers)
