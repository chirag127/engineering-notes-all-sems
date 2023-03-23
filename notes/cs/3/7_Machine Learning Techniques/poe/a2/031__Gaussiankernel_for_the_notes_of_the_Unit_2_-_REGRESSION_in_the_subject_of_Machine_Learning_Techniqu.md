 Here is the content in markdown format without any emojis or external links:

### Gaussiankernel for the notes of the Unit 2 - REGRESSION in the subject of Machine Learning Techniques

1. Gaussian kernel is a kernel function used in kernel methods for pattern analysis and machine learning techniques.
2. It is used to transform the input data to a higher dimensional space. This transformation makes the datapoints separable so that they can be classified using a hyperplane.
3. The Gaussian kernel is a radial basis function kernel. It means that it depends only on the distance between the points x and y.
4. The Gaussian kernel is parameterized by a parameter σ > 0 (also called the bandwidth). Larger values of σ lead to more smoothing, while smaller values lead to less smoothing.
5. The Gaussian kernel has the form :

K(x, y) = e^- (||x-y||^2 / 2σ^2 )

6. Sigma (σ) is a hyperparameter that controls the "width" of the kernel and therefore the flexibility of the resulting classifier. A smaller sigma means that points must be closer to be considered similar. A larger sigma means more points are considered similar.
7. The Gaussian kernel produces smooth decision boundaries and is a good default kernel choice. However, the optimal value of sigma (σ) can be hard to select.
8. Some pros and cons of the Gaussian kernel are:

Pros:
- Smooth decision boundaries
- Flexible (can capture non-linearities)
- Locally-weighted (points nearby in input space get high weights)

Cons:
- Finding an optimal σ value can be challenging
- Can overfit if σ is too small
- Computing time increases with number of support vectors (due to evaluating kernel on all pairs of points)