### Dirichlet’s integral and its applications to area and volume

- Dirichlet's integral is a type of integral that appears in various contexts in mathematics and physics, such as Dirichlet's principle, Fourier series, and phase volume .
- One form of Dirichlet's integral is given by

```math
D(f) = \int_{\Omega} |\nabla f|^2 dV
```

where `f` is a function defined on a domain `Ω` and `∇f` is its gradient.
- Another form of Dirichlet's integral is given by

```math
D_n(f) = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \left( \frac{\sin \left( \frac{2n+1}{2} x \right)}{\sin \left( \frac{x}{2} \right)} \right) dx
```

where `f` is a periodic function with period `2π` and the kernel is the Dirichlet kernel .
- A third form of Dirichlet's integral is given by

```math
D_{n_1, \dots, n_k}(f) = \int_{-\infty}^{\infty} \cdots \int_{-\infty}^{\infty} f(x_1, \dots, x_k) \cos(n_1 x_1 + \cdots + n_k x_k) dx_1 \cdots dx_k
```

where `f` is a function of `k` variables and `n_1, \dots, n_k` are integers .
- Dirichlet's integral can be used to calculate the area and volume of various surfaces and solids by applying the divergence theorem or the Stokes' theorem .
- For example, if `x` is a smooth map from a bounded domain `B` in the plane to a surface `S` in space, then the area of `S` is given by

```math
A(S) = \int_B |x_u \times x_v| du dv = \int_B \sqrt{|\nabla x|^2 - |\nabla x \cdot \hat{n}|^2} du dv
```

where `x_u` and `x_v` are the partial derivatives of `x` with respect to `u` and `v`, `×` is the cross product, `∇x` is the Jacobian matrix of `x`, and `∇x · n̂` is the dot product of `∇x` and the unit normal vector `n̂` to `B`.
- Similarly, if `x` is a smooth map from a bounded domain `B` in the plane to a solid `V` in space, then the volume of `V` is given by

```math
V(V) = \int_B x \cdot (x_u \times x_v) du dv = \int_B \det(\nabla x) du dv
```

where `·` is the dot product and `det` is the determinant.