### Chinese Remainder Theorem

- The Chinese remainder theorem is a theorem that gives the conditions necessary for multiple equations to have a simultaneous integer solution .
- The theorem has its origin in the work of the 3rd-century-AD Chinese mathematician Sun Zi, although the complete theorem was first given in 1247 by Qin Jiushao.
- The theorem states that if one knows the remainders of the Euclidean division of an integer n by several integers, then one can determine uniquely the remainder of the division of n by the product of these integers, under the condition that the divisors are pairwise coprime (no two divisors share a common factor other than 1) .
- The theorem can be expressed in terms of congruences as follows :

  - Let n1, n2, ..., nk be positive integers that are pairwise coprime (that is, gcd(ni, nj) = 1 for all i ≠ j).
  - Let a1, a2, ..., ak be any integers.
  - Then, there exists an integer x that satisfies the system of congruences:

    - x ≡ a1 (mod n1)
    - x ≡ a2 (mod n2)
    - ...
    - x ≡ ak (mod nk)

  - Moreover, any two such integers x and y are congruent modulo N, where N = n1n2...nk (that is, x ≡ y (mod N)).

- The theorem can be proved using the properties of modular arithmetic and the Euclidean algorithm  .
- The theorem can be used to solve systems of congruences, as well as to compute with large integers by replacing a computation for which one knows a bound on the size of the result by several similar computations on small integers  .
- The theorem is widely used in cryptography, especially in public key cryptosystems such as RSA, where it allows to encrypt and decrypt messages using modular exponentiation .