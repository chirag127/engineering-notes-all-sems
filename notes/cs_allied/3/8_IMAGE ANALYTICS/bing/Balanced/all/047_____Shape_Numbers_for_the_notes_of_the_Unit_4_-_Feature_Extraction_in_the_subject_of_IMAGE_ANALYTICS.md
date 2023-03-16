# Shape Numbers for the notes of the Unit 4 - Feature Extraction in the subject of IMAGE ANALYTICS

- Shape numbers are numerical representations of the shape of an object in an image.
- Shape numbers can be used for image shape recognition and classification, as well as for content-based image retrieval (CBIR).
- Shape numbers can be derived from various shape features, such as boundary, area, perimeter, moments, Fourier descriptors, curvature, etc.
- Shape numbers can be classified into two types: global and local.
  - Global shape numbers capture the overall shape of an object, such as circularity, eccentricity, elongation, etc.
  - Local shape numbers capture the local variations of an object's boundary, such as corners, edges, curvature, etc.
- Shape numbers can be computed using different methods, such as chain codes, polygonal approximation, invariant moments, shape context, etc.
  - Chain codes encode the direction of the boundary pixels of an object using a fixed number of symbols, such as 4 or 8. The chain code can be normalized and converted into a shape number by finding the minimum value among all possible circular shifts of the code.
  - Polygonal approximation simplifies the boundary of an object by approximating it with a polygon with a fixed number of vertices. The shape number can be obtained by computing the angles and distances between the vertices and normalizing them.
  - Invariant moments are scalar values that are invariant to translation, rotation, and scaling of an object. The shape number can be formed by concatenating the invariant moments of an object.
  - Shape context is a histogram of the relative positions of the boundary pixels of an object with respect to a reference point. The shape number can be obtained by computing the shape context for each boundary pixel and concatenating them.