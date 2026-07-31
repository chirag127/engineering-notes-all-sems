### Lagrange's theorem for the notes of the Unit 2 - Algebraic Structures in the subject of Discrete Structures & Theory of Logic

- Lagrange's theorem is one of the central theorems of abstract algebra. It states that in group theory, for any finite group say G, the order of subgroup H of group G divides the order of G. The order of the group represents the number of elements .
- Lagrange's theorem can be expressed as |G| = n|H|, where n is a positive integer called the index of H in G.
- Lagrange's theorem can be proved by using the concept of cosets of a subgroup. A coset of H in G is a subset of G that is obtained by multiplying all the elements of H by a fixed element of G. There are two types of cosets: left cosets and right cosets. A left coset of H in G is of the form gH, where g is an element of G. A right coset of H in G is of the form Hg, where g is an element of G.
- The key properties of cosets are:

  - Every element of G belongs to exactly one left coset of H and exactly one right coset of H.
  - Every left coset of H has the same number of elements as H, and every right coset of H has the same number of elements as H.
  - Two left cosets of H are either equal or disjoint, and two right cosets of H are either equal or disjoint.
  - The number of left cosets of H in G is equal to the number of right cosets of H in G, and this number is the index of H in G.

- Using these properties, we can prove Lagrange's theorem as follows:

  - Let G be a finite group and H be a subgroup of G. Let n be the index of H in G, and let g1, g2, ..., gn be the distinct elements of G that form the left cosets of H. That is, G = g1H ∪ g2H ∪ ... ∪ gnH, where the union is disjoint.
  - Since every left coset of H has the same number of elements as H, we have |giH| = |H| for every i = 1, 2, ..., n.
  - Therefore, by the principle of counting, we have |G| = |g1H| + |g2H| + ... + |gnH| = n|H|.
  - Hence, |H| divides |G|, which proves Lagrange's theorem.

- Lagrange's theorem has some important consequences, such as:

  - The order of any element of a finite group divides the order of the group.
  - If G is a finite group and H is a subgroup of G such that |H| = |G|/2, then H is a normal subgroup of G.
  - If G is a finite group of prime order, then G is cyclic and has no proper subgroups.
  - If G is a finite group and K is a normal subgroup of G, then the order of the quotient group G/K divides the order of G.