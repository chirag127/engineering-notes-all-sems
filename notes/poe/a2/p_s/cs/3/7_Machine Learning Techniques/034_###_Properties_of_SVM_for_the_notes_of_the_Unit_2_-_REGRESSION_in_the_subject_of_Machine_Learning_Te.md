 Here is the content in markdown format for the given topic:

### Properties of Support Vector Machine (SVM)

1. SVM is a linear classifier. It separates the data points into two classes by drawing a hyperplane that maximizes the margin between the classes.
2. SVM can solve nonlinear classification problems by using kernel trick. The data is transformed into a higher dimensional space where it can be separated by a hyperplane. Some commonly used kernels are:
- Linear kernel: `K(x, y) = x*y`
- Polynomial kernel: `K(x, y) = (γx*y + r)^d`
- Radial basis function (RBF) kernel: `K(x, y) = exp(-γ||x-y||^2)`
3. SVM is robust to overfitting as it focuses on maximizing the margin instead of minimizing the training error.
4. The training time complexity of SVM is quadratic in the number of training examples as it essentially solves a quadratic programming problem. This makes SVM not suitable for large datasets.
5. SVM can be used for both linearly separable and non-linearly separable data. For the non-linear case, the kernel trick is used to map the data to a higher dimensional space.

Some applications of SVM are:

- Object recognition
- Image classification
- Text classification
- Bioinformatics
- Handwriting recognition

Advantages of SVM:

- Effective in high dimensional spaces.
- Still effective in cases where number of dimensions is greater than the number of samples.
- Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.
- Flexible: different kernels can be specified for the decision function.

Disadvantages of SVM:

- If the number of features is much greater than the number of samples, avoid overfitting is challenging.
- For non-linear kernel functions, determining the right parameters can be time consuming.
- Training time complexity is higher than some other algorithms due to solving a quadratic programming problem.

[Include diagrams and codes if required]