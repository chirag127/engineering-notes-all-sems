### Normal Subgroups

- A normal subgroup H of a group G is a subgroup of G that is invariant under conjugation by members of the group. In other words, for every element g in G and every element h in H, we have g h g^-1 in H. The usual notation for this relation is H ≤ N G.
- Equivalently, a normal subgroup H of a group G is a subgroup of G such that every left coset and right coset corresponding to an element g are the same, that is, g H = H g.
- Normal subgroups are important because they allow us to define quotient groups, which are groups obtained by dividing a group by a normal subgroup. Quotient groups are useful for studying the structure and properties of groups.
- Some properties of normal subgroups are:

  - The trivial subgroup {e} and the whole group G are always normal subgroups of G.
  - The intersection of any collection of normal subgroups of G is a normal subgroup of G.
  - The product of any collection of normal subgroups of G is a normal subgroup of G, if the collection is finite or if G is abelian.
  - If H and K are normal subgroups of G such that H ∩ K = {e}, then H K is isomorphic to H × K.
  - If H is a normal subgroup of G and K is a subgroup of G, then H K is a subgroup of G and K / (H ∩ K) is isomorphic to H K / H.
  - If H is a normal subgroup of G and K is a normal subgroup of H, then K is a normal subgroup of G if and only if H K = K H.
  - If H is a normal subgroup of G and g is an element of G, then g H g^-1 is also a normal subgroup of G, and is called the conjugate subgroup of H by g.
  - If H is a normal subgroup of G and g is an element of G, then the map h ↦ g h g^-1 is an automorphism of H, called the inner automorphism of H by g.
  - If H is a normal subgroup of G, then the map g ↦ g H is a homomorphism from G to G / H, called the natural or canonical homomorphism. The kernel of this homomorphism is H, and the image is G / H.
  - If H is a normal subgroup of G and f is a homomorphism from G to another group K, then f(H) is a normal subgroup of f(G), and there is a unique homomorphism g from G / H to f(G) such that f = g ∘ (g H), where g H is the natural homomorphism from G to G / H. This is called the first isomorphism theorem or the homomorphism theorem.
  - If H is a normal subgroup of G and K is a subgroup of G containing H, then K / H is a normal subgroup of G / H if and only if K is a normal subgroup of G. This is called the correspondence theorem or the fourth isomorphism theorem.
  - If H is a normal subgroup of G and K is a normal subgroup of G containing H, then (G / H) / (K / H) is isomorphic to G / K. This is called the third isomorphism theorem.
  - If H is a normal subgroup of G and G is abelian, then H is a direct summand of G, that is, there exists a subgroup K of G such that G = H ⊕ K. This is called the splitting lemma or the second isomorphism theorem.
  - If H is a normal subgroup of G and G is finite, then the order of H divides the order of G. This is called Lagrange's theorem.
  - If H is a normal subgroup of G and G is finite, then the number of distinct conjugate subgroups of H in G is equal to the index of the normalizer of H in G, that is, [G : N_G(H)] = |G / H|. This is called the orbit-stabilizer theorem or the class equation.
  - If H is a normal subgroup of G and G is finite, then the number of elements in each conjugacy class of G is equal to the index of the centralizer of any element in that class, that is, [G : C_G(g)] = |g^G| for any g in G. This is also called the orbit-stabilizer