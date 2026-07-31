# Chinese Remainder Theorem

- The Chinese remainder theorem is a theorem that gives the conditions necessary for multiple equations to have a simultaneous integer solution .
- The theorem has its origin in the work of the 3rd-century-AD Chinese mathematician Sun Zi, although the complete theorem was first given in 1247 by Qin Jiushao.
- The theorem states that if one knows the remainders of the Euclidean division of an integer n by several integers, then one can determine uniquely the remainder of the division of n by the product of these integers, under the condition that the divisors are pairwise coprime (no two divisors share a common factor other than 1) .
- In its basic form, the Chinese remainder theorem will determine a number p that, when divided by some given divisors, leaves given remainders.
- For example, if we want to find a number p that satisfies the following system of congruences:

```
p ≡ 2 (mod 3)
p ≡ 3 (mod 5)
p ≡ 2 (mod 7)
```

- Then we can use the Chinese remainder theorem to find that p = 23 + 105k, where k is any integer .
- The Chinese remainder theorem can be proved using the properties of congruences and the Euclidean algorithm .
- The Chinese remainder theorem is widely used for computing with large integers, as it allows replacing a computation for which one knows a bound on the size of the result by several similar computations on small integers.
- The Chinese remainder theorem is also useful for solving problems involving modular arithmetic, such as cryptography, coding theory, and number theory.