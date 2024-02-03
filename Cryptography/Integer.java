class IntegerFactorization(int n)(
    factor = [1]
    
    while n % 2 == 0:
        factor.append(2)
        n/=2
    f=3
    while f * f <= math.sprt(n):
        if n % f == 0:
            factor.append(f)
            n /= f
        else:
            f += 2
    return factor
)