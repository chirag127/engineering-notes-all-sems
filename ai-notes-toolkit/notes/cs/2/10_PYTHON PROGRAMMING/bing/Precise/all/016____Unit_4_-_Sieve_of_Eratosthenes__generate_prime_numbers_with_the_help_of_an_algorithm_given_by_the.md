## Unit 4 - Sieve of Eratosthenes

The Sieve of Eratosthenes is an algorithm used to generate prime numbers. It was created by the Greek Mathematician named Eratosthenes. The algorithm is known as the Sieve of Eratosthenes.

The algorithm works by iteratively marking as composite (i.e., not prime) the multiples of each prime, starting with the first prime number, 2. The multiples of a given prime are generated as a sequence of numbers starting from that prime, with constant difference between them that is equal to that prime. This is the sieve's key distinction from using trial division to sequentially test each candidate number for divisibility by each prime.

Here are the steps to implement the Sieve of Eratosthenes algorithm:

1. Create a list of consecutive integers from 2 to n: (2, 3, 4, ..., n).
2. Initially, let p equal 2, the smallest prime number.
3. Enumerate the multiples of p by counting in increments of p from p*p to n, and mark them in the list (these will be p*p, p*p + p, p*p + 2p, p*p + 3p, ...; the p itself should not be marked).
4. Find the smallest number in the list greater than p that is not marked. If there was no such number, stop. Otherwise, let p now equal this new number (which is the next prime), and repeat from step 3.
5. When the algorithm terminates, the numbers remaining not marked in the list are all the primes below n.

The Sieve of Eratosthenes is one of the most efficient ways to find all primes smaller than n when n is smaller than 10 million or so.