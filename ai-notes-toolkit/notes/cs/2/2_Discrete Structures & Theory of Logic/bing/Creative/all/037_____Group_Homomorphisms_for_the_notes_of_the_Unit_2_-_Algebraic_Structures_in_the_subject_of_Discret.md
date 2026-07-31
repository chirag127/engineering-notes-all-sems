# Group Homomorphisms

- A group homomorphism is a function that maps one group to another group and preserves the group operation. That is, if $G$ and $H$ are groups with operations $\ast$ and $\cdot$, respectively, then a function $h:G\to H$ is a group homomorphism if
$$h(x\ast y) = h(x)\cdot h(y)$$
for all $x,y\in G$  .
- A group homomorphism has the following properties:
  - It maps the identity element of $G$ to the identity element of $H$. That is, $h(e_G) = e_H$ .
  - It maps the inverse of any element in $G$ to the inverse of its image in $H$. That is, $h(x^{-1}) = h(x)^{-1}$ for all $x\in G$ .
  - It preserves the order of any element in $G$. That is, if $x\in G$ has order $n$, then $h(x)\in H$ has order $n$ or $1$.
- A group homomorphism can be classified into different types based on its injectivity and surjectivity:
  - An injective homomorphism is one that maps distinct elements of $G$ to distinct elements of $H$. That is, $h(x) = h(y)$ implies $x=y$ for all $x,y\in G$ .
  - A surjective homomorphism is one that maps $G$ onto $H$. That is, for any $h\in H$, there exists $x\in G$ such that $h(x) = h$ .
  - A bijective homomorphism is one that is both injective and surjective. It is also called an isomorphism of groups. It implies that $G$ and $H$ are essentially the same group, just with different names for the elements and the operation  .
- A group homomorphism can be used to study the properties and structure of groups. Some important concepts related to group homomorphisms are:
  - The kernel of a homomorphism is the set of all elements in $G$ that are mapped to the identity element of $H$. That is, $\ker h = \{x\in G \mid h(x) = e_H\}$   .
  - The image of a homomorphism is the set of all elements in $H$ that are mapped from some element in $G$. That is, $\operatorname{im} h = \{h(x) \mid x\in G\}$   .
  - The kernel and the image of a homomorphism are both subgroups of $G$ and $H$, respectively   .
  - The first isomorphism theorem states that if $h:G\to H$ is a homomorphism, then $G/\ker h \cong \operatorname{im} h$, where $G/\ker h$ is the quotient group of $G$ by the kernel of $h$   .
  - The second isomorphism theorem states that if $h:G\to H$ is a homomorphism and $K$ is a subgroup of $G$ that contains $\ker h$, then $K/\ker h \cong h(K)$, where $h(K)$ is the image of $K$ under $h$   .
  - The third isomorphism theorem states that if $h:G\to H$ is a homomorphism and $K$ and $L$ are subgroups of $G$ that contain $\ker h$, then $(K/L)/h(L) \cong h(K)/h(L)$, where $K/L$ and $h(K)/h(L)$ are the quotient groups of $