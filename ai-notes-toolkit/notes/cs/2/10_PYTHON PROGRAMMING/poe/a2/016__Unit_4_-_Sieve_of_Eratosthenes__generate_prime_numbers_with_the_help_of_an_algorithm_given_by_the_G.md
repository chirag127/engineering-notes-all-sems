 Here is the content in markdown format without any feelings or friendliness and being formal:

## Unit 4 - Sieve of Eratosthenes: generate prime numbers with the help of an algorithm given by the Greek Mathematician named Eratosthenes, whose algorithm is known as Sieve of Eratosthenes.

1. Sieve of Eratosthenes is an algorithm to find all prime numbers up to any given limit.
2. It does this by iteratively marking as composite (i.e. not prime) the multiples of each prime, starting with the multiples of 2.
3. The algorithm consists of the following steps:

a) Create a list of consecutive integers from 2 to n: (2, 3, 4, ..., n).
b) Let p be 2, the smallest prime number.
c) Eliminate all multiples of p greater than p from the list. These numbers are not prime.
d) Find the smallest number greater than p in the list. Let this be the next prime p.
e) Repeat steps c and d until p?? is greater than or equal to the square root of n.
f) The numbers that are left in the list are prime.

4. The algorithm makes use of the fact that if n is not prime, then n must be divisible by some prime number p less than or equal to ???n. So we only need to check prime numbers up to ???n.
5. The time complexity of Sieve of Eratosthenes is O(n log log n). It is one of the most efficient algorithms for finding prime numbers up to a given limit.