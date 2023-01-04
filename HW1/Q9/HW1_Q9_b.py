"""
Abhinav Sinha
SR. No. - 18750
"""
from HW1_Q9_a import a5

def BperA(A, Z):
    a1 = 15.67
    a2 = 17.23
    a3 = 0.75
    a4 = 93.2

    return a1 - a2 / A ** (1 / 3) - a3 * Z ** 2 / A ** (4 / 3) - a4 * (A - 2 * Z) ** 2 / A ** 2 + a5(A, Z) / A ** (3 / 2)


if __name__ == "__main__":
    A = float(input("Enter mass number A: "))
    Z = float(input("Enter atomic number Z: "))
    print("Binding Energy per nucleon: %0.5f MeV" % BperA(A, Z))
