### Shape Numbers for the notes of the Unit 4 - Feature Extraction in the subject of IMAGE ANALYTICS

- Shape numbers are numerical representations of the shape of an object in an image, which can be used for shape recognition and classification .
- Shape numbers can be derived from various shape features, such as boundary, contour, region, moments, Fourier descriptors, etc .
- Shape numbers can be classified into two types: global and local .
  - Global shape numbers capture the overall shape of an object, such as its area, perimeter, circularity, eccentricity, etc .
  - Local shape numbers capture the local variations of an object's boundary or contour, such as its curvature, angle, length, etc .
- Shape numbers can be computed using different methods, such as chain codes, polygonal approximation, signature, skeleton, etc .
  - Chain codes encode the direction of the boundary pixels of an object using a fixed number of symbols, such as 4 or 8 .
  - Polygonal approximation simplifies the boundary of an object by approximating it with a polygon of minimum vertices .
  - Signature represents the boundary of an object by plotting the distance or angle of each boundary pixel from a reference point or axis .
  - Skeleton reduces the object to a thin line that preserves its topology and shape features .
- Shape numbers can be used for shape-based image retrieval (SBIR), which is a technique of finding images that contain objects of similar shape to a given query image  .
  - SBIR can be performed by comparing the shape numbers of the query image and the database images using a similarity measure, such as Euclidean distance, cosine similarity, etc  .
  - SBIR can be improved by using feature selection, dimensionality reduction, and machine learning techniques, such as principal component analysis (PCA), multilayer perceptron (MLP), etc.