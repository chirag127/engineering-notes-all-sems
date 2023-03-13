## Unit 3 - DIMENTIONALITY REDUCTION

Dimensionality reduction is a process that transforms a high-dimensional dataset into a lower-dimensional dataset without losing the valuable properties of the original data. It is a common technique in fields that deal with large numbers of observations and/or large numbers of variables, such as signal processing, speech recognition, neuroinformatics, and bioinformatics.

Dimensionality reduction can be done in two different ways:

- By only keeping the most relevant variables from the original dataset (this technique is called **feature selection**)
- By finding a smaller set of new variables, each being a combination of the input variables, containing basically the same information as the input variables (this technique is called **dimensionality reduction**)

The following diagram illustrates the basic idea of feature selection and dimensionality reduction:

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  High-Dimensional  +----->  Feature Selection  +----->  Low-Dimensional  |
|     Dataset      |      |                 |      |     Dataset      |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+

+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  High-Dimensional  +----->  Dimensionality   +----->  Low-Dimensional  |
|     Dataset      |      |    Reduction     |      |     Dataset      |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
```

Some of the common techniques for dimensionality reduction are  :

- **Principal component analysis (PCA)**: PCA is an unsupervised machine learning algorithm that reduces the dimensions of a dataset whilst retaining as much information as possible. It does so by finding the directions of maximum variance in the data and projecting the data onto a lower-dimensional space spanned by these directions.
- **Singular value decomposition (SVD)**: SVD is a matrix factorization technique that decomposes a matrix into three smaller matrices: a left singular matrix, a diagonal matrix of singular values, and a right singular matrix. SVD can be used to reduce the dimensions of a dataset by keeping only the largest singular values and discarding the rest.
- **Linear discriminant analysis (LDA)**: LDA is a supervised machine learning algorithm that reduces the dimensions of a dataset by finding the linear combinations of the input variables that best separate the classes. It does so by maximizing the between-class variance and minimizing the within-class variance in the data.
- **t-distributed stochastic neighbor embedding (t-SNE)**: t-SNE is a nonlinear dimensionality reduction technique that preserves the local structure of the data. It does so by mapping the high-dimensional data points to low-dimensional ones in such a way that similar points are close together and dissimilar points are far apart. It uses a probabilistic measure of similarity based on the Student's t-distribution.