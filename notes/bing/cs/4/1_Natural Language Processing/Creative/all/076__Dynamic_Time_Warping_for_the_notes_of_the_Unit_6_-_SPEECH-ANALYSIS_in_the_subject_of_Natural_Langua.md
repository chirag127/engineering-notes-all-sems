### Dynamic Time Warping for the notes of the Unit 6 - SPEECH-ANALYSIS in the subject of Natural Language Processing

- Dynamic Time Warping (DTW) is a method to measure the similarity between two time series that may have different lengths, nonlinear distortions, and different rates .
- It was introduced in 1978 by Sakoe and Chiba to match speech patterns .
- DTW is useful for speech recognition, data mining, financial markets, and other domains where temporal alignment and similarity are important .
- DTW works by finding the optimal alignment between two time series that minimizes the distance between them .
- DTW uses a dynamic programming approach to compute a matrix of distances between all possible pairs of points from the two time series .
- DTW then finds the optimal path through the matrix that represents the best alignment between the two time series .
- The optimal path is called the warping path and it satisfies some constraints such as boundary, continuity, and monotonicity .
- The warping path can be used to calculate the warping distance, which is the sum of the distances along the path .
- The warping distance can be used as a measure of similarity or dissimilarity between the two time series .
- The lower the warping distance, the more similar the two time series are .
- DTW can handle time series that have different lengths, nonlinear distortions, and different rates by allowing the points to be stretched or compressed along the time axis .
- DTW can also handle time series that have different features or dimensions by using a suitable distance metric to compare the points .
- DTW can be generalized to handle multiple time series by using a multidimensional warping path .
- DTW can be improved by using various techniques such as windowing, pruning, lower bounding, and indexing to reduce the computational complexity and memory requirements .
- DTW can also be modified by using different constraints, distance metrics, normalization methods, and weighting schemes to suit different applications and scenarios .

#### Example of DTW

- Suppose we have two time series, X and Y, that represent the speech signals of two speakers saying the word "cat".
- X has 5 points and Y has 7 points, as shown in the figure below.

```
X: 1 2 3 4 5
Y: 1 2 3 4 5 6 7
```

- We want to measure the similarity between X and Y using DTW.
- We first compute the matrix of distances between all possible pairs of points from X and Y, using the Euclidean distance as the metric.
- The matrix is shown below, where each cell contains the distance between the corresponding pair of points.

```
    1 2 3 4 5 6 7
  +----------------
1 | 0 1 2 3 4 5 6
2 | 1 0 1 2 3 4 5
3 | 2 1 0 1 2 3 4
4 | 3 2 1 0 1 2 3
5 | 4 3 2 1 0 1 2
```

- We then find the optimal path through the matrix that minimizes the distance between X and Y, subject to some constraints.
- The constraints are:
  - The path must start at the top-left corner and end at the bottom-right corner of the matrix.
  - The path must move one step at a time, either horizontally, vertically, or diagonally.
  - The path must not move backwards or cross itself.
- The optimal path is shown below, where each cell is marked with an asterisk.

```
    1 2 3 4 5 6 7
  +----------------
1 | * 1 2 3 4 5 6
2 | 1 * 1 2 3 4 5
3 | 2 1 *