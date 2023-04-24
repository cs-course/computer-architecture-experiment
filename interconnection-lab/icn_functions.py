def identity(x):
    """恒等函数"""
    return x

def switch(x, n):
    """交换函数：将第 n 位取反"""
    return x ^ (1 << n)

def shuffle_sub(x, k):
    """均匀洗牌函数第k个子函数"""
    mask = (1 << k) - 1
    low_bits = x & mask
    high_bits = x - low_bits
    return high_bits | ((low_bits << 1) & mask) | (low_bits >> (k - 1))

def shuffle_sup(x, k, n):
    """均匀洗牌函数第k个超函数"""
    mask = (1 << (k - 1)) - 1
    mask_sup = (1 << n) - 1
    low_bits = x & mask
    high_bits = x - low_bits
    return low_bits | ((high_bits << 1) & mask_sup) | ((high_bits >> (k - 1)) & (mask_sup - mask))

def _swap_bits(x, i, j):
    # Get the bit values of position i and j
    bit_i = (x >> i) & 1
    bit_j = (x >> j) & 1
    
    # Swap the values by XORing them
    if (bit_i == 1):
        x |= (1 << j)
    else:
        x &= ~(1 << j)
    if (bit_j == 1):
        x |= (1 << i)
    else:
        x &= ~(1 << i)
    
    # Return the result
    return x

def butterfly_sub(x, k):
    """蝶式函数第k(>=0)个子函数"""
    return _swap_bits(x, 0, k)

def butterfly_sup(x, k, n):
    """蝶式函数第k个超函数"""
    return _swap_bits(x, n-k-1, n-1)

# Under construction, to be verified ...

def bit_reverse(x, n):
    """反位序函数"""
    result = 0
    for i in range(n):
        result <<= 1
        result |= (x & 1)
        x >>= 1
    return result

def cyclic_shift(x, n):
    """移数函数：循环左移 n 位"""
    mask = (1 << n) - 1
    high_bits = (x >> (32 - n)) & mask
    return ((x << n) & 0xffffffff) | high_bits

def pm2i(x, n):
    """PM2I函数：将 x 映射到 [0, n-1]"""
    return (x * 31) % n
