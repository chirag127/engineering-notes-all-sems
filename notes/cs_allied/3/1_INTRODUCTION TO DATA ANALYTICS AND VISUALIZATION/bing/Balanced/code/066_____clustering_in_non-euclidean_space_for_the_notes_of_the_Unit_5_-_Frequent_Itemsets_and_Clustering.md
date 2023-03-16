### Clustering in Non-Euclidean Space

- Clustering is the process of grouping data points into meaningful and coherent subsets based on some similarity or distance measure.
- Non-Euclidean space is a space that does not follow the rules of Euclidean geometry, such as having a constant curvature, a non-zero angle sum for a triangle, or a different number of dimensions.
- Clustering in non-Euclidean space can be challenging because the usual notions of distance, center, and shape may not apply or may be different from the Euclidean case.
- Some examples of non-Euclidean spaces are:
  - Spherical space, where the distance between two points is the length of the shortest arc on the sphere connecting them, and the center of a cluster is the point that minimizes the sum of squared distances to all cluster members.
  - Hyperbolic space, where the distance between two points is the natural logarithm of the cross-ratio of four points on a line, and the center of a cluster is the point that minimizes the sum of hyperbolic distances to all cluster members.
  - Graph space, where the distance between two nodes is the length of the shortest path connecting them, and the center of a cluster is the node that has the smallest average distance to all cluster members.
- Some methods for clustering in non-Euclidean space are:
  - Non-Euclidean c-means, which generalizes the k-means algorithm by using weighted norms to measure the distance between feature vectors and cluster prototypes.
  - Ward method, which is a hierarchical clustering algorithm that minimizes the within-cluster sum of squares, but requires a positive definite similarity matrix.
  - Medoid method, which is a point-assignment clustering algorithm that uses the most representative point in each cluster as the center, and works with arbitrary metrics.
  - Spectral clustering, which is a graph-based clustering algorithm that uses the eigenvectors of the graph Laplacian matrix to embed the data points into a lower-dimensional Euclidean space, and then applies k-means or another clustering algorithm  .