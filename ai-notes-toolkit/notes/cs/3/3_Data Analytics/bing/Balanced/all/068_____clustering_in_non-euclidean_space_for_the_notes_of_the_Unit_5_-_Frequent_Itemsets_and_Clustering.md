# Clustering in Non-Euclidean Space

- Clustering is the process of grouping data points into meaningful and coherent subsets based on some similarity or distance measure.
- Non-Euclidean space is a space that does not follow the rules of Euclidean geometry, such as having a constant curvature, a different number of dimensions, or a different metric.
- Clustering in non-Euclidean space is challenging because the standard methods and assumptions of Euclidean clustering may not apply or be optimal.
- Some examples of non-Euclidean spaces are:
  - Spherical space: the surface of a sphere, where the distance between two points is the length of the shortest arc connecting them, and the sum of the angles of a triangle is more than 180 degrees.
  - Hyperbolic space: a space with constant negative curvature, where the distance between two points is the length of the shortest curve connecting them, and the sum of the angles of a triangle is less than 180 degrees.
  - Graph space: a space where the data points are nodes of a graph, and the distance between two points is the length of the shortest path connecting them, or some function of the edge weights.
  - Feature space: a space where the data points are vectors of attributes, and the distance between two points is some function of the vector norms and angles, such as the cosine similarity or the Mahalanobis distance.
- Some methods and techniques for clustering in non-Euclidean space are:
  - Non-Euclidean c-means: a generalization of the k-means algorithm that uses weighted norms to measure the distance between the feature vectors and the cluster prototypes.
  - Ward method: a hierarchical clustering method that minimizes the within-cluster variance, which can be adapted to non-Euclidean similarity by using a transformation matrix.
  - Medoid method: a point-assignment clustering method that uses the most representative point of each cluster as the centroid, which can work with arbitrary metrics.
  - Spectral clustering: a clustering method that uses the eigenvectors of the graph Laplacian matrix to embed the data points into a lower-dimensional Euclidean space, where k-means or other methods can be applied .
  - Density-based clustering: a clustering method that identifies clusters as regions of high density separated by regions of low density, which can work with arbitrary metrics and shapes.