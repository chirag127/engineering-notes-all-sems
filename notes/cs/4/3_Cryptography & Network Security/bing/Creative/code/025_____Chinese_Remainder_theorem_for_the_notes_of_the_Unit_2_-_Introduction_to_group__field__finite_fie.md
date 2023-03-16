### Chinese Remainder Theorem

- The Chinese remainder theorem is a theorem that gives the conditions necessary for multiple equations to have a simultaneous integer solution .
- The theorem has its origin in the work of the 3rd-century-AD Chinese mathematician Sun Zi, although the complete theorem was first given in 1247 by Qin Jiushao.
- The theorem states that if one knows the remainders of the Euclidean division of an integer n by several integers, then one can determine uniquely the remainder of the division of n by the product of these integers, under the condition that the divisors are pairwise coprime (no two divisors share a common factor other than 1) .
- In other words, the theorem says that if n ≡ a_i (mod m_i) for i = 1, 2, ..., k, where m_i are pairwise coprime, then there exists a unique solution n (mod M), where M = m_1 m_2 ... m_k, and n can be found by the formula:

n = ∑_{i=1}^k a_i M_i (M_i^{-1} mod m_i) (mod M)

where M_i = M / m_i and M_i^{-1} is the multiplicative inverse of M_i modulo m_i .

- The Chinese remainder theorem is widely used for computing with large integers, as it allows replacing a computation for which one knows a bound on the size of the result by several similar computations on small integers. It is also useful for solving systems of congruences and for cryptography .