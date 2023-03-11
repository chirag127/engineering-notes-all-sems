
### Types of Support Vector Kernels for Unit 2 - Regression in Machine Learning Techniques

1. Linear Kernel: This kernel is used when the data is linearly separable. It is represented by the equation K(x, x') = x.x'. It is used when there is no need to map the data into higher dimensional space.

2. Polynomial Kernel: This kernel is used when the data is not linearly separable and needs to be mapped into a higher dimensional space. It is represented by the equation K(x, x') = (x.x' + c)^d, where c is a constant and d is the degree of the polynomial.

3. Radial Basis Function (RBF) Kernel: This kernel is used when the data is not linearly separable and needs to be mapped into a higher dimensional space. It is represented by the equation K(x, x') = exp(-gamma * ||x-x'|| ^2), where gamma is a constant.

4. Sigmoid Kernel: This kernel is used when the data is not linearly separable and needs to be mapped into a higher dimensional space. It is represented by the equation K(x, x') = tanh(gamma * x.x' + c), where gamma and c are constants.

The advantages of using kernels in regression include improved accuracy, better generalization, and less computation time. The disadvantage of using kernels in regression is that they can be computationally expensive.

Kernels can be used in various applications such as text classification, image classification, and natural language processing. Examples of applications include sentiment analysis, document classification, and facial recognition.