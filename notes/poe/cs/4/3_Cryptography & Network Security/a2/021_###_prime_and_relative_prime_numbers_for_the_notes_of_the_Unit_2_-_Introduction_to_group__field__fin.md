 Here is the content in markdown format for the given topic:

### Prime and Relative Prime Numbers

- A prime number is a positive integer greater than 1 whose only factors are 1 and itself. Eg: 2, 3, 5, 7, 11, 13, 17, 19, ...
- Two integers a and b are said to be relatively prime if their greatest common divisor is 1. Eg: 2 and 3 are relatively prime.
- Every integer greater than 1 can be expressed as the product of prime numbers in a unique way (Fundamental Theorem of Arithmetic). Eg: 30 = 2 x 3 x 5
- Relative primality is important in cryptography for ensuring that a and n are coprime for efficient working of RSA algorithm.

**Mnemonics:**
- Prime numbers can only be divisible by 1 and itself.
- For relative primality, GCD should be 1.

**Applications:**
- Used in encryption algorithms like RSA.
- Foundations of number theory.
- Studying patterns in prime numbers has applications in computer science like cryptography.

**Examples:**
Prime numbers: 2, 3, 5, 7, 11, 13, 17
Relative prime pairs: (2, 3), (5, 7), (11, 13)

**Advantages:**
- Fundamental building blocks of all integers.
- Relative primality ensures efficient working of RSA algorithm.

**Disadvantages:**
- Difficult to find larger prime numbers.
- Prime number distribution is random and chaotic.

**Notes:**
- Prime factorization of large integers is difficult (NP-hard) due to random distribution of primes. This forms the basis of security of RSA algorithm.
- Two numbers are relatively prime if their GCD is 1. This is used to ensure that public and private keys are coprime in RSA.
- Sieve of Eratosthenes is an efficient algorithm to find all primes upto a given integer.