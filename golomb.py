from bitarray import bitarray

def golomb_encoding(numbers, m, chunk_size, lengthBit = 32):
    bits = bitarray()

    chunk = bitarray()
    for i, number in enumerate(numbers):
        if i != 0 and i % chunk_size == 0:
            bits.extend(f"{len(chunk):0{lengthBit}b}")
            bits.extend(chunk)
            chunk.clear()
        chunk.extend(golomb_encode(number, m))
    
    if len(chunk) > 0:
        bits.extend(f"{len(chunk):0{lengthBit}b}")
        bits.extend(chunk)

    return bits

def golomb_encode(number, m):
    "Yields a sequence of bits Golomb-coding the number with divisor 2**bits."
    qq, rr = divmod(number, 2**m)

    for ii in range(qq):
        yield 1
    yield 0

    for ii in range(m-1, -1, -1):    # most significant bit first
        yield 1 if rr & (1 << ii) else 0

def golomb_decoding(bits, m, lengthBit = 32):
    ret = []
    i = 0
    while i < len(bits):
        length = int(bits[i:i+lengthBit].to01(), 2)
        i += lengthBit
        ret.extend(golomb_decode(bits[i:i +length], m))
        i += length
    return ret

def golomb_decode(bits, m):
    numbers = []
    idx = 0

    while idx < len(bits):
        qq = 0
        while idx < len(bits) and bits[idx] == 1:
            qq += 1
            idx += 1

        if idx >= len(bits):
            break

        if bits[idx] == 0:
            idx += 1
            rr = 0
            for ii in range(m-1, -1, -1):
                if idx < len(bits):
                    rr |= (bits[idx] << ii)
                    idx += 1
            numbers.append(qq * (2**m) + rr)
    return numbers

if __name__ == "__main__":
    # Example usage:
    print(bitarray(golomb_encode(9, 2)))  # Output should match the example given for G4(9) in the images
    print(bitarray(golomb_encode(10, 2)))  # Output should match the example given for G4(9) in the images
    print(bitarray(golomb_encode(11, 2)))  # Output should match the example given for G4(9) in the images
    # print(golomb_encoding([9], 2))
    # print(golomb_decoding(bitarray('11001'), 2))
    # Example usage:
    # print(bitarray(golomb_encode(9999, 9999)))  # Output should match the example given for G4(9) in the images
    # print(golomb_encoding([9], 2))
    # print(golomb_decoding(bitarray('11001'), 2))

    print(golomb_encoding([9, 10, 11], 2, 1))
    print(golomb_decoding(bitarray('000000000000010111001000000000000010111010000000000000010111011'), 2))