

def generate_primes(n):
    primes = []
    num = 2
    while num <= n:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primes.append(num)
        num += 1
    return primes

def primeFactorization(n):
    primes = generate_primes(n)

    factors = {}

    for p in primes:
        counter = 0
        while n >= p and n % p == 0:
            n /= p
            counter += 1

        if counter > 0:
            factors[p] = counter

    return factors


print(primeFactorization(32499))