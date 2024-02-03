import time
import Crypto.Util.number
import math
time.clock = time.time
def naive_factorization(n):
    factorList = [1]
    while n % 2 == 0:
        factorList.append(2)
        n/=2
    f=3
    while f <= math.sqrt(n):
        if n % f == 0:
            factorList.append(f)
            n/=f
        else:
            f+=2
    if n > 1:
        factorList.append(n)
    return factorList

def factors(n):
    start = time.process_time()
    x = Crypto.Util.number.getPrime(n)
    y = Crypto.Util.number.getPrime(n)
    factors = naive_factorization(x*y)
    end = time.process_time() - start
    return x,y,end

if __name__ == '__main__':
    for i in range(10,33):
      x,y,timer = factors(i)
      print(f'{i} bit primes. Duration = {timer}s: n={x*y}, p={x}, q={y}')


