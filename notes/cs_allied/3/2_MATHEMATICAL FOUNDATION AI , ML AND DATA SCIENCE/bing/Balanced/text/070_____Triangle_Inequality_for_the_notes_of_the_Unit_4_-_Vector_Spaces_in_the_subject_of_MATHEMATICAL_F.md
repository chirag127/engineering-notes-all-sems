### Triangle Inequality

- The triangle inequality is a property of vectors that states that the norm (or length) of the sum of two vectors is less than or equal to the sum of their norms. Mathematically, for any two vectors **u** and **v** in a vector space, we have:

  $$\| \mathbf{u} + \mathbf{v} \| \leq \| \mathbf{u} \| + \| \mathbf{v} \|$$

- The triangle inequality can be understood geometrically by considering the vectors **u** and **v** as two sides of a triangle, and the vector **u** + **v** as the third side. The length of the third side is always less than or equal to the sum of the lengths of the other two sides, as shown in the figure below:

  ![Triangle Inequality](https://www.cuemath.com/geometry/images/triangle-inequality.png)

- The triangle inequality can be proved using the Cauchy-Schwarz inequality, which states that for any two vectors **u** and **v** in an inner product space, we have:

  $$| \langle \mathbf{u}, \mathbf{v} \rangle | \leq \| \mathbf{u} \| \| \mathbf{v} \|$$

- The proof of the triangle inequality is as follows:

  - Start with the norm of the vector **u** + **v** and square both sides:

    $$\| \mathbf{u} + \mathbf{v} \|^2 = \langle \mathbf{u} + \mathbf{v}, \mathbf{u} + \mathbf{v} \rangle$$

  - Use the properties of the inner product to expand the right-hand side:

    $$\| \mathbf{u} + \mathbf{v} \|^2 = \langle \mathbf{u}, \mathbf{u} \rangle + \langle \mathbf{u}, \mathbf{v} \rangle + \langle \mathbf{v}, \mathbf{u} \rangle + \langle \mathbf{v}, \mathbf{v} \rangle$$

  - Use the fact that the inner product is symmetric and real-valued to simplify the right-hand side:

    $$\| \mathbf{u} + \mathbf{v} \|^2 = \| \mathbf{u} \|^2 + 2 \langle \mathbf{u}, \mathbf{v} \rangle + \| \mathbf{v} \|^2$$

  - Apply the Cauchy-Schwarz inequality to the inner product term:

    $$\| \mathbf{u} + \mathbf{v} \|^2 \leq \| \mathbf{u} \|^2 + 2 \| \mathbf{u} \| \| \mathbf{v} \| + \| \mathbf{v} \|^2$$

  - Factor the right-hand side using the formula for the square of a sum:

    $$\| \mathbf{u} + \mathbf{v} \|^2 \leq (\| \mathbf{u} \| + \| \mathbf{v} \|)^2$$

  - Take the square root of both sides and obtain the triangle inequality:

    $$\| \mathbf{u} + \mathbf{v} \| \leq \| \mathbf{u} \| + \| \mathbf{v} \|$$

- The triangle inequality is useful for many applications in mathematics, such as measuring distances, angles, and norms of vectors and matrices. It is also a fundamental property of metric spaces, which are abstract spaces where distances between points are defined.