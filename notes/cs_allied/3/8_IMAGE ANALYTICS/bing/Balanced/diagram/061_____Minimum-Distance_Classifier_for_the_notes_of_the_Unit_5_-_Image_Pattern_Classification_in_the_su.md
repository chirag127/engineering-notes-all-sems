### Minimum-Distance Classifier

- A minimum-distance classifier is a supervised image classification technique that assigns an unknown image data to a class that minimizes the distance between the image data and the class in a multi-feature space .
- The distance is defined as an index of similarity so that the minimum distance is identical to the maximum similarity.
- The distance can be measured by different metrics, such as Euclidean distance, Mahalanobis distance, or spectral angle mapper .
- The minimum-distance classifier requires the mean values of the classes as the reference points for the distance calculation .
- The mean values of the classes can be obtained from training samples or from prior knowledge .
- The minimum-distance classifier can be represented by the following algorithm:

  - For each class, compute the mean vector from the training samples or from prior knowledge.
  - For each unknown image data, calculate the distance between the image data and each class mean vector using a chosen metric.
  - Assign the image data to the class with the minimum distance.

- The minimum-distance classifier is simple and fast, but it may not be accurate if the classes have different variances or covariances .
- The minimum-distance classifier can be improved by using weighted distances, quadratic discriminant functions, or neural networks .
- The minimum-distance classifier can be illustrated by the following diagram:

![Minimum-Distance Classifier Diagram](https://drr.ikcest.org/remote-sensing-tutorial/chapter01/Sect1_180_files/image002.jpg)

- The minimum-distance classifier is widely used in remote sensing applications, such as land cover classification, crop identification, and change detection  .