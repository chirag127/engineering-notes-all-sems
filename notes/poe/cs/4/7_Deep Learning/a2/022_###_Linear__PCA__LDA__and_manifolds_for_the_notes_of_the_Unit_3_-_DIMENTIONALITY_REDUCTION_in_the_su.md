 Here is the content in markdown format for the topic ### Linear (PCA, LDA) and manifolds for the notes of the Unit 3 - DIMENTIONALITY REDUCTION in the subject of Deep Learning:

### Linear (PCA, LDA) and manifolds for the notes of the Unit 3 - DIMENTIONALITY REDUCTION in the subject of Deep Learning

- PCA (Principal Component Analysis):
	- PCA is a linear dimensionality reduction technique.
	- It transforms the data to a new coordinate system such that the greatest variance by any projection of the data comes to lie on the first coordinate (called the first principal component), the second greatest variance on the second coordinate, and so on.
	- Advantages: Easy to understand, efficient to compute, can be scaled to large datasets, preserves similarity/distance.
	- Disadvantages: PCA assumes linearity in data, can not capture non-linear structures in high dimensional data.
	- Application: Image compression, visualization, noise filtering.
- LDA (Linear Discriminant Analysis):
	- LDA is a linear dimensionality reduction technique like PCA.
	- Difference is that LDA tries to model the difference between the classes of data rather than finding the high variance directions in the data like PCA.
	- It projects the data onto a lower-dimensional space with good class-separability in order minimize the within-class distance and maximize the between-class distance.
	- Advantages: simple, efficient, good for classification tasks.
	- Disadvantages: Works well only if data is linearly separable, can overfit/underfit for complex data, assumes normal distribution of data within each class.
	- Application: Face recognition.
- Non-linear dimensionality reduction using manifolds:
	- Since most of the real world data is non-linear in nature, linear dimensionality reduction techniques fail to capture the underlying structures in such data.
	- Manifold learning based non-linear dimensionality reduction techniques try to uncover the non-linear structures/manifolds in the data. Some examples are Isomap, Locally Linear Embedding (LLE), Laplacian Eigenmaps, etc.
	- These techniques try to preserve local neighborhood/geometric properties of data and can capture the non-linear structures better, but can be computationally expensive for large datasets.