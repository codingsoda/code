import multiprocessing
from concurrent.futures import ProcessPoolExecutor
from golomb import golomb_encoding
from bitarray import bitarray

def parallel_golomb_encoding_worker(args):
    """
    Worker function to encode a single number using Golomb coding.
    This is a helper function for multiprocessing to unpack the arguments.
    """
    return golomb_encoding(*args)

def parallel_golomb_encode(numbers, m):
    """
    Encodes a list of numbers using Golomb coding in parallel using multiprocessing.
    :param numbers: The list of numbers to encode.
    :param m: The divisor for Golomb coding.
    :return: List of Golomb coded strings.
    """

    num_processes = multiprocessing.cpu_count()
    print("Number of processes: ", num_processes)
    
    chunk_size = (len(numbers) + num_processes - 1) // num_processes
    args = [(numbers[i:i+chunk_size], m) for i in range(0, len(numbers), chunk_size)]
    with ProcessPoolExecutor(max_workers=num_processes) as executor:
        ret = bitarray()
        for result in executor.map(parallel_golomb_encoding_worker, args):
            ret.extend(result)
        return ret

if __name__ == "__main__":
    numbers = [9, 9]
    m = 2
    print(golomb_encoding(numbers, m))
    print(parallel_golomb_encode(numbers, m))
