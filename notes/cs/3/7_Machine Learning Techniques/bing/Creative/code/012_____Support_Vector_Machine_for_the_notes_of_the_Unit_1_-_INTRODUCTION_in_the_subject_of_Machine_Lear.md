### Support Vector Machine

- Support Vector Machine (SVM) is a supervised machine learning algorithm that can be used for classification or regression tasks .
- The main idea behind SVM is to find a hyperplane that maximally separates the different classes in the training data .
- A hyperplane is a linear decision boundary that splits the input space into two or more subspaces.
- A hyperplane is defined by the equation `w.x + b = 0`, where `w` is the normal vector to the hyperplane, `x` is the input vector, and `b` is the bias term.
- The optimal hyperplane is the one that minimizes the classification error and maximizes the margin between the classes .
- The margin is the distance between the hyperplane and the closest data points from each class, called the support vectors .
- The support vectors are the data points that lie on the boundary of the margin or on the wrong side of the hyperplane .
- The SVM algorithm tries to maximize the margin by solving a quadratic optimization problem that involves the Lagrange multipliers and the Karush-Kuhn-Tucker (KKT) conditions .
- The SVM algorithm can handle linearly separable and non-linearly separable data by using different kernels  .
- A kernel is a function that maps the input data into a higher-dimensional feature space, where a linear hyperplane can be found  .
- Some common kernels are the linear kernel, the polynomial kernel, the radial basis function (RBF) kernel, and the sigmoid kernel  .
- The choice of the kernel and its parameters affects the performance and accuracy of the SVM algorithm  .
- The SVM algorithm can also be extended to handle multi-class classification, regression, and outlier detection problems  .
- SVMs deliver state-of-the-art performance in real-world applications such as text categorization, handwritten character recognition, image classification, biosequences analysis, etc., and are now established as one of the standard tools for machine learning and data mining.