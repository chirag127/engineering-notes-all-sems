### Chinese Remainder theorem for the notes of the Unit 2 - Introduction to group, field, finite field of the form GF(p), modular arithmetic, prime and relative prime numbers, Extended Euclidean Algorithm, Advanced Encryption Standard (AES) encryption and decryptionFermat’s and Euler’s theorem, Primarily testing, Chinese Remainder theorem, Discrete Logarithmic Problem,Principals of public key crypto systems, RSA algorithm, security of RSA in the subject of Cryptography & Network Security

- The Chinese Remainder theorem (CRT) is a mathematical result that allows us to solve a system of linear congruences with pairwise coprime moduli.
- A linear congruence is an equation of the form ax ≡ b (mod m), where a, b, and m are integers and x is an unknown variable.
- A system of linear congruences is a set of equations of the form:

  ```
  x ≡ a1 (mod m1)
  x ≡ a2 (mod m2)
  ...
  x ≡ ak (mod mk)
  ```

- where a1, a2, ..., ak and m1, m2, ..., mk are integers and x is an unknown variable.
- The moduli m1, m2, ..., mk are said to be pairwise coprime if no two of them have a common factor other than 1. For example, 3, 5, and 7 are pairwise coprime, but 4, 6, and 8 are not.
- The CRT states that if the moduli m1, m2, ..., mk are pairwise coprime, then the system of linear congruences has a unique solution modulo M, where M is the product of the moduli, i.e., M = m1m2...mk. That is, there exists an integer x such that x satisfies all the equations in the system, and any two such integers are congruent modulo M.
- The CRT can be proved using the Extended Euclidean Algorithm (EEA) and the properties of modular arithmetic. The EEA is an algorithm that can find the greatest common divisor (gcd) of two integers and also find integers u and v such that au + bv = gcd(a, b). The properties of modular arithmetic include the following:

  - If a ≡ b (mod m) and c ≡ d (mod m), then a + c ≡ b + d (mod m) and ac ≡ bd (mod m).
  - If a ≡ b (mod m) and n is any integer, then an ≡ bn (mod m).
  - If a and m are coprime, then there exists an integer a^-1 such that aa^-1 ≡ 1 (mod m). This is called the multiplicative inverse of a modulo m.

- The proof of the CRT is as follows:

  - Let M = m1m2...mk and Mi = M/mi for each i = 1, 2, ..., k. Note that Mi and mi are coprime for each i, since they have no common factor other than 1.
  - By the EEA, for each i, there exist integers ui and vi such that uiMi + vimi = 1. Taking both sides modulo mi, we get uiMi ≡ 1 (mod mi). This means that uiMi is the multiplicative inverse of Mi modulo mi.
  - Let x = a1u1M1 + a2u2M2 + ... + akukMk. Then, for each i, we have:

    ```
    x ≡ aiuiMi (mod mi)
    x ≡ ai (mod mi)
    ```

    This shows that x satisfies all the equations in the system.
  - To show that x is unique modulo M, suppose that y is another integer that satisfies the system. Then, for each i, we have x ≡ y (mod mi). This implies that x - y is divisible by mi for each i. Therefore, x - y is divisible by M, since M is the product of all the mi. This means that x ≡ y (mod M), as required.

- The CRT can be used to compute with large integers, as it allows us to break down a computation into smaller parts and then combine the results. For example, suppose we want to compute 7^1000 (mod 1001). We can use the CRT as follows:

  - First, we factor 1001 as 7 * 11 *