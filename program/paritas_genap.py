def even_parity(x):
    parity = 0
    while x:
        parity ^= x & 1
        x >>= 1
    return parity
