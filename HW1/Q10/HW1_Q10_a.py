"""
Abhinav Sinha
SR. No. - 18750
"""


def binomial(n, k):
    if k < 0 or n <= 0:
        return None
    if k == 0:
        return 1

    num = 1
    for i in range(n-k+1,n+1):
        num = num*i

    den = 1
    for i in range(2,k+1):
        den = den*i

    return num // den
