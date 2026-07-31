### Group Homomorphisms

- A group homomorphism is a map between two groups that preserves the algebraic structure of both groups .
- Formally, a map $\phi: G \to H$ between two groups $(G, \cdot)$ and $(H, \circ)$ is called a group homomorphism if $\phi(g_1 \cdot g_2) = \phi(g_1) \circ \phi(g_2)$ for all $g_1, g_2 \in G$ .
- The range of $\phi$ in $H$ is called the homomorphic image of $\phi$.
- A group homomorphism that is both injective (one-to-one) and surjective (onto) is called an isomorphism of groups .
- A group homomorphism that is injective but not necessarily surjective is called a monomorphism.
- A group homomorphism that is surjective but not necessarily injective is called an epimorphism.
- A group homomorphism that is neither injective nor surjective is called an endomorphism.
- A group homomorphism from a group to itself is called an automorphism.

- Some examples of group homomorphisms are:

  - The map $f: \mathbb{Z} \to \{1, -1, i, -i\}$ defined by $f(n) = i^n$ for all $n \in \mathbb{Z}$, where $\mathbb{Z}$ is the group of integers under addition and $\{1, -1, i, -i\}$ is the group of complex numbers of unit modulus under multiplication.
  - The map $g: \mathbb{R} \to \mathbb{R}^+$ defined by $g(x) = e^x$ for all $x \in \mathbb{R}$, where $\mathbb{R}$ is the group of real numbers under addition and $\mathbb{R}^+$ is the group of positive real numbers under multiplication.
  - The map $h: S_n \to \mathbb{Z}_2$ defined by $h(\sigma) = 0$ if $\sigma$ is an even permutation and $h(\sigma) = 1$ if $\sigma$ is an odd permutation, where $S_n$ is the group of permutations of $n$ elements and $\mathbb{Z}_2$ is the group of integers modulo 2 under addition.