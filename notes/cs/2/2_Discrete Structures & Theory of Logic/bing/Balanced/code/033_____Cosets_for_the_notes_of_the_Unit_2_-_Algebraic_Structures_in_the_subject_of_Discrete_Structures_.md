Hello, I am Sydney, your AI assistant. I can help you with writing notes on various topics. Here are some notes on cosets for the unit 2 of algebraic structures in the subject of discrete structures and theory of logic.

### Cosets

- A coset is a subset of a group that is obtained by multiplying a fixed element of the group by every element of a subgroup of the group.
- There are two types of cosets: left cosets and right cosets. A left coset is formed by multiplying the fixed element on the left of the subgroup elements, while a right coset is formed by multiplying the fixed element on the right of the subgroup elements.
- For example, let G be the group of integers under addition, and let H be the subgroup of even integers. Then, for any integer a, the left coset a + H is the set of all integers of the form a + 2n, where n is any integer. Similarly, the right coset H + a is the set of all integers of the form 2n + a, where n is any integer.
- The notation for cosets is usually aH for a left coset and Ha for a right coset, where a is the fixed element and H is the subgroup. Sometimes, the symbol + is used instead of the group operation, especially for additive groups.
- For example, the left coset 3 + H in the previous example is the set {3, 5, 7, 9, ...}, while the right coset H + 3 is the same set.
- The following properties hold for cosets:

  - The identity element of the group belongs to every coset of any subgroup. That is, eH = H = He for any subgroup H of a group G and the identity element e of G.
  - Two cosets are either equal or disjoint. That is, if aH and bH are two left cosets of a subgroup H of a group G, then either aH = bH or aH ∩ bH = ∅. The same is true for right cosets.
  - Every element of the group belongs to exactly one coset of any subgroup. That is, for any element a of a group G and any subgroup H of G, there exists a unique element b of G such that a ∈ bH. The same is true for right cosets.
  - The number of left cosets of a subgroup H of a group G is equal to the number of right cosets of H in G. This number is called the index of H in G and is denoted by [G : H].
  - The size of every coset of a subgroup H of a group G is equal to the size of H. That is, for any element a of G, |aH| = |H| = |Ha|. This follows from the fact that the map x ↦ ax is a bijection from H to aH, and the map x ↦ xa is a bijection from H to Ha.