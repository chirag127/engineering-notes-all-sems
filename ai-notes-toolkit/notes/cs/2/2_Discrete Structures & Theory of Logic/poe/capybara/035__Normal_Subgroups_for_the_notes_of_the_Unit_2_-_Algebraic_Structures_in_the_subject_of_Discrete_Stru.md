### Normal Subgroups

Normal subgroups are an important concept in algebraic structures. In this section, we will define normal subgroups, discuss their properties, and give examples.

#### Definition

A subgroup H of a group G is said to be a normal subgroup if and only if for every element g in G, the conjugate of H by g, denoted by gHg^-1, is contained in H. Symbolically, we write gHg^-1 ⊆ H for all g in G.

#### Properties

1. If H is a normal subgroup of G, then the left cosets of H are the same as the right cosets of H.
2. The quotient group G/H, defined as the set of left cosets of H in G, is a group under the operation (aH)(bH) = abH.
3. The center of a group G is a normal subgroup of G.
4. The intersection of normal subgroups of G is itself a normal subgroup of G.
5. The image and kernel of a homomorphism are normal subgroups.

#### Examples

1. Let G = D4 be the dihedral group of order 8. Let H = {1, r^2} be the subgroup of rotations of order 2. Then H is a normal subgroup of G since gr^2g^-1 = r^2 for all g in G.
2. Let G = S3 be the symmetric group of order 6. Let H = {(), (12)} be the subgroup of order 2. Then H is a normal subgroup of G since gHg^-1 = H for all g in G.
3. Let G = Z be the group of integers under addition. Let H = 2Z be the subgroup of even integers. Then H is a normal subgroup of G since gHg^-1 = H for all g in G. The quotient group G/H is isomorphic to the group of integers modulo 2, denoted by Z/2Z.

#### Conclusion

Normal subgroups play a crucial role in the study of algebraic structures. They provide a natural way to define quotient groups and to understand the structure of groups. It is important to master the concept of normal subgroups and their properties in order to succeed in the subject of Discrete Structures & Theory of Logic.