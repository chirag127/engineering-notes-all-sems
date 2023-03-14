### Chinese Remainder Theorem

- The Chinese remainder theorem is a theorem that gives a unique solution to a system of linear congruences with coprime moduli.
- A linear congruence is an equation of the form x ≡ a (mod n), where x, a, and n are integers and n > 0.
- The Chinese remainder theorem states that if n1, n2, ..., nk are pairwise coprime positive integers (meaning that they have no common factors other than 1) and a1, a2, ..., ak are arbitrary integers, then the system of congruences

x ≡ a1 (mod n1)  
x ≡ a2 (mod n2)  
...  
x ≡ ak (mod nk)

has a solution, and the solution is unique modulo N = n1n2...nk.

- For example, if we have the system of congruences

x ≡ 2 (mod 3)  
x ≡ 3 (mod 5)  
x ≡ 2 (mod 7)

then the Chinese remainder theorem tells us that there is a unique solution modulo 105 (the product of 3, 5, and 7), and that solution is x = 23. This means that x = 23 is a solution, and any other solution is congruent to 23 modulo 105, such as x = 128 or x = -82.

- The Chinese remainder theorem can be used to solve problems involving simultaneous divisibility, remainders, modular arithmetic, and cryptography. It can also be used to simplify computations with large numbers by breaking them down into smaller ones.

- The Chinese remainder theorem can be proved using the following algorithm, which also gives a way to find the solution to a system of congruences:

1. Compute N = n1 × n2 × ... × nk, the product of all the moduli.
2. For each i = 1, 2, ..., k, compute yi = N/ni, the quotient of N and ni.
3. For each i = 1, 2, ..., k, compute zi, the multiplicative inverse of yi modulo ni. This means that zi is an integer such that yizi ≡ 1 (mod ni). This can be done using the extended Euclidean algorithm, which also ensures that zi exists since ni and yi are coprime.
4. The integer x = a1y1z1 + a2y2z2 + ... + akykzk is a solution to the system of congruences, and x mod N is the unique solution modulo N.

- To see why this algorithm works, we can check that x satisfies each congruence in the system. For each i = 1, 2, ..., k, we have

x ≡ (a1y1z1 + a2y2z2 + ... + akykzk) (mod ni)  
≡ aiyizi (mod ni)  
≡ ai (mod ni),

where the second line follows since yj ≡ 0 (mod ni) for each j ≠ i, and the third line follows since yizi ≡ 1 (mod ni).

- To see why x mod N is the unique solution modulo N, suppose that there are two solutions u and v to the system of congruences. Then ni divides u - v for each i = 1, 2, ..., k, and since n1, n2, ..., nk are pairwise coprime, we have that N divides u - v, or u ≡ v (mod N). Thus, the solution is unique modulo N.

- A mnemonic to remember the algorithm is to use the acronym CYZ: Compute, Y, Z. Alternatively, one can use the phrase "Chinese Yields Zolution" to recall the steps.

- Here is an example of applying the algorithm to the system of congruences given above:

1. Compute N = 3 × 5 × 7 = 105.
2. Compute y1 = N/3 = 35, y2 = N/5 = 21, y3 = N/7 = 15.
3. Compute z1, the inverse of y1 modulo 3. Since 35 ≡ 2 (mod 3), we need to find an integer z1 such that 2z1 ≡ 1 (mod 3). This is satisfied by z1 = 2, since 2 × 2 ≡ 1 (mod 3). Similarly