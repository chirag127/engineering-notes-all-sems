# Hyperplane

- A hyperplane is a linear subspace of a vector space that has one dimension less than the original space.
- For example, a hyperplane in a two-dimensional space is a line, and a hyperplane in a three-dimensional space is a plane.
- A hyperplane can be used to separate or classify data points in a vector space based on some criteria.
- A hyperplane can be defined by two terms: a normal vector **w** and an intercept term **b**.
- The normal vector **w** is perpendicular to the hyperplane and determines its orientation.
- The intercept term **b** determines the position of the hyperplane relative to the origin.
- The equation of a hyperplane is given by **w**^T^**x** + **b** = 0, where **x** is any point on the hyperplane.
- A hyperplane can divide the vector space into two half-spaces, where the points on one side satisfy **w**^T^**x** + **b** > 0 and the points on the other side satisfy **w**^T^**x** + **b** < 0.
- A hyperplane is a key tool to create support vector machines, which are machine learning models that can perform tasks such as classification and regression .
- A support vector machine tries to find the optimal hyperplane that maximizes the margin between the data points of different classes or labels.
- The margin is the distance between the hyperplane and the closest data points, which are called support vectors.
- A support vector machine can also handle nonlinearly separable data by using a kernel function to map the data to a higher-dimensional space where a hyperplane can be found.