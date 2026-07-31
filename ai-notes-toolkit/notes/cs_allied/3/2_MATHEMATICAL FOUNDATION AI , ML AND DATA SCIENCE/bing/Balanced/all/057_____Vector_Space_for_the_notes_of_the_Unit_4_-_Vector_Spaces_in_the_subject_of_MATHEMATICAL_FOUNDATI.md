# Vector Space

A vector space is a mathematical structure that allows us to add and scale vectors. Vectors are objects that have both magnitude and direction, such as arrows, forces, displacements, etc. In a vector space, we can perform two operations on vectors: addition and scalar multiplication. Addition means combining two vectors to get a new vector, and scalar multiplication means multiplying a vector by a number (called a scalar) to get a new vector.

To be a vector space, a set of vectors must satisfy some properties, called axioms. These axioms ensure that the operations of addition and scalar multiplication are well-defined and consistent. There are eight axioms that a vector space must satisfy:

1. **Closure under addition**: For any two vectors **u** and **v** in the vector space, their sum **u** + **v** is also in the vector space.
2. **Commutativity of addition**: For any two vectors **u** and **v** in the vector space, **u** + **v** = **v** + **u**.
3. **Associativity of addition**: For any three vectors **u**, **v**, and **w** in the vector space, (**u** + **v**) + **w** = **u** + (**v** + **w**).
4. **Existence of additive identity**: There exists a vector **0** in the vector space such that for any vector **u** in the vector space, **u** + **0** = **u**.
5. **Existence of additive inverse**: For any vector **u** in the vector space, there exists a vector **-u** in the vector space such that **u** + (**-u**) = **0**.
6. **Closure under scalar multiplication**: For any vector **u** in the vector space and any scalar c, the product c**u** is also in the vector space.
7. **Distributivity of scalar multiplication over vector addition**: For any two vectors **u** and **v** in the vector space and any scalar c, c(**u** + **v**) = c**u** + c**v**.
8. **Distributivity of scalar addition over scalar multiplication**: For any vector **u** in the vector space and any two scalars c and d, (c + d)**u** = c**u** + d**u**.
9. **Associativity of scalar multiplication**: For any vector **u** in the vector space and any two scalars c and d, (cd)**u** = c(d**u**).

These properties are common to many familiar examples of vector spaces, such as the set of n-dimensional vectors, the set of polynomials, the set of matrices, etc. However, not every set of vectors is a vector space. For example, the set of positive vectors (those with positive components) is not a vector space, because it does not satisfy the existence of additive inverse.

A vector space is a very abstract and general concept, but it is useful for studying many topics in mathematics, physics, engineering, and computer science. By defining a vector space, we can apply the same rules and methods to different kinds of vectors, and discover common patterns and properties among them. A vector space also allows us to define other concepts, such as subspaces, linear combinations, linear independence, basis, dimension, etc. These concepts will be discussed in the following sections.