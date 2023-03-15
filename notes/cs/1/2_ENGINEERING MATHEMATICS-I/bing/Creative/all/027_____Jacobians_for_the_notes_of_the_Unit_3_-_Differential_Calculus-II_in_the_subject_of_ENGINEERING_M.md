# Jacobians

- A **Jacobian matrix** is a matrix that contains the **first-order partial derivatives** of a **vector-valued function** of several variables  .
- A vector-valued function is a function that takes one or more variables as input and outputs a vector, such as $\mathbf{f}(x,y) = (x^2 + y, y^2 - x)$.
- The Jacobian matrix can be used to **approximate the change** of the vector-valued function near a given point, by using a **linear transformation** .
- The Jacobian matrix can also be used to **convert integrals** from one coordinate system to another, by using the **Jacobian determinant** .
- The **Jacobian determinant** is the **determinant** of the Jacobian matrix, and it represents the **ratio of the area** (or volume) elements in the two coordinate systems .
- The Jacobian matrix and determinant depend on the **order** and **choice** of the variables in the vector-valued function and the coordinate system .

## Example

- Consider the vector-valued function $\mathbf{f}(x,y) = (x^2 + y, y^2 - x)$ and the point $(1,1)$.
- The Jacobian matrix of $\mathbf{f}$ at $(1,1)$ is given by

$$
\mathbf{J}(\mathbf{f})|_{(1,1)} = \begin{bmatrix}
\frac{\partial f_1}{\partial x} & \frac{\partial f_1}{\partial y} \\
\frac{\partial f_2}{\partial x} & \frac{\partial f_2}{\partial y}
\end{bmatrix}|_{(1,1)} = \begin{bmatrix}
2x & 1 \\
-1 & 2y
\end{bmatrix}|_{(1,1)} = \begin{bmatrix}
2 & 1 \\
-1 & 2
\end{bmatrix}
$$

- The Jacobian determinant of $\mathbf{f}$ at $(1,1)$ is given by

$$
\det(\mathbf{J}(\mathbf{f}))|_{(1,1)} = 2 \times 2 - 1 \times (-1) = 5
$$

- The Jacobian matrix can be used to approximate the change of $\mathbf{f}$ near $(1,1)$, by using the formula

$$
\mathbf{f}(x,y) \approx \mathbf{f}(1,1) + \mathbf{J}(\mathbf{f})|_{(1,1)} \begin{bmatrix}
x - 1 \\
y - 1
\end{bmatrix}
$$

- The Jacobian determinant can be used to convert integrals from the Cartesian coordinate system $(x,y)$ to the polar coordinate system $(r,\theta)$, by using the formula

$$
\int \int_R f(x,y) \, dx \, dy = \int \int_S f(r \cos \theta, r \sin \theta) \, |\det(\mathbf{J}(r,\theta))| \, dr \, d\theta
$$

where $R$ is the region in the Cartesian plane, $S$ is the region in the polar plane, and $\mathbf{J}(r,\theta)$ is the Jacobian matrix of the transformation from $(x,y)$ to $(r,\theta)$, which is given by

$$
\mathbf{J}(r,\theta) = \begin{bmatrix}
\frac{\partial x}{\partial r} & \frac{\partial x}{\partial \theta} \\
\frac{\partial y}{\partial r} & \frac{\partial y}{\partial \theta}
\end{bmatrix} = \begin{bmatrix}
\cos \theta & -r \sin \theta \\
\sin \theta & r \cos \theta
\end{bmatrix}
$$

and $\det(\mathbf{J}(r,\theta)) = r$.