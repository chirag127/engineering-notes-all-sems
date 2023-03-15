# Support Vector Machine

- Support Vector Machine (SVM) is a supervised machine learning model that can be used for classification or regression tasks .
- The main idea behind SVM is to find a hyperplane that maximally separates the different classes in the training data .
- A hyperplane is a linear decision boundary that splits the input space into two or more subspaces.
- A hyperplane is defined by the equation `w^T x + b = 0`, where `w` is the normal vector to the hyperplane, `x` is the input vector, and `b` is the bias term.
- The optimal hyperplane is the one that maximizes the margin, which is the distance between the hyperplane and the closest data points of each class .
- The closest data points to the hyperplane are called support vectors, and they determine the position and orientation of the hyperplane .
- SVM can handle nonlinearly separable data by using a kernel function, which maps the input data to a higher-dimensional feature space where a linear hyperplane can be found  .
- A kernel function is a function that computes the inner product of two vectors in the feature space without explicitly mapping them.
- Some common kernel functions are linear, polynomial, radial basis function (RBF), and sigmoid.
- SVM can also perform regression by using a different loss function, such as epsilon-insensitive loss, which penalizes the errors that exceed a certain threshold.
- SVM has many advantages, such as high accuracy, robustness to outliers, and ability to handle high-dimensional data .
- SVM also has some disadvantages, such as high computational cost, sensitivity to parameter selection, and difficulty in interpreting the results .
- SVM is widely used in real-world applications, such as text categorization, handwritten character recognition, image classification, biosequence analysis, and more.