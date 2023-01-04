"""
Abhinav Sinha
SR. No. - 18750

Binding Energy for A=58, Z=28: 493.93561 MeV
"""

def a5(A, Z):
    if A % 2 == 1:
        a5 = 0
    else:
        a5 = (-1) ** (Z % 2) * 12
    return a5


def B(A, Z):
    a1 = 15.67
    a2 = 17.23
    a3 = 0.75
    a4 = 93.2

    return a1 * A - a2 * A ** (2 / 3) - a3 * Z ** 2 / A ** (1 / 3) - a4 * (A - 2 * Z) ** 2 / A + a5(A, Z) / A ** (1 / 2)


if __name__ == "__main__":
    A = float(input("Enter mass number A: "))
    Z = float(input("Enter atomic number Z: "))
    print("Binding Energy: %0.5f MeV" % B(A, Z))
