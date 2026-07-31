 Here is the content in markdown format without any emojis or external links:

### Linear Independence

- A set of vectors {v1, v2, ..., vn} in a vector space V is said to be linearly independent if the only way to express the zero vector 0 in terms of these vectors is:

0 = c1v1 + c2v2 + ... + cnvn

Where all ci = 0 for i = 1, 2, ..., n

- Otherwise, the vectors are said to be linearly dependent.

- Geometrically, a set of vectors is linearly independent if none of the vectors can be expressed as a linear combination of the others.

- The vectors (1, 0) and (0, 1) in R2 are linearly independent since neither can be expressed as a linear combination of the other.

- The vectors (1, 1) and (2, 2) are not linearly independent since (1, 1) can be expressed as (2/1) × (2, 2).

- Maximum number of linearly independent vectors in a vector space is called the dimension of the vector space.

- Basis of a vector space is a maximal set of linearly independent vectors. Every vector in the vector space can be expressed uniquely as a linear combination of basis vectors.

- A vector space is finite dimensional if it has a finite basis. Otherwise, it is infinite dimensional.

- Examples: Rn is n-dimensional, polynomial space is infinite dimensional.

- Properties:
- Linearly independent vectors cannot be scaled versions of each other.
- If {v1, v2, ..., vn} is a linearly independent set, then removing any vector from the set will still give a linearly independent set. Adding a vector that is a linear combination of the others will result in a linearly dependent set.