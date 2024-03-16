import math


def unary_encode(q):
    """
    Encodes an integer using unary coding.
    :param q: The quotient to encode.
    :return: Unary coded string.
    """
    return '1' * q + '0'


def binary_encode(r, k):
    """
    Encodes the remainder using binary encoding.
    :param r: The remainder to encode.
    :param k: The number of bits to use for encoding.
    :return: Binary coded string.
    """
    return format(r, f'0{k}b')


def golomb_encode(n, m):
    """
    Encodes a number using Golomb coding.
    :param n: The number to encode.
    :param m: The divisor for Golomb coding.
    :return: Golomb coded string.
    """
    q = n // m
    r = n % m
    k = int(math.ceil(math.log2(m)))
    c = (2 ** k) - m

    if r < c:
        return unary_encode(q) + binary_encode(r, k - 1)
    else:
        return unary_encode(q) + binary_encode(r + c, k)

# Example usage:
# print(golomb_encode(9, 4))  # Output should match the example given for G4(9) in the images
