import math
def is_prime(num, primes):
    root = int(math.sqrt(num))
    if num == 0 or num == 1:
        return False
    if num == 2:
        return True
    if num in primes:
        return True
    for i in primes:
        if i > root:
            return True
        elif num%i == 0:
            return False

primes = []
i = 1
while len(primes) < 10001:
    if is_prime(i, primes):
        primes.append(i)
    i += 1

print primes[-1]