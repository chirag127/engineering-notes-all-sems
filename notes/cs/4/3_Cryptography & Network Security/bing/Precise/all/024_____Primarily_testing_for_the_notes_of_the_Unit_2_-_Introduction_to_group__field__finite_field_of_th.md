### Unit 2 - Introduction to Group, Field, Finite Field of the form GF(p), Modular Arithmetic, Prime and Relative Prime Numbers, Extended Euclidean Algorithm, Advanced Encryption Standard (AES) Encryption and Decryption, Fermat’s and Euler’s Theorem, Primality Testing, Chinese Remainder Theorem, Discrete Logarithmic Problem, Principals of Public Key Crypto Systems, RSA Algorithm, Security of RSA

#### Group
- A group is a set of elements with a binary operation that satisfies the following properties:
  - Closure: For all elements a and b in the group, the result of the operation a * b is also in the group.
  - Associativity: For all elements a, b, and c in the group, the equation (a * b) * c = a * (b * c) holds.
  - Identity: There exists an element e in the group such that for all elements a in the group, the equation e * a = a * e = a holds.
  - Inverse: For every element a in the group, there exists an element b in the group such that a * b = b * a = e, where e is the identity element.

#### Field
- A field is a set of elements with two binary operations, addition and multiplication, that satisfy the following properties:
  - The set is an abelian group under addition, with the additive identity denoted by 0.
  - The set of non-zero elements is an abelian group under multiplication, with the multiplicative identity denoted by 1.
  - The distributive property holds: For all elements a, b, and c in the field, the equation a * (b + c) = (a * b) + (a * c) holds.

#### Finite Field of the form GF(p)
- A finite field is a field with a finite number of elements.
- A finite field of the form GF(p) is a field with p elements, where p is a prime number.
- The elements of GF(p) are the integers 0, 1, 2, ..., p-1.
- The operations of addition and multiplication are performed modulo p.

#### Modular Arithmetic
- Modular arithmetic is a system of arithmetic for integers, where numbers "wrap around" after reaching a certain value, called the modulus.
- The result of an arithmetic operation performed modulo n is the remainder when the result is divided by n.
- For example, in arithmetic modulo 7, the result of 5 + 3 is 1, because 8 divided by 7 has a remainder of 1.

#### Prime and Relative Prime Numbers
- A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers.
- Two numbers are relatively prime if their greatest common divisor is 1.

#### Extended Euclidean Algorithm
- The extended Euclidean algorithm is an algorithm to compute the greatest common divisor of two numbers, as well as the coefficients of Bézout's identity.
- Bézout's identity states that for any two integers a and b, there exist integers x and y such that ax + by = gcd(a, b).

#### Advanced Encryption Standard (AES) Encryption and Decryption
- The Advanced Encryption Standard (AES) is a symmetric key encryption algorithm.
- In AES, the same key is used for both encryption and decryption.
- AES operates on blocks of data, typically 128 bits in size.
- The key size can be 128, 192, or 256 bits.

#### Fermat’s and Euler’s Theorem
- Fermat's Little Theorem states that if p is a prime number, then for any integer a, the number a^p - a is an integer multiple of p.
- Euler's Theorem states that if a and n are relatively prime, then a^phi(n) ≡ 1 (mod n), where phi(n) is Euler's totient function.

#### Primality Testing
- Primality testing is the process of determining whether a given number is prime or not.
- There are several algorithms for primality testing, including trial division, the Miller-Rabin test, and the AKS primality test.

#### Chinese Remainder Theorem
- The Chinese Remainder Theorem is a theorem that provides a method for solving a system of linear congruences.
- The theorem states that if n1, n2, ..., nk are pairwise relatively prime, then the system of congruences x ≡ a1 (mod n1), x ≡ a2 (mod n2), ..., x ≡ ak (mod nk) has a unique solution modulo n1n2...nk.

#### Discrete Logarithmic Problem
- The discrete logarithm problem is