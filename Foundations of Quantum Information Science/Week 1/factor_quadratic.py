#!/usr/bin/env python3
"""factor_quadratic.py"""
import numpy as np 

# factor the quadratic 
def factor_quadratic(J: int, K: int, L: int) -> None:
    print("Given the quadratic:", end=" ")
    print(f"{J}x^2 + {K}x + {L}")

    for a in range (1,J+1):
       if J % abs(a) == 0:
            c: int = J // a
            for b in range (1,(L+1)):
                if L % abs(b) ==0:
                    d: int = L // b
                    if a * d + b * c == K:
                        print("The factors are:", end=" ")
                        print(f"({a}x+{b})({c}x+{d})")

def main() -> None:
    factor_quadratic(115425, 3254121, 379020)

if __name__ == "__main__":
    main()

#GCD work below

print(min(np.gcd(115425, 3254121),np.gcd(115425, 379020),np.gcd(379020, 3254121)))

k=min(np.gcd(115425, 3254121),np.gcd(115425, 379020),np.gcd(379020, 3254121))

def f(x):
    return 115425*x**2+3254121*x+379020

def g(x):
    return k*((115425/k)*x**2+(3254121/k)*x+(379020/k))

#g(x)=k*(f(x)/k)=f(x) GCD factored from f(x)

#factor the quadratic with GCD and one output

def factor_quadratic2(J: int, K: int, L: int) -> None:
    m=min(np.gcd(J, K),np.gcd(K, L),np.gcd(J, L))
    print("Given the quadratic with factored GCD:", end=" ")
    print(f"{m}({J/m}x^2 + {K/m}x + {L/m})")

    for a in range (1,J+1):
       if J % a == 0:
            c: int = J // a
            for b in range (1,(L+1)):
                if L % b ==0:
                    d: int = L // b
                    if a * d + b * c == K and d % m == 0 and a<c/m:
                        print(f"The factors are: {m}({a}x+{b})({c/m}x+{d/m})")
                        
                        
def main() -> None:
    factor_quadratic2(115425, 3254121, 379020)

if __name__ == "__main__":
    main()

# want to additionally factor negative coefficients, let's see:


def factor_quadratic2(J: int, K: int, L: int) -> None:
    m=min(np.gcd(J, K),np.gcd(K, L),np.gcd(J, L))
    print("Given the quadratic with factored GCD:", end=" ")
    print(f"{m}({J/m}x^2 + {K/m}x + {L/m})")

    for a in range (1,J+1):
       if J % a == 0:
            c: int = J // a
            for b in range (1,(L+1)):
                if L % b ==0:
                    d: int = L // b
                    if a * d + b * c == K and d % m == 0 and a<c/m:
                        print(f"The factors are: {m}({a}x+{b})({c/m}x+{d/m})")
                        
                        
def main() -> None:
    factor_quadratic2(115425, 3254121, 379020)
    # Dave Biersach: The requirement was to factor a quadratic with the constant term is 379021
    # That turns out to be a prime quadratic, so you have to give the user some feedback
    # that it cannot be factored!

if __name__ == "__main__":
    main()
