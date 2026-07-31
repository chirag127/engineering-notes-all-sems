## Unit 4 - Complex Variable–Differentiation

- A complex variable is a variable that can take the form of a complex number, which is a number of the form $z = x + iy$, where $x$ and $y$ are real numbers and $i$ is the imaginary unit such that $i^2 = -1$.
- A complex function is a function that maps complex numbers to complex numbers, such as $f(z) = z^2 + 2z + 1$.
- The derivative of a complex function is defined as the limit of the difference quotient, similar to the real case, as follows:

$$f'(z) = \lim_{\Delta z \to 0} \frac{f(z + \Delta z) - f(z)}{\Delta z}$$

- However, unlike the real case, the limit of the difference quotient may depend on the direction of approach of $\Delta z$ to $0$. For example, consider the function $f(z) = |z|^2$, which is not differentiable at any point. If we approach $z = 0$ along the real axis, we have:

$$f'(0) = \lim_{\Delta x \to 0} \frac{f(0 + \Delta x) - f(0)}{\Delta x} = \lim_{\Delta x \to 0} \frac{|\Delta x|^2 - 0}{\Delta x} = \lim_{\Delta x \to 0} |\Delta x| = 0$$

- But if we approach $z = 0$ along the imaginary axis, we have:

$$f'(0) = \lim_{\Delta y \to 0} \frac{f(0 + i\Delta y) - f(0)}{i\Delta y} = \lim_{\Delta y \to 0} \frac{|i\Delta y|^2 - 0}{i\Delta y} = \lim_{\Delta y \to 0} \frac{-\Delta y^2}{i\Delta y} = \lim_{\Delta y \to 0} -i\Delta y = 0$$

- However, if we approach $z = 0$ along any other direction, such as $z = \Delta x + i\Delta x$, we have:

$$f'(0) = \lim_{\Delta x \to 0} \frac{f(0 + \Delta x + i\Delta x) - f(0)}{\Delta x + i\Delta x} = \lim_{\Delta x \to 0} \frac{|\Delta x + i\Delta x|^2 - 0}{\Delta x + i\Delta x} = \lim_{\Delta x \to 0} \frac{2\Delta x^2}{\Delta x + i\Delta x} = \lim_{\Delta x \to 0} \frac{2\Delta x}{1 + i} = \frac{2}{1 + i}$$

- Therefore, the limit of the difference quotient does not exist, and the function is not differentiable at $z = 0$.

- A complex function is said to be **analytic** at a point $z_0$ if it is differentiable at $z_0$ and at every point in some neighborhood of $z_0$. A function that is analytic in the whole complex plane is called **entire**.
- Analytic functions have many nice properties, such as the **Cauchy-Riemann equations**, which relate the partial derivatives of the real and imaginary parts of the function, and the **Cauchy integral formula**, which gives the value of the function at any point in terms of a contour integral around that point.
- Some examples of analytic functions are:

  - $f(z) = e^z$, which is entire and satisfies $f'(z) = e^z$ for all $z$.
  - $f(z) = \sin z$, which is entire and satisfies $f'(z) = \cos z$ for all $z$.
  - $f(z) = \log z$, which is analytic in the complex plane except for the negative real axis and satisfies $f'(z) = \frac{1}{z}$ for all $z \neq 0$.
  - $f(z) = z^n$, where $n$ is any integer, which is entire and satisfies $f'(z) = nz^{n-1}$ for all $z$.
  - $f(z) = \frac{