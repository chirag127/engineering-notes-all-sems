## Unit 4 - Sieve of Eratosthenes: generate prime numbers with the help of an algorithm given by the Greek Mathematician named Eratosthenes, whose algorithm is known as Sieve of Eratosthenes.

The Sieve of Eratosthenes is a simple and efficient algorithm for finding all prime numbers up to a specified limit. It was first described by the ancient Greek mathematician Eratosthenes, who lived in the third century BC.

### How does the Sieve of Eratosthenes work?

The algorithm works by marking the multiples of each prime number, starting with 2, as composite (i.e., not prime). This is done by iteratively crossing out multiples of each prime number. The remaining numbers that are not crossed out are prime.

Here are the steps to generate prime numbers using the Sieve of Eratosthenes:

1. Create a list of all the numbers from 2 to the limit you want to check for primes.
2. Start with the first prime number, 2.
3. Mark all of its multiples as composite by crossing them out in the list.
4. Move to the next number in the list that is not crossed out. This will be the next prime number.
5. Repeat steps 3 and 4 until you have crossed out all multiples of all prime numbers up to the square root of the limit.
6. The remaining numbers in the list that are not crossed out are prime.

### Example

Let's say we want to find all prime numbers up to 30 using the Sieve of Eratosthenes.

1. Create a list of all the numbers from 2 to 30: [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30].
2. Start with the first prime number, 2.
3. Mark all of its multiples as composite: [2, 3, ~~4~~, 5, ~~6~~, 7, ~~8~~, 9, ~~10~~, 11, ~~12~~, 13, ~~14~~, 15, ~~16~~, 17, ~~18~~, 19, ~~20~~, 21, ~~22~~, 23, ~~24~~, 25, ~~26~~, 27, ~~28~~, 29, ~~30~~].
4. Move to the next number in the list that is not crossed out, which is 3.
5. Mark all of its multiples as composite: [2, 3, ~~4~~, 5, ~~6~~, 7, ~~8~~, ~~9~~, ~~10~~, 11, ~~12~~, 13, ~~14~~, ~~15~~, ~~16~~, 17, ~~18~~, 19, ~~20~~, ~~21~~, ~~22~~, 23, ~~24~~, ~~25~~, ~~26~~, 27, ~~28~~, 29, ~~30~~].
6. Move to the next number in the list that is not crossed out, which is 5.
7. Mark all of its multiples as composite: [2, 3, ~~4~~, 5, ~~6~~, 7, ~~8~~, ~~9~~, ~~10~~, 11, ~~12~~, 13, ~~14~~, ~~15~~, ~~16~~, 17, ~~18~~, 19, ~~20~~, ~~21~~, ~~22~~, 23, ~~24~~, ~~25~~, ~~26~~, ~~27~~, ~~28~~, 29, ~~30~~].
8. Move to the next number in the list that is not crossed out, which is 7.
9. Mark all of its multiples as composite: [2, 3, ~~4~~, 5, ~~6~~, 7, ~~8~~, ~~9~~, ~~10~~, 11, ~~12~~, 13, ~~14~~, ~~15~~, ~~16~~, 17, ~~18~~, 19, ~~20~~, ~~21~~, ~~22~~, 23, ~~24~~, ~~25~~, ~~26~~, ~~27~~, ~~28~~, 29, ~~30~~].
10. We have now crossed out all multiples of all prime numbers up to the square root of 30, which is approximately 5.48. The remaining numbers in the list that are not crossed out are prime: [2, 3, 5, 7,