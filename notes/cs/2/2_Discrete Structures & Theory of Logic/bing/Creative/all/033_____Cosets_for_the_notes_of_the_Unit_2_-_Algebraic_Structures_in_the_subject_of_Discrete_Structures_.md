# Cosets

- A **coset** of a subgroup H of a group G is a subset of G obtained by multiplying H with elements of G from left or right.
- For example, if H = {e, a, a^2} is a subgroup of G = {e, a, a^2, b, ab, a^2b}, then Ha = {a, a^2, e} and bH = {b, ba, ba^2} are cosets of H in G.
- Depending on the multiplication from left or right, we can classify cosets as **left cosets** or **right cosets**.
- For example, Ha is a left coset of H in G, and bH is a right coset of H in G.
- The notation for left and right cosets is usually Hg and gH, respectively, where g is any element of G.
- Cosets are mainly used to decompose a group G into equal-sized disjoint subsets of G. They play an important role in many topics in group theory, such as normal subgroups, Lagrange's theorem, quotient groups, etc.
- Some properties of cosets are:
  - The number of left cosets of H in G is equal to the number of right cosets of H in G, and is called the **index** of H in G, denoted by [G : H].
  - The size of any left coset of H in G is equal to the size of H, and is called the **order** of H, denoted by |H|.
  - The size of any right coset of H in G is also equal to the size of H.
  - Two left cosets Hg and Hg' are either equal or disjoint, and similarly for right cosets.
  - The union of all left cosets of H in G is equal to G, and similarly for right cosets.
  - A subgroup H of G is called a **normal subgroup** if every left coset of H in G is also a right coset of H in G, and vice versa. In other words, Hg = gH for all g in G. Normal subgroups are important because they allow us to define quotient groups, which are groups formed by the cosets of a normal subgroup.
  - Lagrange's theorem states that for any finite group G and any subgroup H of G, the order of G is equal to the product of the order of H and the index of H in G, i.e., |G| = |H| [G : H]. This implies that the order of any subgroup and any coset of G divides the order of G.