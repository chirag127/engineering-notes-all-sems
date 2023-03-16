### Chinese Remainder Theorem

- The Chinese remainder theorem is a theorem that gives the conditions necessary for multiple equations to have a simultaneous integer solution .
- The theorem has its origin in the work of the 3rd-century-AD Chinese mathematician Sun Zi, although the complete theorem was first given in 1247 by Qin Jiushao.
- The theorem states that if one knows the remainders of the Euclidean division of an integer n by several integers, then one can determine uniquely the remainder of the division of n by the product of these integers, under the condition that the divisors are pairwise coprime (no two divisors share a common factor other than 1) .
- The theorem can be expressed in terms of congruences as follows :

  - Let n1, n2, ..., nk be positive integers that are pairwise coprime (i.e., gcd(ni, nj) = 1 for all i ≠ j).
  - Let a1, a2, ..., ak be any integers.
  - Then, there exists an integer x that satisfies the system of congruences:

    - x ≡ a1 (mod n1)
    - x ≡ a2 (mod n2)
    - ...
    - x ≡ ak (mod nk)

  - Moreover, any two such integers x and y are congruent modulo N = n1n2...nk, i.e., x ≡ y (mod N).

- The theorem can be proved using the properties of modular arithmetic and the extended Euclidean algorithm  .
- The theorem is widely used for computing with large integers, as it allows replacing a computation for which one knows a bound on the size of the result by several similar computations on small integers.
- The theorem is also useful for solving systems of congruences, cryptography, number theory, and combinatorics .