from golomb import golomb_encode
from parallel_golomb import parallel_golomb_encode
from performance_comparison import measure_performance


def main():
    # Define a much larger list of numbers to encode and the divisor m
    numbers = list(range(80000))  # A larger list with 100,000 numbers
    m = 4

    # Measure and display performance comparison
    original_time, parallel_time = measure_performance(numbers, m)
    print("\nPerformance comparison for the full dataset:")
    print(f"Original Golomb coding time: {original_time:.6f} seconds")
    print(f"Parallel Golomb coding time: {parallel_time:.6f} seconds")


if __name__ == "__main__":
    main()
