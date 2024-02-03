import math

def naive_factorization(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n//=2
    f=3
    while f <= math.sqrt(n):
        if n % f == 0:
            factors.append(f)
            n//=f
        else:
            f+=2
    if n > 1:
        factors.append(n)
    return factors

def rsakey(n, e):
    factors = naive_factorization(n)
    p = factors[-1]
    q = factors[-2]
    assert p*q == n, "not equal"
    phi = (p-1)*(q-1)
    d = pow(e,-1,phi)
    return d

if __name__ == '__main__':
    n = 712446816787
    e = 6551
    c = 273095689186
    factors = naive_factorization(n)
    pkey = rsakey(n,e)
    d = pow(c,pkey,n)
    plaintext = ""
    while d > 0:
      plaintext = chr((d%100) + 96) + plaintext
      d //= 100
    print(plaintext)