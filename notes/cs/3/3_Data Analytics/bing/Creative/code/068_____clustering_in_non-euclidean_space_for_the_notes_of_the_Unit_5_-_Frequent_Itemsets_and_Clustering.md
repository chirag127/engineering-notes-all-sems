### Clustering in Non-Euclidean Space

- Clustering is the process of grouping data points into meaningful and coherent subsets based on some similarity or distance measure.
- Non-Euclidean space is a space that does not follow the rules of Euclidean geometry, such as having a constant curvature, a non-zero angle sum for a triangle, or a different number of dimensions.
- Clustering in non-Euclidean space can be challenging because the standard methods and measures of clustering may not be applicable or appropriate.
- Some examples of non-Euclidean spaces are:
  - Spherical space: the surface of a sphere, where the shortest distance between two points is an arc of a great circle, and the angle sum of a triangle is greater than 180 degrees.
  - Hyperbolic space: a space with a constant negative curvature, where the shortest distance between two points is a hyperbolic segment, and the angle sum of a triangle is less than 180 degrees.
  - Graph space: a space where the data points are nodes of a graph, and the distance between two points is the length of the shortest path between them, which may not be unique or symmetric.
- Some methods and measures of clustering in non-Euclidean space are:
  - Non-Euclidean c-means: a generalization of the k-means algorithm that uses weighted norms to measure the distance between the feature vectors and the prototypes that represent the clusters.
  - Ward method: a hierarchical clustering method that minimizes the within-cluster variance, which can be adapted for non-Euclidean similarity by using a transformation matrix to convert the similarity into a dissimilarity.
  - Medoid: a representative point of a cluster that minimizes the sum of distances to all other points in the cluster, which can be used as a cluster center for any metric space.
  - Spectral clustering: a method that uses the eigenvectors of a similarity matrix to project the data points into a lower-dimensional space, where they can be clustered by a standard algorithm such as k-means .
  - Density-based clustering: a method that identifies clusters as regions of high density separated by regions of low density, which can be applied to any space that has a notion of neighborhood and density.