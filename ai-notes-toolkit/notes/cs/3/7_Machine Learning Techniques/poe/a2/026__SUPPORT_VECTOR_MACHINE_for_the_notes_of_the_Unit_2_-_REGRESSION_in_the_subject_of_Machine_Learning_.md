 Here are the notes for SUPPORT VECTOR MACHINE for the Unit 2 - REGRESSION in Machine Learning Techniques:

### SUPPORT VECTOR MACHINE

1. SVM is a supervised learning algorithm which is used for classification and regression problems.
2. In SVM, we plot each data item as a point in n-dimensional space (where n is number of features) and then perform classification by finding the hyperplane that separates the data points of two classes.
3. The hyperplane is the line that separates the two classes and is at the maximized margin from the nearest points of each class. These nearest points are called support vectors.
4. For linearly separable data, the hyperplane can be found by maximizing the margin margin = w/||w||. This is formulated as a constrained optimization problem.
5. For non-linearly separable data, kernel tricks are used to map the non-linear input space to a higher-dimensional linear separable feature space. Some common kernels are:
 - Linear Kernel: K(x, y) = x*y
 - Polynomial Kernel: K(x, y) = (x*y + c)^d where c and d are parameters.
 - Radial Basis Function Kernel: K(x, y) = exp(-??||x-y||^2) where ?? is a parameter.
6. For regression problems using SVR (Support Vector Regression), the loss function to minimize is epsilon-insensitive loss function. The SVM finds a hyperplane with maximum margin for regression.

The notes cover the key points about SVM for classification and regression problems. The points are written in a formal tone with no emojis or external links as per the instructions. Let me know if you would like me to elaborate on any of the points or modify the notes.