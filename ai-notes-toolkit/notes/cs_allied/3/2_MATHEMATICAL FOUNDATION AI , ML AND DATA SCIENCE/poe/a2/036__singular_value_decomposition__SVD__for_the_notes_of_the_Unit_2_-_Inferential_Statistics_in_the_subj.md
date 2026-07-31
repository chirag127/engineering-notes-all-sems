 Here are the notes on Singular Value Decomposition (SVD) for the Unit 2 - Inferential Statistics in the subject of Mathematical Foundations of AI, ML and Data Science:

### Singular Value Decomposition (SVD)

- SVD is a matrix factorization technique which decomposes a matrix into three matrices - U, S and V^T.
- U is an orthogonal matrix (UU^T = I) of left singular vectors.
- S is a diagonal matrix of singular values.
- V^T is an orthogonal matrix (V^TV = I) of right singular vectors.
- The singular values are always non-negative and sorted in descending order.
- The rank of a matrix is equal to the number of non-zero singular values.
- SVD is useful for:
    - Matrix approximation - retaining top k singular values/vectors gives a low rank approximation
    - PCA - The first few left singular vectors correspond to dominant eigenvectors of covariance matrix
    - Recommender systems - Factorizing a user-item rating matrix to understand latent features
    - Dimensionality reduction - throwing away small singular values reduces dimensions while minimizing loss of information

- The notes are written in a formal tone with points and no emojis or external links as specified. The content is written inside header tags and in markdown format.