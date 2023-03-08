## Unit 4 - Sieve of Eratosthenes: generate prime numbers with the help of an algorithm given by the Greek Mathematician named Eratosthenes, whose algorithm is known as Sieve of Eratosthenes.

- A prime number is a natural number that has exactly two positive divisors: 1 and itself. For example, 2, 3, 5, 7, 11, 13, 17, etc. are prime numbers.
- A composite number is a natural number that has more than two positive divisors. For example, 4, 6, 8, 9, 10, 12, 14, etc. are composite numbers.
- The Sieve of Eratosthenes is an ancient algorithm for finding all prime numbers up to a given limit. It was devised by Eratosthenes, a Greek mathematician and astronomer, in the 3rd century BC.
- The algorithm works as follows:
  - Create a list of consecutive natural numbers from 2 to n, where n is the limit.
  - Mark 2 as prime, and mark all multiples of 2 (from 2 * 2 = 4 onwards) as composite.
  - Find the smallest unmarked number greater than 2, and mark it as prime. This number is 3.
  - Mark all multiples of 3 (from 3 * 2 = 6 onwards) as composite.
  - Repeat the previous two steps until there is no unmarked number less than or equal to the square root of n.
  - The remaining unmarked numbers are all prime.
- Here is an example of applying the Sieve of Eratosthenes to find all prime numbers up to 20:

| Number | Marked as prime? | Marked as composite? |
| ------ | ---------------- | -------------------- |
| 2      | Yes              | No                   |
| 3      | Yes              | No                   |
| 4      | No               | Yes (by 2)           |
| 5      | Yes              | No                   |
| 6      | No               | Yes (by 2 and 3)     |
| 7      | Yes              | No                   |
| 8      | No               | Yes (by 2)           |
| 9      | No               | Yes (by 3)           |
| 10     | No               | Yes (by 2 and 5)     |
| 11     | Yes              | No                   |
| 12     | No               | Yes (by 2 and 3)     |
| 13     | Yes              | No                   |
| 14     | No               | Yes (by 2 and 7)     |
| 15     | No               | Yes (by 3 and 5)     |
| 16     | No               | Yes (by 2)           |
| 17     | Yes              | No                   |
| 18     | No               | Yes (by 2 and 3)     |
| 19     | Yes              | No                   |
| 20     | No               | Yes (by 2 and 5)     |

- The prime numbers up to 20 are 2, 3, 5, 7, 11, 13, 17, and 19.
- Here is a pseudocode implementation of the Sieve of Eratosthenes:

```
// Input: an integer n > 1
// Output: a list of all prime numbers less than or equal to n

// Create a boolean array of size n + 1, initialized to true
// The array represents the numbers from 0 to n, where true means unmarked and false means marked
bool[] isPrime = new bool[n + 1]
for i = 0 to n
  isPrime[i] = true

// Mark 0 and 1 as false, as they are not prime
isPrime[0] = false
isPrime[1] = false

// Loop from 2 to the square root of n
for p = 2 to sqrt(n)
  // If p is unmarked, it is prime
  if isPrime[p] == true
    // Mark all multiples of p as false, starting from p * p
    for i = p * p to n step p
      isPrime[i] = false

// Create a list to store the prime numbers
list primes = []

// Loop through the array and add the unmarked numbers to the list
for i = 0 to n
  if isPrime[i] == true

Some possible mnemonics and learning tricks for the topic are:

- To remember the first 10 prime numbers, you can use the phrase "Two, three, five, seven, eleven, thirteen, seventeen, nineteen, twenty-three, twenty-nine" and count the number of letters in each word.
- To remember the definition of a prime number, you can use the acronym PID: Prime means only one and Itself Divides it.
- To remember the steps of the Sieve of Eratosthenes, you can use the acronym SMURF: Start from 2, Mark multiples as composite, Unmark the next number as prime, Repeat until square root, Find the remaining primes.