# Minimum-Distance Classifier

- A minimum-distance classifier is a supervised image classification technique that assigns an unknown image data to a class that minimizes the distance between the image data and the class in a multi-feature space .
- The distance is defined as an index of similarity so that the minimum distance is identical to the maximum similarity.
- The distance can be measured by different metrics, such as Euclidean distance, Mahalanobis distance, or spectral angle mapper .
- The minimum-distance classifier requires the mean values of the classes as the reference points for the distance calculation .
- The mean values of the classes can be obtained from training samples or prior knowledge .
- The minimum-distance classifier can be illustrated by the following steps :
  - For each class, calculate the mean value of each band from the training samples.
  - For each unknown pixel, calculate the distance between its value and the mean value of each class for each band.
  - Sum up the distances for each band to get the total distance for each class.
  - Assign the pixel to the class with the smallest total distance.
- The minimum-distance classifier is simple and fast, but it may not be very accurate if the classes have different variances or covariances  .
- The minimum-distance classifier can be improved by using weighted distances, adaptive thresholds, or fuzzy membership functions  .