def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

primes = [x for x in range(2, 100) if is_prime(x)]
pairs = [(p, q) for p in primes for q in primes if is_prime(p + q)]
print(pairs)
