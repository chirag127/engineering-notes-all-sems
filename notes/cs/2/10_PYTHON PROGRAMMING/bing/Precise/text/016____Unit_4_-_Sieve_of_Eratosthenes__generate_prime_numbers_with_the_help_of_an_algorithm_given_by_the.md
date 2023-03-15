## Unit 4 - Sieve of Eratosthenes

The Sieve of Eratosthenes is an algorithm used to generate prime numbers. It was created by the Greek mathematician Eratosthenes.

The algorithm works as follows:
1. Create a list of consecutive integers from 2 to the maximum number you want to search for primes (n).
2. Start with the first number in the list (2) and mark it as prime.
3. Remove all multiples of the first number (excluding the number itself) from the list.
4. Move to the next number in the list and repeat the process until all numbers in the list have been processed.
5. The remaining numbers in the list are all prime numbers up to n.

This algorithm is an efficient way to generate prime numbers up to a certain limit. It is particularly useful for generating large sets of prime numbers.