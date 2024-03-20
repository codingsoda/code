from performance_comparison import measure_performance
import multiprocessing

def main():
    num_processes = multiprocessing.cpu_count()
    print("Number of processes: ", num_processes)

    # Define a much larger list of numbers to encode and the divisor m
    numbers = list(range(100000))  # A larger list with 100,000 numbers
    m = 4
    
    chunk_size = (len(numbers) + num_processes - 1) // num_processes

    # Measure and display performance comparison
    original_encoding_time, original_decoding_time, parallel_encoding_time, parallel_decoding_time = measure_performance(numbers, m, chunk_size)
    print("\nPerformance comparison for the full dataset:")
    print(f"Original Golomb encoding time: {original_encoding_time:.6f} seconds")
    print(f"Parallel Golomb encoding time: {parallel_encoding_time:.6f} seconds")

    print("")

    print(f"Original Golomb decoding time: {original_decoding_time:.6f} seconds")
    print(f"Parallel Golomb decoding time: {parallel_decoding_time:.6f} seconds")


if __name__ == "__main__":
    main()
