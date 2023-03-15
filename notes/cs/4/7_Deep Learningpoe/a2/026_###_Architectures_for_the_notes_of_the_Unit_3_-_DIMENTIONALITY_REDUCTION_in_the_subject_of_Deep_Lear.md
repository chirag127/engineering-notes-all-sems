 Here is the content in markdown format:

### Architectures for the notes of the Unit 3 - DIMENTIONALITY REDUCTION in the subject of Deep Learning

1. Principal Component Analysis (PCA)
- Finds the principal components ( Directions of maximum variance in the data) and projects the data onto a lower-dimensional space using only the most significant principal components.
- Preserves as much of the variance in the data as possible.
- Useful for visualizing high-dimensional data and reducing dimensionality before further processing.
- **Mnemonic:** PCA finds the "main directions of variance" and cuts out the "less important ones".

2. Linear Discriminant Analysis (LDA)
- Projects the data onto a lower-dimensional space while preserving the separation between classes.
- Maximizes the ratio of between-class variance to within-class variance.
- Useful for classification tasks.
- **Mnemonic:** LDA finds the "directions of best separability" and throws away the rest.

3. t-Distributed Stochastic Neighbor Embedding (t-SNE)
- Converts similarities between data points into joint probabilities and tries to minimize the Kullback-Leibler divergence between the joint probabilities of the low-dimensional embedding and the high-dimensional data.
- Often produces better visualizations than PCA and LDA by being better at preserving local structure.
- More computationally expensive and doesn't have a closed-form solution, so it uses an iterative optimization approach.
- **Mnemonic:** t-SNE models "probabilities of similarity" and tries to make the low-dimensional probabilities match the high-dimensional ones.

[Additional details, diagrams, examples, pros, cons, applications, etc. can be added here if required.]