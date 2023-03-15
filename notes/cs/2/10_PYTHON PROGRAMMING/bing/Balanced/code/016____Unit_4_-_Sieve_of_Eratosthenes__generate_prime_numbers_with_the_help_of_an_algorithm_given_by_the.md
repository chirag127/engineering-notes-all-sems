## Unit 4 - Sieve of Eratosthenes: generate prime numbers with the help of an algorithm given by the Greek Mathematician named Eratosthenes, whose algorithm is known as Sieve of Eratosthenes.

- A prime number is a natural number that has exactly two positive divisors: 1 and itself. For example, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, etc. are prime numbers.
- A composite number is a natural number that has more than two positive divisors. For example, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, etc. are composite numbers.
- The Sieve of Eratosthenes is an ancient algorithm for finding all prime numbers up to a given limit. It was invented by Eratosthenes, a Greek mathematician who lived in the 3rd century BC.
- The algorithm works as follows:
  - Create a list of consecutive natural numbers from 2 to the limit, and mark them all as unmarked.
  - Start from the smallest unmarked number, which is 2, and mark it as prime.
  - Find all the multiples of 2 in the list, starting from 2 × 2 = 4, and mark them as composite.
  - Move to the next unmarked number, which is 3, and mark it as prime.
  - Find all the multiples of 3 in the list, starting from 3 × 2 = 6, and mark them as composite.
  - Repeat this process for the next unmarked number, which is 5, and so on, until you reach the limit or the square root of the limit, whichever is smaller.
  - The remaining unmarked numbers in the list are all prime.
- Here is an example of applying the Sieve of Eratosthenes to find all the prime numbers up to 30:

| Number | Mark | Reason |
| ------ | ---- | ------ |
| 2      | P    | Smallest unmarked number, mark as prime |
| 3      | P    | Next unmarked number, mark as prime |
| 4      | C    | Multiple of 2, mark as composite |
| 5      | P    | Next unmarked number, mark as prime |
| 6      | C    | Multiple of 2 and 3, mark as composite |
| 7      | P    | Next unmarked number, mark as prime |
| 8      | C    | Multiple of 2, mark as composite |
| 9      | C    | Multiple of 3, mark as composite |
| 10     | C    | Multiple of 2 and 5, mark as composite |
| 11     | P    | Next unmarked number, mark as prime |
| 12     | C    | Multiple of 2 and 3, mark as composite |
| 13     | P    | Next unmarked number, mark as prime |
| 14     | C    | Multiple of 2 and 7, mark as composite |
| 15     | C    | Multiple of 3 and 5, mark as composite |
| 16     | C    | Multiple of 2, mark as composite |
| 17     | P    | Next unmarked number, mark as prime |
| 18     | C    | Multiple of 2 and 3, mark as composite |
| 19     | P    | Next unmarked number, mark as prime |
| 20     | C    | Multiple of 2 and 5, mark as composite |
| 21     | C    | Multiple of 3 and 7, mark as composite |
| 22     | C    | Multiple of 2 and 11, mark as composite |
| 23     | P    | Next unmarked number, mark as prime |
| 24     | C    | Multiple of 2 and 3, mark as composite |
| 25     | C    | Multiple of 5, mark as composite |
| 26     | C    | Multiple of 2 and 13, mark as composite |
| 27     | C    | Multiple of 3, mark as composite |
| 28     | C    | Multiple of 2 and 7, mark as composite |
| 29     | P    | Next unmarked number, mark as prime |
| 30     | C    | Multiple of 2, 3 and 5, mark