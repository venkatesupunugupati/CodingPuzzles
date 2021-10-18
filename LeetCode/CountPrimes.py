def countPrimes( n: int) -> int:
        if n < 2: return 0
        prime = [1]*n
        
        for i in range(2,int(n*0.5)+1):
            prime[i*i:n:i] = [0] * len(prime[i*i:n:i])
        
        return sum(prime)-2 #-2 because 0 and 1 is not a prime number

res = countPrimes(10)
print(res)