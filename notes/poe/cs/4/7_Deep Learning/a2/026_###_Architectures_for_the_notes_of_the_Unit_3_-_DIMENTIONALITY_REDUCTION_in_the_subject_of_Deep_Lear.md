 Here is the content in markdown format:

### Architectures for the notes of the Unit 3 - DIMENTIONALITY REDUCTION in the subject of Deep Learning

1. Principal Component Analysis (PCA)
- PCA is a linear dimensionality reduction technique.
- It transforms the data to a new coordinate system such that the greatest variance by some projection of the data comes to lie on the first coordinate (called the first principal component), the second greatest variance on the second coordinate, and so on.
- PCA tries to preserve as much of the variance in the data as possible in the lower dimensions.
- Advantages: Simple to understand, efficient to compute, can be used for visualization.
- Disadvantages: PCA cannot capture non-linear relationships in the data.
- Examples: Image compression, face recognition.

2. Linear Discriminant Analysis (LDA)
- LDA is a supervised dimensionality reduction technique.
- It projects the input data onto a lower-dimensional space while preserving as much of the class discriminatory information as possible.
- The goal is to find a linear combination of features that separates the classes as much as possible.
- Advantages: Preserves class separability, can handle nonlinear input data using kernel trick.
- Disadvantages: Sensitive to outliers, requires label information.
- Examples: Feature extraction for classification problems.

3. t-Distributed Stochastic Neighbor Embedding (t-SNE)
- t-SNE is a nonlinear dimensionality reduction technique.
- It converts similarities between data points to joint probabilities and tries to minimize the Kullback-Leibler divergence between the joint probabilities of the low-dimensional embedding and the high-dimensional data.
- t-SNE is good at capturing nonlinear structure in the data and revealing clusters of similar data points.
- Advantages: Captures non-linear relationships, reveals clusters, produces visually appealing images.
- Disadvantages: Does not preserve distances, does not have a straightforward out-of-sample extension.
- Examples: Data visualization, exploratory data analysis.