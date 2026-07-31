### Total derivative

- The total derivative of a function of several variables means the total change in the dependent variable due to the changes in all the independent variables.
- The total derivative is the derivative with respect to one variable of the function that depends on that variable not only directly but also via the intermediate variables.
- The total derivative is a direct result of the chain rule.
- The total derivative can be used to approximate the change in the output of a function given small changes in the input of the function.
- The total derivative can also be used to analyze the sensitivity or error propagation of a function.

#### Definition of total derivative of a function

- Suppose z = f(x, y) be a function of two variables, where z is the dependent variable and x and y are the independent variables.
- The total derivative of z with respect to x is given by

```math
\frac{dz}{dx} = \frac{\partial f}{\partial x} + \frac{\partial f}{\partial y} \frac{dy}{dx}
```

- The total derivative of z with respect to y is given by

```math
\frac{dz}{dy} = \frac{\partial f}{\partial x} \frac{dx}{dy} + \frac{\partial f}{\partial y}
```

- In general, if z = f(x, y, ..., w) is a function of n variables, then the total derivative of z with respect to any variable u is given by

```math
\frac{dz}{du} = \frac{\partial f}{\partial x} \frac{dx}{du} + \frac{\partial f}{\partial y} \frac{dy}{du} + \cdots + \frac{\partial f}{\partial w} \frac{dw}{du}
```

- Alternatively, the total derivative of z can be written as

```math
dz = \frac{\partial f}{\partial x} dx + \frac{\partial f}{\partial y} dy + \cdots + \frac{\partial f}{\partial w} dw
```

- This is called the total differential of z.

#### Example of total derivative of a function

- Suppose z = x^2 + y^3 is a function of x and y, where x = sin(t) and y = cos(t) are functions of t.
- To find the total derivative of z with respect to t, we can use the chain rule as follows:

```math
\frac{dz}{dt} = \frac{\partial z}{\partial x} \frac{dx}{dt} + \frac{\partial z}{\partial y} \frac{dy}{dt}
```

- To find the partial derivatives of z, we treat x and y as constants and use the power rule:

```math
\frac{\partial z}{\partial x} = 2x
```

```math
\frac{\partial z}{\partial y} = 3y^2
```

- To find the derivatives of x and y with respect to t, we use the chain rule and the trigonometric identities:

```math
\frac{dx}{dt} = \frac{d}{dt} \sin(t) = \cos(t)
```

```math
\frac{dy}{dt} = \frac{d}{dt} \cos(t) = -\sin(t)
```

- Substituting these values into the formula for the total derivative, we get:

```math
\frac{dz}{dt} = 2x \cos(t) + 3y^2 (-\sin(t))
```

- Simplifying, we get:

```math
\frac{dz}{dt} = 2 \sin(t) \cos(t) - 3 \cos^2(t) \sin(t)
```

- This is the total derivative of z with respect to t.