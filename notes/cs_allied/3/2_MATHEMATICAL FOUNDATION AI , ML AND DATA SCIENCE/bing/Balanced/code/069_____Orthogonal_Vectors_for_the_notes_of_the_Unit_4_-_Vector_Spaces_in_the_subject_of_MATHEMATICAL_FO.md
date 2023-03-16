Hello, I am Sydney, your AI assistant. I can help you with any topic you want to learn or discuss. You have asked me to write the content on the topic of orthogonal vectors for the notes of the unit 4 - vector spaces in the subject of mathematical foundation AI, ML and data science. Here is the content I have written in markdown format:

### Orthogonal Vectors

- Two vectors **u** and **v** in a vector space are called **orthogonal** if their inner product is zero, i.e., **u** · **v** = 0.
- Orthogonal vectors are also called **perpendicular** vectors, since they form a right angle with each other.
- For example, in **R**<sup>2</sup>, the vectors **u** = (1, 0) and **v** = (0, 1) are orthogonal, since **u** · **v** = 1 × 0 + 0 × 1 = 0.
- Orthogonal vectors have some important properties, such as:
  - The zero vector is orthogonal to any vector, since **0** · **v** = 0 for any **v**.
  - If **u** and **v** are orthogonal, then **u** + **v** has the same length as the hypotenuse of a right triangle with sides **u** and **v**, by the Pythagorean theorem. That is, ||**u** + **v**||<sup>2</sup> = ||**u**||<sup>2</sup> + ||**v**||<sup>2</sup>.
  - If **u** and **v** are orthogonal and nonzero, then they are linearly independent, since neither of them can be written as a scalar multiple of the other.
  - If **u** and **v** are orthogonal and have unit length, then they are called **orthonormal** vectors. Orthonormal vectors form an **orthonormal basis** for the subspace they span, which means that any vector in that subspace can be written as a linear combination of the orthonormal vectors with coefficients equal to the inner products of the vector with the basis vectors. For example, in **R**<sup>2</sup>, the vectors **u** = (1/√2, 1/√2) and **v** = (-1/√2, 1/√2) are orthonormal, and they form an orthonormal basis for **R**<sup>2</sup>. Any vector **w** = (x, y) in **R**<sup>2</sup> can be written as **w** = (**w** · **u**)**u** + (**w** · **v**)**v** = (x/2 + y/2)**u** + (-x/2 + y/2)**v**.
  - If **u** and **v** are orthogonal, then the projection of **u** onto **v** is zero, and vice versa. That is, proj<sub>**v**</sub>**u** = 0 and proj<sub>**u**</sub>**v** = 0. This means that orthogonal vectors are not influenced by each other in terms of direction or magnitude.