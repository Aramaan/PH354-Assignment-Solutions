"""
Abhinav Sinha
SR. No. - 18750
"""


def gcd(m, n):
    if n == 0:
        return m

    return gcd(n, m % n)


print("GCD of 108 and 192 is %d"%gcd(192,108))
