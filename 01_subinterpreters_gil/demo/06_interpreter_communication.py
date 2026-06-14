from concurrent import interpreters


def worker(queue):
    import math

    numbers = [112272535095293, 112582705942171, 115280095190773]

    for n in numbers:
        sqrt_n = int(math.floor(math.sqrt(n)))
        result = n > 1 and all(n % i != 0 for i in range(2, sqrt_n + 1))
        queue.put((n, result))


queue = interpreters.create_queue()
interpreter = interpreters.create()

t = interpreter.call_in_thread(worker, queue)

for _ in range(3):
    number, is_prime = queue.get()
    print(f"{number}: {'prime' if is_prime else 'not prime'}")

t.join()
interpreter.close()