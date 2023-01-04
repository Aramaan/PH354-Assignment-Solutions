"""
Abhinav Sinha
SR. No. - 18750
"""

from HW1_Q9_c import stableA

print("Z    |   A   |   Binding Energy per nucleon")
maxZ = 0
maxA = 0
maxBE = 0
for i in range(1,101):
    A, BE = stableA(i)
    print("%d   |   %d  | %.5f"%(i,A,BE))
    if maxBE < BE:
        maxBE = BE
        maxZ = i
        maxA = A

print("Maximum binding energy per nucleon occurs for atomic number Z = %d, atomic mass A = %d with  per nucleon Binding energy = %.5f"%(maxZ, maxA, maxBE))


