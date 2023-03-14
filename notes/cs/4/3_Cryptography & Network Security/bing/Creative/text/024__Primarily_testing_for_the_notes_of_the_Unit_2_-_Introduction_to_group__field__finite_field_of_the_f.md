### Primality testing

- A primality test is an algorithm for determining whether an input number is prime or not.  
- Primality testing is used for cryptography, among other fields of mathematics.  
- Primality tests can be classified into two types: deterministic and probabilistic. 
  - Deterministic tests can prove with absolute certainty whether a number is prime or not. Examples of deterministic tests include the Lucas-Lehmer test and elliptic curve primality proving. 
  - Probabilistic tests can potentially (although with very small probability) falsely identify a composite number as prime (although not vice versa). However, they are in general much faster than deterministic tests. Numbers that have passed a probabilistic test are called probable primes until their primality can be confirmed deterministically. A number that passes a probabilistic test but is in fact composite is called a pseudoprime. 
- The simplest primality test is trial division: given an input number, n, check whether it is evenly divisible by any prime number between 2 and √n. If so, then n is composite. Otherwise, it is prime. 
- Trial division can be improved by observing that all primes greater than 3 are of the form 6k ± 1, where k is any integer greater than 0. This is because all integers can be expressed as (6k + i), where i = −1, 0, 1, 2, 3, or 4. Note that 2 divides (6k + 0), (6k + 2), and (6k + 4) and 3 divides (6k + 3). So, a more efficient method is to test whether n is divisible by 2 or 3, then to check through all numbers of the form 6k ± 1 up to √n. 
- Generalizing further, all primes greater than c# (c primorial) are of the form c# · k + i, for i < c#, where c and k are integers and i represents the numbers that are coprime to c#. 
- There are many other primality tests, such as the Rabin-Miller strong pseudoprime test, the Adleman-Pomerance-Rumely primality test, the AKS primality test, and the Pépin's test.  
- The state of the art in deterministic primality testing for arbitrary numbers is elliptic curve primality proving. 
- The AKS primality test is the first polynomial time algorithm for primality testing that has asymptotic complexity of O((log n)^6).  

: https://en.wikipedia.org/wiki/Primality_test
: https://mathworld.wolfram.com/PrimalityTest.html
: https://www.cse.iitk.ac.in/primality.pdf