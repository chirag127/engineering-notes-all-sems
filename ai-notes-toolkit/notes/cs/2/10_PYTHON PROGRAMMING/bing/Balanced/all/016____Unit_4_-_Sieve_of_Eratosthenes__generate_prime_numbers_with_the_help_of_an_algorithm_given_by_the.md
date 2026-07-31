## Unit 4 - Sieve of Eratosthenes: generate prime numbers with the help of an algorithm given by the Greek Mathematician named Eratosthenes, whose algorithm is known as Sieve of Eratosthenes.

- A prime number is a natural number that has exactly two positive divisors: 1 and itself. For example, 2, 3, 5, 7, 11, 13, 17, etc. are prime numbers.
- A composite number is a natural number that has more than two positive divisors. For example, 4, 6, 8, 9, 10, 12, 14, etc. are composite numbers.
- The Sieve of Eratosthenes is an efficient algorithm to find all the prime numbers up to a given limit n. It was invented by the Greek mathematician Eratosthenes in the 3rd century BC.
- The algorithm works as follows:
  - Create a list of consecutive natural numbers from 2 to n: 2, 3, 4, ..., n.
  - Start with the smallest number 2, which is the first prime number. Mark it as prime and cross out all its multiples from the list, starting from 2 × 2 = 4.
  - Find the next number in the list that is not crossed out. It is the next prime number. Mark it as prime and cross out all its multiples from the list, starting from its square.
  - Repeat this process until you reach the square root of n. The remaining numbers in the list that are not crossed out are all prime numbers.
- Here is an example of applying the Sieve of Eratosthenes to find all the prime numbers up to 30:

| 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 |
|---|---|---|---|---|---|---|---|---|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| P | P | X | P | X | P | X | X | X  | P  | X  | P  | X  | X  | X  | P  | X  | P  | X  | X  | X  | P  | X  | X  | X  | X  | X  | P  | X  |

- The prime numbers are marked as P and the composite numbers are marked as X. The algorithm stops at the square root of 30, which is about 5.5. The numbers 2, 3, 5, 7, 11, 13, 17, 19, 23, and 29 are the prime numbers up to 30.
- The Sieve of Eratosthenes is useful for generating prime numbers quickly and efficiently. It can also be used to test whether a given number is prime or not, by checking if it is crossed out in the sieve or not. However, the algorithm requires a lot of memory to store the list of numbers, and it becomes slower as the limit n increases. Therefore, it is not practical for finding very large prime numbers, such as those used in cryptography. For that purpose, other algorithms, such as the Miller-Rabin test, are more suitable.