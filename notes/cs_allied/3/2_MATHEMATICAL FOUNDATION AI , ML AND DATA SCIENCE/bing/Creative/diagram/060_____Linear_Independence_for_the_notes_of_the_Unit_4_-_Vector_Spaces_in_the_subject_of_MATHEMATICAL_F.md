Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of Mathematical Foundation AI, ML and Data Science. Here is the content for the topic of Linear Independence for the notes of the Unit 4 - Vector Spaces.

### Linear Independence

- A set of vectors is said to be **linearly independent** if none of the vectors can be written as a linear combination of the others.
- A set of vectors is said to be **linearly dependent** if at least one of the vectors can be written as a linear combination of the others.
- A set of vectors is linearly dependent if and only if there exists a non-trivial linear combination of the vectors that equals the zero vector, i.e., there exists scalars c1, c2, ..., cn, not all zero, such that c1v1 + c2v2 + ... + cnvn = 0.
- A set of vectors is linearly independent if and only if the only linear combination of the vectors that equals the zero vector is the trivial one, i.e., the scalars c1, c2, ..., cn are all zero.
- A set of vectors that contains the zero vector is always linearly dependent, since the zero vector can be written as a linear combination of the other vectors with zero coefficients.
- A set of vectors that contains only one non-zero vector is always linearly independent, since the only way to write the non-zero vector as a linear combination of the other vectors is to multiply it by one and the zero vector by zero.
- A set of two vectors is linearly dependent if and only if one of the vectors is a scalar multiple of the other, i.e., there exists a scalar k such that v1 = kv2 or v2 = kv1.
- A set of two vectors is linearly independent if and only if they are not scalar multiples of each other, i.e., there is no scalar k such that v1 = kv2 or v2 = kv1.
- A set of n vectors in R^n is linearly dependent if and only if the determinant of the matrix formed by the vectors as columns (or rows) is zero.
- A set of n vectors in R^n is linearly independent if and only if the determinant of the matrix formed by the vectors as columns (or rows) is non-zero.
- A set of more than n vectors in R^n is always linearly dependent, since there are more vectors than dimensions, and hence there must be some linear dependence among them.
- A set of less than n vectors in R^n may or may not be linearly independent, depending on the vectors. For example, the standard basis vectors e1, e2, ..., en are linearly independent, but any subset of them is also linearly independent. However, the vectors (1, 0), (0, 1), and (1, 1) in R^2 are linearly dependent, since the third vector is the sum of the first two.