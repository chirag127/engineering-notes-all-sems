# Group Homomorphisms

- A group homomorphism is a function that maps one group to another group and preserves the group operation. That is, if \\(G\\) and \\(H\\) are groups with operations \\(*\\) and \\(\\cdot\\) respectively, and \\(h: G \\to H\\) is a group homomorphism, then for any \\(u, v \\in G\\), we have \\(h(u * v) = h(u) \\cdot h(v)\\)  .
- A group homomorphism also preserves the identity element and the inverse element of a group. That is, if \\(e_G\\) and \\(e_H\\) are the identity elements of \\(G\\) and \\(H\\) respectively, and \\(h: G \\to H\\) is a group homomorphism, then \\(h(e_G) = e_H\\) and \\(h(u^{-1}) = h(u)^{-1}\\) for any \\(u \\in G\\) .
- A group homomorphism can be injective, surjective, or bijective. An injective group homomorphism is also called a monomorphism, a surjective group homomorphism is also called an epimorphism, and a bijective group homomorphism is also called an isomorphism. Two groups that are isomorphic have the same algebraic structure and are essentially the same group .
- Some examples of group homomorphisms are:
  - The identity map \\(id: G \\to G\\) defined by \\(id(x) = x\\) for any \\(x \\in G\\) is a group homomorphism. It is also an isomorphism.
  - The zero map \\(z: G \\to H\\) defined by \\(z(x) = e_H\\) for any \\(x \\in G\\) is a group homomorphism. It is neither injective nor surjective, unless \\(H\\) is the trivial group.
  - The sign map \\(s: (\\mathbb{R} - \\{0\\}, \\times) \\to (\\{-1, 1\\}, \\times)\\) defined by \\(s(x) = \\frac{x}{|x|}\\) for any \\(x \\in \\mathbb{R} - \\{0\\}\\) is a group homomorphism. It is surjective but not injective.
  - The determinant map \\(d: (GL_n(\\mathbb{R}), \\cdot) \\to (\\mathbb{R} - \\{0\\}, \\times)\\) defined by \\(d(A) = \\det(A)\\) for any \\(A \\in GL_n(\\mathbb{R})\\) is a group homomorphism. It is neither injective nor surjective.
- Some properties of group homomorphisms are:
  - The kernel of a group homomorphism \\(h: G \\to H\\) is the set of all elements in \\(G\\) that are mapped to the identity element in \\(H\\). That is, \\(\\ker(h) = \\{x \\in G | h(x) = e_H\\}\\). The kernel of a group homomorphism is a normal subgroup of \\(G\\) .
  - The image of a group homomorphism \\(h: G \\to H\\) is the set of all elements in \\(H\\) that are mapped from some element in \\(G\\). That is, \\(\\operatorname{im}(h) = \\{h(x) | x \\in G\\}\\). The image of a group homomorphism is a subgroup of \\(H\\) .
  - The first isomorphism theorem states that if \\(h: G \\to H\\) is a group homomorphism, then \\(G/\\ker(h) \\cong \\operatorname{im}(h)\\). That is, the quotient group of \\(G\\) by the kernel of \\(h\\) is isomorphic to the image of \\(h\\) .
  - The second isomorphism theorem states that if \\(h: G \\to H\\) is a group homomorphism