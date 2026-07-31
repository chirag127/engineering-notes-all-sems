# Minimum-Distance Classifier

- A minimum-distance classifier is a supervised image classification technique that assigns an unknown image data to a class that minimizes the distance between the image data and the class in a multi-feature space .
- The distance is defined as an index of similarity so that the minimum distance is identical to the maximum similarity.
- The distance can be measured by different metrics, such as Euclidean distance, Mahalanobis distance, or spectral angle mapper .
- The minimum-distance classifier requires the mean values of the classes as the reference points for the distance calculation .
- The mean values of the classes can be obtained from training samples that represent the spectral characteristics of the classes .
- The minimum-distance classifier can be formulated as follows:

  - Let x be an unknown image data vector, and let m<sub>i</sub> be the mean vector of class i, i = 1, 2, ..., c, where c is the number of classes.
  - The distance between x and m<sub>i</sub> can be computed by any distance metric, such as d(x, m<sub>i</sub>) = ||x - m<sub>i</sub>||<sub>2</sub>, where ||.||<sub>2</sub> denotes the Euclidean norm.
  - The minimum-distance classifier assigns x to the class that has the smallest distance to x, i.e.,

    - x belongs to class j if and only if d(x, m<sub>j</sub>) = min<sub>i</sub> d(x, m<sub>i</sub>).

- The minimum-distance classifier is simple and fast, but it has some limitations :

  - It assumes that the classes have equal variance and covariance, which may not be true in reality.
  - It does not take into account the shape and size of the class clusters, which may affect the classification accuracy.
  - It may be sensitive to outliers and noise in the training samples, which may distort the mean values of the classes .
  - It may produce ambiguous results when the distances to multiple classes are very close or equal.