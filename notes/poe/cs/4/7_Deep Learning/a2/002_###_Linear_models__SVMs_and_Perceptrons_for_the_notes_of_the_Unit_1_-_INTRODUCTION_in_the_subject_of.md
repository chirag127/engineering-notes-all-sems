 Here is the content in markdown format for the topic ### Linear models (SVMs and Perceptrons for the notes of the Unit 1 - INTRODUCTION in the subject of Deep Learning:

### Linear models (SVMs and Perceptrons)

- **Perceptrons**: Perceptrons are the simplest type of neural networks. They are linear classifiers that classify data points into two classes (binary classification) by determining which side of a hyperplane they fall on. They have a set of inputs and weights and a threshold function that outputs a class.
- **Advantages**: Simple to understand and implement. Can learn linear decision boundaries.
- **Disadvantages**: Limited to only linear separable problems. Cannot learn complex non-linear patterns.

- **Support Vector Machines (SVMs)**: SVMs are more advanced linear models that use a hyperplane to classify data points. They aim to maximize the margin (distance) between the hyperplane and closest data points of each class. The closest data points are called support vectors. SVMs can handle non-linear data using kernel tricks that project the data into higher dimensional space.
- **Advantages**: Effective in high-dimensional spaces. Flexible (can handle linear and non-linear data). Often gives good performance.
- **Disadvantages**: Complexity increases with kernel tricks and higher dimensions. Overfitting can occur. Choosing kernels and parameters can be challenging.

**Mnemonics**:
- Perceptrons: "Simple neurons with weights and threshold"
- SVMs: "Max margin hyperplanes with support vectors"

**Application examples**:
- Perceptrons: Basic image classification, spam detection.
- SVMs: Complex image classification, text classification, regression.

The above content summarizes the key points about Perceptrons and SVMs which are simple linear models used for classification in Deep Learning. The advantages, disadvantages, mnemonics and application examples mentioned can help in learning and understanding these models for exams. Please let me know if you would like me to elaborate on any part of the content.