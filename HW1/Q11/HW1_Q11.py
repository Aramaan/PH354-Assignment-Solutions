"""
Abhinav Sinha
SR. No. - 18750
"""

import numpy as np

list_primes = np.array([2, ])
for n in range(3, 10001):
    prime = 1
    for x in list_primes[list_primes <= np.sqrt(n)]:
        if n % x == 0:
            prime = 0
            break
    if prime == 1:
        list_primes = np.append(list_primes, n)

print(list(list_primes))