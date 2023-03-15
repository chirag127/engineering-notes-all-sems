# Support Vector Machine

- Support Vector Machine (SVM) is a supervised machine learning model that can be used for classification or regression tasks .
- The main idea behind SVM is to find a hyperplane that maximally separates the different classes in the training data .
- A hyperplane is a subspace of one dimension less than the original space. For example, a hyperplane in a two-dimensional space is a line, and a hyperplane in a three-dimensional space is a plane.
- A hyperplane can be defined by a normal vector and a bias term. The normal vector is perpendicular to the hyperplane, and the bias term determines the offset of the hyperplane from the origin.
- The optimal hyperplane is the one that maximizes the margin between the hyperplane and the closest points of each class. These points are called support vectors, as they support the hyperplane .
- The margin is the distance between the hyperplane and the support vectors. The larger the margin, the better the generalization of the classifier .
- To find the optimal hyperplane, SVM solves a quadratic optimization problem that minimizes the norm of the normal vector subject to some constraints that ensure the correct classification of the support vectors .
- Sometimes, the data is not linearly separable, meaning that there is no hyperplane that can separate the classes perfectly. In this case, SVM can use a technique called kernel trick to map the data to a higher-dimensional space where it becomes linearly separable  .
- A kernel is a function that computes the inner product of two vectors in the mapped space without explicitly performing the mapping. Some common kernels are linear, polynomial, radial basis function (RBF), and sigmoid  .
- SVM can also handle multi-class classification problems by using one-vs-one or one-vs-all strategies, where multiple binary classifiers are trained and combined to make the final decision .
- SVM has many advantages, such as high accuracy, robustness to outliers, and ability to handle nonlinear and high-dimensional data. However, it also has some disadvantages, such as high computational cost, sensitivity to parameter selection, and lack of interpretability  .