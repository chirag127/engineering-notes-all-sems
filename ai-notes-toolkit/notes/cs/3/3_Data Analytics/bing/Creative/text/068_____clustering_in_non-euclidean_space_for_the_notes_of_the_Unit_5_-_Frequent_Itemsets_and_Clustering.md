### Clustering in Non-Euclidean Space

- Clustering is the process of grouping data points into meaningful and coherent subsets based on some similarity or distance measure.
- Non-Euclidean space is a space that does not follow the rules of Euclidean geometry, such as having a constant curvature, a non-zero angle sum for a triangle, or a different number of dimensions.
- Clustering in non-Euclidean space can be challenging because the standard methods and measures of clustering may not be applicable or appropriate for the data.
- Some examples of non-Euclidean spaces are:
  - Spherical space: the surface of a sphere, where the shortest distance between two points is not a straight line, but an arc of a great circle.
  - Hyperbolic space: a space with a constant negative curvature, where the area of a circle grows exponentially with its radius, and parallel lines diverge from each other.
  - Graph space: a space where the data points are nodes of a graph, and the distance between them is defined by the length or weight of the shortest path connecting them.
- Some methods and measures of clustering in non-Euclidean space are:
  - Non-Euclidean c-means: a generalization of the k-means algorithm that uses weighted norms to measure the distance between the feature vectors and the cluster prototypes.
  - Ward method: a hierarchical clustering method that minimizes the within-cluster variance, but requires the similarity matrix to be positive definite.
  - Medoid: a representative point of a cluster that minimizes the sum of distances to all other points in the cluster, which works with arbitrary metrics.
  - Spectral clustering: a method that uses the eigenvectors of the graph Laplacian matrix to embed the data points into a lower-dimensional Euclidean space, where k-means or other methods can be applied  .