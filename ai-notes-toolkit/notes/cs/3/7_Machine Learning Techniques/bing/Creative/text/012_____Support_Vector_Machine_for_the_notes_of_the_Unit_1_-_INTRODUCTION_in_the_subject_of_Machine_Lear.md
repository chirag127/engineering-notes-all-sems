### Support Vector Machine

- Support Vector Machine (SVM) is a supervised machine learning model that can be used for classification or regression tasks .
- The main idea behind SVM is to find a hyperplane that maximally separates the different classes in the training data .
- A hyperplane is a d-1 dimensional subspace in a d-dimensional space that can be used as a decision boundary.
- A hyperplane is defined by a normal vector w and a bias term b, such that w.x + b = 0, where x is any point on the hyperplane.
- The optimal hyperplane is the one that maximizes the margin, which is the distance between the hyperplane and the closest points from each class, called support vectors .
- The margin can be computed as 2/||w||, where ||w|| is the norm of w.
- The optimal hyperplane can be found by solving a quadratic optimization problem that minimizes ||w||^2^ subject to some constraints that ensure the correct classification of the training data .
- The constraints are of the form y_i(w.x_i + b) >= 1, where y_i is the class label of x_i, either +1 or -1 .
- The quadratic optimization problem can be solved using the Lagrange multiplier method, which introduces a dual problem that depends only on the inner products of the data points .
- The dual problem can be solved using a kernel function, which maps the data points to a higher dimensional space where they are more likely to be linearly separable  .
- A kernel function is a function that computes the inner product of two points in the feature space without explicitly mapping them  .
- Some common kernel functions are linear, polynomial, radial basis function (RBF), and sigmoid  .
- The choice of the kernel function and its parameters can affect the performance and generalization of the SVM model  .
- SVM can also be used for regression tasks by using a different loss function, called epsilon-insensitive loss, which penalizes the errors that are larger than a given threshold epsilon .
- SVM can handle nonlinear, high-dimensional, and sparse data, and deliver state-of-the-art performance in real-world applications such as text categorization, handwritten character recognition, image classification, biosequences analysis, etc.  .