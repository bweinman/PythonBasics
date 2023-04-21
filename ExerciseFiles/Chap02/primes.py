#!/usr/bin/env python3
# primes.py by Bill Weinman [https://bw.org]
# as of 2023-03-21

def isprime(n):
    if n <= 1:
        return False
    for x in range(2, n // 2):
        if n % x == 0:
            return False
    else:
        return True

print(isprime(5))
