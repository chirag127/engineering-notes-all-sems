### Chinese Remainder Theorem

- The Chinese Remainder Theorem (CRT) is a theorem that gives the conditions necessary for multiple equations to have a simultaneous integer solution.
- The theorem has its origin in the work of the 3rd-century-AD Chinese mathematician Sun Zi, although the complete theorem was first given in 1247 by Qin Jiushao.
- The CRT states that if one knows the remainders of the Euclidean division of an integer n by several integers, then one can determine uniquely the remainder of the division of n by the product of these integers, under the condition that the divisors are pairwise coprime (no two divisors share a common factor other than 1).
- The CRT can be expressed in terms of congruences as follows:

  - Suppose we have a system of k congruences:

    - x ≡ a1 (mod m1)
    - x ≡ a2 (mod m2)
    - ...
    - x ≡ ak (mod mk)

  - where the moduli m1, m2, ..., mk are pairwise coprime, and the remainders a1, a2, ..., ak are arbitrary integers.

  - Then, there exists a unique solution x to this system modulo M, where M = m1m2...mk.

  - Moreover, this solution can be found by the following formula:

    - x = (a1b1c1 + a2b2c2 + ... + akbkck) mod M

  - where bi = M/mi and ci = bi^-1 mod mi for each i.

- The CRT is widely used for computing with large integers, as it allows replacing a computation for which one knows a bound on the size of the result by several similar computations on small integers.
- The CRT is also useful for solving problems involving modular arithmetic, such as finding the last digits of large numbers, or finding the day of the week for a given date.
- The CRT can be generalized to other algebraic structures, such as rings and fields, where it is true over every principal ideal domain.
- The CRT is also related to other topics in number theory, such as Fermat's little theorem, Euler's theorem, and the RSA algorithm.