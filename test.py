from performance_comparison import measure_performance
import multiprocessing
from PIL import Image

def main(image_path, num_processes, k):
    assert num_processes <= multiprocessing.cpu_count()

    image = Image.open(image_path)

    image = image.convert("RGB")

    width, height = image.size
    print("width, height:", width, height)

    data = []
    for x in range(width):
        for y in range(height):
            rgb = image.getpixel((x, y))
            data.extend(rgb)

    chunk_size = len(data) // num_processes
    print("chunk_size: ", chunk_size)

    # Measure and display performance comparison
    original_encoding_time, original_decoding_time, parallel_encoding_time, parallel_decoding_time = measure_performance(data, k, chunk_size)

    print("Speedup for encoding: ", original_encoding_time / parallel_encoding_time)
    print("Speedup for decoding: ", original_decoding_time / parallel_decoding_time)

    # print("\nPerformance comparison for the full dataset:")
    # print(f"Original Golomb encoding time: {original_encoding_time:.6f} seconds")
    # print(f"Parallel Golomb encoding time: {parallel_encoding_time:.6f} seconds")

    # print("")

    # print(f"Original Golomb decoding time: {original_decoding_time:.6f} seconds")
    # print(f"Parallel Golomb decoding time: {parallel_decoding_time:.6f} seconds")


if __name__ == "__main__":
    num_processes = 2
    while num_processes <= multiprocessing.cpu_count():
        for k in range(10):
            image = "pexels-pok-rie-982263.jpg"
            print("processes: ", num_processes, " M: ", 2 ** k)
            main(image, num_processes, k)
            print("--------------------")
        num_processes *= 2
