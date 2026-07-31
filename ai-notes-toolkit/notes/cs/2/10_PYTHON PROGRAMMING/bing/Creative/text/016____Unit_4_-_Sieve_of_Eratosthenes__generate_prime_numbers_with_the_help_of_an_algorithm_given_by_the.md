## Unit 4 - Sieve of Eratosthenes: generate prime numbers with the help of an algorithm given by the Greek Mathematician named Eratosthenes, whose algorithm is known as Sieve of Eratosthenes.

- A prime number is a natural number that has exactly two positive divisors: 1 and itself. For example, 2, 3, 5, 7, 11, 13, 17, etc. are prime numbers.
- A composite number is a natural number that has more than two positive divisors. For example, 4, 6, 8, 9, 10, 12, 14, etc. are composite numbers.
- The Sieve of Eratosthenes is an ancient algorithm for finding all prime numbers up to a given limit. It works by iteratively marking as composite (i.e., not prime) the multiples of each prime, starting with the multiples of 2.
- The algorithm can be described as follows:

  1. Create a list of consecutive integers from 2 to n: (2, 3, 4, ..., n).
  2. Initially, let p equal 2, the first prime number.
  3. Starting from p, mark all the multiples of p in the list as composite. For example, if p = 2, mark 2 × 2 = 4, 2 × 3 = 6, 2 × 4 = 8, and so on.
  4. Find the first number greater than p in the list that is not marked as composite. If there is no such number, stop. Otherwise, let p equal this number (the next prime), and repeat from step 3.
  5. When the algorithm terminates, all the numbers in the list that are not marked as composite are prime.

- Here is an example of the algorithm applied to find all prime numbers up to 20:

  1. Create a list of consecutive integers from 2 to 20: (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20).
  2. Let p = 2, the first prime number.
  3. Mark all the multiples of 2 in the list as composite: (2, 3, **4**, 5, **6**, 7, **8**, 9, **10**, 11, **12**, 13, **14**, 15, **16**, 17, **18**, 19, **20**).
  4. Find the first number greater than 2 in the list that is not marked as composite: 3. Let p = 3, the next prime number.
  5. Mark all the multiples of 3 in the list as composite: (2, 3, 4, 5, 6, 7, 8, **9**, 10, 11, 12, 13, 14, **15**, 16, 17, 18, 19, 20).
  6. Find the first number greater than 3 in the list that is not marked as composite: 5. Let p = 5, the next prime number.
  7. Mark all the multiples of 5 in the list as composite: (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, **14**, 15, **16**, 17, **18**, 19, **20**).
  8. Find the first number greater than 5 in the list that is not marked as composite: 7. Let p = 7, the next prime number.
  9. Mark all the multiples of 7 in the list as composite: (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, **19**, 20).
  10. Find the first number greater than 7 in the list that is not marked as composite: 11. Let p = 11, the next prime number.
  11. Mark all the multiples of 11 in the list as composite: (2, 3, 4, 5, 6, 7, 8