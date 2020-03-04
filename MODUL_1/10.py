from math import sqrt as akar
def selesaikanABC(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    D = b**2 - 4*a*c
    if (D < 0):
        print("Determinannya negatif. Persamaan tidak mempunyai akar real.")
    else:
        x1 = (-b + akar(D))/(2*a)
        x2 = (-b - akar(D))/(2*a)
        hasil = (x1,x2)
        return hasil
