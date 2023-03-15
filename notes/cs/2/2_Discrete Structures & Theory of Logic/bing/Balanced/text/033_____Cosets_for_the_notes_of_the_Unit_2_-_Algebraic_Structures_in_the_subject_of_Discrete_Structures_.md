### Cosets

- A **coset** of a subgroup H of a group (G, o) is a subset of G obtained by multiplying H with elements of G from left or right .
- Depending on the multiplication from left or right, we can classify cosets as **left cosets** or **right cosets** as follows:
  - A **left coset** of H in G is a subset of G of the form aH = {ah | h ∈ H} for some a ∈ G.
  - A **right coset** of H in G is a subset of G of the form Ha = {ha | h ∈ H} for some a ∈ G.
- For example, take H = {0, 2, 4, 6} and G = {0, 1, 2, 3, 4, 5, 6, 7} with addition modulo 8 as the operation. Then 1 + H = {1, 3, 5, 7} and H + 5 = {5, 7, 1, 3} are left and right cosets of H in G, respectively.
- Cosets are mainly used to decompose a group G into equal-sized disjoint subsets of G. It plays an important role to study many things in Group Theory; for example, normal group, Lagrange’s theorem on finite groups, etc.
- Some properties of cosets are :
  - The number of elements in a left coset of H in G is equal to the number of elements in H. Similarly, the number of elements in a right coset of H in G is equal to the number of elements in H.
  - Two left cosets of H in G are either equal or disjoint. Similarly, two right cosets of H in G are either equal or disjoint.
  - The union of all left cosets of H in G is equal to G. Similarly, the union of all right cosets of H in G is equal to G.
  - The number of left cosets of H in G is equal to the number of right cosets of H in G. This number is called the **index** of H in G and is denoted by [G : H].
  - If H is a finite subgroup of a finite group G, then [G : H] = |G| / |H|, where |G| and |H| are the orders of G and H, respectively. This is known as **Lagrange's theorem**.