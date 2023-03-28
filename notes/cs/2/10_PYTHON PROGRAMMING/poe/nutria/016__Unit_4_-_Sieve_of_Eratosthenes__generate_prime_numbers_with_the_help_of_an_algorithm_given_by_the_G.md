
## Unit 4 - Sieve of Eratosthenes: Generate Prime Numbers with the Help of an Algorithm

The Sieve of Eratosthenes is an algorithm devised by the Greek Mathematician Eratosthenes, which is used to generate prime numbers. It is an efficient way to find all prime numbers up to a certain limit.

1. Start by creating a list of all numbers from 2 to the desired limit.
2. Mark all multiples of 2 (other than 2 itself) as composite (not prime).
3. Find the next unmarked number in the list and mark all of its multiples as composite.
4. Repeat step 3 until the desired limit is reached.
5. All unmarked numbers in the list are prime numbers.