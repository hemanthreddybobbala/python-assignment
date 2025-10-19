# Helper function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
numbers = [1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
prime_flags = [is_prime(num) for num in numbers]

print(prime_flags)