from performance_comparison import measure_performance
from PIL import Image

def main():

    image = Image.open("pexels-pok-rie-982263.jpg")

    image = image.convert("RGB")

    width, height = image.size
    print("width, height:", width, height)

    data = []
    for x in range(width):
        for y in range(height):
            rgb = image.getpixel((x, y))
            data.extend(rgb)
    
    # print("data:", len(data))

    m = 8

    # # Measure and display performance comparison
    original_encoding_time, parallel_encoding_time = measure_performance(data, m)
    print("\nPerformance comparison for the full dataset:")
    print(f"Original Golomb coding time: {original_encoding_time:.6f} seconds")
    print(f"Parallel Golomb coding time: {parallel_encoding_time:.6f} seconds")


if __name__ == "__main__":
    main()
