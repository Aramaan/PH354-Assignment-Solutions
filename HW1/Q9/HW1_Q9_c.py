"""
Abhinav Sinha
SR. No. - 18750
"""

from HW1_Q9_b import BperA

def stableA(Z):
    BE = []
    for i in range(Z, 3*Z +1):
        BE.append(BperA(i, Z))

    maxBE = max(BE)
    A = BE.index(maxBE) + Z
    return A, maxBE

if __name__ == "__main__":
    Z = int(input("Enter atomic number Z: "))
    print("Most stable nucleus is for atomic mass %d and Binding energy per nucleon is %.5f MeV"%stableA(Z))