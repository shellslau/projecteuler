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

# for problem 7 - finds the nth prime number
def find_number_prime(n):
    primes = [2]
    i = 1
    while len(primes) < n:
        if is_prime(i, primes):
            primes.append(i)
        i += 2
    return primes[-1]

print(find_number_prime(10001))

# for problem 10
def find_prime_sum(maxNum):
    primes = [2]
    i = 1
    while (primes[-1] < maxNum):
        if is_prime(i, primes):
            primes.append(i)
        i += 2
        print (primes[-1])

    sum = 0
    for prime in primes:
        sum += prime
    return sum - prime[-1]

print ("##########")
print (find_prime_sum(2000000))
