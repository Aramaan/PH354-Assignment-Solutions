"""
Abhinav Sinha
SR. No. - 18750
"""


def catalan(n):
    if n < 0:
        return None
    if n == 0:
        return 1

    return (4*n-2)*catalan(n-1)//(n+1)


print("100th Catalan number: %d"%catalan(100))
