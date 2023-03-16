### Orthonormal (Orthogonal) Basis

- A set of vectors $\{v_1, v_2, ..., v_n\}$ in a vector space $V$ is called an **orthogonal basis** if the vectors are linearly independent and pairwise orthogonal, i.e., $v_i \cdot v_j = 0$ for $i \neq j$.
- An orthogonal basis has the property that the length of any vector $v \in V$ can be computed as $\|v\| = \sqrt{(v \cdot v_1)^2 + (v \cdot v_2)^2 + ... + (v \cdot v_n)^2}$.
- An orthogonal basis can be normalized by dividing each vector by its length, resulting in an **orthonormal basis**, i.e., a set of vectors $\{u_1, u_2, ..., u_n\}$ such that $u_i \cdot u_j = \delta_{ij}$, where $\delta_{ij}$ is the Kronecker delta function, which is $1$ if $i = j$ and $0$ otherwise.
- An orthonormal basis has the property that the coordinates of any vector $v \in V$ with respect to the basis are given by $v = (v \cdot u_1)u_1 + (v \cdot u_2)u_2 + ... + (v \cdot u_n)u_n$.
- An orthonormal basis is also called an **orthogonal coordinate system** or an **orthogonal frame**.
- An orthonormal basis is useful for simplifying calculations involving inner products, norms, angles, and projections of vectors.
- An example of an orthonormal basis in $\mathbb{R}^2$ is $\{(1, 0), (0, 1)\}$, which is also the standard basis. An example of an orthonormal basis in $\mathbb{R}^3$ is $\{(1, 0, 0), (0, 1, 0), (0, 0, 1)\}$, which is also the standard basis. An example of an orthonormal basis that is not the standard basis is $\{(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}, 0), (-\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}, 0), (0, 0, 1)\}$, which is obtained by rotating the standard basis by $45$ degrees around the $z$-axis.
- Any vector space with an inner product has an orthonormal basis, which can be constructed by applying the **Gram-Schmidt process** to any linearly independent set of vectors. The Gram-Schmidt process is an algorithm that takes a set of vectors $\{v_1, v_2, ..., v_n\}$ and produces an orthonormal set of vectors $\{u_1, u_2, ..., u_n\}$ such that the span of $\{v_1, ..., v_k\}$ is equal to the span of $\{u_1, ..., u_k\}$ for any $k \leq n$. The algorithm works as follows:

  - Set $u_1 = \frac{v_1}{\|v_1\|}$.
  - For $k = 2, 3, ..., n$, do the following:
    - Let $w_k = v_k - (v_k \cdot u_1)u_1 - (v_k \cdot u_2)u_2 - ... - (v_k \cdot u_{k-1})u_{k-1}$, which is the projection of $v_k$ onto the orthogonal complement of the span of $\{u_1, ..., u_{k-1}\}$.
    - Set $u_k = \frac{w_k}{\|w_k\|}$.
  - Return $\{u_1, u_2, ..., u_n\}$.

- An example of applying the Gram-Schmidt process to find an orthonormal basis for $\mathbb{R}^3$ is as follows:

  - Let $\{v_1, v_2, v_3\} = \{(1, 1, 1), (1, 0, 1), (0, 1, 0)\}$.
  - Set $u_1 = \frac{v_1}{\|v_1\|} = \frac{(1, 1, 1)}{\sqrt{