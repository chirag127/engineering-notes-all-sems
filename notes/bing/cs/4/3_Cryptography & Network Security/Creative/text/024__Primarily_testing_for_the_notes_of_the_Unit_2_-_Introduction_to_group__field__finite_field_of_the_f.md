### Primality testing

- Primality testing is the process of checking whether a given number is prime or not.
- A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
- Primality testing is important for cryptography, especially for public key cryptosystems that rely on large prime numbers.
- There are two types of primality tests: deterministic and probabilistic.
- A deterministic primality test is an algorithm that always gives a correct answer, whether the input number is prime or not.
- A probabilistic primality test is an algorithm that gives a correct answer with high probability, but may sometimes give a wrong answer (either a false positive or a false negative).
- Examples of deterministic primality tests are trial division, the Sieve of Eratosthenes, the AKS algorithm, etc.
- Examples of probabilistic primality tests are the Fermat test, the Miller-Rabin test, the Solovay-Strassen test, etc.
- A probabilistic primality test can be made more reliable by repeating it several times with different random choices, reducing the probability of error exponentially.
- A probabilistic primality test can also be made more efficient by using a smaller set of possible witnesses, such as the first few primes, or the bases 2 and 3, etc.