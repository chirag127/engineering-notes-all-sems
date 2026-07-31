### Singular Value Decomposition (SVD)

- Singular Value Decomposition (SVD) is a fundamental technique in data science, providing the mathematical basis for many modern algorithms, including text mining, recommender systems, image processing, and classification problems.
- SVD is a way of factorizing a matrix: any real matrix A of size m x n decomposes as A = USigma V^T.
- The singular values are defined as the square root of the obtained Eigen values.
- SVD divides a matrix into 2 unitary matrices that are orthogonal in nature and a rectangular diagonal matrix containing singular values till r.
- The SVD produces orthonormal bases of v’s and u’s for the four fundamental subspaces.
- Using those bases, A becomes a diagonal matrix Σ and Avi = σiui: σi = singular value.
- The two-bases diagonalization A = UΣV T often has more information than A = XΛX−1.
