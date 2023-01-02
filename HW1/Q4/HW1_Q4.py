"""
Abhinav Sinha
SR. No. - 18750

For v = 0.99c
Time taken in the rest frame of an observer on Earth is 10.10101 years
Time taken  as perceived by a passenger on board the ship is 1.42492 years
"""

import numpy as np

x = float(input("Enter the distance x in light years: "))
v = float(input("Enter the speed v as a fraction of speed of light c: "))

t1 = x / v
t2 = t1 * np.sqrt(1-v**2)

print("Time taken in the rest frame of an observer on Earth is %.5f years"%t1)
print("Time taken  as perceived by a passenger on board the ship is %.5f years"%t2)
