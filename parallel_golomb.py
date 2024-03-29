import multiprocessing
from concurrent.futures import ProcessPoolExecutor
from golomb import golomb_encoding, golomb_decode, get_block
from bitarray import bitarray

def parallel_golomb_encoding_worker(args):
    """
    Worker function to encode a single number using Golomb coding.
    This is a helper function for multiprocessing to unpack the arguments.
    """
    return golomb_encoding(*args)

def parallel_golomb_decoding_worker(args):
    l, k = args
    ret = []
    for ll in l:
        ret.extend(golomb_decode(ll, k))
    return ret

def parallel_golomb_encode(numbers, k, chunk_size):
    """
    Encodes a list of numbers using Golomb coding in parallel using multiprocessing.
    :param numbers: The list of numbers to encode.
    :param m: The divisor for Golomb coding.
    :return: List of Golomb coded strings.
    """
    
    args = [(numbers[i:i+chunk_size], k, chunk_size) for i in range(0, len(numbers), chunk_size)]
    with ProcessPoolExecutor(max_workers = multiprocessing.cpu_count()) as executor:
        ret = bitarray()
        for result in executor.map(parallel_golomb_encoding_worker, args):
            ret.extend(result)
        return ret

def parallel_golomb_decode(bits, k):
    numbers = []
    i = 0
    while i < len(bits):
        block, i = get_block(bits, i)
        numbers.append(block)

    # print("len(numbers)", len(numbers))
    num_processes = multiprocessing.cpu_count()
    chunk_size = (len(numbers) + num_processes - 1) // num_processes
    # print("chunk_size: ", chunk_size)

    args = [(numbers[i:i+chunk_size], k) for i in range(0, len(numbers), chunk_size)]
    with ProcessPoolExecutor(max_workers = multiprocessing.cpu_count()) as executor:
        ret = []
        for result in executor.map(parallel_golomb_decoding_worker, args):
            ret.extend(result)
        return ret

if __name__ == "__main__":
    numbers = [9, 10, 11]
    # 000000000000010111001000000000000010111010000000000000010111011
    # 000000000001010100000000000001011100100000000000101010000000000000101110100000000000010101000000000000010111011
    k = 2
    print(golomb_encoding(numbers, k, 1))
    print(parallel_golomb_encode(numbers, k, 1))
    print(parallel_golomb_decode(parallel_golomb_encode(numbers, k, 1), k))
