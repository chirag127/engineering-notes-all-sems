 Here is the content in markdown format for the topic -

### Support Vector Machine

- SVM is a supervised learning algorithm which can be used for both classification or regression problems. However, it is mainly used for classification problems.
- In SVM, we plot each data item as a point in n-dimensional space (where n is number of features) and then determine the hyper-plane that separates the data points of two classes. The hyper-plane with the largest separation between the two classes is chosen as the decision boundary.
- The data points nearest to the hyper-plane are called support vectors. The middle line is equidistant from the support vectors of both classes.
- For linear separable data, the hyper-plane that separates the two classes is a straight line. For non-linear separable data, the algorithm uses kernel trick to map the data into higher dimension to find a separating hyper-plane.
- Some key advantages of SVM are:
-- It has high accuracy in high dimensional spaces.
-- It is less prone to overfitting as it focuses on maximizing the margin between classes.
-- It uses kernel trick to deal with non-linear data.
-- It is a memory-efficient algorithm.

Some key disadvantages are:
-- It does not directly provide probability estimates, these are calculated using expensive techniques like Platt scaling.
-- It does not scale well with very large datasets.

Applications:
- SVM is widely used in tasks like object recognition, face detection, text classification, cancer classification, handwriting recognition, etc. due to its promising generalization capability and accurate predictions.

[Include diagrams and codes if required.]