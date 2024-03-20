from golomb import golomb_encode
from parallel_golomb import parallel_golomb_encode
from performance_comparison import measure_performance


def main():
    # Define a list of numbers to encode and the divisor m
    numbers = [9, 14, 28, 35] * 100  # Larger list to showcase performance differences
    k = 4

    # Perform and display original Golomb coding
    print("Original Golomb coding results:")
    for n in numbers[:4]:  # Only display the first few to keep the output concise
        print(f"The number {n} is encoded as {golomb_encode(n, k)}")

    # Perform and display parallel Golomb coding
    print("\nParallel Golomb coding results:")
    encoded_numbers = parallel_golomb_encode(numbers[:4], k)
    for n, code in zip(numbers[:4], encoded_numbers):
        print(f"The number {n} is encoded as {code}")

    # Measure and display performance comparison
    original_time, parallel_time = measure_performance(numbers, k)
    print("\nPerformance comparison:")
    print(f"Original Golomb coding time: {original_time:.6f} seconds")
    print(f"Parallel Golomb coding time: {parallel_time:.6f} seconds")


if __name__ == "__main__":
    main()
