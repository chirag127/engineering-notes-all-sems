### Hyperplane

- A hyperplane is a subspace of one dimension less than its ambient space.
- In the context of regression, a hyperplane is a linear decision boundary that separates the data into different classes or categories.
- In a two-dimensional space, a hyperplane is a line. In a three-dimensional space, it is a plane, and in higher dimensions, it is called a hyperplane.
- The equation of a hyperplane is given by `w^T x + b = 0`, where `w` is the weight vector, `x` is the input vector, and `b` is the bias term.
- The weight vector `w` is perpendicular to the hyperplane and determines its orientation, while the bias term `b` determines its position.
- The distance of a point `x` from the hyperplane is given by `|w^T x + b| / ||w||`.
- In the context of support vector machines, the hyperplane is chosen to maximize the margin, which is the distance between the hyperplane and the closest data points from each class.
- The points closest to the hyperplane are called support vectors, and they determine the position and orientation of the hyperplane.
- The hyperplane can be used for both linear and non-linear classification by using kernel functions to map the data into a higher-dimensional space where a linear hyperplane can be used to separate the data.