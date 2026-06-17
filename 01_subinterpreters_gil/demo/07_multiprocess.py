import math
import sys
import time
from concurrent.futures import ProcessPoolExecutor

NUMBERS = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
] * 10


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    start = time.time()

    workers = int(sys.argv[1]) if len(sys.argv) > 1 else 4

    with ProcessPoolExecutor(max_workers=workers) as executor:
        executor.map(is_prime, NUMBERS)

    print(f"{workers} workers took {time.time() - start:.2f} seconds")
