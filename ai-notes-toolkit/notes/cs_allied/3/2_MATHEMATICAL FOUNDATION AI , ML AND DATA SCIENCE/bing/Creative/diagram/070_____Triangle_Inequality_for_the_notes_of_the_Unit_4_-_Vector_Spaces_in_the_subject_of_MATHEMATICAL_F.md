### Triangle Inequality

- The triangle inequality is a property of vectors that states that the norm (or length) of the sum of two vectors is less than or equal to the sum of their norms.
- Mathematically, for any two vectors **u** and **v** in a vector space, we have:

$$\| \mathbf{u} + \mathbf{v} \| \leq \| \mathbf{u} \| + \| \mathbf{v} \|$$

- The equality holds if and only if **u** and **v** are linearly dependent, that is, one is a scalar multiple of the other.
- The triangle inequality can be derived from the Cauchy-Schwarz inequality, which states that for any two vectors **u** and **v** in an inner product space, we have:

$$| \langle \mathbf{u}, \mathbf{v} \rangle | \leq \| \mathbf{u} \| \| \mathbf{v} \|$$

- The equality holds if and only if **u** and **v** are linearly dependent.
- To prove the triangle inequality, we can use the following steps:

  - Square both sides of the inequality and expand the terms using the properties of norms and inner products:

$$\| \mathbf{u} + \mathbf{v} \|^2 \leq (\| \mathbf{u} \| + \| \mathbf{v} \|)^2$$

$$\| \mathbf{u} \|^2 + 2 \langle \mathbf{u}, \mathbf{v} \rangle + \| \mathbf{v} \|^2 \leq \| \mathbf{u} \|^2 + 2 \| \mathbf{u} \| \| \mathbf{v} \| + \| \mathbf{v} \|^2$$

  - Simplify the inequality by canceling out the common terms:

$$\langle \mathbf{u}, \mathbf{v} \rangle \leq \| \mathbf{u} \| \| \mathbf{v} \|$$

  - Apply the Cauchy-Schwarz inequality to obtain the desired result:

$$\| \mathbf{u} + \mathbf{v} \| \leq \| \mathbf{u} \| + \| \mathbf{v} \|$$

- The triangle inequality can be visualized as follows:

![Triangle inequality](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Triangle_inequality.svg/1200px-Triangle_inequality.svg.png)

- In the figure, the vectors **u** and **v** are represented by the sides of a triangle, and their sum **u + v** is represented by the third side. The length of the third side is always less than or equal to the sum of the other two sides, as shown by the inequality. The equality holds only when the triangle is degenerate, that is, when the vectors are collinear.