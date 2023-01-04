"""
Abhinav Sinha
SR. No. - 18750
"""


from HW1_Q10_a import binomial

for i in range(1,21):
    bin_all = [str(binomial(i,k)) for k in range(0, i+1)]
    print(" ".join(bin_all))
