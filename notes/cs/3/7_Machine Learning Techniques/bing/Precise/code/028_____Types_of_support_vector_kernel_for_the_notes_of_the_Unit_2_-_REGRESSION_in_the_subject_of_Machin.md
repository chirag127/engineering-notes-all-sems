### Types of Support Vector Kernel

Support Vector Machines (SVMs) are a popular machine learning technique used for classification and regression analysis. SVMs use a technique called the "kernel trick" to transform the data into a higher dimensional space where it is easier to find a separating hyperplane. There are several types of kernel functions that can be used with SVMs, including:

1. **Linear Kernel:** The linear kernel is the simplest kernel function. It is given by the inner product `<x,y>+c` where `c` is a constant. This kernel is used when the data is linearly separable.

2. **Polynomial Kernel:** The polynomial kernel is a non-linear kernel function that can model non-linear relationships between the data points. It is given by `(gamma*<x,y>+c)^d` where `d` is the degree of the polynomial, `gamma` is a scaling parameter, and `c` is a constant.

3. **Radial Basis Function (RBF) Kernel:** The RBF kernel is another non-linear kernel function that is commonly used with SVMs. It is given by `exp(-gamma*||x-y||^2)` where `gamma` is a scaling parameter. This kernel is used when the data is not linearly separable and can model complex non-linear relationships.

4. **Sigmoid Kernel:** The sigmoid kernel is a non-linear kernel function that is similar to the sigmoid function used in logistic regression. It is given by `tanh(gamma*<x,y>+c)` where `gamma` is a scaling parameter and `c` is a constant. This kernel is used when the data is not linearly separable and can model non-linear relationships.

These are some of the most commonly used kernel functions with SVMs. The choice of kernel function depends on the nature of the data and the problem at hand. It is important to experiment with different kernel functions to find the one that works best for a given problem.