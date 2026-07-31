# Group Homomorphisms

- A group homomorphism is a function that maps one group to another group in such a way that the group operation is preserved. That is, if $G$ and $H$ are groups and $h: G \to H$ is a group homomorphism, then for any $g_1, g_2 \in G$, we have $h(g_1 \cdot g_2) = h(g_1) \circ h(g_2)$, where $\cdot$ is the operation in $G$ and $\circ$ is the operation in $H$  .
- A group homomorphism has the following properties  :
  - It maps the identity element of $G$ to the identity element of $H$, i.e., $h(e_G) = e_H$.
  - It maps the inverse of any element in $G$ to the inverse of its image in $H$, i.e., $h(g^{-1}) = h(g)^{-1}$ for any $g \in G$.
  - It preserves the order of any element in $G$, i.e., if $g \in G$ has order $n$, then $h(g)$ has order $n$ or $1$ in $H$.
  - It preserves the commutativity of $G$, i.e., if $G$ is abelian, then $H$ is abelian.
- A group homomorphism can be classified into different types based on its injectivity and surjectivity :
  - An injective homomorphism is called a monomorphism. It means that $h(g_1) = h(g_2)$ implies $g_1 = g_2$ for any $g_1, g_2 \in G$.
  - A surjective homomorphism is called an epimorphism. It means that for any $h \in H$, there exists some $g \in G$ such that $h(g) = h$.
  - A bijective homomorphism is called an isomorphism. It means that $h$ is both a monomorphism and an epimorphism. It also means that $G$ and $H$ are essentially the same group, except for the names of the elements and the operation.
  - A homomorphism from a group to itself is called an endomorphism. It means that $G = H$ and $h: G \to G$.
  - An isomorphism from a group to itself is called an automorphism. It means that $h$ is an endomorphism and an isomorphism. It also means that $h$ is a permutation of the elements of $G$ that preserves the group structure.