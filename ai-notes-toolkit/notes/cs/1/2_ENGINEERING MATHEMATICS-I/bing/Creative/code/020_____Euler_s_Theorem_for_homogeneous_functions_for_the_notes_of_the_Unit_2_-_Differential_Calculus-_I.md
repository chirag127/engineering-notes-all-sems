### Euler’s Theorem for homogeneous functions

- A function $f(x,y)$ is said to be **homogeneous** of degree $n$ if $f(tx,ty) = t^n f(x,y)$ for any $t \neq 0$.
- For example, $f(x,y) = x^2 + y^2$ is homogeneous of degree $2$ because $f(tx,ty) = (tx)^2 + (ty)^2 = t^2 (x^2 + y^2) = t^2 f(x,y)$.
- A function $f(x,y,z)$ is said to be **homogeneous** of degree $n$ if $f(tx,ty,tz) = t^n f(x,y,z)$ for any $t \neq 0$.
- For example, $f(x,y,z) = x^3 + y^3 + z^3$ is homogeneous of degree $3$ because $f(tx,ty,tz) = (tx)^3 + (ty)^3 + (tz)^3 = t^3 (x^3 + y^3 + z^3) = t^3 f(x,y,z)$.
- **Euler's theorem** for homogeneous functions states that if $f(x,y)$ is a homogeneous function of degree $n$, then $x \frac{\partial f}{\partial x} + y \frac{\partial f}{\partial y} = n f(x,y)$.
- For example, if $f(x,y) = x^2 + y^2$, then $x \frac{\partial f}{\partial x} + y \frac{\partial f}{\partial y} = 2x^2 + 2y^2 = 2 f(x,y)$.
- **Euler's theorem** can be generalized to any number of variables. If $f(x_1, x_2, \dots, x_k)$ is a homogeneous function of degree $n$, then $x_1 \frac{\partial f}{\partial x_1} + x_2 \frac{\partial f}{\partial x_2} + \dots + x_k \frac{\partial f}{\partial x_k} = n f(x_1, x_2, \dots, x_k)$.
- For example, if $f(x,y,z) = x^3 + y^3 + z^3$, then $x \frac{\partial f}{\partial x} + y \frac{\partial f}{\partial y} + z \frac{\partial f}{\partial z} = 3x^3 + 3y^3 + 3z^3 = 3 f(x,y,z)$.
- **Euler's theorem** can be used to find the partial derivatives of homogeneous functions more easily.
- For example, to find $\frac{\partial f}{\partial x}$ when $f(x,y) = x^2 + y^2$, we can use Euler's theorem to get $x \frac{\partial f}{\partial x} + y \frac{\partial f}{\partial y} = 2 f(x,y)$. Then, we can solve for $\frac{\partial f}{\partial x}$ by subtracting $y \frac{\partial f}{\partial y}$ from both sides and dividing by $x$. We get $\frac{\partial f}{\partial x} = \frac{2 f(x,y) - y \frac{\partial f}{\partial y}}{x} = \frac{2 (x^2 + y^2) - 2y^2}{x} = \frac{2x^2}{x} = 2x$.