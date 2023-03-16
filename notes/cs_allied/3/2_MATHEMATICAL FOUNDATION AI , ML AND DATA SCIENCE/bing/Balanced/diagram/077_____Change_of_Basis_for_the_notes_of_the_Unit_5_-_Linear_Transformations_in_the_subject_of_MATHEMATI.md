### Change of Basis

- Change of basis is a technique applied to finite-dimensional vector spaces in order to rewrite vectors in terms of a different set of basis elements .
- A basis is a set of linearly independent vectors that span the vector space .
- The coordinates of a vector depend on the choice of basis .
- To change the basis of a vector, we need to find a linear transformation that maps the old basis to the new basis  .
- The matrix of this linear transformation is called the change of basis matrix .
- The change of basis matrix can be found by writing the new basis vectors as column vectors in a matrix and then finding its inverse  .
- The change of basis matrix can be used to convert the coordinates of any vector from the old basis to the new basis by multiplying the matrix with the vector  .
- The change of basis matrix is unique for a given pair of bases.
- The change of basis matrix is invertible and its inverse is the change of basis matrix from the new basis to the old basis .
- The change of basis matrix preserves the inner product and the norm of vectors.

#### Example

Let $V$ be a vector space with the standard basis $\{e_1, e_2\}$, where $e_1 = (1, 0)$ and $e_2 = (0, 1)$. Let $B = \{v_1, v_2\}$ be another basis for $V$, where $v_1 = (2, 1)$ and $v_2 = (1, -1)$. Find the change of basis matrix from $B$ to the standard basis and use it to find the coordinates of the vector $u = (3, 4)$ with respect to $B$.

##### Solution

To find the change of basis matrix from $B$ to the standard basis, we write the vectors $v_1$ and $v_2$ as column vectors in a matrix and then find its inverse:

$$
C = \begin{bmatrix} 2 & 1 \\ 1 & -1 \end{bmatrix}
$$

$$
C^{-1} = \frac{1}{-2 - 1} \begin{bmatrix} -1 & -1 \\ -1 & 2 \end{bmatrix} = \begin{bmatrix} \frac{1}{3} & \frac{1}{3} \\ \frac{1}{3} & -\frac{2}{3} \end{bmatrix}
$$

This is the change of basis matrix from $B$ to the standard basis. To find the coordinates of $u$ with respect to $B$, we multiply $C^{-1}$ with $u$:

$$
[u]_B = C^{-1}u = \begin{bmatrix} \frac{1}{3} & \frac{1}{3} \\ \frac{1}{3} & -\frac{2}{3} \end{bmatrix} \begin{bmatrix} 3 \\ 4 \end{bmatrix} = \begin{bmatrix} \frac{7}{3} \\ -\frac{1}{3} \end{bmatrix}
$$

Therefore, the coordinates of $u$ with respect to $B$ are $(\frac{7}{3}, -\frac{1}{3})$.