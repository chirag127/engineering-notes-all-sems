### Properties of SVM

- **Support Vector Machine (SVM)** is a supervised machine learning algorithm used for both classification and regression problems  .
- The objective of SVM algorithm is to find a **hyperplane** in an N-dimensional space that distinctly classifies the data points .
- A hyperplane is a decision boundary that separates the data points of different classes. It can be a line, a plane, or a higher-dimensional surface.
- The best hyperplane is the one that **maximizes the margin** between the two classes  . The margin is the distance between the hyperplane and the closest data points of each class .
- The data points that are closest to the hyperplane are called **support vectors**  . They are the most influential points in determining the optimal hyperplane .
- SVM algorithm has the characteristics to **ignore the outliers** and finds the best hyperplane that maximizes the margin. SVM is robust to outliers.
- SVM algorithm uses a **kernel function** to transform the data into a higher-dimensional space where a linear hyperplane can be found  . The kernel function can be linear, polynomial, radial basis function (RBF), or sigmoid  .
- SVM algorithm is based on the **duality principle** which allows to solve the optimization problem in either the primal or the dual space. The dual space has the advantage of being easier to solve and allowing the use of kernel functions .
- SVM algorithm is a **convex optimization** problem which means that it has a unique global solution and no local minima . This makes SVM algorithm more reliable and stable than other algorithms that may get stuck in suboptimal solutions .
- SVM algorithm is **sparse** which means that only a subset of the data points (the support vectors) are used to determine the hyperplane . This reduces the computational complexity and memory requirements of the algorithm .