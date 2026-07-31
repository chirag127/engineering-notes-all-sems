# Cosets

- A coset of a subgroup H of a group G is a subset of G obtained by multiplying H with elements of G from left or right.
- For example, if H = {e, a, a^2} is a subgroup of G = {e, a, a^2, b, ab, a^2b}, then Ha = {a, a^2, e} and bH = {b, ba, ba^2} are cosets of H in G.
- Depending on the multiplication from left or right, we can classify cosets as left cosets or right cosets.
- A left coset of H in G is a subset of the form gH = {gh : h in H}, where g is any element of G.
- A right coset of H in G is a subset of the form Hg = {hg : h in H}, where g is any element of G.
- For example, in the above case, Ha and aH are left cosets of H in G, and bH and Hb are right cosets of H in G.
- The number of left cosets of H in G is called the index of H in G, denoted by [G : H].
- The number of right cosets of H in G is equal to the number of left cosets of H in G.
- For any finite group G and any subgroup H of G, the number of elements of H divides the number of elements of G. This is known as Lagrange's theorem.
- Cosets of a normal subgroup of G can be used to define another group called the quotient group or factor group of G by H, denoted by G/H.
- A normal subgroup of G is a subgroup H such that gH = Hg for all g in G.
- The quotient group G/H is the set of all left (or right) cosets of H in G, with the operation defined as (gH)(g'H) = (gg')H for any g, g' in G.
- For example, if H = {e, a, a^2} is a normal subgroup of G = {e, a, a^2, b, ab, a^2b}, then G/H = {H, bH} is a quotient group of G by H, with the operation H(bH) = bH and (bH)(bH) = H.