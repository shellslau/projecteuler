import math

def is_prime(num):
    root = int(math.sqrt(num))
    if num == 0 or num == 1:
        return False
    for i in range (2, root + 1):
        if num%i == 0:
            return False
    return True

def factors(num):
    factors = []

    i = 2
    while not is_prime(num):
        if is_prime(i):
            while (num%i == 0) and (num/i != 1):
                factors.append(i)
                num = num / i
        i += 1
    factors.append(num)
    return factors



facts = []
for i in range(2,21):
    temp  = facts
    facti = factors(i)
    for b in temp:
        if b in facti:
            facti.remove(b)
    for a in facti:
        facts.append(a)

total = 1
for i in facts:
    total = total * i

print total
