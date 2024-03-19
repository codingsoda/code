from bitarray import bitarray

def golomb_encoding(numbers, m):
    bits = bitarray()
    for number in numbers:
        bits.extend(golomb_encode(number, m))
    return bits

def golomb_encode(number, m):
    "Yields a sequence of bits Golomb-coding the number with divisor 2**bits."
    qq, rr = divmod(number, 2**m)

    for ii in range(qq):
        yield 1
    yield 0

    for ii in range(m-1, -1, -1):    # most significant bit first
        yield 1 if rr & (1 << ii) else 0

# Example usage:
# print(bitarray(golomb_encode(9, 2)))  # Output should match the example given for G4(9) in the images
# print(golomb_encoding([9], 2))