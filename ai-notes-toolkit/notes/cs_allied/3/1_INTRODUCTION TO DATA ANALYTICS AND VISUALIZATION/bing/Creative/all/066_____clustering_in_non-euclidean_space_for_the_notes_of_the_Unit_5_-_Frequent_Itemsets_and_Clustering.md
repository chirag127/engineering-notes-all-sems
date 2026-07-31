# Clustering in Non-Euclidean Space

- Clustering is the process of grouping data points into meaningful and coherent subsets based on some similarity or distance measure.
- Non-Euclidean space is a space that does not follow the rules of Euclidean geometry, such as having a constant curvature, a non-zero angle sum for a triangle, or a different number of dimensions.
- Clustering in non-Euclidean space can be challenging because the usual notions of distance, center, and shape may not apply or may be different from the Euclidean case.
- Some examples of non-Euclidean spaces are:
  - Spherical space: the surface of a sphere, where the shortest distance between two points is along a great circle, and the angle sum of a triangle is greater than 180 degrees.
  - Hyperbolic space: a space with a constant negative curvature, where the shortest distance between two points is along a hyperbolic arc, and the angle sum of a triangle is less than 180 degrees.
  - Graph space: a space where the data points are nodes of a graph, and the distance between two points is the length of the shortest path between them, which may not be unique or symmetric.
  - Feature space: a space where the data points are vectors of attributes, and the distance between two points is a function of their similarity or dissimilarity, which may not be a metric or a norm.
- Some methods for clustering in non-Euclidean space are:
  - Non-Euclidean c-means: a generalization of the k-means algorithm that uses weighted norms to measure the distance between the feature vectors and the prototypes that represent the clusters.
  - Ward method: a hierarchical clustering method that minimizes the within-cluster variance, which can be applied to non-Euclidean similarity matrices, but may not preserve the original structure of the data.
  - Medoid method: a point-assignment clustering method that uses the most representative point of each cluster as the center, which can work with arbitrary metrics, but may not be unique or stable.
  - Spectral clustering: a clustering method that uses the eigenvectors of a similarity matrix derived from the graph structure of the data, which can capture the global properties of the data and handle non-convex clusters .
  - Density-based clustering: a clustering method that identifies clusters as regions of high density separated by regions of low density, which can handle arbitrary shapes and outliers, but may require tuning of parameters.