# Discrete Logarithmic Problem

- The discrete logarithm problem is defined as: given a group G, a generator g of the group and an element h of G, to find the discrete logarithm to the base g of h in the group G.
- The discrete logarithm problem is not always hard. The hardness of finding discrete logarithms depends on the groups.
- The discrete logarithm problem is considered to be computationally intractable. That is, no efficient classical algorithm is known for computing discrete logarithms in general.
- A general algorithm for computing log<sub>g</sub>h in finite groups G is to raise g to larger and larger powers k until the desired h is found. This is called the **brute-force** or **exhaustive search** algorithm.
- The brute-force algorithm has a time complexity of O(|G|) and a space complexity of O(1), where |G| is the order of the group.
- There are more efficient algorithms for computing discrete logarithms in some special groups, such as the group Z<sub>p</sub><sup>*</sup>, where p is a prime number.
- The current best algorithm for solving the discrete logarithm problem in Z<sub>p</sub><sup>*</sup> is the **Number Field Sieve (NFS)**, whose running time is exponential in log<sub>e</sub>p.
- The NFS algorithm has a time complexity of O(exp((c+o(1))(log p)<sup>1/3</sup>(log log p)<sup>2/3</sup>)) and a space complexity of O(exp((c+o(1))(log p)<sup>1/3</sup>(log log p)<sup>2/3</sup>)), where c is a constant.
- The discrete logarithm problem is the basis of many cryptographic schemes, such as the **Diffie-Hellman key exchange**, the **ElGamal encryption** and the **Digital Signature Algorithm (DSA)**.
- The security of these schemes relies on the assumption that the discrete logarithm problem is hard to solve in the chosen group.