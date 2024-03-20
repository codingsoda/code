from performance_comparison import measure_performance
import multiprocessing
from PIL import Image


def main():
    num_processes = multiprocessing.cpu_count()
    print("Number of processes: ", num_processes)

    image = Image.open("pexels-pok-rie-982263.jpg")

    image = image.convert("RGB")

    width, height = image.size
    print("width, height:", width, height)

    data = []
    for x in range(width):
        for y in range(height):
            rgb = image.getpixel((x, y))
            data.extend(rgb)
    
    m = 8

    chunk_size = (len(data) + num_processes - 1) // num_processes

    # Measure and display performance comparison
    original_encoding_time, original_decoding_time, parallel_encoding_time, parallel_decoding_time = measure_performance(data, m, chunk_size)

    print("\nPerformance comparison for the full dataset:")
    print(f"Original Golomb encoding time: {original_encoding_time:.6f} seconds")
    print(f"Parallel Golomb encoding time: {parallel_encoding_time:.6f} seconds")

    print("")

    print(f"Original Golomb decoding time: {original_decoding_time:.6f} seconds")
    print(f"Parallel Golomb decoding time: {parallel_decoding_time:.6f} seconds")


if __name__ == "__main__":
    main()
