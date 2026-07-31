### Euler’s Theorem for Homogeneous Functions

In calculus, a function is said to be homogeneous of degree $n$ if it satisfies the following property for any non-zero scalar $\lambda$ and any point $(x_1, x_2, \ldots, x_n)$:

$$f(\lambda x_1, \lambda x_2, \ldots, \lambda x_n) = \lambda^n f(x_1, x_2, \ldots, x_n)$$

Euler’s theorem for homogeneous functions is a useful tool in calculus that relates partial derivatives of a homogeneous function with the function itself. 

#### Statement of Euler’s Theorem

Let $f(x_1, x_2, \ldots, x_n)$ be a homogeneous function of degree $k$. Then, Euler’s theorem states that:

$$\sum_{i=1}^n x_i \frac{\partial f}{\partial x_i} = kf(x_1, x_2, \ldots, x_n)$$

#### Proof of Euler’s Theorem

To prove Euler’s theorem, we start by applying the chain rule of differentiation to the function $f(\lambda x_1, \lambda x_2, \ldots, \lambda x_n)$ with respect to $\lambda$:

$$\frac{d}{d\lambda} f(\lambda x_1, \lambda x_2, \ldots, \lambda x_n) = \sum_{i=1}^n x_i \frac{\partial f}{\partial x_i}(\lambda x_1, \lambda x_2, \ldots, \lambda x_n)$$

On the other hand, using the definition of a homogeneous function, we can write:

$$f(\lambda x_1, \lambda x_2, \ldots, \lambda x_n) = \lambda^k f(x_1, x_2, \ldots, x_n)$$

Differentiating both sides with respect to $\lambda$, we get:

$$\frac{d}{d\lambda} f(\lambda x_1, \lambda x_2, \ldots, \lambda x_n) = k\lambda^{k-1} f(x_1, x_2, \ldots, x_n)$$

Equating the two expressions for $\frac{d}{d\lambda} f(\lambda x_1, \lambda x_2, \ldots, \lambda x_n)$, we obtain Euler’s theorem:

$$\sum_{i=1}^n x_i \frac{\partial f}{\partial x_i} = kf(x_1, x_2, \ldots, x_n)$$

#### Applications of Euler’s Theorem

Euler’s theorem has several applications in calculus, including:

- Finding the degree of homogeneity of a function: By comparing the left-hand side and right-hand side of Euler’s theorem, we can determine the degree of homogeneity of a function. Specifically, if the function is homogeneous of degree $k$, then the right-hand side of Euler’s theorem is equal to $kf(x_1, x_2, \ldots, x_n)$, which implies that the left-hand side must also be equal to $kf(x_1, x_2, \ldots, x_n)$.

- Simplifying partial derivatives of homogeneous functions: Euler’s theorem can be used to simplify expressions involving partial derivatives of homogeneous functions. For example, suppose we want to find $\frac{\partial f}{\partial x_i}$ for a homogeneous function $f(x_1, x_2, \ldots, x_n)$. Then, we can apply Euler’s theorem to obtain:

  $$\frac{\partial f}{\partial x_i} = \frac{1}{k} \left(\sum_{j=1}^n x_j \frac{\partial f}{\partial x_j} \right)$$
  
  This expression allows us to express the partial derivative in terms of a simpler expression involving only partial derivatives of the function.

- Solving optimization problems: Euler’s theorem can be used to solve optimization problems involving homogeneous functions. Specifically, suppose we want to find the maximum or minimum value of a homogeneous function $f(x_1, x_2, \ldots, x_n)$ subject to the constraint $g(x_1, x_2, \ldots, x_n) = c$, where $g$ is also a homogeneous function. Then, we can use Euler’s theorem to eliminate one of the variables and obtain an expression for the function in terms of the remaining variables. This reduces the problem to a one-variable optimization problem, which can be solved using standard techniques.