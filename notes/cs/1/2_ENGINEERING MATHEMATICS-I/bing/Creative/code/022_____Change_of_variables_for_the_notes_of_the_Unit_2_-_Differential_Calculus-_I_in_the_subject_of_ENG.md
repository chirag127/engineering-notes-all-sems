Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of change of variables in differential calculus.

### Change of variables

- Change of variables is a technique for simplifying the calculation of integrals and derivatives by transforming the original variables into new ones.
- The main idea is to find a suitable substitution that makes the integrand or the derivative easier to handle, and then apply the chain rule or the inverse function theorem to relate the new variables to the old ones.
- For example, if we want to calculate the integral of `e^(x^2)` from 0 to 1, we can use the change of variable `u = x^2`, which gives us `du = 2x dx`. Then, the integral becomes

```
integral(e^(x^2) dx) from 0 to 1
= integral(e^u * (1/2) du) from 0 to 1
= (1/2) integral(e^u du) from 0 to 1
= (1/2) (e^u) from 0 to 1
= (1/2) (e - 1)
```

- Similarly, if we want to find the derivative of `sin(x^2)`, we can use the change of variable `u = x^2`, which gives us `du = 2x dx`. Then, the derivative becomes

```
d/dx (sin(x^2))
= d/du (sin(u)) * du/dx
= cos(u) * 2x
= 2x cos(x^2)
```

- Change of variables can also be used for multivariable functions, where we can transform the coordinates from one system to another, such as from Cartesian to polar, cylindrical, or spherical coordinates. This can help us to simplify the domain of integration or the expression of the function.
- For example, if we want to calculate the integral of `x^2 + y^2` over the unit circle, we can use the change of variable `x = r cos(theta)`, `y = r sin(theta)`, which gives us `dx dy = r dr dtheta`. Then, the integral becomes

```
integral(integral(x^2 + y^2 dx dy)) over the unit circle
= integral(integral(r^2 * r dr dtheta)) from 0 to 2pi and from 0 to 1
= integral(r^3 / 3 dtheta) from 0 to 2pi and from 0 to 1
= (r^3 / 3) from 0 to 1 * (theta) from 0 to 2pi
= (1/3) * 2pi
= 2pi/3
```

- Change of variables can also be used for partial derivatives, where we can transform the independent variables into new ones that are more convenient or natural for the given function. For example, if we want to find the partial derivative of `f(x,y) = x^2 + y^2` with respect to `r`, where `r = sqrt(x^2 + y^2)`, we can use the change of variable `x = r cos(theta)`, `y = r sin(theta)`, which gives us `dx/dr = cos(theta)`, `dy/dr = sin(theta)`. Then, the partial derivative becomes

```
df/dr
= df/dx * dx/dr + df/dy * dy/dr
= 2x * cos(theta) + 2y * sin(theta)
= 2r cos^2(theta) + 2r sin^2(theta)
= 2r (cos^2(theta) + sin^2(theta))
= 2r
```

- Change of variables is a useful and powerful technique for solving problems in differential calculus, as it can help us to reduce the complexity and difficulty of the calculations. However, it requires careful attention to the details of the substitution, the limits of integration, and the Jacobian determinant, which is the factor that relates the area or volume elements in the new and old coordinate systems.