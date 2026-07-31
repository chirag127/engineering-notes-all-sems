### Singular Value Decomposition (SVD)

- Singular Value Decomposition (SVD) is a factorization of a matrix into three matrices .
- SVD can be applied to any matrix, regardless of its shape, symmetry, or rank  .
- SVD has some interesting algebraic properties and conveys important geometrical and theoretical insights about linear transformations .
- SVD is a fundamental technique for multivariate data analysis, as it can reduce the dimension of the problem by choosing a small linear subspace that captures important properties of the data .
- SVD also has some important applications in data science, such as image compression, noise reduction, principal component analysis, latent semantic analysis, and recommender systems .

#### SVD Formula

- Given a matrix A of size m x n, SVD decomposes A into three matrices U, Σ, and V such that A = UΣV<sup>T</sup>     .
- U is an m x m orthogonal matrix, whose columns are called the left singular vectors of A    .
- Σ is an m x n diagonal matrix, whose diagonal elements are called the singular values of A    .
- V is an n x n orthogonal matrix, whose columns are called the right singular vectors of A    .
- The singular values of A are the square roots of the eigenvalues of A<sup>T</sup>A or AA<sup>T</sup>, and they are arranged in descending order along the diagonal of Σ    .
- The left singular vectors of A are the eigenvectors of AA<sup>T</sup>, and the right singular vectors of A are the eigenvectors of A<sup>T</sup>A    .
- The rank of A is equal to the number of nonzero singular values of A    .

#### SVD Example

- Consider the matrix A = \\twomat22−1−2 .
- The SVD of A is A = UΣV<sup>T</sup>, where U = \\twomat1 / √21 / √2−1 / √21 / √2, Σ = \\twomat√80, V = \\twomat10−11 .
- The singular values of A are σ<sub>1</sub> = √8 and σ<sub>2</sub> = 0, and they are the square roots of the eigenvalues of A<sup>T</sup>A = \\twomat50−50 .
- The left singular vectors of A are u<sub>1</sub> = \\twovec1 / √21 / √2 and u<sub>2</sub> = \\twovec−1 / √21 / √2, and they are the eigenvectors of AA<sup>T</sup> = \\twomat40−40 .
- The right singular vectors of A are v<sub>1</sub> = \\twovec10 and v<sub>2</sub> = \\twovec−11, and they are the eigenvectors of A<sup>T</sup>A = \\twomat50−50 .
- The rank of A is 1, as there is only one nonzero singular value of A.

#### SVD Properties

- SVD is unique, up to the signs of the singular vectors   .
- SVD can be computed efficiently using numerical algorithms, such as the power method or the QR algorithm