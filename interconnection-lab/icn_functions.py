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

# Under construction, to be verified ...

def butterfly(x, n):
    """蝶式函数"""
    mask_a = (1 << n) - 1
    mask_b = mask_a << n
    a = x & mask_a
    b = x & mask_b
    b >>= n
    c = a ^ b
    return (x & ~mask_b) | (c << n)

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
