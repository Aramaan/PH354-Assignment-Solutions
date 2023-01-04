"""
Abhinav Sinha
SR. No. - 18750
"""

from HW1_Q10_a import binomial

# part (a)
print("Probability of getting heads 60 times out of 100 tosses is %.5f"%(binomial(100, 60)/2**100))

#part (b)
list_coeff = [binomial(100,k) for k in range(60,101)]
print("Probability of getting heads 60 or more times in 100 tosses is %.5f"%(sum(list_coeff)/2**100))
