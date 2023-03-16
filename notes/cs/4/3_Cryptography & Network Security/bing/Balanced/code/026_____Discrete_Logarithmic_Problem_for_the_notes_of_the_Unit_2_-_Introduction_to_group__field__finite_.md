### Discrete Logarithmic Problem

- The discrete logarithm problem is defined as: given a group G, a generator g of the group and an element h of G, to find the discrete logarithm to the base g of h in the group G.
- The discrete logarithm problem is not always hard. The hardness of finding discrete logarithms depends on the groups.
- Discrete logarithms are perhaps simplest to understand in the group Zp*, where p is a prime number. Let g be the generator of Zp*, then the discrete logarithm problem reduces to computing a, given (g, p, ga mod p) for a randomly chosen a < (p −1).
- The discrete logarithm problem is considered to be computationally intractable. That is, no efficient classical algorithm is known for computing discrete logarithms in general.
- A general algorithm for computing log b a in finite groups G is to raise b to larger and larger powers k until the desired a is found. This is called the **exhaustive search** or **brute force** method.
- The **baby-step giant-step** algorithm is a faster method than the exhaustive search for computing discrete logarithms in groups of moderate size. It uses a trade-off between time and space complexity.
- The **index calculus** algorithm is a more efficient method than the baby-step giant-step algorithm for computing discrete logarithms in some groups, such as Zp* for large p. It uses a factor base and a system of linear equations to find the discrete logarithm.
- The **Pollard's rho** algorithm is a randomized algorithm for computing discrete logarithms in any group. It uses a pseudo-random function and a cycle detection technique to find the discrete logarithm with high probability.
- The **Pollard's lambda** algorithm, also known as the **kangaroo** algorithm, is another randomized algorithm for computing discrete logarithms in any group. It uses a distinguished point and a trap function to find the discrete logarithm with high probability.
- The discrete logarithm problem is the basis of many cryptographic schemes, such as the **Diffie-Hellman** key exchange, the **ElGamal** encryption and signature schemes, and the **Digital Signature Algorithm** (DSA).