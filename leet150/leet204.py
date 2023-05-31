class Solution:
    def countPrimes(self, n: int) -> int:

        if n < 2:
            return 0

        # Initially, set all numbers are prime
        prime = [1] * n 

        # 0 and 1 are not prime numbers.
        prime[0] = 0
        prime[1] = 0

        # If any number is prime, set all of its multiples as non-prime.
        for i in range(2, n):
            if prime[i] == 1:
                for j in range(i*i, n, i):
                    prime[j] = 0

        return sum(prime)