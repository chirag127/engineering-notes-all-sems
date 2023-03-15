### Group Homomorphisms

- A group homomorphism is a function that maps one group to another group and preserves the group operation. That is, if $G$ and $H$ are groups with operations $\ast$ and $\cdot$, respectively, then a function $h:G\to H$ is a group homomorphism if
$$h(x\ast y) = h(x)\cdot h(y)$$
for all $x,y\in G$  .
- A group homomorphism has the following properties:
  - It maps the identity element of $G$ to the identity element of $H$. That is, $h(e_G) = e_H$ .
  - It preserves the inverse of each element. That is, $h(x^{-1}) = h(x)^{-1}$ for all $x\in G$ .
  - It maps the order of each element to a divisor of the order of the image. That is, if $x\in G$ has order $n$, then $h(x)\in H$ has order $m$ such that $m|n$.
  - It induces a partition of $G$ into equivalence classes called the fibers of $h$. The fiber of an element $y\in H$ is the set of all elements in $G$ that map to $y$. That is, $h^{-1}(y) = \{x\in G | h(x) = y\}$ .
- A group homomorphism is called an isomorphism if it is both one-to-one and onto. That is, $h:G\to H$ is an isomorphism if for every $y\in H$, there is exactly one $x\in G$ such that $h(x) = y$ . An isomorphism preserves all the group properties and shows that $G$ and $H$ are essentially the same group, just with different names for the elements.
- A group homomorphism is called a monomorphism if it is one-to-one but not necessarily onto. That is, $h:G\to H$ is a monomorphism if for every $y\in H$, there is at most one $x\in G$ such that $h(x) = y$. A monomorphism shows that $G$ is a subgroup of $H$ that is isomorphic to the image of $h$.
- A group homomorphism is called an epimorphism if it is onto but not necessarily one-to-one. That is, $h:G\to H$ is an epimorphism if for every $y\in H$, there is at least one $x\in G$ such that $h(x) = y$. An epimorphism shows that $H$ is a quotient group of $G$ by the kernel of $h$.
- A group homomorphism is called an endomorphism if the domain and codomain are the same group. That is, $h:G\to G$ is an endomorphism. An endomorphism is a way of transforming a group into itself while preserving the group structure.
- A group homomorphism is called an automorphism if it is an endomorphism and an isomorphism. That is, $h:G\to G$ is an automorphism if it is a bijective endomorphism. An automorphism is a way of relabeling the elements of a group without changing the group structure.