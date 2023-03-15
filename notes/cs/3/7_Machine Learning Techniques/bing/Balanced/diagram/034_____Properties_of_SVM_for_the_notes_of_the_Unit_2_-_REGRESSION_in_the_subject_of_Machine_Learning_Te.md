### Properties of SVM

- Support Vector Machine (SVM) is a supervised machine learning algorithm used for both classification and regression problems  .
- The objective of SVM is to find a hyperplane in an N-dimensional space that distinctly classifies the data points into two classes .
- The hyperplane is chosen to maximize the margin, which is the distance between the hyperplane and the nearest data points of each class  .
- The data points that are closest to the hyperplane are called support vectors, and they determine the optimal hyperplane  .
- SVM is robust to outliers, as it ignores the data points that cross the margin and adds a penalty to the objective function for each violation .
- SVM can handle nonlinearly separable data by using a kernel function that transforms the data into a higher-dimensional space where a linear hyperplane can be found   .
- SVM has the property of duality, which means that the optimization problem can be solved either in the primal space (original data space) or in the dual space (kernel space).
- SVM has the property of convexity, which means that the objective function is convex and has a unique global minimum.
- SVM has the property of sparseness, which means that only a subset of the data points (support vectors) are used to determine the hyperplane, and the rest can be discarded.