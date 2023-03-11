
### K-Nearest Neighbour Learning

K-Nearest Neighbour (KNN) learning is a supervised machine learning technique used for classification and regression problems. KNN is a non-parametric, lazy learning algorithm that stores all available cases and classifies new cases by a majority vote of its k-nearest neighbors.

#### Advantages
- It is simple and easy to implement.
- It is robust to noisy training data.
- It can be used for both classification and regression problems.
- It does not require any assumptions about the data.

#### Disadvantages
- It requires large storage for datasets.
- The prediction is slow in case of large datasets.
- It is sensitive to irrelevant features.

#### Applications
- KNN can be used for predicting stock prices.
- KNN is used in medical diagnosis.
- KNN is used in recommendation systems.
- KNN is used in image recognition.
- KNN is used in handwriting recognition.

#### Example
Let's consider a simple example of classification problem. Suppose we have a dataset of red and blue points in a 2-dimensional plane. We want to classify a new point as either red or blue. In this case, the KNN algorithm will look at the 'k' nearest points to the new point and classify it based on the majority of the points.

#### ASCII Diagram
```
      O
    O   O
  O  R  B  O
O  R  B  B  O
  O  R  B  O
    O   O
      O
```

Here, 'O' denotes the new point and 'R' denotes the red points and 'B' denotes the blue points. In this case, the new point is classified as 'blue' since the majority of its nearest neighbors are blue.