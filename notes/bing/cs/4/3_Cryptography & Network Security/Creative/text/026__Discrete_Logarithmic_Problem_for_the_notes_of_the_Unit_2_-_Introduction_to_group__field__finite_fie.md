### Discrete Logarithmic Problem

- The discrete logarithm problem is defined as: given a group G, a generator g of the group and an element h of G, to find the discrete logarithm to the base g of h in the group G.
- The discrete logarithm problem is not always hard. The hardness of finding discrete logarithms depends on the groups.
- Discrete logarithms are perhaps simplest to understand in the group Zp*, where p is a prime number. Let g be the generator of Zp*, then the discrete logarithm problem reduces to computing a, given (g, p, ga mod p) for a randomly chosen a < (p −1).
- The discrete logarithm problem is considered to be computationally intractable. That is, no efficient classical algorithm is known for computing discrete logarithms in general.
- A general algorithm for computing log b a in finite groups G is to raise b to larger and larger powers k until the desired a is found. This is called the **exhaustive search** or **brute force** algorithm.
- The exhaustive search algorithm has a time complexity of O(|G|) and a space complexity of O(1), where |G| is the order of the group.
- There are some algorithms that can solve the discrete logarithm problem faster than the exhaustive search algorithm, but they are still exponential in the size of the input. Some examples are the **baby-step giant-step** algorithm, the **Pollard's rho** algorithm, and the **index calculus** algorithm .
- The baby-step giant-step algorithm has a time complexity of O(√|G|) and a space complexity of O(√|G|).
- The Pollard's rho algorithm has a time complexity of O(√|G|) and a space complexity of O(1).
- The index calculus algorithm has a time complexity of Lp[1/2, c] for some constant c, where Lp is a subexponential function, and a space complexity of Lp[1/2, c].
- The discrete logarithm problem is the basis of some cryptographic schemes, such as the **Diffie-Hellman** key exchange, the **ElGamal** encryption and signature schemes, and the **Digital Signature Algorithm** (DSA) .
- The security of these schemes relies on the assumption that the discrete logarithm problem is hard to solve in certain groups, such as the multiplicative group of a large prime field, or the group of points on an elliptic curve .
- However, the discrete logarithm problem may not be hard to solve in quantum computers, as there is a quantum algorithm called **Shor's algorithm** that can solve it in polynomial time. Therefore, the cryptographic schemes based on the discrete logarithm problem may not be secure against quantum attacks.