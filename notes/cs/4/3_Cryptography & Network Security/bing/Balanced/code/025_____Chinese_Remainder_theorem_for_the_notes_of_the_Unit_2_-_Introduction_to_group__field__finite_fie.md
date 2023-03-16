# Chinese Remainder Theorem

- The Chinese remainder theorem is a theorem that gives the conditions necessary for multiple equations to have a simultaneous integer solution.
- The theorem has its origin in the work of the 3rd-century-AD Chinese mathematician Sun Zi, although the complete theorem was first given in 1247 by Qin Jiushao.
- The theorem can be stated as follows: Let n1, n2, ..., nk be positive integers that are pairwise coprime (no two of them share a common factor other than 1). Then, for any given sequence of integers a1, a2, ..., ak, there exists an integer x that satisfies the following system of congruences:

x ≡ a1 (mod n1)

x ≡ a2 (mod n2)

...

x ≡ ak (mod nk)

Moreover, any two such integers x and y are congruent modulo the product N = n1n2...nk, that is, x ≡ y (mod N).

- The theorem can be proved by using the Euclidean algorithm and the principle of mathematical induction.
- The theorem is widely used for computing with large integers, as it allows replacing a computation for which one knows a bound on the size of the result by several similar computations on small integers.
- The theorem can also be used to solve problems involving simultaneous linear congruences, such as finding the smallest positive integer that leaves a given remainder when divided by some given divisors.
- The theorem can be generalized to other algebraic structures, such as rings and modules, where it is known as the Chinese remainder theorem for rings or modules.
- The theorem has applications in cryptography, number theory, combinatorics, and coding theory. For example, the RSA algorithm, a widely used public-key encryption scheme, relies on the difficulty of finding the factors of a large number that is the product of two large primes, which can be viewed as a special case of the Chinese remainder theorem.