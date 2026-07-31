### Closure properties of CFL

Context-free languages (CFLs) are closed under several operations, meaning that if we apply these operations to CFLs, the resulting language will also be a CFL. Here are some of the closure properties of CFLs:

1. **Union**: If L1 and L2 are CFLs, then L1 ∪ L2 is also a CFL.
2. **Concatenation**: If L1 and L2 are CFLs, then L1L2 is also a CFL.
3. **Kleene Star**: If L is a CFL, then L* is also a CFL.
4. **Reversal**: If L is a CFL, then LR is also a CFL.
5. **Homomorphism**: If L is a CFL and h is a homomorphism, then h(L) is also a CFL.
6. **Inverse Homomorphism**: If L is a CFL and h is a homomorphism, then h^-1(L) is also a CFL.
7. **Intersection with a Regular Language**: If L1 is a CFL and L2 is a regular language, then L1 ∩ L2 is also a CFL.

It is important to note that CFLs are not closed under intersection, complementation, or set difference. This means that if we apply these operations to CFLs, the resulting language may not be a CFL.