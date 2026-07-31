# Linear models (SVMs and Perceptrons)

Linear models are a type of machine learning algorithm that can be used for classification and regression tasks. Two common linear models are Support Vector Machines (SVMs) and Perceptrons.

## Support Vector Machines (SVMs)

SVMs are a type of linear classifier that can be used for binary classification tasks. They work by finding the hyperplane that best separates the data into two classes. The hyperplane is chosen to maximize the margin, which is the distance between the hyperplane and the closest data points from each class. These closest data points are called support vectors.

SVMs can also be used for multi-class classification by training multiple binary classifiers and combining their results. Additionally, SVMs can be extended to handle non-linearly separable data by using kernel functions to map the data into a higher-dimensional space where a linear hyperplane can be used to separate the data.

## Perceptrons

Perceptrons are another type of linear classifier that can be used for binary classification tasks. They work by finding a hyperplane that separates the data into two classes. The hyperplane is defined by a weight vector and a bias term, and the algorithm iteratively updates these parameters to minimize the classification error on the training data.

Perceptrons are similar to SVMs in that they both find a hyperplane to separate the data. However, Perceptrons use a different algorithm to find the hyperplane and do not explicitly maximize the margin like SVMs do. Additionally, Perceptrons are not as easily extended to handle non-linearly separable data or multi-class classification tasks.

In summary, SVMs and Perceptrons are two common linear models that can be used for binary classification tasks. SVMs explicitly maximize the margin between the classes and can be extended to handle non-linearly separable data and multi-class classification tasks, while Perceptrons use a different algorithm to find the separating hyperplane and are not as easily extended to handle more complex tasks.