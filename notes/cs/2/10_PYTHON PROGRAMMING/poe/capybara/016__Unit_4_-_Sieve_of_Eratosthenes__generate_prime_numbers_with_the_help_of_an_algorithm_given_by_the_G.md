## Unit 4 - Sieve of Eratosthenes: Generate Prime Numbers

The Sieve of Eratosthenes is an algorithm used to find all prime numbers up to a given limit. It was named after the Greek mathematician Eratosthenes, who first described the algorithm.

Here are the steps to generate prime numbers using the Sieve of Eratosthenes:

1. Create a list of all numbers from 2 to the given limit.
2. Start with the first number in the list (which is 2), and mark all of its multiples as composite (not prime).
3. Move to the next unmarked number in the list (which is 3), and mark all of its multiples as composite.
4. Repeat step 3 for each unmarked number in the list, until you reach the end.
5. The numbers that are still unmarked in the list are prime numbers.

Here's an example of using the Sieve of Eratosthenes to find all prime numbers up to 30:

1. Create a list of all numbers from 2 to 30: `[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]`
2. Start with the first number in the list (which is 2), and mark all of its multiples as composite: `[2, 3, ~4~ , 5, ~6~ , 7, ~8~ , ~9~ , ~10~ , 11, ~12~ , 13, ~14~ , ~15~ , ~16~ , 17, ~18~ , 19, ~20~ , ~21~ , ~22~ , 23, ~24~ , ~25~ , ~26~ , ~27~ , ~28~ , 29, ~30~ ]`
3. Move to the next unmarked number in the list (which is 3), and mark all of its multiples as composite: `[2, 3, ~4~ , 5, ~6~ , 7, ~8~ , ~9~ , ~10~ , 11, ~12~ , 13, ~14~ , ~15~ , ~16~ , 17, ~18~ , 19, ~20~ , ~21~ , ~22~ , 23, ~24~ , ~25~ , ~26~ , ~27~ , ~28~ , 29, ~30~ ]`
4. Repeat step 3 for each unmarked number in the list, until you reach the end: `[2, 3, ~4~ , 5, ~6~ , 7, ~8~ , ~9~ , ~10~ , 11, ~12~ , 13, ~14~ , ~15~ , ~16~ , 17, ~18~ , 19, ~20~ , ~21~ , ~22~ , 23, ~24~ , ~25~ , ~26~ , ~27~ , ~28~ , 29, ~30~ ]`
5. The numbers that are still unmarked in the list are prime numbers: `[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]`

Using the Sieve of Eratosthenes can be much more efficient than checking each number individually to see if it's prime. This algorithm is commonly used in computer programs that need to find prime numbers.