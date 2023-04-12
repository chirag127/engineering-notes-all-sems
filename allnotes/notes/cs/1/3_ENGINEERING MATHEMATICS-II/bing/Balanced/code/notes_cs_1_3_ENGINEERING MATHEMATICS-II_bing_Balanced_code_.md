

# The topic is

- The topic is a general term for the subject or theme of a text, speech, or conversation.
- The topic can be expressed in different ways, such as a word, a phrase, a question, or a statement.
- The topic can be identified by looking for clues in the text, such as the title, the introduction, the main idea, the keywords, or the summary.
- The topic can be narrowed down or broadened by adding or removing details, examples, or subtopics.
- The topic can be related to other topics by finding similarities, differences, causes, effects, or connections.
- The topic can be evaluated by considering its relevance, importance, accuracy, validity, or significance.



# Engineering Mathematics-II

Engineering Mathematics-II is a course that covers various topics in mathematics that are relevant and useful for engineering students. The syllabus and content of the course may vary depending on the institution, branch and semester. However, some of the common topics that are covered in Engineering Mathematics-II are:

- Matrices: This topic deals with the properties and operations of matrices, such as eigenvalues, eigenvectors, diagonalization, quadratic forms, Cayley-Hamilton theorem, etc. Matrices are useful for solving systems of linear equations, representing transformations, and modeling various phenomena in engineering.
- Calculus: This topic deals with the techniques and applications of differentiation and integration, such as limits, continuity, derivatives, chain rule, product rule, quotient rule, implicit differentiation, optimization, related rates, integration by parts, integration by substitution, integration by partial fractions, improper integrals, area, volume, work, arc length, surface area, etc. Calculus is useful for studying the rates of change, the behavior and properties of functions, and the analysis of physical phenomena in engineering.
- Vector Algebra and Statics: This topic deals with the properties and operations of vectors, such as addition, subtraction, scalar multiplication, dot product, cross product, projection, angle, magnitude, direction, etc. Vectors are useful for representing quantities that have both magnitude and direction, such as force, displacement, velocity, acceleration, etc. Statics is the branch of mechanics that deals with the equilibrium of forces and moments acting on rigid bodies or systems of particles.
- Complex Analysis: This topic deals with the properties and functions of complex numbers, such as modulus, argument, conjugate, polar form, exponential form, De Moivre's theorem, roots of unity, etc. Complex analysis also deals with the study of analytic functions, which are functions that are differentiable in the complex plane, such as harmonic functions, Cauchy-Riemann equations, Cauchy's integral theorem, Cauchy's integral formula, Taylor series, Laurent series, residue theorem, etc. Complex analysis is useful for solving differential equations, evaluating integrals, and analyzing various phenomena in engineering that involve complex variables, such as alternating current, electromagnetic waves, fluid dynamics, etc.
- Numerical Analysis: This topic deals with the methods and algorithms for approximating the solutions of mathematical problems that cannot be solved exactly or analytically, such as root finding, interpolation, differentiation, integration, linear systems, nonlinear systems, ordinary differential equations, partial differential equations, etc. Numerical analysis is useful for implementing and evaluating the solutions of various engineering problems using computers and software.
- Transform Techniques: This topic deals with the methods and applications of transforming functions from one domain to another, such as Laplace transform, Fourier transform, Z-transform, etc. Transform techniques are useful for simplifying and solving differential equations, analyzing signals and systems, and studying various phenomena in engineering that involve frequency, time, or space domains, such as electrical circuits, vibrations, heat transfer, etc.

These are some of the main topics that are covered in Engineering Mathematics-II. However, there may be other topics or subtopics that are also included in the course depending on the syllabus and the instructor. Engineering Mathematics-II is a course that aims to provide the students with the mathematical tools and skills that are essential for engineering applications and problem solving.



## Unit 1 - Ordinary Differential Equation of Higher Order

- An ordinary differential equation (ODE) is an equation that involves one or more derivatives of an unknown function with respect to a single independent variable.
- The order of an ODE is the highest order of the derivative that occurs in the equation. For example, the ODE `y'' + y = 0` is of second order, while the ODE `y' + y = x` is of first order.
- A linear ODE is an ODE that can be written in the form `a_n(x)y^(n) + a_(n-1)(x)y^(n-1) + ... + a_1(x)y' + a_0(x)y = b(x)`, where `a_i(x)` and `b(x)` are given functions of `x`, and `y^(n)` denotes the `n`-th derivative of `y` with respect to `x`.
- A linear ODE of `n`-th order is called a higher order linear ODE if `n > 2`. For example, the ODE `y''' + x^2 y'' + xy' + 3 = 0` is a higher order linear ODE of third order.
- The general solution of a higher order linear ODE is a linear combination of `n` linearly independent solutions, where `n` is the order of the ODE. For example, the general solution of the ODE `y'' + y = 0` is `y = c_1 cos(x) + c_2 sin(x)`, where `c_1` and `c_2` are arbitrary constants.
- To find the general solution of a higher order linear ODE, one can use various methods, such as the method of undetermined coefficients, the method of variation of parameters, or the method of power series. The choice of method depends on the form and complexity of the ODE and its coefficients.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on the topic of linear differential equation of nth order with constant coefficients.

### Linear differential equation of nth order with constant coefficients

- A linear differential equation of nth order with constant coefficients is an equation of the form

```math
a_n y^{(n)} + a_{n-1} y^{(n-1)} + \cdots + a_1 y' + a_0 y = f(x)
```

where \(a_n, a_{n-1}, \ldots, a_0\) are constants, \(a_n \neq 0\), and \(f(x)\) is a given function of \(x\).

- The equation is called **homogeneous** if \(f(x) = 0\) and **non-homogeneous** otherwise.

- The general solution of a homogeneous linear differential equation of nth order with constant coefficients is a linear combination of \(n\) linearly independent solutions, which can be found by solving the **characteristic equation**

```math
a_n r^n + a_{n-1} r^{n-1} + \cdots + a_1 r + a_0 = 0
```

- The characteristic equation may have \(n\) distinct real roots, repeated real roots, or complex roots. Depending on the nature of the roots, the general solution of the homogeneous equation may involve exponential, trigonometric, or hyperbolic functions.

- The general solution of a non-homogeneous linear differential equation of nth order with constant coefficients is the sum of the general solution of the homogeneous equation and a **particular solution** of the non-homogeneous equation, which can be found by various methods, such as **undetermined coefficients** or **variation of parameters**.

- The method of undetermined coefficients involves guessing a particular solution of the non-homogeneous equation based on the form of \(f(x)\) and then finding the coefficients by substituting the guess into the equation.

- The method of variation of parameters involves finding a particular solution of the non-homogeneous equation by multiplying the solutions of the homogeneous equation by unknown functions and then finding the functions by solving a system of equations.

- The general solution of a linear differential equation of nth order with constant coefficients can be used to model various phenomena, such as harmonic oscillations, electrical circuits, heat conduction, and population growth.



### Simultaneous linear differential equations

- A simultaneous differential equation is one of the mathematical equations for an indefinite function of one or more than one variables that relate the values of the function.
- A simultaneous linear differential equation is a system of two or more linear differential equations with a single independent variable and two or more dependent variables.
- The general form of a simultaneous linear differential equation with two dependent variables is:

$$
\begin{cases}
a_1(x) \frac{dy_1}{dx} + b_1(x) y_1 = c_1(x) \\
a_2(x) \frac{dy_2}{dx} + b_2(x) y_2 = c_2(x)
\end{cases}
$$

- The solution of a simultaneous linear differential equation is a pair of functions $(y_1, y_2)$ that satisfy both equations simultaneously.
- There are different methods to solve simultaneous linear differential equations, such as elimination, substitution, matrix method, and variation of parameters  .
- Simultaneous linear differential equations can be used to model real-life problems involving quantities, prices, speed, time, distance, etc. For example, the population growth of two competing species, the temperature distribution in a metal plate, the electric current in a circuit, etc.



### Second order linear differential equations with variable coefficients

- A second order linear differential equation is an equation of the form `a2(x)y'' + a1(x)y' + a0(x)y = r(x)`, where `a2(x)`, `a1(x)`, `a0(x)`, and `r(x)` are real-valued functions and `a2(x)` is not identically zero.
- A second order linear differential equation is called homogeneous if `r(x) = 0` for every value of `x`, and nonhomogeneous otherwise.
- A second order linear differential equation is called with variable coefficients if `a2(x)`, `a1(x)`, and `a0(x)` are not constant functions, and with constant coefficients otherwise.
- The general solution of a second order linear differential equation with variable coefficients is given by `y = c1y1 + c2y2 + yp`, where `c1` and `c2` are arbitrary constants, `y1` and `y2` are linearly independent solutions of the corresponding homogeneous equation, and `yp` is a particular solution of the nonhomogeneous equation.
- The method of finding the general solution depends on the form and complexity of the coefficients and the nonhomogeneous term. Some common methods are:
  - The method of reduction of order, which reduces a second order equation to a first order equation by assuming a solution of the form `y = v(x)y1`, where `y1` is a known solution of the homogeneous equation.
  - The method of variation of parameters, which assumes a solution of the form `y = v1(x)y1 + v2(x)y2`, where `y1` and `y2` are known solutions of the homogeneous equation, and `v1(x)` and `v2(x)` are unknown functions to be determined by substituting into the original equation.
  - The method of power series, which assumes a solution of the form `y = sum_{n=0}^infty a_n x^n`, where `a_n` are unknown coefficients to be determined by substituting into the original equation and equating the coefficients of the same powers of `x`.
  - The method of Frobenius, which is a generalization of the method of power series that allows for solutions of the form `y = x^r sum_{n=0}^infty a_n x^n`, where `r` is a constant and `a_n` are unknown coefficients to be determined by substituting into the original equation and applying the indicial equation.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is some information on the topic of solution by changing independent variable for ordinary differential equations of higher order.

### Solution by changing independent variable for ordinary differential equations of higher order

- An ordinary differential equation (ODE) is an equation that involves an unknown function y = f(x) and one or more of its derivatives.
- A solution to an ODE is a function y = f(x) that satisfies the ODE when f and its derivatives are substituted into the equation.
- A general solution of an ODE is a solution that contains one or more arbitrary constants that can take any value.
- A particular solution of an ODE is a solution that is obtained by assigning specific values to the arbitrary constants in the general solution.
- Sometimes, it is possible to simplify an ODE or reduce its order by changing the independent variable x to a new variable t, such that x = g(t) for some function g.
- To perform this change of variable, we need to use the chain rule to express the derivatives of y with respect to x in terms of the derivatives of y and x with respect to t.
- For example, if we have an ODE of the form

  `y'' + p(x)y' + q(x)y = 0`

  where y'' denotes the second derivative of y with respect to x, and p and q are some functions of x, we can change the independent variable to t by letting x = g(t) and then applying the chain rule as follows:

  `y' = dy/dx = (dy/dt) / (dx/dt) = y'(t) / g'(t)`

  `y'' = d^2y/dx^2 = (d/dt) (dy/dx) / (dx/dt) = (y''(t)g'(t) - y'(t)g''(t)) / (g'(t))^3`

  Substituting these expressions into the original ODE, we get a new ODE of the form

  `(y''(t)g'(t) - y'(t)g''(t)) / (g'(t))^3 + p(g(t))y'(t) / g'(t) + q(g(t))y(t) = 0`

  which may be easier to solve than the original one.

- The change of variable method can also be used to transform a non-homogeneous ODE into a homogeneous one, by choosing a suitable function g that makes the coefficients of the ODE depend only on the ratio y/x.
- For example, if we have an ODE of the form

  `f(x,y)dy = g(x,y)dx`

  where f and g are homogeneous functions of the same degree of x and y, we can change the independent variable to t by letting y = ux, where u is a function of t, and then applying the chain rule as follows:

  `dy = udx + xdu`

  Substituting these expressions into the original ODE, we get a new ODE of the form

  `f(x,ux)(udx + xdu) = g(x,ux)dx`

  Dividing both sides by x, we get

  `f(1,u)(udu + du) = g(1,u)`

  which is a homogeneous ODE that depends only on u.

- To find the general solution of the original ODE, we need to solve the transformed ODE for u, and then substitute back x = g(t) and y = ux to get y in terms of x .



### Method of variation of parameters

- The method of variation of parameters is a general method to find a particular solution of a non-homogeneous differential equation of the form `Lx(t) = F(t)`, where `L` is a linear differential operator, `x(t)` is the unknown function, and `F(t)` is a given function.
- The method is based on the idea of replacing the constants in the solution of the homogeneous equation `Lx(t) = 0` by functions and determining these functions such that the original equation is satisfied.
- The steps of the method are as follows:

  1. Find the complementary solution `x_c(t)` of the homogeneous equation `Lx(t) = 0` by using the characteristic equation or other methods.
  2. Assume a particular solution of the form `x_p(t) = u_1(t)y_1(t) + u_2(t)y_2(t) + ... + u_n(t)y_n(t)`, where `y_1(t), y_2(t), ..., y_n(t)` are the linearly independent solutions of the homogeneous equation, and `u_1(t), u_2(t), ..., u_n(t)` are unknown functions to be determined.
  3. Impose the condition that `u_1'(t)y_1(t) + u_2'(t)y_2(t) + ... + u_n'(t)y_n(t) = 0`, which ensures that `x_p(t)` is linearly independent of `x_c(t)`.
  4. Substitute `x_p(t)` and its derivatives into the original equation `Lx(t) = F(t)` and solve for `u_1'(t), u_2'(t), ..., u_n'(t)`.
  5. Integrate `u_1'(t), u_2'(t), ..., u_n'(t)` to obtain `u_1(t), u_2(t), ..., u_n(t)`.
  6. Substitute `u_1(t), u_2(t), ..., u_n(t)` into `x_p(t)` to obtain the particular solution.
  7. Add the complementary solution and the particular solution to obtain the general solution `x(t) = x_c(t) + x_p(t)`.

- The method of variation of parameters can be applied to any order of differential equations, as well as to systems of differential equations. It can also handle various types of non-homogeneous terms, such as polynomials, trigonometric functions, exponential functions, logarithmic functions, etc.



# Cauchy-Euler equation

- A Cauchy-Euler equation is a linear homogeneous ordinary differential equation with variable coefficients of the form 

$$
a_nx^ny^{(n)} + a_{n-1}x^{n-1}y^{(n-1)} + \cdots + a_1xy' + a_0y = f(x)
$$

where $a_0, a_1, \ldots, a_n$ are constants and $f(x)$ is a given function.

- The Cauchy-Euler equation is also known as the Euler-Cauchy equation or the equidimensional equation.

- The Cauchy-Euler equation is important in the theory of linear differential equations because it has direct applications to Fourier's method in the study of partial differential equations, such as when solving Laplace's equation in polar coordinates .

- The most common Cauchy-Euler equation is the second-order equation 

$$
ax^2y'' + bxy' + cy = f(x)
$$

- The solutions of the second-order Cauchy-Euler equation can be found using the characteristic equation 

$$
ar(r-1) + br + c = 0
$$

- Just like the constant coefficient differential equation, the nature of the roots of the characteristic equation leads to three classes of solutions:

  - If the roots are distinct and real, say $r_1$ and $r_2$, then the general solution is 

  $$
  y(x) = c_1x^{r_1} + c_2x^{r_2} + y_p(x)
  $$

  where $c_1$ and $c_2$ are arbitrary constants and $y_p(x)$ is a particular solution of the nonhomogeneous equation.

  - If the roots are repeated and real, say $r_1 = r_2 = r$, then the general solution is 

  $$
  y(x) = c_1x^r + c_2x^r\ln x + y_p(x)
  $$

  where $c_1$ and $c_2$ are arbitrary constants and $y_p(x)$ is a particular solution of the nonhomogeneous equation.

  - If the roots are complex, say $r_1 = \alpha + i\beta$ and $r_2 = \alpha - i\beta$, then the general solution is 

  $$
  y(x) = x^\alpha(c_1\cos \beta \ln x + c_2\sin \beta \ln x) + y_p(x)
  $$

  where $c_1$ and $c_2$ are arbitrary constants and $y_p(x)$ is a particular solution of the nonhomogeneous equation.

- A particular solution of the nonhomogeneous equation can be found using various methods, such as undetermined coefficients, variation of parameters, or Laplace transform.

- The method of solving higher-order Cauchy-Euler equations is similar to the second-order case, by assuming a trial solution of the form $y(x) = x^r$ and finding the roots of the characteristic equation .



### Application of differential equations in solving engineering problems

Differential equations are mathematical equations that relate the rate of change of a function to the function itself and other variables. They are widely used in various engineering and science disciplines to model the behavior of physical systems and phenomena. Some examples of engineering applications of differential equations are:

- Mechanical vibrations: The motion of a mass attached to a spring or a pendulum can be described by a second-order differential equation that involves the displacement, velocity, acceleration, mass, stiffness, and damping of the system. The solution of this equation can help engineers design and analyze the performance of mechanical systems, such as bridges, buildings, vehicles, machines, etc.   
- Heat transfer: The temperature distribution in a solid or a fluid can be modeled by a partial differential equation that involves the thermal conductivity, heat capacity, heat source, and boundary conditions of the system. The solution of this equation can help engineers design and optimize the thermal performance of systems, such as heat exchangers, furnaces, boilers, refrigerators, etc.  
- Electric circuits: The voltage and current in a circuit that contains resistors, capacitors, and inductors can be modeled by a first-order or second-order differential equation that involves the resistance, capacitance, inductance, and source of the circuit. The solution of this equation can help engineers design and analyze the electrical behavior of systems, such as filters, amplifiers, oscillators, etc.  
- Population dynamics: The growth or decay of a population of organisms can be modeled by a first-order differential equation that involves the birth rate, death rate, and carrying capacity of the system. The solution of this equation can help engineers and scientists study and predict the population trends and ecological impacts of systems, such as bacteria, animals, plants, etc.  

These are some of the common engineering applications of differential equations. There are many more applications in other fields, such as fluid mechanics, chemical kinetics, control theory, etc. Differential equations are powerful tools for engineers to understand and solve complex problems.



## Unit 2 - Laplace Transform

- The Laplace transform is a mathematical technique that converts a function of time, f(t), into a function of a complex variable, F(s), where s is the Laplace variable.
- The Laplace transform is useful for solving linear differential equations, analyzing linear systems, and modeling physical phenomena.
- The Laplace transform is defined as:

```math
F(s) = \int_{0}^{\infty} f(t) e^{-st} dt
```

- The inverse Laplace transform is defined as:

```math
f(t) = \frac{1}{2\pi i} \int_{\gamma - i\infty}^{\gamma + i\infty} F(s) e^{st} ds
```

- The Laplace transform has some important properties, such as:

  - Linearity: If f(t) and g(t) are two functions with Laplace transforms F(s) and G(s), then for any constants a and b, the Laplace transform of a f(t) + b g(t) is a F(s) + b G(s).
  - Shifting: If f(t) has Laplace transform F(s), then the Laplace transform of f(t-a) u(t-a), where u(t) is the unit step function, is e^{-as} F(s).
  - Scaling: If f(t) has Laplace transform F(s), then the Laplace transform of f(at), where a is a positive constant, is \frac{1}{a} F(\frac{s}{a}).
  - Differentiation: If f(t) has Laplace transform F(s), then the Laplace transform of f'(t) is s F(s) - f(0).
  - Integration: If f(t) has Laplace transform F(s), then the Laplace transform of \int_{0}^{t} f(\tau) d\tau is \frac{1}{s} F(s).
  - Convolution: If f(t) and g(t) are two functions with Laplace transforms F(s) and G(s), then the Laplace transform of f(t) * g(t), where * denotes the convolution operation, is F(s) G(s).

- The Laplace transform can be used to solve linear differential equations with constant coefficients and initial conditions. The general procedure is:

  - Take the Laplace transform of both sides of the differential equation, using the properties of the Laplace transform.
  - Solve for the Laplace transform of the unknown function, F(s), by algebraic manipulation.
  - Take the inverse Laplace transform of F(s), using the method of partial fractions, the method of residues, or a table of Laplace transforms.
  - Check the solution by substituting it into the original differential equation and verifying that it satisfies the initial conditions.



### Laplace transform for the notes of the Unit 2 - Laplace Transform in the subject of ENGINEERING MATHEMATICS-II

- The Laplace transform is an integral transform that converts a function of a real variable (usually time) to a function of a complex variable (usually frequency).
- The Laplace transform can be used to solve linear differential equations, analyze systems and signals, and study stability and control problems.
- The Laplace transform of a function f(t) is defined as:

```math
F(s) = \mathcal{L}\{f(t)\} = \int_{0}^{\infty} e^{-st} f(t) dt
```

where s is a complex variable of the form s = σ + jω.

- The inverse Laplace transform of a function F(s) is defined as:

```math
f(t) = \mathcal{L}^{-1}\{F(s)\} = \frac{1}{2\pi j} \int_{\sigma - j\infty}^{\sigma + j\infty} e^{st} F(s) ds
```

where σ is a real constant such that F(s) is analytic in the region Re(s) > σ.

- The Laplace transform has many important properties, such as linearity, scaling, shifting, differentiation, integration, convolution, and initial and final value theorems. These properties can be used to simplify the calculation of Laplace transforms and inverse Laplace transforms, and to manipulate functions in the s-domain.

- Some common Laplace transforms and inverse Laplace transforms are:

| f(t) | F(s) |
| --- | --- |
| 1 | 1/s |
| t | 1/s^2 |
| e^at | 1/(s-a) |
| sin(at) | a/(s^2 + a^2) |
| cos(at) | s/(s^2 + a^2) |
| t^n | n!/s^(n+1) |
| e^at sin(bt) | b/((s-a)^2 + b^2) |
| e^at cos(bt) | (s-a)/((s-a)^2 + b^2) |

| F(s) | f(t) |
| --- | --- |
| 1/s | 1 |
| 1/s^2 | t |
| 1/(s-a) | e^at |
| a/(s^2 + a^2) | sin(at) |
| s/(s^2 + a^2) | cos(at) |
| n!/s^(n+1) | t^n |
| b/((s-a)^2 + b^2) | e^at sin(bt) |
| (s-a)/((s-a)^2 + b^2) | e^at cos(bt) |



### Existence theorem for the notes of the Unit 2 - Laplace Transform in the subject of ENGINEERING MATHEMATICS-II

- The existence theorem for Laplace transform states the conditions under which a function has a Laplace transform.
- A function f(t) has a Laplace transform F(s) if and only if:
  - f(t) is piecewise continuous on every finite interval in [0, ∞), meaning that f(t) has only a finite number of discontinuities in any finite interval.
  - f(t) is of exponential order, meaning that there exist constants M, c, and T such that |f(t)| ≤ Me<sup>ct</sup> for all t ≥ T.
- The Laplace transform F(s) is unique, meaning that if two functions f<sub>1</sub>(t) and f<sub>2</sub>(t) have the same Laplace transform, then they are equal almost everywhere (except for a set of measure zero).
- The Laplace transform F(s) exists for all s > c, where c is the constant in the exponential order condition.




Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some properties of Laplace transform for the notes of the Unit 2 - Laplace Transform in the subject of Engineering Mathematics-II.

### Properties of Laplace Transform

- Laplace transform is a linear operator, which means that if `f(t)` and `g(t)` are two functions and `a` and `b` are two constants, then

```
L{a f(t) + b g(t)} = a L{f(t)} + b L{g(t)}
```

- Laplace transform is also a one-to-one operator, which means that if `f(t)` and `g(t)` are two functions that have the same Laplace transform, then they are equal except for a finite number of points.

- Laplace transform has the property of differentiation in the `s`-domain, which means that if `f(t)` is a function and `n` is a positive integer, then

```
L{f^(n)(t)} = s^n L{f(t)} - s^(n-1) f(0) - s^(n-2) f'(0) - ... - f^(n-1)(0)
```

- Laplace transform has the property of integration in the `s`-domain, which means that if `f(t)` is a function, then

```
L{∫f(t) dt} = 1/s L{f(t)} + c/s
```

where `c` is an arbitrary constant.

- Laplace transform has the property of multiplication by `t^n`, which means that if `f(t)` is a function and `n` is a positive integer, then

```
L{t^n f(t)} = (-1)^n d^n/ds^n L{f(t)}
```

- Laplace transform has the property of division by `t`, which means that if `f(t)` is a function, then

```
L{f(t)/t} = ∫s^∞ L{f(u)} du
```

- Laplace transform has the property of shifting in the `t`-domain, which means that if `f(t)` is a function and `a` is a positive constant, then

```
L{f(t-a) u(t-a)} = e^(-as) L{f(t)}
```

where `u(t)` is the unit step function.

- Laplace transform has the property of shifting in the `s`-domain, which means that if `f(t)` is a function and `a` is a constant, then

```
L{e^(at) f(t)} = L{f(t)} | s -> s-a
```

- Laplace transform has the property of scaling in the `t`-domain, which means that if `f(t)` is a function and `a` is a positive constant, then

```
L{f(at)} = 1/a L{f(t)} | s -> s/a
```

- Laplace transform has the property of scaling in the `s`-domain, which means that if `f(t)` is a function and `a` is a positive constant, then

```
L{f(t)/a} = L{f(t)} | s -> as
```

- Laplace transform has the property of convolution, which means that if `f(t)` and `g(t)` are two functions, then

```
L{f(t) * g(t)} = L{f(t)} L{g(t)}
```

where `*` denotes the convolution operation.



### Laplace transform of derivatives and integrals

- The Laplace transform is an integral transform that converts a function of a real variable (usually time) to a function of a complex variable (usually frequency).
- The Laplace transform of a function f(t) is defined as

$$
F(s) = \mathcal{L}\{f(t)\} = \int_0^\infty e^{-st} f(t) dt
$$

- where s is a complex variable and the integral is taken over the positive real axis.
- The Laplace transform has many properties that make it useful for solving differential and integral equations, such as linearity, scaling, shifting, differentiation, integration, convolution, and initial and final value theorems.
- The Laplace transform of a derivative of a function f(t) is given by

$$
\mathcal{L}\{f'(t)\} = sF(s) - f(0)
$$

- where f(0) is the initial value of f(t) at t = 0.
- Similarly, the Laplace transform of a higher-order derivative of f(t) is given by

$$
\mathcal{L}\{f^{(n)}(t)\} = s^nF(s) - s^{n-1}f(0) - s^{n-2}f'(0) - \cdots - f^{(n-1)}(0)
$$

- where f'(0), f''(0), ..., f^(n-1)(0) are the initial values of the derivatives of f(t) at t = 0.
- The Laplace transform of an integral of a function f(t) is given by

$$
\mathcal{L}\left\{\int_0^t f(\tau) d\tau\right\} = \frac{1}{s}F(s)
$$

- where F(s) is the Laplace transform of f(t).
- The Laplace transform can be used to solve differential and integral equations by transforming them into algebraic equations in the frequency domain and then applying the inverse Laplace transform to obtain the solution in the time domain.



### Unit step function for the notes of the Unit 2 - Laplace Transform in the subject of ENGINEERING MATHEMATICS-II

- The unit step function is a function that is zero for negative values of the argument and one for positive values. It is denoted by u(t) and defined as:

```
u(t) = { 1, t >= 0
         0, t < 0
```

- The unit step function can be used to model a switch that turns on or off at a certain time, or a signal that starts or stops abruptly.

- The Laplace transform of the unit step function is given by :

```
L[u(t)] = int_0^infty u(t) e^(-st) dt = [e^(-st)/(-s)]_0^infty = 1/s, s > 0
```

- The Laplace transform of a function multiplied by a unit step function is given by the time displacement theorem :

```
L[u(t-a) f(t-a)] = e^(-as) L[f(t)], s > 0
```

- This theorem allows us to find the Laplace transform of a piecewise continuous function by breaking it into segments and multiplying each segment by a unit step function that indicates when it starts.

- For example, if f(t) is defined as:

```
f(t) = { 0, 0 <= t < 1
         t, 1 <= t < 2
         2, t >= 2
```

- Then we can write f(t) as:

```
f(t) = u(t-1) t + u(t-2) (2-t)
```

- And the Laplace transform of f(t) is:

```
L[f(t)] = L[u(t-1) t] + L[u(t-2) (2-t)]
        = e^(-s) L[t] + e^(-2s) L[2-t]
        = e^(-s) 1/s^2 + e^(-2s) (2/s - 1/s^2)
        = (e^(-s) - 2e^(-2s))/s^2 + 2e^(-2s)/s
```



### Laplace transform of periodic function

- A periodic function is a function that repeats itself after a fixed interval of time, called the period.
- The Laplace transform of a periodic function can be obtained by using the time-shifting property of the Laplace transform, which states that if F(s) is the Laplace transform of f(t), then e^(-sT)F(s) is the Laplace transform of f(t-T), where T is a constant.
- If f(t) is a periodic function with period T, then f(t) = f(t+nT) for any integer n. Therefore, we can write f(t) as a sum of shifted functions:

  f(t) = f(t) + f(t-T) + f(t-2T) + ...

- Applying the Laplace transform to both sides, we get:

  F(s) = F(s) + e^(-sT)F(s) + e^(-2sT)F(s) + ...

- Solving for F(s), we get:

  F(s) = F(s) / (1 - e^(-sT))

- This formula gives the Laplace transform of a periodic function in terms of the Laplace transform of one cycle of the function.
- For example, if f(t) is a periodic function with period 2 and f(t) = t for 0 < t < 1 and f(t) = 2-t for 1 < t < 2, then the Laplace transform of f(t) is:

  F(s) = (1/s^2 - e^(-s)/s^2) / (1 - e^(-2s))



### Inverse Laplace Transform

- The inverse Laplace transform is a process of finding a function of time, f(t), from its Laplace transform, F(s).
- The inverse Laplace transform is denoted by L<sup>-1</sup>{F(s)} or f(t) = L<sup>-1</sup>{F(s)}.
- The inverse Laplace transform can be obtained by using the following methods:
  - Partial fraction decomposition
  - Completing the square
  - Convolution theorem
  - Residue theorem
  - Inverse Laplace transform tables
- The inverse Laplace transform has the following properties:
  - Linearity: L<sup>-1</sup>{aF(s) + bG(s)} = aL<sup>-1</sup>{F(s)} + bL<sup>-1</sup>{G(s)}
  - First shifting theorem: L<sup>-1</sup>{e<sup>-as</sup>F(s)} = f(t-a)u(t-a), where u(t) is the unit step function
  - Second shifting theorem: L<sup>-1</sup>{F(s-a)} = e<sup>at</sup>f(t)
  - Scaling theorem: L<sup>-1</sup>{F(cs)} = (1/c)f(t/c)
  - Differentiation theorem: L<sup>-1</sup>{sF(s) - f(0)} = f'(t)
  - Integration theorem: L<sup>-1</sup>{F(s)/s} = ∫<sub>0</sub><sup>t</sup> f(τ) dτ
  - Initial value theorem: lim<sub>s→∞</sub> sF(s) = f(0)
  - Final value theorem: lim<sub>s→0</sub> sF(s) = lim<sub>t→∞</sub> f(t)



### Convolution theorem for the notes of the Unit 2 - Laplace Transform in the subject of ENGINEERING MATHEMATICS-II

- The convolution theorem states that the Laplace transform of a convolution of two functions is the product of the Laplace transforms of the individual functions .
- The convolution of two functions f and g is defined as

```math
f * g (t) = \int_{0}^{t} f(\tau) g(t - \tau) d\tau
```

- The convolution theorem can be written as

```math
\mathcal{L}[f * g] = F(s) G(s)
```

- where F(s) and G(s) are the Laplace transforms of f and g respectively .
- The convolution theorem can be used to simplify the process of finding the inverse Laplace transform of a product of two functions.
- For example, if we want to find the inverse Laplace transform of

```math
H(s) = \frac{s + 1}{s^2 + 2s + 2}
```

- we can write it as

```math
H(s) = \frac{1}{s + 1} \frac{s + 1}{s^2 + 2s + 2}
```

- and use the convolution theorem to get

```math
\mathcal{L}^{-1}[H(s)] = \mathcal{L}^{-1}[\frac{1}{s + 1}] * \mathcal{L}^{-1}[\frac{s + 1}{s^2 + 2s + 2}]
```

- Then we can use the table of Laplace transforms to find the inverse Laplace transforms of the individual functions and perform the convolution integral.
- The convolution theorem can also be used to solve differential equations with non-constant coefficients or non-homogeneous boundary conditions.



# Application of Laplace Transform to solve ordinary differential equations and simultaneous differential equations

- Laplace transform is a mathematical technique that converts a function of time into a function of a complex variable, called the Laplace variable or the frequency parameter.
- Laplace transform can be used to solve differential equations by transforming them from the time domain to the frequency domain, where they become algebraic equations that are easier to manipulate and solve.
- The basic steps to apply Laplace transform to solve ordinary differential equations are:

  1. Take the Laplace transform of both sides of the differential equation using the properties of Laplace transform, such as linearity, derivative, initial value, etc.
  2. Solve for the Laplace transform of the unknown function, denoted by Y(s), by algebraic methods.
  3. Find the inverse Laplace transform of Y(s) using the inverse Laplace transform table or the partial fraction decomposition method.
  4. Check the solution by substituting it into the original differential equation.

- An example of solving an ordinary differential equation using Laplace transform is:

  - Given the initial value problem: y' + 3y = e^2t, y(0) = 1, find y(t).
  - Taking the Laplace transform of both sides, we get: L[y' + 3y] = L[e^2t], L[y(0)] = 1
  - Using the properties of Laplace transform, we get: (s + 3)Y - 1 = 1/(s - 2)
  - Solving for Y, we get: Y = (1 + s)/(s^2 + s - 6)
  - Using the partial fraction decomposition method, we get: Y = 1/(s - 2) - 1/(s + 3)
  - Taking the inverse Laplace transform of both sides, we get: y(t) = e^2t - e^-3t
  - Checking the solution by substituting it into the original differential equation, we get: y' + 3y = 2e^2t + 3e^-3t + 3e^2t - 3e^-3t = e^2t, which is true.

- Laplace transform can also be used to solve simultaneous differential equations by transforming them into a system of linear equations in the frequency domain, and then solving them by matrix methods or Cramer's rule.
- The basic steps to apply Laplace transform to solve simultaneous differential equations are:

  1. Take the Laplace transform of each differential equation in the system using the properties of Laplace transform, such as linearity, derivative, initial value, etc.
  2. Write the system of equations in matrix form, where the unknowns are the Laplace transforms of the functions, denoted by Y_1(s), Y_2(s), ..., Y_n(s).
  3. Solve for the unknowns by matrix methods, such as Gaussian elimination, inverse matrix, or Cramer's rule.
  4. Find the inverse Laplace transform of each unknown using the inverse Laplace transform table or the partial fraction decomposition method.
  5. Check the solution by substituting it into the original system of differential equations.

- An example of solving a system of simultaneous differential equations using Laplace transform is:

  - Given the system of differential equations: x' + y = 2, y' + x = 3, x(0) = 1, y(0) = 0, find x(t) and y(t).
  - Taking the Laplace transform of each equation, we get: L[x' + y] = 2, L[y' + x] = 3, L[x(0)] = 1, L[y(0)] = 0
  - Using the properties of Laplace transform, we get: (sX - 1) + Y = 2, (sY - 0) + X = 3
  - Writing the system of equations in matrix form, we get: [s 1; 1 s][X; Y] = [3; 2]
  - Solving for X and Y by inverse matrix method, we get: [X; Y] = [s 1; 1 s]^-1[3; 2] = [1/(s^2 - 1) 1/(s^2 - 1); -1/(s^2 - 1) 1/(s



## Unit 3 - Sequence and Series

A sequence is a list of numbers or objects that follow a certain pattern or rule. A series is the sum of the terms of a sequence.

Some examples of sequences are:

- The natural numbers: 1, 2, 3, 4, ...
- The even numbers: 2, 4, 6, 8, ...
- The Fibonacci numbers: 1, 1, 2, 3, 5, 8, ...
- The geometric sequence: 2, 4, 8, 16, ...

Some examples of series are:

- The arithmetic series: 1 + 2 + 3 + 4 + ...
- The geometric series: 1 + 2 + 4 + 8 + ...
- The harmonic series: 1 + 1/2 + 1/3 + 1/4 + ...
- The alternating series: 1 - 1/2 + 1/3 - 1/4 + ...

There are different types of sequences and series, such as arithmetic, geometric, harmonic, alternating, etc. Each type has its own formula to find the general term, the nth term, the sum, the partial sum, the convergence, the divergence, etc.

Some important concepts and formulas related to sequences and series are:

- The general term of a sequence is denoted by a_n and it represents the value of the nth term in the sequence.
- The nth term of a sequence can be found by using a formula that depends on the type of the sequence. For example, for an arithmetic sequence, a_n = a_1 + (n - 1)d, where a_1 is the first term and d is the common difference.
- The sum of a series is denoted by S_n and it represents the value of adding all the terms of the series up to the nth term.
- The partial sum of a series is denoted by s_n and it represents the value of adding the first n terms of the series. For example, s_4 = a_1 + a_2 + a_3 + a_4.
- The convergence of a series means that the series has a finite sum as n approaches infinity. For example, the geometric series 1 + 1/2 + 1/4 + 1/8 + ... converges to 2.
- The divergence of a series means that the series does not have a finite sum as n approaches infinity. For example, the harmonic series 1 + 1/2 + 1/3 + 1/4 + ... diverges to infinity.
- The ratio test is a method to determine the convergence or divergence of a series by comparing the ratio of two consecutive terms. For example, if |a_(n+1)/a_n| < 1, then the series converges; if |a_(n+1)/a_n| > 1, then the series diverges; if |a_(n+1)/a_n| = 1, then the test is inconclusive.
- The integral test is a method to determine the convergence or divergence of a series by comparing it to an improper integral. For example, if the integral from n to infinity of f(x) dx converges, then the series a_n = f(n) also converges; if the integral diverges, then the series also diverges. The function f(x) must be positive, continuous, and decreasing for this test to work.



### Definition of Sequence and Series with Examples

- A **sequence** is an ordered list of numbers or objects that follow a certain rule or pattern. For example, 1, 3, 5, 7, 9 is a sequence of odd numbers. A sequence can be finite or infinite, depending on how many terms it has.
- A **series** is the sum of the terms of a sequence. For example, 1 + 3 + 5 + 7 + 9 is a series that adds up to 25. A series can be convergent or divergent, depending on whether the sum approaches a finite value or not.
- A sequence can be represented by a general term or a formula that gives the nth term of the sequence. For example, the general term of the sequence 1, 3, 5, 7, 9 is a_n = 2n - 1, where n is the position of the term in the sequence.
- A series can be represented by a partial sum or a formula that gives the sum of the first n terms of the series. For example, the partial sum of the series 1 + 3 + 5 + 7 + 9 is S_n = n^2, where n is the number of terms in the series.
- There are different types of sequences and series, such as arithmetic, geometric, harmonic, alternating, etc. Each type has its own rule or formula for finding the general term or the partial sum. For example, an arithmetic sequence is a sequence where each term is obtained by adding a constant value to the previous term. An arithmetic series is the sum of an arithmetic sequence. The general term of an arithmetic sequence is a_n = a_1 + (n - 1)d, where a_1 is the first term and d is the common difference. The partial sum of an arithmetic series is S_n = n/2 (2a_1 + (n - 1)d), where n is the number of terms in the series.



### Convergence of series

- A series is an expression of the form `a_1 + a_2 + a_3 + ...` where `a_n` is the n-th term of a sequence.
- A series is convergent if the sequence of its partial sums `S_n = a_1 + a_2 + ... + a_n` tends to a limit `L` as `n` goes to infinity. In this case, we write `a_1 + a_2 + a_3 + ... = L`  .
- A series is divergent if the sequence of its partial sums does not have a limit, or has a limit that is infinite  .
- A necessary condition for a series to converge is that the sequence of its terms `a_n` must tend to zero as `n` goes to infinity. This follows from the fact that if `a_n` does not tend to zero, then `S_n` cannot tend to a finite limit.
- However, this condition is not sufficient, as there are series whose terms tend to zero but the series diverges. For example, the harmonic series `1 + 1/2 + 1/3 + 1/4 + ...` diverges, even though `1/n` tends to zero as `n` goes to infinity.
- To determine whether a series converges or diverges, we need to use various tests and methods that compare the series with known convergent or divergent series, or that examine the behavior of the series terms or partial sums. Some of these tests and methods are:

  - The geometric series test: A geometric series is a series of the form `a + ar + ar^2 + ...` where `a` and `r` are constants. A geometric series converges if and only if `|r| < 1`, and in this case, the sum is `a/(1-r)`  .
  - The p-series test: A p-series is a series of the form `1/n^p` where `p` is a constant. A p-series converges if and only if `p > 1`, and in this case, the sum is `pi^2/6` for `p = 2`, and `zeta(p)` for `p > 2`, where `zeta` is the Riemann zeta function  .
  - The integral test: If `f` is a positive, continuous, and decreasing function on `[1, infinity)` and `a_n = f(n)`, then the series `a_1 + a_2 + a_3 + ...` converges if and only if the improper integral `int_1^infinity f(x) dx` converges  .
  - The comparison test: If `0 <= a_n <= b_n` for all `n`, and the series `b_1 + b_2 + b_3 + ...` converges, then the series `a_1 + a_2 + a_3 + ...` also converges. Conversely, if `0 <= b_n <= a_n` for all `n`, and the series `b_1 + b_2 + b_3 + ...` diverges, then the series `a_1 + a_2 + a_3 + ...` also diverges  .
  - The limit comparison test: If `a_n` and `b_n` are positive sequences and `lim_(n->infinity) a_n/b_n = L` where `L` is a positive finite number, then the series `a_1 + a_2 + a_3 + ...` and `b_1 + b_2 + b_3 + ...` either both converge or both diverge  .
  - The alternating series test: An alternating series is a series of the form `a_1 - a_2 + a_3 - a_4 + ...` where `a_n > 0` for all `n`. An alternating series converges if the sequence `a_n` is decreasing and tends to zero as `n` goes to infinity[^1



### Tests for convergence of series

A series is a sum of infinitely many terms, such as

$$\sum_{n=1}^{\infty} a_n = a_1 + a_2 + a_3 + \cdots$$

where $a_n$ is the n-th term of the series. A series is said to converge if the partial sums

$$S_N = \sum_{n=1}^{N} a_n$$

approach a finite limit as $N$ goes to infinity. Otherwise, the series is said to diverge.

There are several tests that can be used to determine whether a series converges or diverges. Some of the most common tests are:

- **The n-th term test**: This test states that if $\lim_{n \to \infty} a_n \neq 0$, then the series $\sum_{n=1}^{\infty} a_n$ diverges. This test can only be used to show divergence, not convergence.

- **The comparison test**: This test compares a given series with another series that is known to converge or diverge. If the given series is smaller than a convergent series, then it also converges. If the given series is larger than a divergent series, then it also diverges.

- **The geometric test**: This test applies to series of the form $\sum_{n=1}^{\infty} ar^{n-1}$, where $a$ and $r$ are constants. Such series are called geometric series. The test states that a geometric series converges if and only if $|r| < 1$. The sum of a convergent geometric series is $\frac{a}{1-r}$.

- **The ratio test**: This test uses the ratio of consecutive terms of a series to determine its convergence or divergence. The test states that if $\lim_{n \to \infty} \left|\frac{a_{n+1}}{a_n}\right| = L$, then the series $\sum_{n=1}^{\infty} a_n$ converges if $L < 1$, diverges if $L > 1$, and is inconclusive if $L = 1$.

- **The root test**: This test uses the n-th root of the n-th term of a series to determine its convergence or divergence. The test states that if $\lim_{n \to \infty} \sqrt[n]{|a_n|} = L$, then the series $\sum_{n=1}^{\infty} a_n$ converges if $L < 1$, diverges if $L > 1$, and is inconclusive if $L = 1$.

These are some of the basic tests for convergence of series. There are other tests that can be used for more specific types of series, such as the alternating series test, the integral test, the p-series test, and the Dirichlet's test. For more details and examples, you can refer to the following sources:

: Convergent series - Definition, Tests, and Examples - Story of Mathematics
: Series Convergence Tests - Statistics How To
: (PDF) Tests for Convergence of Series | nuratikah norman - Academia.edu
: 9.2: Tests for Convergence - Mathematics LibreTexts
: Calculus II - Convergence/Divergence of Series - Lamar University



### Ratio test

- The ratio test is a method to determine the convergence or divergence of an infinite series of the form $\sum_{n=1}^{\infty} a_n$, where $a_n$ is a positive term for all $n$.
- The ratio test is based on the idea that if the ratio of successive terms of a series is less than one, then the series is convergent, and if the ratio is greater than one, then the series is divergent.
- The ratio test can be stated as follows:

  - Let $\sum_{n=1}^{\infty} a_n$ be an infinite series of positive terms, and let $L = \lim_{n \to \infty} \frac{a_{n+1}}{a_n}$ be the limit of the ratio of successive terms. Then,
    - If $L < 1$, the series is **convergent**.
    - If $L > 1$, the series is **divergent**.
    - If $L = 1$, the test is **inconclusive**, and the series may be convergent or divergent.

- The ratio test is useful for series that involve factorials, exponentials, or powers of $n$.
- The ratio test can also be applied to series of alternating terms, by taking the absolute value of the terms before computing the ratio.
- The ratio test does not give any information about the value of the sum of a convergent series, only its existence.



### D’ Alembert’s test for convergence of series

- D’ Alembert’s test, also known as the ratio test, is a criterion for the convergence of a series of real or complex numbers, where each term is nonzero when n is large .
- The test was first published by Jean le Rond d'Alembert in 1768.
- The test is based on the limit of the ratio of consecutive terms of the series .
- The test can be stated as follows:

  - Let $\sum_{n=1}^{\infty} a_n$ be a series of real or complex numbers, and let the sequence $a_n$ satisfy: $$\lim_{n \to \infty} \frac{a_{n+1}}{a_n} = L$$
  - If $L > 1$, then the series diverges.
  - If $L < 1$, then the series converges absolutely.
  - If $L = 1$, then the test is inconclusive and the series may converge or diverge.

- The test can be applied to series of positive terms by taking the absolute value of the ratio.
- The test can also be modified to use the root of the terms instead of the ratio, which is known as the Cauchy root test.
- The test is useful for series involving factorials, exponentials, or powers.
- The test can be proved using the comparison test and the squeeze theorem.
- The test can be illustrated by some examples:

  - The series $\sum_{n=1}^{\infty} \frac{1}{n}$ diverges, since $$\lim_{n \to \infty} \frac{\frac{1}{n+1}}{\frac{1}{n}} = \lim_{n \to \infty} \frac{n}{n+1} = 1$$
  - The series $\sum_{n=1}^{\infty} \frac{1}{n^2}$ converges, since $$\lim_{n \to \infty} \frac{\frac{1}{(n+1)^2}}{\frac{1}{n^2}} = \lim_{n \to \infty} \frac{n^2}{(n+1)^2} = \frac{1}{1 + \frac{2}{n} + \frac{1}{n^2}} < 1$$
  - The series $\sum_{n=1}^{\infty} \frac{n!}{n^n}$ converges, since $$\lim_{n \to \infty} \frac{\frac{(n+1)!}{(n+1)^{n+1}}}{\frac{n!}{n^n}} = \lim_{n \to \infty} \frac{n^n}{(n+1)^n} \cdot \frac{1}{n+1} = \lim_{n \to \infty} \frac{1}{(1 + \frac{1}{n})^n} \cdot \frac{1}{n+1} = \frac{1}{e} \cdot 0 = 0 < 1$$



### Raabe's test

Raabe's test is a test for the convergence of a series of the form

$$\sum_{n=1}^{\infty} a_n$$

where each term is a real or complex number and $a_n \neq 0$ for large $n$.

The test is based on the ratio of consecutive terms of the series, defined as

$$R_n = \frac{a_n}{a_{n+1}}$$

The test states that:

- If $\lim_{n \to \infty} (R_n - 1)n > 1$, then the series converges.
- If $\lim_{n \to \infty} (R_n - 1)n < 1$, then the series diverges.
- If $\lim_{n \to \infty} (R_n - 1)n = 1$, then the test is inconclusive.

The test was developed by Swiss mathematician Joseph Ludwig Raabe in 1832 .

Some examples of applying Raabe's test are:

- The series $\sum_{n=1}^{\infty} \frac{n!}{n^n}$ converges, since

$$\lim_{n \to \infty} \left(\frac{n!}{n^n} \cdot \frac{(n+1)^{n+1}}{(n+1)!} - 1\right)n = \lim_{n \to \infty} \left(\frac{(n+1)^n}{n^n} - 1\right) = \lim_{n \to \infty} \left(\left(1 + \frac{1}{n}\right)^n - 1\right) = e - 1 > 1$$

- The series $\sum_{n=1}^{\infty} \frac{1}{n}$ diverges, since

$$\lim_{n \to \infty} \left(\frac{1}{n} \cdot n - 1\right)n = \lim_{n \to \infty} (1 - n) = -\infty < 1$$

- The series $\sum_{n=1}^{\infty} \frac{1}{n^2}$ is inconclusive by Raabe's test, since

$$\lim_{n \to \infty} \left(\frac{1}{n^2} \cdot \frac{(n+1)^2}{1} - 1\right)n = \lim_{n \to \infty} \left(\frac{n^2 + 2n + 1}{n^2} - 1\right) = \lim_{n \to \infty} \left(\frac{2}{n} + \frac{1}{n^2}\right) = 0 = 1$$

However, this series converges by the p-series test.



### Comparison test for the notes of the Unit 3 - Sequence and Series in the subject of ENGINEERING MATHEMATICS-II

- The comparison test for series is a method to determine the convergence or divergence of a series by comparing it to another series whose behavior is known .
- There are two types of comparison tests: direct comparison test and limit comparison test   .
- The direct comparison test states that:
  - If the infinite series $\sum_{n=1}^\infty a_n$ converges and $0 \leq b_n \leq a_n$ for all sufficiently large $n$, then the infinite series $\sum_{n=1}^\infty b_n$ also converges .
  - If the infinite series $\sum_{n=1}^\infty a_n$ diverges and $0 \leq a_n \leq b_n$ for all sufficiently large $n$, then the infinite series $\sum_{n=1}^\infty b_n$ also diverges .
- The limit comparison test states that:
  - If the infinite series $\sum_{n=1}^\infty a_n$ and $\sum_{n=1}^\infty b_n$ have positive terms and $\lim_{n \to \infty} \frac{a_n}{b_n} = c$, where $c$ is a positive finite number, then the two series either both converge or both diverge  .
- The comparison test is useful when the series involves functions that are difficult to integrate, such as rational, exponential, or logarithmic functions  .
- The comparison test can be applied to geometric series and p-series, which have known convergence properties.
- The comparison test can also be combined with other tests, such as the integral test, the ratio test, or the root test, to determine the convergence or divergence of a series .



### Fourier Series

- A Fourier series is an expansion of a periodic function f(x) in terms of an infinite sum of sines and cosines   .
- Fourier series make use of the orthogonality relationships of the sine and cosine functions   .
- A Fourier series is analogous to a Taylor series, which represents functions as possibly infinite sums of monomial terms.
- The computation and study of Fourier series is known as harmonic analysis and is extremely useful as a way to break up an arbitrary periodic function into a set of simple terms that can be plugged in, solved individually, and then recombined to obtain the solution to the original problem or an approximation to it to whatever accuracy is desired or practical.
- The general form of a Fourier series is:

Fourier series formula

where omega is the fundamental frequency of the function and a_n and b_n are the Fourier coefficients, which can be calculated by the following formulas:

a_n formula

b_n formula

where L is the period of the function    .

- Some examples of Fourier series are:

  - The Fourier series of the function f(x) = x with period 2 pi is:

  Fourier series of x




Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on half range Fourier sine and cosine series.

### Half range Fourier sine and cosine series

- A half range Fourier series is a Fourier series that is defined over half the range of the original function, instead of the full range.
- A half range Fourier series can be either a sine series or a cosine series, depending on the symmetry of the function.
- A sine series is a Fourier series that contains only sine terms, and it is used to represent odd functions, which are functions that satisfy f(-x) = -f(x) for all x.
- A cosine series is a Fourier series that contains only cosine terms, and it is used to represent even functions, which are functions that satisfy f(-x) = f(x) for all x.
- To find the half range Fourier sine or cosine series of a function f(x) defined over the interval [0, L], we need to extend the function to the interval [-L, L] by using either odd or even symmetry, and then apply the standard formulas for the Fourier coefficients.
- The half range Fourier sine series of f(x) is given by:

f(x) = sum_(n=1)^infty b_n sin(n pi x/L)

where b_n = (2/L) int_0^L f(x) sin(n pi x/L) dx

- The half range Fourier cosine series of f(x) is given by:

f(x) = a_0/2 + sum_(n=1)^infty a_n cos(n pi x/L)

where a_0 = (2/L) int_0^L f(x) dx

and a_n = (2/L) int_0^L f(x) cos(n pi x/L) dx

- Half range Fourier series are useful for solving boundary value problems involving heat conduction, wave propagation, and vibration.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for Unit 4 - Complex Variable–Differentiation:

## Unit 4 - Complex Variable–Differentiation

- A complex variable is a variable that can take on values in the complex plane, i.e., numbers of the form $z = x + iy$, where $x$ and $y$ are real numbers and $i$ is the imaginary unit.
- A complex function is a function that maps complex variables to complex values, i.e., $f: \mathbb{C} \to \mathbb{C}$, such as $f(z) = z^2 + 2z + 1$.
- A complex function is said to be differentiable at a point $z_0$ if the limit $$f'(z_0) = \lim_{\Delta z \to 0} \frac{f(z_0 + \Delta z) - f(z_0)}{\Delta z}$$ exists and is independent of the direction of $\Delta z$.
- A complex function is said to be analytic at a point $z_0$ if it is differentiable at $z_0$ and in some neighborhood of $z_0$. A function that is analytic in the whole complex plane is called entire.
- The derivative of a complex function has the following properties:
  - Linearity: $(af + bg)' = af' + bg'$, where $a$ and $b$ are constants and $f$ and $g$ are complex functions.
  - Product rule: $(fg)' = f'g + fg'$, where $f$ and $g$ are complex functions.
  - Quotient rule: $(f/g)' = (f'g - fg')/g^2$, where $f$ and $g$ are complex functions and $g \neq 0$.
  - Chain rule: $(f \circ g)' = (f' \circ g)g'$, where $f$ and $g$ are complex functions.
- The Cauchy-Riemann equations are a set of necessary conditions for a complex function to be differentiable. They state that if $f(z) = u(x,y) + iv(x,y)$, where $u$ and $v$ are real functions of two variables, then $$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y} \quad \text{and} \quad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$$ at any point where $f$ is differentiable.
- The Cauchy-Riemann equations can also be written in polar coordinates as $$\frac{\partial u}{\partial r} = \frac{1}{r}\frac{\partial v}{\partial \theta} \quad \text{and} \quad \frac{\partial v}{\partial r} = -\frac{1}{r}\frac{\partial u}{\partial \theta}$$ where $z = re^{i\theta}$ and $f(z) = u(r,\theta) + iv(r,\theta)$.
- The Cauchy-Riemann equations imply that if $f$ is differentiable, then $u$ and $v$ are harmonic functions, i.e., they satisfy the Laplace equation $$\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0 \quad \text{and} \quad \frac{\partial^2 v}{\partial x^2} + \frac{\partial^2 v}{\partial y^2} = 0$$
- The Cauchy-Riemann equations also imply that the modulus and the argument of a complex function are related by $$|f'(z)| = \left(\frac{\partial |f|}{\partial x}\right)^2 + \left(\frac{\partial |f|}{\partial y}\right)^2 \quad \text{and} \quad \arg(f'(z)) = \frac{\partial \arg(f)}{\partial x} = -\frac{\partial \arg(f)}{\partial y}$$ where $|f|$ and $\arg(f)$ denote the modulus and the argument of $f$, respectively.
- Some examples of complex functions and their derivatives are:
  - $f(z) = z^n$, where $n$ is a positive integer. Then $f'(z) = nz^{n-1}$.
  - $f(z) = e^z$, where



### Functions of complex variable

- A complex function is a function that maps complex numbers to complex numbers, i.e., $w(z) = u(x,y) + iv(x,y)$, where $z = x + iy$ and $w, u, v$ are complex-valued functions of two real variables $x$ and $y$  .
- A complex function can be seen as a pair of real functions, the real part $u(x,y)$ and the imaginary part $v(x,y)$, that satisfy the Cauchy-Riemann equations  :
$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}$$
$$\frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$$
- A complex function is said to be holomorphic or analytic if it is differentiable at every point in its domain, i.e., if the limit
$$\lim_{\Delta z \to 0} \frac{w(z + \Delta z) - w(z)}{\Delta z}$$
exists and is independent of the direction of $\Delta z$  .
- A holomorphic function has many remarkable properties, such as:
  - It is infinitely differentiable and can be expressed as a power series in a neighborhood of any point in its domain  .
  - It satisfies the maximum modulus principle, which states that the modulus of a holomorphic function cannot have a local maximum in the interior of its domain  .
  - It satisfies the Cauchy integral formula, which relates the value of a holomorphic function at a point to its values on a closed contour around that point  .
  - It satisfies the residue theorem, which relates the integral of a holomorphic function over a closed contour to the sum of its residues at the isolated singularities inside the contour  .
- A complex function can be extended to a function of several complex variables, i.e., $w(z_1, z_2, \dots, z_n) = u(x_1, y_1, \dots, x_n, y_n) + iv(x_1, y_1, \dots, x_n, y_n)$, where $z_i = x_i + iy_i$ and $w, u, v$ are complex-valued functions of $2n$ real variables .
- A function of several complex variables is said to be holomorphic or analytic if it is holomorphic in each variable separately, i.e., if the partial derivatives
$$\frac{\partial w}{\partial z_i} = \frac{1}{2} \left( \frac{\partial w}{\partial x_i} - i \frac{\partial w}{\partial y_i} \right)$$
exist and are continuous for all $i = 1, 2, \dots, n$ .
- A function of several complex variables has similar properties to a function of one complex variable, such as power series expansion, maximum modulus principle, Cauchy integral formula, and residue theorem, but they are more complicated and require more assumptions .

: https://people.umass.edu/bvs/605.pdf
: https://vdocument.in/functions-of-a-complex-variables.html
: https://en.wikipedia.org/wiki/Complex_analysis
: https://ocw.mit.edu/courses/18-112-functions-of-a-complex-variable-fall-2008/
: https://en.wikipedia.org/wiki/Function_of_several_complex_variables



### Limit for the notes of the Unit 4 - Complex Variable–Differentiation in the subject of ENGINEERING MATHEMATICS-II

- Complex variable–differentiation is the study of functions of a complex variable and their derivatives.
- A complex variable is a variable that can take values in the complex plane, which is the set of all numbers of the form `z = x + iy`, where `x` and `y` are real numbers and `i` is the imaginary unit such that `i^2 = -1`.
- A function of a complex variable is a rule that assigns a complex number to each complex number in its domain, which is a subset of the complex plane. For example, `f(z) = z^2 + 2z - 1` is a function of a complex variable with domain `C`, the set of all complex numbers.
- A function of a complex variable is said to be differentiable at a point `z0` in its domain if the limit
`f'(z0) = lim_(z->z0) (f(z) - f(z0))/(z - z0)`
exists and is independent of the direction of approach of `z` to `z0`. The limit `f'(z0)` is called the derivative of `f` at `z0`.
- A function of a complex variable that is differentiable at every point in its domain is called an analytic function or a holomorphic function. Analytic functions have many remarkable properties, such as the Cauchy-Riemann equations, the Cauchy integral formula, the Taylor and Laurent series expansions, and the residue theorem.
- The Cauchy-Riemann equations are a set of necessary and sufficient conditions for a function of a complex variable to be differentiable. They state that if `f(z) = u(x,y) + iv(x,y)`, where `u` and `v` are real-valued functions of two real variables, then `f` is differentiable at `z0 = x0 + iy0` if and only if
`u_x(x0,y0) = v_y(x0,y0)` and `u_y(x0,y0) = -v_x(x0,y0)`,
where the subscripts denote partial derivatives.
- The Cauchy integral formula is a fundamental result that relates the value of an analytic function at a point inside a simple closed curve to the values of the function on the curve. It states that if `f` is an analytic function in a domain `D` that contains a simple closed curve `C` and its interior, and `z0` is a point inside `C`, then
`f(z0) = (1/(2pi i)) int_C (f(z)/(z - z0)) dz`,
where the integral is taken in the counterclockwise direction along `C`.
- The Taylor series expansion of an analytic function is a representation of the function as an infinite sum of terms involving powers of the variable. It states that if `f` is an analytic function in a domain `D` that contains a disk centered at `z0` with radius `R`, then for any `z` in the disk, 
`f(z) = sum_(n=0)^infty (f^(n)(z0)/n!) (z - z0)^n`,
where `f^(n)` denotes the `n`-th derivative of `f`.
- The Laurent series expansion of an analytic function is a generalization of the Taylor series expansion that allows for singularities in the function. It states that if `f` is an analytic function in an annulus `A = {z : R1 < |z - z0| < R2}`, where `0 <= R1 < R2 <= infty`, then for any `z` in `A`, 
`f(z) = sum_(n=-infty)^infty a_n (z - z0)^n`,
where the coefficients `a_n` are given by
`a_n = (1/(2pi i)) int_C (f(z)/(z - z0)^(n+1)) dz`,
where `C` is any simple closed curve in `A` that encloses `z0` in the counterclockwise direction.
- The residue theorem is a powerful tool for evaluating complex integrals that involve singularities. It states that if `f` is an analytic function in a domain `D` except for a finite number of isolated singularities `z1, z2, ..., zn`, and `C



### Continuity and Differentiability of Complex Functions

- A complex function is a function that maps complex numbers to complex numbers, such as f(z) = z^2 + 1.
- A complex function is continuous at a point z_0 if the limit of the function as z approaches z_0 is equal to the value of the function at z_0, i.e., lim_(z->z_0) f(z) = f(z_0) .
- A complex function is differentiable at a point z_0 if the limit of the difference quotient as h approaches zero exists and is finite, i.e., lim_(h->0) (f(z_0 + h) - f(z_0))/h = f'(z_0) .
- A complex function is analytic at a point z_0 if it is differentiable at z_0 and in some neighborhood of z_0. A complex function is analytic in a domain D if it is analytic at every point in D .
- A complex function that is differentiable at a point is also continuous at that point, but the converse is not true. For example, the function f(z) = |z| is continuous at z = 0 but not differentiable there .
- A complex function that is analytic in a domain is also infinitely differentiable in that domain, and its derivatives satisfy the Cauchy-Riemann equations .



### Analytic functions

- A function `f(z)` of a complex variable `z = x + iy` is **analytic** if it has a complex derivative `f'(z)` at every point in its domain.
- A complex derivative `f'(z)` is defined as the limit of the difference quotient `f(z+h) - f(z) / h` as `h` approaches zero.
- A function `f(z)` is analytic if and only if it is **holomorphic**, i.e., it satisfies the **Cauchy-Riemann equations**:
  - `u_x = v_y` and `u_y = -v_x`, where `u` and `v` are the real and imaginary parts of `f(z)`, respectively.
- A function `f(z)` is analytic if and only if it is equal to its **Taylor series** in some neighborhood of every point in its domain:
  - `f(z) = f(z_0) + f'(z_0)(z-z_0) + f''(z_0)(z-z_0)^2 / 2! + ...`, where `z_0` is any point in the domain of `f(z)`.
- Analytic functions have many remarkable properties that do not hold for real differentiable functions, such as:
  - **Identity theorem**: If two analytic functions `f(z)` and `g(z)` agree on a set of points that has a limit point, then they are equal everywhere in their common domain.
  - **Maximum modulus principle**: If `f(z)` is a non-constant analytic function in a domain `D`, then `|f(z)|` cannot attain a maximum value in `D`.
  - **Liouville's theorem**: If `f(z)` is a bounded entire function (analytic in the whole complex plane), then `f(z)` is constant.
  - **Fundamental theorem of algebra**: If `p(z)` is a non-constant polynomial with complex coefficients, then `p(z)` has at least one complex root.
  - **Residue theorem**: If `f(z)` is an analytic function in a simply connected domain `D` except for a finite number of isolated singularities, then the integral of `f(z)` along any closed contour in `D` is equal to `2πi` times the sum of the residues of `f(z)` at the singularities.



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here are some notes on the Cauchy-Riemann equations:

### Cauchy-Riemann equations (Cartesian and Polar form)

- The Cauchy-Riemann equations are a system of two partial differential equations that form a necessary and sufficient condition for a complex function to be holomorphic (complex differentiable).
- A complex function f(z) = u(x, y) + iv(x, y) is holomorphic at a point z = x + iy if and only if it satisfies the Cauchy-Riemann equations at that point:
  - (1a) `u_x = v_y`
  - (1b) `u_y = -v_x`
  - where `u_x` and `u_y` are the partial derivatives of u with respect to x and y, and `v_x` and `v_y` are the partial derivatives of v with respect to x and y.
- The Cauchy-Riemann equations can also be written in polar form, using the polar coordinates `z = r(cos θ + i sin θ)`, `u = u(r, θ)`, and `v = v(r, θ)`. In this case, the equations are:
  - (2a) `u_r = (1/r)v_θ`
  - (2b) `u_θ = -(1/r)v_r`
  - where `u_r` and `u_θ` are the partial derivatives of u with respect to r and θ, and `v_r` and `v_θ` are the partial derivatives of v with respect to r and θ.
- The Cauchy-Riemann equations allow us to check if a complex function is holomorphic and to compute its complex derivative. If f(z) = u(x, y) + iv(x, y) is holomorphic, then its complex derivative is given by:
  - `f'(z) = u_x + iv_x = v_y - iu_y`
  - or, in polar form, by:
  - `f'(z) = u_r + iv_r = i(u_θ + iv_θ)`
- The Cauchy-Riemann equations also imply some important properties of holomorphic functions, such as the Cauchy integral formula, the Cauchy integral theorem, and the maximum modulus principle.



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is some information on harmonic functions for the notes of the Unit 4 - Complex Variable–Differentiation in the subject of ENGINEERING MATHEMATICS-II.

### Harmonic function

- A harmonic function is a function that satisfies Laplace's equation, which is a partial differential equation of the form: `∇^2 u = u_xx + u_yy = 0`  .
- A harmonic function is twice continuously differentiable and has the property that the average value of the function over any circle is equal to the value at the center of the circle.
- A harmonic function is the real part of a holomorphic function, which is a complex-valued function that is differentiable everywhere in a domain  .
- A holomorphic function can be written as `f(z) = u(x,y) + iv(x,y)`, where `z = x + iy` is a complex variable, and `u` and `v` are harmonic functions  .
- A harmonic function can be obtained from a holomorphic function by applying the Cauchy-Riemann equations, which are: `u_x = v_y` and `u_y = -v_x`  .
- A harmonic function can also be obtained from a holomorphic function by applying the Laplace operator, which is: `∇^2 u = 4∂/∂z ∂/∂z̅ u`, where `z̅` is the complex conjugate of `z`.
- A harmonic function has many applications in physics and engineering, such as heat conduction, electrostatics, fluid dynamics, and potential theory .



### Method to find Analytic functions for the notes of the Unit 4 - Complex Variable–Differentiation in the subject of ENGINEERING MATHEMATICS-II

- A function of a complex variable is said to be **analytic** in a region of the complex plane if it has a derivative at each point of the region and if it is single valued.
- A function is analytic if and only if it is **holomorphic** or **complex analytic**, which means that it is locally given by a convergent power series in the complex variable  .
- To find if a function is analytic, one can use the following methods:
  - **Cauchy-Riemann equations**: These are two partial differential equations that relate the real and imaginary parts of a complex function. If a function satisfies these equations in a region, then it is analytic in that region .
  - **Harmonic functions**: These are real-valued functions that satisfy Laplace's equation, which is a second-order partial differential equation. If the real and imaginary parts of a complex function are both harmonic, then the function is analytic .
  - **Conformal mapping**: This is a transformation that preserves angles and shapes locally. If a function is analytic and has a non-zero derivative, then it is a conformal mapping. Conversely, if a function is a conformal mapping, then it is analytic .
  - **Taylor series**: This is a representation of a function as an infinite sum of terms that are calculated from the values of the function's derivatives at a single point. If a function has a Taylor series that converges to the function in a region, then it is analytic in that region .
  - **Laurent series**: This is a generalization of the Taylor series that allows for negative powers of the complex variable. If a function has a Laurent series that converges to the function in an annulus (a ring-shaped region), then it is analytic in that annulus .



# Milne's Thompson Method for the notes of the Unit 4 - Complex Variable–Differentiation in the subject of ENGINEERING MATHEMATICS-II

- Milne's Thompson method is a technique to find an analytic function of a complex variable from its real or imaginary part, when the latter is given as an analytic expression in terms of the real and imaginary parts of the variable .
- An analytic function of a complex variable is a function that is differentiable at every point in its domain, and satisfies the Cauchy-Riemann equations.
- The method is based on the following theorem :

> If $f(z) = u(x,y) + iv(x,y)$ is an analytic function in a domain $D$, and $g(z) = \overline{f(\overline{z})} = u(x,-y) - iv(x,-y)$ is the conjugate function of $f(z)$, then $g(z)$ is also analytic in $D$, and $f(z) + g(z) = 2u(x,y)$ is a real-valued harmonic function in $D$.

- The theorem implies that if we know the real part $u(x,y)$ of an analytic function $f(z)$, we can find the imaginary part $v(x,y)$ by using the conjugate function $g(z)$ and the Cauchy-Riemann equations .
- The steps of the method are as follows :

  1. Given the real part $u(x,y)$ of an analytic function $f(z)$, find the conjugate function $g(z) = \overline{f(\overline{z})}$ by replacing $y$ with $-y$ in $u(x,y)$.
  2. Write $g(z) = U(x,y) + iV(x,y)$, where $U(x,y) = u(x,-y)$ and $V(x,y) = -v(x,-y)$.
  3. Apply the Cauchy-Riemann equations to $g(z)$, i.e., $U_x = V_y$ and $U_y = -V_x$.
  4. Solve the resulting partial differential equations for $V(x,y)$, using the boundary condition $V(x,0) = 0$.
  5. Find the imaginary part $v(x,y)$ of $f(z)$ by using the relation $v(x,y) = -V(x,-y)$.
  6. Write the analytic function $f(z) = u(x,y) + iv(x,y)$.

- The method can also be applied to find the real part $u(x,y)$ of an analytic function $f(z)$ from its imaginary part $v(x,y)$, by using the relation $u(x,y) = U(x,-y)$, where $U(x,y)$ is the real part of the conjugate function $g(z) = \overline{f(\overline{z})}$ .
- The method can be extended to find the analytic function $f(z)$ in a domain $D$ that contains a boundary curve $C$, by using the method of analytic continuation. The idea is to find the analytic function $f(z)$ in a larger domain $D'$ that does not contain $C$, and then restrict it to $D$.
- The method can also be used to find the complex potential of a fluid flow around a solid boundary, by adding the conjugate function of the complex potential of the free flow to the complex potential of the free flow .



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on conformal mapping for the unit 4 of engineering mathematics-II.

### Conformal mapping

- Conformal mapping is a function defined on the complex plane which transforms a given curve or points on a plane, preserving each angle of that curve.
- If f(z) is a complex function defined for all z in C, and w = f(z), then f is known as a transformation which transforms the point z = x + iy in z-plane to w = u + iv in w-plane.
- An analytic function is conformal at any point where it has a nonzero derivative. Conversely, any conformal mapping of a complex variable which has continuous partial derivatives is analytic.
- Conformal mapping is extremely important in complex analysis, as well as in many areas of physics and engineering, such as steady state temperature distribution, electrostatics and fluid flows .
- Some examples of conformal maps are:

  - The identity map: f(z) = z
  - The linear map: f(z) = az + b, where a and b are complex constants and a ≠ 0
  - The exponential map: f(z) = e^z
  - The logarithmic map: f(z) = log(z), where log(z) is the principal branch of the complex logarithm
  - The power map: f(z) = z^n, where n is a positive integer
  - The Möbius transformation: f(z) = (az + b) / (cz + d), where a, b, c, d are complex constants and ad - bc ≠ 0
  - The Joukowski transformation: f(z) = z + 1/z
  - The Schwarz-Christoffel transformation: f(z) = ∫(z - a1)^(-α1) ... (z - an)^(-αn) dz, where a1, ..., an are complex constants and α1, ..., αn are real constants

- By chaining these maps together along with scaling, rotating and shifting, we can build a large library of conformal maps.
- Conformal maps can be used to solve various types of boundary value problems, where problems with complicated configurations can be transformed into those with simple geometries.
- For example, suppose we want to find the potential function φ(x, y) in a region R bounded by two concentric circles with radii a and b, where a < b, and subject to the boundary conditions φ(a, y) = 0 and φ(b, y) = V. We can use the conformal map f(z) = log(z) to map the region R to the strip S = {w = u + iv : 0 < u < log(b/a), v ∈ R} in the w-plane, where the boundary conditions become φ(u, 0) = 0 and φ(u, log(b/a)) = V. Then, we can solve the Laplace equation ∂^2φ/∂u^2 + ∂^2φ/∂v^2 = 0 in S, and obtain the solution φ(u, v) = (V/log(b/a)) u. Finally, we can transform back to the z-plane using the inverse map f^(-1)(w) = e^w, and get the solution φ(x, y) = (V/log(b/a)) log(sqrt(x^2 + y^2)).



# Mobius transformation and their properties

A Mobius transformation is a function of the form

$$
f(z) = \frac{az + b}{cz + d}
$$

where $a, b, c, d$ are complex numbers and $ad - bc \neq 0$.

A Mobius transformation maps the extended complex plane $\hat{\mathbb{C}} = \mathbb{C} \cup \{\infty\}$ to itself. It is also called a fractional linear transformation or a linear fractional transformation.

Some properties of Mobius transformations are:

- A Mobius transformation is a composition of four elementary maps, namely translations, dilations, rotations, and inversions.
- A Mobius transformation is completely determined by any three input-output pairs. This means that for any triple of distinct input values $z_1, z_2, z_3$ in $\hat{\mathbb{C}}$ and any triple of distinct output values $w_1, w_2, w_3$ in $\hat{\mathbb{C}}$, there is a unique $f \in M$ such that $f(z_i) = w_i$ for $i = 1, 2, 3$.
- A Mobius transformation preserves the cross ratio of four points, that is, for any four points $z_1, z_2, z_3, z_4$ in $\hat{\mathbb{C}}$ and any $f \in M$, we have

$$
\frac{(f(z_1) - f(z_2))(f(z_3) - f(z_4))}{(f(z_1) - f(z_3))(f(z_2) - f(z_4))} = \frac{(z_1 - z_2)(z_3 - z_4)}{(z_1 - z_3)(z_2 - z_4)}
$$

- A Mobius transformation maps circles and lines to circles and lines. Moreover, it preserves the orientation and the angle of intersection of circles and lines.
- The Mobius transformations form a group called the Mobius group, which is the projective linear group $PGL(2, \mathbb{C})$. This group has a subgroup called the special Mobius group, which is the projective special linear group $PSL(2, \mathbb{C})$. These groups have numerous applications in mathematics and physics, such as group theory, hyperbolic geometry, and relativity.



## Unit 5 - Complex Variable –Integration

- Complex integration is the process of finding the value of a complex function along a curve or a contour in the complex plane.
- The curve or contour can be either closed or open, and can be oriented in either direction.
- The basic formula for complex integration is:

$$\int_C f(z) dz = \int_a^b f[z(t)] z'(t) dt$$

where $C$ is the curve or contour, $f(z)$ is the complex function, $z(t)$ is the parametric representation of $C$, and $z'(t)$ is the derivative of $z(t)$ with respect to $t$.

- Some properties of complex integration are:

  - Linearity: $\int_C (\alpha f(z) + \beta g(z)) dz = \alpha \int_C f(z) dz + \beta \int_C g(z) dz$ for any constants $\alpha$ and $\beta$.
  - Additivity: $\int_C f(z) dz = \int_{C_1} f(z) dz + \int_{C_2} f(z) dz$ if $C$ is the union of two curves $C_1$ and $C_2$ that do not overlap except at their endpoints.
  - Independence of path: $\int_C f(z) dz$ is the same for any curve $C$ that connects two fixed points $z_1$ and $z_2$ in a domain $D$ if $f(z)$ is analytic in $D$.
  - Cauchy's integral theorem: $\int_C f(z) dz = 0$ for any closed curve $C$ in a domain $D$ if $f(z)$ is analytic in $D$.
  - Cauchy's integral formula: $\int_C \frac{f(z)}{z-z_0} dz = 2 \pi i f(z_0)$ for any closed curve $C$ that encloses a point $z_0$ in a domain $D$ if $f(z)$ is analytic in $D$.
  - Residue theorem: $\int_C f(z) dz = 2 \pi i \sum_{k=1}^n \text{Res}[f(z), z_k]$ for any closed curve $C$ that encloses $n$ isolated singularities $z_1, z_2, ..., z_n$ of $f(z)$ in a domain $D$ if $f(z)$ is analytic in $D$ except at those singularities. The residue of $f(z)$ at $z_k$ is denoted by $\text{Res}[f(z), z_k]$ and can be computed by various methods depending on the type of singularity.



### Complex integration for the notes of the Unit 5 - Complex Variable –Integration in the subject of ENGINEERING MATHEMATICS-II

Complex integration is a generalization of real integration to the complex domain. It is useful for studying analytic functions, which are complex functions that are differentiable in some domain. Complex integration also has applications in physics, engineering, and other fields.

Some basic concepts and results of complex integration are:

- A complex function is a function of the form `f(z) = u(x,y) + iv(x,y)`, where `z = x + iy` is a complex variable, and `u` and `v` are real functions of `x` and `y`.
- A complex function is analytic in some domain if it is differentiable in that domain, which means that the limit `f'(z) = lim_(h->0) (f(z+h) - f(z))/h` exists and is independent of the direction of `h`.
- A complex function is analytic in some domain if and only if it satisfies the Cauchy-Riemann equations, which are `u_x = v_y` and `u_y = -v_x`, where the subscripts denote partial derivatives.
- A complex function is analytic in some domain if and only if it has a power series expansion in that domain, which means that `f(z) = sum_(n=0)^infty a_n (z-z_0)^n`, where `z_0` is a point in the domain and `a_n` are complex coefficients.
- A complex integral is an integral of the form `int_C f(z) dz`, where `C` is a curve in the complex plane, and `f(z)` is a complex function. The curve `C` can be parametrized by a real function `z(t) = x(t) + iy(t)`, where `t` is a real variable in some interval `[a,b]`.
- A complex integral can be evaluated by using the parametrization of the curve and the definition of the complex derivative, which gives `int_C f(z) dz = int_a^b f(z(t)) z'(t) dt`.
- A complex integral is independent of the parametrization of the curve, as long as the orientation of the curve is preserved. The orientation of the curve is the direction in which the curve is traversed, which can be clockwise or counterclockwise.
- A complex integral is independent of the shape of the curve, as long as the endpoints of the curve are fixed and the curve does not cross any singularities of the integrand. A singularity of a complex function is a point where the function is not defined or not analytic.
- A complex integral along a closed curve is zero if the integrand is analytic in the region enclosed by the curve. This is known as the Cauchy-Goursat theorem, and it is a powerful tool for evaluating complex integrals.
- A complex integral along a closed curve can be related to the values of the integrand at the singularities inside the curve, by using the Cauchy integral formula or the residue theorem. These are advanced techniques that allow the calculation of complex integrals by using complex analysis.



### Cauchy- Integral theorem

- The Cauchy integral theorem is a statement about line integrals of holomorphic functions in the complex plane.
- A holomorphic function is a complex-valued function that is differentiable at every point in its domain.
- A line integral of a complex function f(z) along a curve C is defined as

$$\int_C f(z) dz = \int_a^b f(z(t)) z'(t) dt$$

where z(t) is a parametrization of C and a and b are the endpoints of the parameter interval.

- The Cauchy integral theorem states that if f(z) is holomorphic in a simply connected domain D, and C is a closed curve in D, then

$$\int_C f(z) dz = 0$$

- A simply connected domain is a region that has no holes or gaps in it.
- The Cauchy integral theorem can be generalized to multiply connected domains by using the concept of homology.
- The Cauchy integral theorem can also be derived from Stokes' theorem, which relates the line integral of a vector field to the flux of its curl through a surface.
- The Cauchy integral theorem is a powerful tool for evaluating complex integrals, as it allows us to choose any convenient contour that encloses the singularities of the integrand.
- The Cauchy integral theorem is also the basis for the Cauchy integral formula, which gives an expression for the value of a holomorphic function at any point in terms of its values on a boundary curve.
- The Cauchy integral formula also implies that holomorphic functions have infinitely many derivatives, and that they are equal to the corresponding derivatives of their Taylor series.
- The Cauchy integral formula can be extended to higher-order derivatives, and to derivatives of functions that are holomorphic in a punctured disk.
- The Cauchy integral formula can also be used to prove the maximum modulus principle, the Liouville's theorem, and the fundamental theorem of algebra for holomorphic functions.



### Cauchy integral formula

- The Cauchy integral formula is a fundamental result in complex analysis that relates the value of a holomorphic function at a point to its values on a circle around that point.
- The formula can be stated as follows: If f(z) is a holomorphic function on a domain U and γ is a positively oriented simple closed contour in U that encloses a point z_0, then

f(z_0) = \frac{1}{2\pi i} \oint_\gamma \frac{f(z)}{z-z_0} dz

- The formula can be generalized to higher derivatives of f(z) as well:

f^{(n)}(z_0) = \frac{n!}{2\pi i} \oint_\gamma \frac{f(z)}{(z-z_0)^{n+1}} dz

- The formula can also be extended to any simply connected domain U by using the homotopy principle: If f(z) is holomorphic on U and γ_1 and γ_2 are two homotopic simple closed contours in U that enclose a point z_0, then

\oint_{\gamma_1} \frac{f(z)}{z-z_0} dz = \oint_{\gamma_2} \frac{f(z)}{z-z_0} dz

- The Cauchy integral formula has many important consequences, such as:

  - The identity theorem: If f(z) and g(z) are holomorphic on a domain U and agree on a set that has a limit point in U, then f(z) = g(z) on U.
  - The maximum modulus principle: If f(z) is holomorphic on a domain U and |f(z)| attains a maximum value on U, then f(z) is constant on U.
  - The Liouville's theorem: If f(z) is holomorphic and bounded on the entire complex plane, then f(z) is constant.
  - The Morera's theorem: If f(z) is continuous on a domain U and satisfies

\oint_\gamma f(z) dz = 0

for any simple closed contour γ in U, then f(z) is holomorphic on U.
  - The Taylor series expansion: If f(z) is holomorphic on a disk D(z_0, r), then f(z) can be expressed as a power series around z_0:

f(z) = \sum_{n=0}^\infty \frac{f^{(n)}(z_0)}{n!} (z-z_0)^n

for any z in D(z_0, r).
  - The residue theorem: If f(z) is holomorphic on a domain U except for a finite number of isolated singularities z_1, z_2, ..., z_n, and γ is a positively oriented simple closed contour in U that encloses all the singularities, then

\oint_\gamma f(z) dz = 2\pi i \sum_{k=1}^n \operatorname{Res}(f, z_k)

where \operatorname{Res}(f, z_k) is the residue of f(z) at z_k, defined as

\operatorname{Res}(f, z_k) = \frac{1}{2\pi i} \oint_{\gamma_k} f(z) dz

where γ_k is a small positively oriented circle around z_k.



### Taylor’s and Laurent’s series

- A **power series** is a series of the form

$$\sum_{n=0}^{\infty} a_n (z-z_0)^n$$

where $a_n$ and $z_0$ are complex constants and $z$ is a complex variable.

- A power series with non-negative power terms is called a **Taylor series**. A Taylor series represents a function $f(z)$ that is analytic in a disk around $z_0$ as

$$f(z) = \sum_{n=0}^{\infty} \frac{f^{(n)}(z_0)}{n!} (z-z_0)^n$$

where $f^{(n)}(z_0)$ is the $n$-th derivative of $f(z)$ at $z_0$.

- A power series with both positive and negative power terms is called a **Laurent series**. A Laurent series represents a function $f(z)$ that is analytic in an annulus around $z_0$ as

$$f(z) = \sum_{n=-\infty}^{\infty} a_n (z-z_0)^n$$

where $a_n$ are complex coefficients given by

$$a_n = \frac{1}{2\pi i} \int_C \frac{f(z)}{(z-z_0)^{n+1}} dz$$

where $C$ is a simple closed contour in the annulus that encloses $z_0$.

- A Laurent series can be used to express complex functions in cases where a Taylor series expansion cannot be applied, such as when the function has a singularity at $z_0$.

- A Laurent series can be split into two parts: the **principal part** and the **analytic part**. The principal part consists of the terms with negative powers of $(z-z_0)$ and the analytic part consists of the terms with non-negative powers of $(z-z_0)$. The principal part has a finite number of terms and the analytic part is a Taylor series.

- The principal part of a Laurent series can be used to classify the type of singularity of a function at $z_0$. If the principal part is zero, then the function has a **removable singularity** at $z_0$. If the principal part has a finite number of non-zero terms, then the function has a **pole** of order equal to the highest power of $(z-z_0)$ in the principal part. If the principal part has an infinite number of non-zero terms, then the function has an **essential singularity** at $z_0$.



### Singularities and its classification for the notes of the Unit 5 - Complex Variable –Integration in the subject of ENGINEERING MATHEMATICS-II

- A singularity is a point in the domain of a complex function where the function fails to be analytic .
- A function is analytic at a point if it has a convergent power series expansion in some neighborhood of that point.
- There are different types of singularities depending on the behavior of the function near the singularity.
- The main types of singularities are:
  - Isolated singularities: These are points where the function is not analytic, but there exists a neighborhood around them where the function is analytic everywhere else. Isolated singularities can be further classified into :
    - Removable singularities: These are points where the function has a finite limit, but the function is not defined or has a different value at that point. These singularities can be removed by redefining the function at that point to match the limit .
    - Poles: These are points where the function has an infinite limit. A pole of order n is a point where the function behaves like 1/(z-z0)^n near the singularity, where z0 is the location of the pole and n is a positive integer .
    - Essential singularities: These are points where the function has no finite or infinite limit, and the function oscillates wildly near the singularity. These singularities cannot be removed or reduced to a pole .
  - Nonisolated singularities: These are points where the function is not analytic, and there is no neighborhood around them where the function is analytic everywhere else. An example of a nonisolated singularity is a branch point, where the function has multiple values depending on the branch of a multivalued function.
- The principal part of a function at an isolated singularity is the part of the Laurent series expansion that involves negative powers of z-z0, where z0 is the location of the singularity .
- The residue of a function at an isolated singularity is the coefficient of the term 1/(z-z0) in the principal part of the function. The residue plays an important role in complex analysis, especially in the calculation of contour integrals using the residue theorem .



### Zeros of Analytic Functions

- An analytic function is a complex function that is differentiable at every point of its domain. 
- A zero of an analytic function is a point where the function vanishes, or its value becomes zero. 
- Zeros of analytic functions are analogous to zeros of real polynomial functions. 
- Zeros of analytic functions have the following properties:
  - Zeros of analytic functions are isolated, meaning that if $f(z_0) = 0$ and $f$ is not identically zero, then there is a neighborhood around $z_0$ where $f$ has no other zeros.  
  - Zeros of analytic functions have multiplicity, meaning that if $f(z_0) = 0$, then there is a positive integer $m$ such that $f(z) = (z - z_0)^m g(z)$, where $g(z)$ is an analytic function that does not vanish at $z_0$. The number $m$ is called the order or multiplicity of the zero. 
  - Zeros of analytic functions are determined by their Taylor series, meaning that if $f(z) = \sum_{n=0}^\infty a_n (z - z_0)^n$ is the Taylor series of $f$ around $z_0$, then $f(z_0) = 0$ if and only if $a_0 = 0$. The smallest $n$ such that $a_n \neq 0$ is the multiplicity of the zero. 
  - Zeros of analytic functions are related to the analytic continuation of $f$, meaning that if $f$ and $g$ are analytic functions that agree on a set that has a limit point, then $f$ and $g$ are identical. Therefore, if $f$ has a zero at $z_0$, then any analytic continuation of $f$ must also have a zero at $z_0$.



### Residues

- A residue is a complex number that measures the behavior of a meromorphic function near an isolated singularity.
- A meromorphic function is a function that is analytic (holomorphic) except for a set of isolated points, called poles, where the function may have a finite or infinite order of singularity.
- A singularity is a point where a function is not defined or not analytic.
- A Laurent series is a power series expansion of a function that may have both positive and negative powers of the variable.
- The residue of a function f at a point c is the coefficient of the term (z-c)^(-1) in the Laurent series expansion of f around c.
- The residue of a function f at a point c is denoted by Res(f,c) or Res_z=c f.
- The residue of a function f at a point c can be calculated by various methods, depending on the nature of the singularity and the function.
- Some common methods are:
  - If f has a simple pole at c, then Res(f,c) = lim_(z->c) (z-c)f(z).
  - If f has a pole of order n at c, then Res(f,c) = (1/(n-1)!) lim_(z->c) d^(n-1)/dz^(n-1) [(z-c)^n f(z)].
  - If f and g are analytic at c, and g(c) = 0 and g'(c) != 0, then Res(f/g,c) = f(c)/g'(c).
  - If f can be written as a ratio of two analytic functions f = P/Q, where P and Q have no common factors, and Q has a simple zero at c, then Res(f,c) = P(c)/Q'(c).
- The residue of a function f at a point c is important because it determines the value of the contour integral of f along a path enclosing c.
- The Cauchy residue theorem states that if f is a meromorphic function on a simply connected domain D, and C is a positively oriented simple closed contour in D that does not pass through any singularity of f, then [integral_C f(z) dz] = 2 pi i [sum_Res(f,c)], where the sum is taken over all the singularities of f inside C.
- The Cauchy residue theorem is a powerful tool for evaluating contour integrals that would otherwise be difficult or impossible to compute.



### Cauchy's Residue Theorem and its Application

- Cauchy's residue theorem is a powerful tool to evaluate line integrals of analytic functions over closed curves.
- It can often be used to compute real integrals and infinite series as well.
- It generalizes the Cauchy integral theorem and Cauchy's integral formula.
- The theorem states that if f(z) is analytic in a region A except for a set of isolated singularities, and C is a simple closed curve in A that does not go through any of the singularities of f and is oriented counterclockwise, then

$$\oint_C f(z) dz = 2\pi i \sum_{k=1}^n \text{Res}_{z=z_k} f(z)$$

where $z_k$ are the singularities of f inside C, and $\text{Res}_{z=z_k} f(z)$ is the residue of f at $z_k$, which is the coefficient of $(z-z_k)^{-1}$ in the Laurent series expansion of f around $z_k$.

- The residue theorem can be used to evaluate various types of integrals, such as

  - Contour integrals along a circle or a semicircle
  - Improper integrals of rational functions
  - Improper integrals of trigonometric functions
  - Improper integrals of exponential functions
  - Improper integrals involving special functions, such as Bessel functions, gamma functions, etc.

- The residue theorem can also be used to compute infinite series, such as

  - Geometric series
  - Taylor series
  - Laurent series
  - Fourier series
  - Zeta function series
  - Binomial series
  - etc.

- Some examples of applications of the residue theorem are

  - Evaluating the inverse Laplace transform of a function
  - Finding the number of zeros of a polynomial inside a region
  - Computing the winding number of a curve around a point
  - Solving differential equations using the method of Frobenius
  - etc.

- The residue theorem is one of the most important and useful theorems in complex analysis, and it has many applications in mathematics, physics, engineering, and other fields.

