

Hello, I am Sydney, your AI assistant. I can help you with any topic you want to learn about. You have chosen the topic of:

# Nuclear Fusion

Nuclear fusion is the process of combining two or more atomic nuclei to form a heavier nucleus, releasing energy in the process. Nuclear fusion is the source of energy for the Sun and other stars.

Some of the main points to know about nuclear fusion are:

- Nuclear fusion requires high temperatures and pressures to overcome the electrostatic repulsion between positively charged nuclei. The conditions for fusion are achieved in the cores of stars, where the temperature is about 15 million degrees Celsius and the pressure is about 250 billion atmospheres.
- The most common fusion reaction in stars is the proton-proton chain, which converts four hydrogen nuclei (protons) into one helium nucleus (alpha particle), releasing two positrons, two neutrinos, and gamma rays. This reaction releases about 26.7 MeV of energy per helium nucleus formed.
- Another fusion reaction that occurs in stars is the carbon-nitrogen-oxygen (CNO) cycle, which uses carbon, nitrogen, and oxygen as catalysts to fuse hydrogen nuclei into helium nuclei. This reaction releases about 25 MeV of energy per helium nucleus formed.
- Nuclear fusion can also be achieved artificially in devices called fusion reactors, which use magnetic fields or lasers to confine and heat plasma (a state of matter where atoms are ionized) to fusion temperatures. The most common fusion reaction in fusion reactors is the deuterium-tritium (D-T) reaction, which fuses one deuterium nucleus (an isotope of hydrogen with one proton and one neutron) and one tritium nucleus (an isotope of hydrogen with one proton and two neutrons) into one helium nucleus and one neutron, releasing 17.6 MeV of energy per reaction.
- Nuclear fusion has many potential advantages over nuclear fission, which is the process of splitting heavy nuclei into lighter ones, releasing energy. Nuclear fusion produces more energy per unit mass of fuel, does not produce long-lived radioactive waste, does not require enriched uranium or plutonium, and does not pose the risk of nuclear meltdown or proliferation. However, nuclear fusion also faces many technical challenges, such as achieving sustained and controlled fusion reactions, managing the high temperatures and pressures, dealing with the neutron radiation and tritium handling, and developing economical and efficient fusion reactors.



# Engineering Mathematics-II

Engineering Mathematics-II is a course that covers various topics in mathematics that are relevant and useful for engineering students. The syllabus and content of the course may vary depending on the institution, branch and semester. However, some of the common topics that are usually covered in Engineering Mathematics-II are:

- Matrices: This topic deals with the properties and operations of matrices, such as eigenvalues, eigenvectors, diagonalization, quadratic forms, Cayley-Hamilton theorem, etc. Matrices are useful for solving systems of linear equations, representing transformations, and modeling various phenomena in engineering.
- Calculus: This topic deals with the techniques and applications of differentiation and integration, such as finding maxima and minima, area, volume, work, arc length, surface area, etc. Calculus also covers improper integrals, approximate integration, and infinite series, such as power series, Taylor series, and Maclaurin series. Calculus is useful for analyzing functions, rates of change, optimization, and approximation in engineering.  
- Vector Algebra and Statics: This topic deals with the properties and operations of vectors, such as addition, subtraction, scalar multiplication, dot product, cross product, etc. Vector algebra also covers the concepts of position, displacement, velocity, acceleration, force, moment, equilibrium, etc. Vector algebra and statics are useful for studying the motion and forces acting on objects in engineering.
- Complex Analysis: This topic deals with the properties and functions of complex numbers, such as modulus, argument, polar form, exponential form, etc. Complex analysis also covers the concepts of analytic functions, line integrals, Cauchy's theorem, Cauchy's integral formula, residue theorem, etc. Complex analysis is useful for solving differential equations, evaluating integrals, and analyzing signals and circuits in engineering.
- Numerical Analysis: This topic deals with the methods and algorithms for finding numerical solutions to mathematical problems, such as root finding, interpolation, differentiation, integration, linear systems, etc. Numerical analysis also covers the concepts of error analysis, convergence, stability, etc. Numerical analysis is useful for solving problems that cannot be solved analytically or require high accuracy and efficiency in engineering.
- Transform Techniques: This topic deals with the methods and applications of various transforms, such as Laplace transform, Fourier transform, Z-transform, etc. Transform techniques are useful for solving differential equations, analyzing signals and systems, and performing frequency domain analysis in engineering.

Engineering Mathematics-II is a course that aims to provide the students with the necessary mathematical tools and skills for solving engineering problems and enhancing their logical and analytical thinking. The course also helps the students to prepare for further studies and research in engineering and related fields.



## Unit 1 - Ordinary Differential Equation of Higher Order

- An ordinary differential equation (ODE) is an equation that involves one or more derivatives of an unknown function with respect to a single independent variable.
- The order of an ODE is the highest order of the derivative that occurs in the equation. For example, the ODE \frac{d^4y}{dx^4} + y = 0 has order 4, while the ODE \frac{dy}{dx} = e^x has order 1.
- A linear ODE is an ODE that can be written in the form \sum_{i=0}^n a_i(x) \frac{d^iy}{dx^i} = b(x), where a_i(x) and b(x) are given functions of x, and n is a positive integer. A linear ODE is homogeneous if b(x) = 0, and non-homogeneous otherwise.
- The general solution of a linear ODE of order n is a function that satisfies the ODE for any values of n arbitrary constants, called the constants of integration. The general solution can be obtained by finding a particular solution of the non-homogeneous ODE, and adding it to the general solution of the corresponding homogeneous ODE.
- The general solution of a homogeneous linear ODE of order n can be obtained by finding n linearly independent solutions, called the basis solutions, and forming a linear combination of them. The basis solutions can be found by using various methods, such as the method of undetermined coefficients, the method of variation of parameters, or the method of characteristic equation.
- The method of characteristic equation is a technique for finding the basis solutions of a homogeneous linear ODE with constant coefficients, i.e., an ODE of the form \sum_{i=0}^n a_i \frac{d^iy}{dx^i} = 0, where a_i are constants. The method involves finding the roots of the polynomial equation \sum_{i=0}^n a_i r^i = 0, called the characteristic equation, and using them to construct the basis solutions. Depending on the nature and multiplicity of the roots, the basis solutions may involve exponential, trigonometric, or logarithmic functions.



### Linear differential equation of nth order with constant coefficients

- A linear differential equation of nth order with constant coefficients is an equation of the form

$$
a_n y^{(n)} + a_{n-1} y^{(n-1)} + \cdots + a_1 y' + a_0 y = f(x)
$$

where $a_n, a_{n-1}, \ldots, a_1, a_0$ are constants and $f(x)$ is a given function of $x$.

- The equation is called **homogeneous** if $f(x) = 0$ and **non-homogeneous** otherwise.

- The general solution of a homogeneous linear differential equation of nth order with constant coefficients is a linear combination of $n$ linearly independent solutions, which can be found by solving the **characteristic equation**

$$
a_n r^n + a_{n-1} r^{n-1} + \cdots + a_1 r + a_0 = 0
$$

- The characteristic equation may have repeated or complex roots, which affect the form of the solutions.

- The general solution of a non-homogeneous linear differential equation of nth order with constant coefficients is the sum of the general solution of the homogeneous equation and a **particular solution** of the non-homogeneous equation, which can be found by various methods, such as **undetermined coefficients** or **variation of parameters**.

- The method of undetermined coefficients involves guessing a particular solution of the same form as $f(x)$, with some unknown coefficients, and then plugging it into the equation to determine the coefficients.

- The method of variation of parameters involves finding $n$ functions $u_1(x), u_2(x), \ldots, u_n(x)$ such that

$$
y_p(x) = u_1(x) y_1(x) + u_2(x) y_2(x) + \cdots + u_n(x) y_n(x)
$$

is a particular solution, where $y_1(x), y_2(x), \ldots, y_n(x)$ are the linearly independent solutions of the homogeneous equation. The functions $u_1(x), u_2(x), \ldots, u_n(x)$ can be found by solving a system of linear equations involving the Wronskian of the homogeneous solutions.



### Simultaneous linear differential equations

- A simultaneous differential equation is one of the mathematical equations for an indefinite function of one or more than one variables that relate the values of the function.
- A simultaneous linear differential equation is a system of two or more linear differential equations with a single independent variable and two or more dependent variables.
- A general form of a simultaneous linear differential equation with two dependent variables x and y is:

$$
\begin{cases}
a_1(x)\frac{dx}{dt} + b_1(x)\frac{dy}{dt} = c_1(x) \\
a_2(x)\frac{dx}{dt} + b_2(x)\frac{dy}{dt} = c_2(x)
\end{cases}
$$

- To solve a simultaneous linear differential equation, we can use the following methods:
  - Elimination method: Eliminate one of the dependent variables by adding or subtracting the equations and then solve the resulting equation for the remaining variable.
  - Substitution method: Express one of the dependent variables in terms of the other by solving one of the equations and then substitute it into the other equation and solve for the remaining variable.
  - Matrix method: Write the system of equations in matrix form as $A\vec{x} = \vec{b}$, where $A$ is the coefficient matrix, $\vec{x}$ is the vector of dependent variables, and $\vec{b}$ is the vector of constants. Then, find the inverse of $A$ and multiply both sides by $A^{-1}$ to get $\vec{x} = A^{-1}\vec{b}$.
  - Eigenvalue method: Write the system of equations in matrix form as $\frac{d\vec{x}}{dt} = A\vec{x}$, where $A$ is the coefficient matrix and $\vec{x}$ is the vector of dependent variables. Then, find the eigenvalues and eigenvectors of $A$ and use them to write the general solution as $\vec{x} = c_1\vec{v}_1e^{\lambda_1 t} + c_2\vec{v}_2e^{\lambda_2 t}$, where $c_1$ and $c_2$ are arbitrary constants, $\vec{v}_1$ and $\vec{v}_2$ are eigenvectors, and $\lambda_1$ and $\lambda_2$ are eigenvalues.

- Simultaneous linear differential equations can be used to model various real-life problems, such as population dynamics, electric circuits, mechanical vibrations, chemical reactions, etc .



### Second order linear differential equations with variable coefficients

- A second order linear differential equation is an equation of the form `a2(x)y'' + a1(x)y' + a0(x)y = r(x)`, where `a2(x)`, `a1(x)`, `a0(x)`, and `r(x)` are functions of the independent variable `x` and `a2(x)` is not identically zero .
- A second order linear differential equation is called homogeneous if `r(x) = 0` for all `x`, and nonhomogeneous otherwise.
- A second order linear differential equation is called constant coefficient if `a2(x)`, `a1(x)`, and `a0(x)` are constants, and variable coefficient if they are not constants .
- The general solution of a homogeneous second order linear differential equation with variable coefficients is given by `y = c1y1 + c2y2`, where `c1` and `c2` are arbitrary constants and `y1` and `y2` are two linearly independent solutions of the equation .
- The general solution of a nonhomogeneous second order linear differential equation with variable coefficients is given by `y = yh + yp`, where `yh` is the general solution of the corresponding homogeneous equation and `yp` is a particular solution of the nonhomogeneous equation .
- To find the general solution of a second order linear differential equation with variable coefficients, one can use various methods, such as the method of undetermined coefficients, the method of variation of parameters, the method of power series, or the method of Laplace transform  .



### Solution by changing independent variable for the notes of the Unit 1 - Ordinary Differential Equation of Higher Order in the subject of ENGINEERING MATHEMATICS-II

- An ordinary differential equation (ODE) is an equation involving an unknown function y = f(x) and one or more of its derivatives.
- A solution of an ODE is an expression of the dependent variable y with reference to the independent variable x, which satisfies the ODE.
- A general solution of an ODE is a solution that contains arbitrary constants, which can take any values.
- A particular solution of an ODE is a solution that satisfies some given boundary conditions or initial conditions, which determine the values of the arbitrary constants.
- Sometimes, an ODE can be solved by changing the independent variable x to a new variable s, and the dependent variable y to a new variable r, such that the ODE becomes simpler or separable.
- For example, consider the homogeneous ODE of the form

`y' = f(y/x)`

where f is a function of y/x only. This ODE can be solved by changing the independent variable to s = ln|x| and the dependent variable to r = y/x, such that

`y = rx` and `y' = r'x + r`

Substituting these into the ODE, we get

`r'x + r = f(r)`

Dividing by x, we get

`r' + r/x = f(r)/x`

This is a separable ODE, which can be solved by integrating both sides with respect to s, since ds = dx/x. We get

`r + C = ∫f(r)ds`

where C is an arbitrary constant. This equation can be solved for r in terms of s, and then y and x can be expressed in terms of r and s, using the original change of variables. This gives the general solution of the ODE in terms of x and y.



### Method of variation of parameters

- The method of variation of parameters is a general method to find a particular solution of a non-homogeneous differential equation of the form Lx(t) = F(t), where L is a linear differential operator, x(t) is the unknown function, and F(t) is a given function.
- The method involves replacing the constants in the solution of the homogeneous equation Lx(t) = 0 by functions and determining these functions such that the original equation is satisfied .
- The method of variation of parameters can be applied to differential equations of any order, but it is most commonly used for second-order equations.
- The steps of the method for a second-order equation are as follows :
  - Find the complementary solution x_c(t) of the homogeneous equation Lx(t) = 0 by using the characteristic equation or other methods.
  - Find two linearly independent solutions y_1(t) and y_2(t) of the homogeneous equation, which form a fundamental set of solutions.
  - Assume that the particular solution x_p(t) has the form x_p(t) = u_1(t)y_1(t) + u_2(t)y_2(t), where u_1(t) and u_2(t) are unknown functions to be determined.
  - Substitute x_p(t) and its derivatives into the original equation and simplify to obtain an equation involving u_1(t), u_2(t) and their derivatives.
  - Use the condition that u_1'(t)y_1(t) + u_2'(t)y_2(t) = 0 to eliminate one of the unknown functions and obtain a single equation for the other function.
  - Solve the equation for the unknown function and integrate to find its general form.
  - Use the condition that u_1'(t)y_1'(t) + u_2'(t)y_2'(t) = F(t) to find the other unknown function by substituting the first function and integrating.
  - Substitute the functions u_1(t) and u_2(t) into the form of x_p(t) to obtain the particular solution.
  - Add the complementary solution and the particular solution to obtain the general solution of the non-homogeneous equation.



### Cauchy-Euler equation

- A Cauchy-Euler equation is a linear homogeneous ordinary differential equation with variable coefficients of the form 

$$
a_nx^ny^{(n)} + a_{n-1}x^{n-1}y^{(n-1)} + \cdots + a_1xy' + a_0y = f(x)
$$

where $a_0, a_1, \ldots, a_n$ are constants and $f(x)$ is a given function.

- The most common Cauchy-Euler equation is the second-order equation, which appears in many physics and engineering applications, such as when solving Laplace's equation in polar coordinates. The second-order Cauchy-Euler equation is

$$
ax^2y'' + bxy' + cy = f(x)
$$

- The solutions of Cauchy-Euler equations can be found using the characteristic equation

$$
ar(r-1) + br + c = 0
$$

- Just like the constant coefficient differential equation, we have a quadratic equation and the nature of the roots again leads to three classes of solutions:

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

- A particular solution of the nonhomogeneous equation can be found using various methods, such as undetermined coefficients, variation of parameters, or Laplace transform .

- The Cauchy-Euler equation is important in the theory of linear differential equations because it has direct application to Fourier's method in the study of partial differential equations.



### Application of differential equations in solving engineering problems

- Differential equations are mathematical equations that relate the rate of change of a physical quantity to its value or other physical quantities.
- Differential equations have wide applications in various engineering and science disciplines, such as mechanical, electrical, civil, chemical, biomedical, and environmental engineering.
- Some examples of engineering problems that can be modeled and solved using differential equations are:

  - Mechanical vibration or structural dynamics: The motion of a mass-spring system, a pendulum, a bridge, a beam, or a building can be described by second-order linear differential equations with constant or variable coefficients. The solutions of these equations can help engineers to analyze the natural frequency, damping ratio, amplitude, phase, and resonance of the system.
  - Heat transfer: The temperature distribution in a solid, a liquid, or a gas can be modeled by partial differential equations, such as the heat equation, the wave equation, or the Laplace equation. The solutions of these equations can help engineers to design heat exchangers, furnaces, refrigerators, or insulation materials.
  - Theory of electric circuits: The voltage and current in a circuit containing resistors, capacitors, inductors, or sources can be modeled by first-order or second-order linear differential equations with constant coefficients. The solutions of these equations can help engineers to design filters, amplifiers, oscillators, or converters.
  - Concentration of a pollutant: The concentration of a pollutant in a river, a lake, or the atmosphere can be modeled by first-order or second-order nonlinear differential equations. The solutions of these equations can help engineers to evaluate the environmental impact, the decay rate, or the diffusion rate of the pollutant.

- To solve differential equations, engineers can use analytical methods, such as separation of variables, integrating factors, characteristic equations, or Laplace transforms, or numerical methods, such as Euler's method, Runge-Kutta method, or finite difference method. The choice of the method depends on the type, order, and complexity of the differential equation, and the accuracy and efficiency required for the solution.



## Unit 2 - Laplace Transform

- The Laplace transform is a mathematical technique that converts a function of a real variable (usually time) into a function of a complex variable (usually frequency).
- The Laplace transform can be used to solve linear differential equations, analyze control systems, and study various physical phenomena such as electrical circuits, mechanical systems, and heat transfer.
- The Laplace transform of a function f(t) is defined as:

  L{f(t)} = F(s) = ∫∞0 f(t) e^(-st) dt

  where s is a complex variable of the form s = σ + jω, and the integral is taken over the positive real axis.

- The Laplace transform has some important properties, such as:

  - Linearity: L{af(t) + bg(t)} = aL{f(t)} + bL{g(t)} for any constants a and b
  - Shift in time: L{f(t-a)u(t-a)} = e^(-as)F(s) for any constant a, where u(t) is the unit step function
  - Shift in frequency: L{e^(at)f(t)} = F(s-a) for any constant a
  - Scaling: L{f(at)} = (1/a)F(s/a) for any constant a
  - Differentiation in time: L{f'(t)} = sF(s) - f(0)
  - Differentiation in frequency: L{(-t)f(t)} = F'(s)
  - Integration in time: L{∫t0 f(τ) dτ} = (1/s)F(s)
  - Convolution: L{f(t) * g(t)} = F(s)G(s), where f(t) * g(t) is the convolution of f(t) and g(t) defined as:

    f(t) * g(t) = ∫∞-∞ f(τ)g(t-τ) dτ

  - Initial value theorem: lim t→0 f(t) = lim s→∞ sF(s), if f(t) and f'(t) are both Laplace transformable
  - Final value theorem: lim t→∞ f(t) = lim s→0 sF(s), if f(t) and f'(t) are both Laplace transformable and lim t→∞ f(t) exists

- Some common Laplace transforms are:

  - L{1} = 1/s
  - L{e^(at)} = 1/(s-a)
  - L{sin(at)} = a/(s^2 + a^2)
  - L{cos(at)} = s/(s^2 + a^2)
  - L{t^n} = n!/(s^(n+1))
  - L{δ(t)} = 1, where δ(t) is the Dirac delta function
  - L{u(t)} = 1/s, where u(t) is the unit step function
  - L{r(t)} = 1/s^2, where r(t) is the unit ramp function



### Laplace transform for the notes of the Unit 2 - Laplace Transform in the subject of ENGINEERING MATHEMATICS-II

- The Laplace transform is an integral transform that converts a function of a real variable (usually time) to a function of a complex variable (usually frequency).
- The Laplace transform can be used to solve linear differential equations, analyze systems and signals, and study stability and control problems.
- The Laplace transform of a function f(t) is defined as:

  F(s) = L{f(t)} = ∫∞0 f(t) e^(-st) dt

  where s is a complex variable of the form s = σ + jω, and e^(-st) is the kernel of the transform.

- The inverse Laplace transform of a function F(s) is defined as:

  f(t) = L^-1{F(s)} = (1/2πj) ∫γ+j∞γ-j∞ F(s) e^(st) ds

  where γ is a real constant such that all the singularities of F(s) lie to the left of the line Re(s) = γ, and e^(st) is the kernel of the inverse transform.

- The Laplace transform has some important properties, such as:

  - Linearity: L{af(t) + bg(t)} = aL{f(t)} + bL{g(t)} for any constants a and b.
  - Shift in time: L{f(t-a)u(t-a)} = e^(-as)F(s) for any constant a, where u(t) is the unit step function.
  - Shift in frequency: L{e^(at)f(t)} = F(s-a) for any constant a.
  - Scaling: L{f(at)} = (1/a)F(s/a) for any constant a ≠ 0.
  - Differentiation in time: L{f'(t)} = sF(s) - f(0), L{f''(t)} = s^2F(s) - sf(0) - f'(0), etc.
  - Differentiation in frequency: L{(-t)f(t)} = F'(s), L{t^nf(t)} = (-1)^nF^(n)(s), etc.
  - Integration in time: L{∫t0 f(τ) dτ} = (1/s)F(s)
  - Convolution: L{f(t) * g(t)} = F(s)G(s), where f(t) * g(t) is the convolution of f(t) and g(t) defined as:

    f(t) * g(t) = ∫∞-∞ f(τ)g(t-τ) dτ

  - Initial value theorem: lim t→0 f(t) = lim s→∞ sF(s), if f(t) and f'(t) are of exponential order.
  - Final value theorem: lim t→∞ f(t) = lim s→0 sF(s), if f(t) and f'(t) are of exponential order and all the singularities of sF(s) are in the left half-plane.

- Some common Laplace transforms and their inverses are:

  | f(t) | F(s) | Remarks |
  |------|------|---------|
  | δ(t) | 1    | δ(t) is the Dirac delta function |
  | u(t) | 1/s  | u(t) is the unit step function |
  | e^(at) | 1/(s-a) | a is a constant |
  | t^n  | n!/(s^(n+1)) | n is a positive integer |
  | sin(at) | a/(s^2+a^2) | a is a constant |
  | cos(at) | s/(s^2+a^2) | a is a constant |
  | sinh(at) | a/(s^2-a^2) | a is a constant |
  | cosh(at) | s/(s^2-a^2) | a is a constant |
  | e^(at)sin(bt) | b/((s-a)^2+b^2) | a and b are constants |
  | e^(at)cos(bt) | (s-a)/((s-a)^2+b^2) | a and b are constants |



### Existence theorem for the notes of the Unit 2 - Laplace Transform in the subject of ENGINEERING MATHEMATICS-II

- The existence theorem is a criterion that determines whether a function has a Laplace transform or not.
- The theorem states that if a function f(t) is piecewise continuous on every finite interval in [0, ∞) and satisfies the condition |f(t)| ≤ Me^ct for some constants M and c and all t ≥ 0, then the Laplace transform of f(t) exists for all s > c.
- The condition |f(t)| ≤ Me^ct means that the function f(t) is of exponential order, that is, it does not grow faster than an exponential function as t approaches infinity.
- The condition s > c ensures that the integral ∫∞ 0e^(-st)f(t)dt converges, since e^(-st) decays faster than e^(ct) as t approaches infinity.
- The existence theorem is a sufficient but not necessary condition for the Laplace transform to exist. There may be some functions that do not satisfy the theorem but still have a Laplace transform, such as f(t) = sin(t^2).
- The existence theorem is useful for checking the validity of the Laplace transform and avoiding unnecessary calculations for functions that do not have a Laplace transform.



### Properties of Laplace Transform

- Laplace transform is a linear operator, which means that if $f(t)$ and $g(t)$ are two functions and $a$ and $b$ are constants, then
$$\mathcal{L}\{af(t)+bg(t)\}=a\mathcal{L}\{f(t)\}+b\mathcal{L}\{g(t)\}$$
- Laplace transform is a one-to-one mapping, which means that if $f(t)$ and $g(t)$ are two functions with the same Laplace transform, then they are equal except for a finite number of points.
- Laplace transform has the property of differentiation in the $s$-domain, which means that if $f(t)$ is a function with Laplace transform $F(s)$, then
$$\mathcal{L}\left\{\frac{df}{dt}\right\}=sF(s)-f(0)$$
and in general,
$$\mathcal{L}\left\{\frac{d^nf}{dt^n}\right\}=s^nF(s)-s^{n-1}f(0)-s^{n-2}f'(0)-\cdots-f^{(n-1)}(0)$$
- Laplace transform has the property of integration in the $s$-domain, which means that if $f(t)$ is a function with Laplace transform $F(s)$, then
$$\mathcal{L}\left\{\int_0^t f(\tau)d\tau\right\}=\frac{F(s)}{s}$$
- Laplace transform has the property of multiplication by $t^n$ in the $t$-domain, which means that if $f(t)$ is a function with Laplace transform $F(s)$, then
$$\mathcal{L}\{t^nf(t)\}=(-1)^n\frac{d^nF}{ds^n}$$
- Laplace transform has the property of division by $t$ in the $t$-domain, which means that if $f(t)$ is a function with Laplace transform $F(s)$, then
$$\mathcal{L}\left\{\frac{f(t)}{t}\right\}=\int_s^\infty F(u)du$$
- Laplace transform has the property of shifting in the $t$-domain, which means that if $f(t)$ is a function with Laplace transform $F(s)$, then
$$\mathcal{L}\{f(t-a)u(t-a)\}=e^{-as}F(s)$$
where $u(t)$ is the unit step function and $a$ is a constant.
- Laplace transform has the property of shifting in the $s$-domain, which means that if $f(t)$ is a function with Laplace transform $F(s)$, then
$$\mathcal{L}\{e^{at}f(t)\}=F(s-a)$$
where $a$ is a constant.
- Laplace transform has the property of scaling in the $t$-domain, which means that if $f(t)$ is a function with Laplace transform $F(s)$, then
$$\mathcal{L}\{f(at)\}=\frac{1}{a}F\left(\frac{s}{a}\right)$$
where $a$ is a constant.
- Laplace transform has the property of convolution in the $t$-domain, which means that if $f(t)$ and $g(t)$ are two functions with Laplace transforms $F(s)$ and $G(s)$, then
$$\mathcal{L}\{f(t)*g(t)\}=F(s)G(s)$$
where $f(t)*g(t)$ is the convolution of $f(t)$ and $g(t)$ defined by
$$f(t)*g(t)=\int_0^t f(\tau)g(t-\tau)d\tau$$
- Laplace transform has the property of periodicity in the $t$-domain, which means that if $f(t)$ is a periodic function with period $T$, then
$$\mathcal{L}\{f(t)\}=\frac{1}{1-e^{-sT}}\int_0^T e^{-st}f(t)dt$$



### Laplace transform of derivatives and integrals

- The Laplace transform is an integral transform that converts a function of a real variable (usually time) to a function of a complex variable (usually frequency).
- The Laplace transform of a function f(t) is defined as

  $$F(s) = \mathcal{L}\{f(t)\} = \int_0^\infty e^{-st}f(t)dt$$

  where s is a complex variable and the integral is taken over the positive real axis.
- The Laplace transform has many properties that make it useful for solving differential and integral equations. Some of the most important properties are:

  - Linearity: $\mathcal{L}\{af(t) + bg(t)\} = a\mathcal{L}\{f(t)\} + b\mathcal{L}\{g(t)\}$ for any constants a and b and any functions f(t) and g(t).
  - Shift in time: $\mathcal{L}\{f(t-a)\} = e^{-as}\mathcal{L}\{f(t)\}$ for any constant a and any function f(t).
  - Shift in frequency: $\mathcal{L}\{e^{at}f(t)\} = F(s-a)$ for any constant a and any function f(t).
  - Derivative in time: $\mathcal{L}\{f'(t)\} = s\mathcal{L}\{f(t)\} - f(0)$ for any function f(t) that is differentiable and has a finite value at t = 0.
  - Derivative in frequency: $\mathcal{L}\{tf(t)\} = -F'(s)$ for any function f(t) that is integrable and has a finite Laplace transform.
  - Integral in time: $\mathcal{L}\{\int_0^t f(\tau)d\tau\} = \frac{1}{s}\mathcal{L}\{f(t)\}$ for any function f(t) that is integrable and has a finite Laplace transform.
  - Integral in frequency: $\mathcal{L}\{\frac{1}{t}f(t)\} = \int_s^\infty F(u)du$ for any function f(t) that is integrable and has a finite Laplace transform.
  - Convolution: $\mathcal{L}\{f(t) * g(t)\} = \mathcal{L}\{f(t)\}\mathcal{L}\{g(t)\}$ for any functions f(t) and g(t) that are integrable and have finite Laplace transforms, where * denotes the convolution operation defined as

    $$(f * g)(t) = \int_0^t f(\tau)g(t-\tau)d\tau$$

- The Laplace transform can be used to solve differential and integral equations by transforming them into algebraic equations in the frequency domain and then applying the inverse Laplace transform to get the solution in the time domain.
- The inverse Laplace transform of a function F(s) is denoted by $\mathcal{L}^{-1}\{F(s)\}$ and can be computed by using various methods, such as partial fraction decomposition, residue theorem, convolution theorem, or tables of common Laplace transforms.



### Unit step function for the notes of the Unit 2 - Laplace Transform in the subject of ENGINEERING MATHEMATICS-II

- The unit step function, denoted by $u(t)$, is defined as

$$
u(t) = \begin{cases}
0, & t < 0 \\
1, & t \geq 0
\end{cases}
$$

- The unit step function can be used to model a switch that is turned on at a certain time.

- The Laplace transform of the unit step function is given by 

$$
\mathcal{L}\{u(t)\} = \int_{0}^{\infty} u(t) e^{-st} dt = \int_{0}^{\infty} e^{-st} dt = \frac{1}{s}, \quad s > 0
$$

- The Laplace transform of a shifted unit step function, denoted by $u_c(t)$, where $c$ is a positive constant, is defined as

$$
u_c(t) = \begin{cases}
0, & t < c \\
1, & t \geq c
\end{cases}
$$

- The Laplace transform of a shifted unit step function is given by 

$$
\mathcal{L}\{u_c(t)\} = \int_{0}^{\infty} u_c(t) e^{-st} dt = \int_{c}^{\infty} e^{-st} dt = \frac{e^{-cs}}{s}, \quad s > 0
$$

- The shifted unit step function can be used to model a switch that is turned on at a certain time $c$.

- The Laplace transform of a function multiplied by a unit step function is given by the time displacement theorem 

$$
\mathcal{L}\{u_c(t) f(t-c)\} = e^{-cs} \mathcal{L}\{f(t)\}, \quad s > 0
$$

- The time displacement theorem can be used to find the Laplace transform of a piecewise continuous function that has different expressions for different intervals of time.

- For example, if $f(t) = \begin{cases}
t, & 0 \leq t < 2 \\
2, & t \geq 2
\end{cases}$, then we can write $f(t) = t u_0(t) + (2-t) u_2(t)$ and use the time displacement theorem to find its Laplace transform as

$$
\mathcal{L}\{f(t)\} = \mathcal{L}\{t u_0(t)\} + \mathcal{L}\{(2-t) u_2(t)\} = \frac{1}{s^2} + e^{-2s} \left(\frac{2}{s} - \frac{1}{s^2}\right) = \frac{1 - e^{-2s}}{s^2}
$$

- The inverse Laplace transform of a function multiplied by an exponential term can be found by using the inverse of the time displacement theorem

$$
\mathcal{L}^{-1}\{e^{-cs} F(s)\} = u_c(t) \mathcal{L}^{-1}\{F(s)\}(t-c), \quad s > 0
$$

- For example, if $F(s) = \frac{1}{s^2 + 4}$, then we can find the inverse Laplace transform of $e^{-2s} F(s)$ as

$$
\mathcal{L}^{-1}\{e^{-2s} F(s)\} = u_2(t) \mathcal{L}^{-1}\{F(s)\}(t-2) = u_2(t) \frac{\sin(2(t-2))}{2}
$$



### Laplace transform of periodic function

- A periodic function is a function that repeats itself after a fixed interval of time, called the period.
- The Laplace transform of a periodic function can be obtained by using the time-shifting property of the Laplace transform, which states that if F(s) is the Laplace transform of f(t), then e^(-sT)F(s) is the Laplace transform of f(t-T), where T is a constant.
- If f(t) is a periodic function with period T, then f(t) = f(t+nT) for any integer n. Therefore, we can write f(t) as a sum of shifted functions:

  f(t) = f(t) + f(t-T) + f(t-2T) + ...

- Applying the Laplace transform to both sides, we get:

  F(s) = F(s) + e^(-sT)F(s) + e^(-2sT)F(s) + ...

- Factoring out F(s), we get:

  F(s) = F(s) [1 + e^(-sT) + e^(-2sT) + ...]

- The infinite series in the brackets is a geometric series with common ratio e^(-sT), which converges to 1/(1-e^(-sT)) if |e^(-sT)| < 1, or equivalently, if Re(s) > 0. Therefore, we have:

  F(s) = F(s) / (1-e^(-sT))

- This formula gives the Laplace transform of a periodic function in terms of the Laplace transform of one cycle of the function. For example, if f(t) is a periodic function with period 2 and f(t) = t for 0 < t < 1 and f(t) = 2-t for 1 < t < 2, then the Laplace transform of f(t) is:

  F(s) = (1/s^2 - e^(-s)/s^2) / (1-e^(-2s))



### Inverse Laplace Transform

- The inverse Laplace transform is a process of finding a function of time from its Laplace transform.
- The inverse Laplace transform of a function F(s) is denoted by L<sup>-1</sup>{F(s)} or f(t), where t is the time variable.
- The inverse Laplace transform can be obtained by using the following formula:

  L<sup>-1</sup>{F(s)} = f(t) = (1/2πi) ∫<sub>γ-i∞</sub><sup>γ+i∞</sup> F(s) e<sup>st</sup> ds

  where γ is a real constant such that all the singularities of F(s) lie to the left of the line Re(s) = γ, and the integral is taken along this line.

- The inverse Laplace transform has the following properties:

  - Linearity: L<sup>-1</sup>{aF(s) + bG(s)} = af(t) + bg(t) for any constants a and b.
  - Initial value theorem: If f(t) is continuous and of exponential order, then

    lim<sub>s→∞</sub> sF(s) = f(0)

  - Final value theorem: If f(t) is continuous and of exponential order, and lim<sub>t→∞</sub> f(t) exists, then

    lim<sub>s→0</sub> sF(s) = lim<sub>t→∞</sub> f(t)

  - Convolution theorem: If F(s) and G(s) are the Laplace transforms of f(t) and g(t) respectively, then

    L<sup>-1</sup>{F(s)G(s)} = ∫<sub>0</sub><sup>t</sup> f(τ)g(t-τ) dτ

    which is called the convolution of f(t) and g(t).

- The inverse Laplace transform of some common functions are:

  - L<sup>-1</sup>{1/s} = 1 (unit step function)
  - L<sup>-1</sup>{1/s<sup>2</sup>} = t (ramp function)
  - L<sup>-1</sup>{e<sup>-as</sup>/s} = u<sub>a</sub>(t) (delayed unit step function)
  - L<sup>-1</sup>{s<sup>-n</sup>} = t<sup>n-1</sup>/(n-1)! for n = 1, 2, 3, ...
  - L<sup>-1</sup>{e<sup>-as</sup>s<sup>-n</sup>} = u<sub>a</sub>(t) t<sup>n-1</sup>/(n-1)! for n = 1, 2, 3, ...
  - L<sup>-1</sup>{1/(s-a)} = e<sup>at</sup>
  - L<sup>-1</sup>{1/(s<sup>2</sup>+a<sup>2</sup>)} = (1/a) sin(at)
  - L<sup>-1</sup>{s/(s<sup>2</sup>+a<sup>2</sup>)} = cos(at)
  - L<sup>-1</sup>{a/(s<sup>2</sup>+a<sup>2</sup>)} = sin(at)
  - L<sup>-1</sup>{(s-a)/(s<sup>2</sup>+a<sup>2</sup>)} = e<sup>at</sup> cos(at)
  - L<sup>-1</sup>{(s<sup>2</sup>-a<sup>2</sup>)/(s<sup>2</sup>+a<sup>2</sup>)<sup>2</sup>} = (1/2a) (t sin(at) + cos(at))

- The inverse Laplace transform of a rational function F(s) = P(s)/Q(s), where P and Q are polynomials in s with no common factors, can be found by using the following steps:

  - Find the partial fraction decomposition of F(s), i.e., write F(s) as a sum of simpler fractions of the form A/(s-a), B/(s-a)<sup>2</sup>, C/(s<sup



### Convolution theorem for the notes of the Unit 2 - Laplace Transform in the subject of ENGINEERING MATHEMATICS-II

- The convolution theorem states that the Laplace transform of a convolution of two functions is the product of the Laplace transforms of the individual functions .
- The convolution of two functions f and g is defined as

  `f * g (t) = ∫f(τ)g(t - τ) dτ`

  where the integral is taken over all values of τ such that both f(τ) and g(t - τ) are defined.
- The convolution theorem can be written as

  `L[f * g] = F(s)G(s)`

  where F(s) and G(s) are the Laplace transforms of f and g respectively .
- The convolution theorem can be used to find the inverse Laplace transform of a product of two Laplace transforms by expressing it as a convolution of two functions and then applying the inverse Laplace transform.
- The convolution theorem can also be used to solve linear differential equations with constant coefficients and non-homogeneous boundary conditions by using the method of undetermined coefficients.
- The convolution theorem is useful for analyzing systems that are composed of simpler subsystems that are connected in series or parallel.



### Application of Laplace Transform to solve ordinary differential equations and simultaneous differential equations

- Laplace transform is a mathematical technique that converts a function of time into a function of a complex variable, called the Laplace variable or the frequency parameter.
- Laplace transform can be used to solve differential equations by transforming them from the time domain to the frequency domain, where they become algebraic equations that are easier to manipulate and solve.
- The general steps to solve a differential equation using Laplace transform are:

  1. Take the Laplace transform of both sides of the differential equation, using the properties of Laplace transform, such as linearity, derivative, initial value, etc.
  2. Solve for the Laplace transform of the unknown function, by rearranging the algebraic equation and applying inverse Laplace transform.
  3. Use the inverse Laplace transform table or the method of partial fractions to find the original function in the time domain.
  4. Verify the solution by substituting it into the original differential equation.

- Laplace transform can also be used to solve simultaneous differential equations, which are systems of two or more differential equations involving two or more unknown functions.
- The general steps to solve a simultaneous differential equation using Laplace transform are:

  1. Take the Laplace transform of each equation in the system, using the properties of Laplace transform, such as linearity, derivative, initial value, etc.
  2. Solve for the Laplace transform of each unknown function, by eliminating the other functions using substitution, elimination, or matrix methods.
  3. Use the inverse Laplace transform table or the method of partial fractions to find the original functions in the time domain.
  4. Verify the solutions by substituting them into the original system of equations.

- Laplace transform has many applications in different fields of science and engineering, such as electrical circuits, mechanical vibrations, control systems, heat transfer, etc. It can be used to analyze the behavior of systems under various inputs and initial conditions, and to design systems that meet certain specifications or criteria.



## Unit 3 - Sequence and Series

- A **sequence** is a list of numbers or objects that follow a certain rule or pattern.
- A **series** is the sum of the terms of a sequence.
- Examples of sequences are arithmetic sequences, geometric sequences, Fibonacci sequence, etc.
- Examples of series are arithmetic series, geometric series, harmonic series, etc.
- To find the **nth term** of a sequence, we need to know the general formula or rule that generates the sequence.
- To find the **sum** of a series, we need to know the number of terms and the first and last terms of the series, or use a formula if it exists.
- Some series have a **finite sum**, meaning they converge to a fixed number as the number of terms increases. Others have an **infinite sum**, meaning they diverge to infinity or oscillate as the number of terms increases.
- To test whether a series converges or diverges, we can use various methods such as the **nth term test**, the **ratio test**, the **root test**, the **comparison test**, the **integral test**, etc.
- Some series can be expressed as a **power series**, which is a series of the form $\sum_{n=0}^{\infty} a_n x^n$, where $a_n$ are constants and $x$ is a variable.
- A power series has a **radius of convergence**, which is the interval of values of $x$ for which the series converges. It can be found by using the ratio test or the root test.
- A power series can be used to represent functions such as $\sin x$, $\cos x$, $\exp x$, $\log x$, etc. by using **Taylor series** or **Maclaurin series**. These are power series that are equal to the function and its derivatives at a given point.



### Definition of Sequence and Series with Examples

- A **sequence** is an ordered list of numbers or objects that follow a certain rule or pattern. For example, 1, 3, 5, 7, 9 is a sequence of odd numbers. A sequence can be finite or infinite, depending on how many terms it has.
- A **series** is the sum of the terms of a sequence. For example, 1 + 3 + 5 + 7 + 9 is a series that adds up to 25. A series can be convergent or divergent, depending on whether the sum approaches a finite value or not.
- A sequence can be represented by a general term or a formula that gives the nth term of the sequence. For example, the general term of the sequence 1, 3, 5, 7, 9 is a_n = 2n - 1, where n is the position of the term in the sequence.
- A series can be represented by a partial sum or a formula that gives the sum of the first n terms of the sequence. For example, the partial sum of the series 1 + 3 + 5 + 7 + 9 is S_n = n^2, where n is the number of terms in the series.
- There are different types of sequences and series, such as arithmetic, geometric, harmonic, alternating, etc. Each type has its own rule or formula for finding the general term or the partial sum. For example, an arithmetic sequence is a sequence where each term is obtained by adding a constant to the previous term. An arithmetic series is the sum of an arithmetic sequence. The general term of an arithmetic sequence is a_n = a_1 + (n - 1)d, where a_1 is the first term and d is the common difference. The partial sum of an arithmetic series is S_n = n/2 (2a_1 + (n - 1)d), where n is the number of terms in the series.



### Convergence of series

- A series is an expression of the form $\sum_{n=1}^{\infty} a_n$, where $a_n$ is a sequence of real or complex numbers.
- A series is convergent if the sequence of its partial sums $S_n = \sum_{k=1}^n a_k$ tends to a limit $L$ as $n$ goes to infinity. That is, $\lim_{n \to \infty} S_n = L$.
- A series is divergent if the sequence of its partial sums does not have a finite limit, or does not exist at all.
- The value of the limit $L$, if it exists, is called the sum of the series, and is denoted by $\sum_{n=1}^{\infty} a_n = L$.
- There are various tests and criteria to determine whether a series is convergent or divergent, such as the comparison test, the ratio test, the root test, the integral test, the alternating series test, etc.
- Some examples of convergent and divergent series are:

  - The geometric series $\sum_{n=0}^{\infty} r^n$ is convergent if $|r| < 1$ and divergent otherwise. The sum is $\frac{1}{1-r}$ if $|r| < 1$.
  - The harmonic series $\sum_{n=1}^{\infty} \frac{1}{n}$ is divergent, as the partial sums grow without bound.
  - The alternating harmonic series $\sum_{n=1}^{\infty} (-1)^{n+1} \frac{1}{n}$ is convergent, by the alternating series test. The sum is $\ln 2$.
  - The p-series $\sum_{n=1}^{\infty} \frac{1}{n^p}$ is convergent if $p > 1$ and divergent if $p \leq 1$. The sum is $\zeta(p)$ if $p > 1$, where $\zeta$ is the Riemann zeta function.



### Tests for convergence of series

A series is a sum of infinitely many terms, such as

$$\sum_{n=1}^{\infty} a_n = a_1 + a_2 + a_3 + \cdots$$

where $a_n$ is the n-th term of the series. A series is said to converge if the partial sums

$$S_N = \sum_{n=1}^{N} a_n$$

approach a finite limit as $N$ goes to infinity. Otherwise, the series is said to diverge.

There are various tests that can be used to determine whether a series converges or diverges. Some of the common tests are:

- **The n-th term test**: This test states that if $\lim_{n \to \infty} a_n \neq 0$, then the series $\sum_{n=1}^{\infty} a_n$ diverges. This test can only be used to prove divergence, not convergence.
- **The comparison test**: This test compares a given series with another series that is known to converge or diverge. If the given series is smaller than a convergent series, then it also converges. If the given series is larger than a divergent series, then it also diverges.
- **The geometric test**: This test applies to series of the form $\sum_{n=1}^{\infty} ar^{n-1}$, where $a$ and $r$ are constants. Such series are called geometric series. The test states that a geometric series converges if and only if $|r| < 1$. The sum of a convergent geometric series is $\frac{a}{1-r}$.
- **The ratio test**: This test uses the ratio of consecutive terms of a series to determine its convergence or divergence. The test states that if $\lim_{n \to \infty} \left|\frac{a_{n+1}}{a_n}\right| = L$, then the series $\sum_{n=1}^{\infty} a_n$ converges if $L < 1$, diverges if $L > 1$, and is inconclusive if $L = 1$.
- **The root test**: This test uses the n-th root of the n-th term of a series to determine its convergence or divergence. The test states that if $\lim_{n \to \infty} \sqrt[n]{|a_n|} = L$, then the series $\sum_{n=1}^{\infty} a_n$ converges if $L < 1$, diverges if $L > 1$, and is inconclusive if $L = 1$.

These are some of the tests for convergence of series. There are other tests as well, such as the integral test, the alternating series test, the Leibniz test, the Dirichlet test, and the Cauchy condensation test. Each test has its own advantages and limitations, and some tests may work better than others for certain types of series. It is important to know the conditions and assumptions of each test, and to check the validity of the results.



### Ratio test

- The ratio test is a method for testing the convergence or divergence of an infinite series of the form $\sum_{n=1}^{\infty} a_n$.
- The ratio test is based on the idea that if the terms of a series are getting smaller (or larger) at a certain rate, then the series will converge (or diverge) accordingly.
- The ratio test works by comparing the ratio of two consecutive terms of the series, $\frac{a_{n+1}}{a_n}$, to a limit $L$ as $n$ approaches infinity.
- The ratio test states that:

  - If $L < 1$, then the series $\sum_{n=1}^{\infty} a_n$ converges absolutely.
  - If $L > 1$, then the series $\sum_{n=1}^{\infty} a_n$ diverges.
  - If $L = 1$, then the ratio test is inconclusive and the series may converge or diverge.

- The ratio test is useful for testing the convergence of series that involve factorials, exponentials, or powers of $n$.
- The ratio test can also be applied to series of complex numbers, by using the modulus of the ratio instead of the ratio itself.



### D’ Alembert’s test for convergence of series

- D’ Alembert’s test, also known as the ratio test, is a criterion for the convergence of a series of real or complex numbers, where each term is nonzero when n is large .
- The test was first published by Jean le Rond d'Alembert in 1768.
- The test is based on the limit of the ratio of consecutive terms of the series .
- The test states that:

  - Let $\sum_{n=1}^{\infty} a_n$ be a series of real or complex numbers. Let the sequence $a_n$ satisfy: $$\lim_{n \to \infty} \frac{a_{n+1}}{a_n} = l$$
  - If $l > 1$, then the series diverges.
  - If $l < 1$, then the series converges absolutely.
  - If $l = 1$, then the test is inconclusive and the series may converge or diverge.

- The test can be applied to any series of the form $\sum_{n=1}^{\infty} a_n$, where $a_n$ is nonzero for large n, and the limit of the ratio exists or is infinite.
- The test can be used to determine the radius of convergence of a power series.
- The test can be extended to series of functions, where the limit of the ratio is taken uniformly on a set.
- The test can be derived from the comparison test, by comparing the series with a geometric series.



### Raabe's test

- Raabe's test is a test for the convergence of a series of the form $\sum_{n=1}^{\infty} a_n$ where each term is a real or complex number and $a_n \neq 0$ for large $n$ .
- Raabe's test is based on the ratio test, which compares the ratio of consecutive terms of the series to a limit $L$.
- Raabe's test introduces a correction factor $n$ to the ratio test and defines a new limit $R$ as follows:

$$
R = \lim_{n \to \infty} n \left( \frac{a_n}{a_{n+1}} - 1 \right)
$$

- Raabe's test states that:

  - If $R > 1$, the series converges absolutely.
  - If $R < 1$, the series diverges.
  - If $R = 1$, the test is inconclusive and another test is needed.

- Raabe's test is also known as Raabe-Duhamel's test or Raabe's criterion.
- Raabe's test was developed by Swiss mathematician Joseph Ludwig Raabe in 1832.



### Comparison test for the notes of the Unit 3 - Sequence and Series in the subject of ENGINEERING MATHEMATICS-II

- The comparison test for series is a method to determine the convergence or divergence of a series by comparing it to another series with known convergence properties .
- The comparison test can be applied to series with non-negative terms only .
- There are two types of comparison tests: direct comparison test and limit comparison test   .
- The direct comparison test states that:
  - If the infinite series $\sum_{n=1}^{\infty}a_n$ converges and $0 \leq a_n \leq b_n$ for all sufficiently large $n$, then the infinite series $\sum_{n=1}^{\infty}b_n$ also converges .
  - If the infinite series $\sum_{n=1}^{\infty}a_n$ diverges and $0 \leq b_n \leq a_n$ for all sufficiently large $n$, then the infinite series $\sum_{n=1}^{\infty}b_n$ also diverges .
- The limit comparison test states that:
  - If the infinite series $\sum_{n=1}^{\infty}a_n$ and $\sum_{n=1}^{\infty}b_n$ have positive terms and $\lim_{n \to \infty}\frac{a_n}{b_n} = c$, where $c$ is a positive finite number, then the two series either both converge or both diverge  .
- The comparison test is useful when the series involves complicated functions that are hard to integrate or differentiate, such as rational functions, logarithmic functions, exponential functions, etc  .
- The comparison test often requires finding a suitable series to compare with, such as geometric series, p-series, harmonic series, etc .
- The comparison test can be used to prove the convergence or divergence of a series, but it cannot be used to find the exact value of the sum of a series  .



### Fourier Series

- A Fourier series is an expansion of a periodic function f(x) in terms of an infinite sum of sines and cosines  .
- Fourier series make use of the orthogonality relationships of the sine and cosine functions  .
- Fourier series can be used to represent periodic functions as a linear combination of sine and cosine functions  .
- Fourier series are analogous to Taylor series, which represent functions as possibly infinite sums of monomial terms.
- Fourier series are very powerful tools in connection with various problems involving partial differential equations .
- Fourier series have many applications in physics, engineering, signal processing, image processing, etc .

#### Formula of Fourier Series

- The general form of a Fourier series is:

formula

where omega is the angular frequency, a0 is the constant term, and an and bn are the coefficients of the cosine and sine terms, respectively    .

- The coefficients can be calculated using the following formulas:

a0

an

bn

where T is the period of the function    .

#### Examples of Fourier Series

- Example 1: Find the Fourier series of the function f(x) = x, defined on the interval [-pi, pi] and extended periodically.

- Solution: The period of the function is 2pi, so omega = 1. The coefficients are:




### Half range Fourier sine and cosine series

- A half range Fourier series is a Fourier series that is defined over half the range of the original function, instead of the full range.
- A half range Fourier series can be either a sine series or a cosine series, depending on the symmetry of the function.
- A sine series is a Fourier series that contains only sine terms, and it is used to represent odd functions, which satisfy f(-x) = -f(x) for all x.
- A cosine series is a Fourier series that contains only cosine terms, and it is used to represent even functions, which satisfy f(-x) = f(x) for all x.
- To obtain a half range Fourier series, the original function is extended periodically to the full range, either by taking the odd or even extension of the function, and then applying the standard Fourier series formulae.
- The general formulae for the half range Fourier series are:

  - For the sine series:

    f(x) = sum_{n=1}^{infty} b_n sin(n pi x / L)

    where b_n = (2/L) int_{0}^{L} f(x) sin(n pi x / L) dx

  - For the cosine series:

    f(x) = a_0 / 2 + sum_{n=1}^{infty} a_n cos(n pi x / L)

    where a_0 = (2/L) int_{0}^{L} f(x) dx

    and a_n = (2/L) int_{0}^{L} f(x) cos(n pi x / L) dx

- The half range Fourier series can be used to approximate any function over a finite interval, as long as the function is integrable and satisfies the Dirichlet conditions.



## Unit 4 - Complex Variable–Differentiation

- A complex variable is a variable that can take on values in the complex plane, i.e., numbers of the form $z = x + iy$, where $x$ and $y$ are real numbers and $i$ is the imaginary unit such that $i^2 = -1$.
- A complex function is a function that maps complex numbers to complex numbers, i.e., $f: \mathbb{C} \to \mathbb{C}$, such that $f(z) = u(x,y) + iv(x,y)$, where $u$ and $v$ are real-valued functions of two real variables.
- A complex function is said to be differentiable at a point $z_0$ if the limit $$f'(z_0) = \lim_{\Delta z \to 0} \frac{f(z_0 + \Delta z) - f(z_0)}{\Delta z}$$ exists and is independent of the direction of approach of $\Delta z$ to zero.
- A complex function is said to be analytic at a point $z_0$ if it is differentiable at $z_0$ and in some neighborhood of $z_0$. A function that is analytic in the whole complex plane is called entire.
- The Cauchy-Riemann equations are necessary conditions for a complex function to be differentiable at a point. They state that if $f(z) = u(x,y) + iv(x,y)$, then $$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y} \quad \text{and} \quad \frac{\partial u}{\partial y} = - \frac{\partial v}{\partial x}$$ at the point of differentiation.
- The Cauchy-Riemann equations can also be written in polar form as $$\frac{\partial u}{\partial r} = \frac{1}{r} \frac{\partial v}{\partial \theta} \quad \text{and} \quad \frac{\partial v}{\partial r} = - \frac{1}{r} \frac{\partial u}{\partial \theta}$$ where $z = re^{i\theta}$ and $f(z) = u(r,\theta) + iv(r,\theta)$.
- The Cauchy-Riemann equations are not sufficient conditions for a complex function to be differentiable at a point. The function also needs to satisfy the continuity of the partial derivatives of $u$ and $v$ at the point.
- The derivative of a complex function can be interpreted geometrically as the ratio of the infinitesimal change in the function value to the infinitesimal change in the argument, i.e., $$f'(z) = \frac{df}{dz} = \frac{\Delta f}{\Delta z}$$ as $\Delta z \to 0$. This means that the derivative gives the rate of change and the direction of change of the function at a point.
- The derivative of a complex function can also be interpreted as a linear transformation that maps a small neighborhood of the point to a small neighborhood of the function value, i.e., $$f(z + \Delta z) \approx f(z) + f'(z) \Delta z$$ for small $\Delta z$. This means that the derivative gives the magnification and the rotation of the function at a point.



### Functions of complex variable

- A complex function is a function that maps complex numbers to complex numbers.
- A complex function can be written as w(z) = u(x, y) + iv(x, y), where z = x + iy is the complex variable, w = u + iv is the complex value, and u and v are real functions of x and y.
- A complex function is said to be differentiable at a point z0 if the limit

$$\lim_{z \to z_0} \frac{w(z) - w(z_0)}{z - z_0}$$

exists and is finite. This limit is called the derivative of w(z) at z0 and is denoted by w'(z0).
- A complex function is said to be analytic or holomorphic at a point z0 if it is differentiable at z0 and at every point in some neighborhood of z0.
- A complex function is said to be entire if it is analytic at every point in the complex plane.
- A complex function is said to be harmonic if its real and imaginary parts satisfy Laplace's equation, i.e.,

$$\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0$$

and

$$\frac{\partial^2 v}{\partial x^2} + \frac{\partial^2 v}{\partial y^2} = 0$$

- A complex function that is analytic in a domain D satisfies the Cauchy-Riemann equations, i.e.,

$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}$$

and

$$\frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$$

- The Cauchy-Riemann equations are necessary but not sufficient conditions for a complex function to be analytic. A sufficient condition is that the partial derivatives of u and v are continuous and satisfy the Cauchy-Riemann equations.
- A complex function that is analytic in a domain D has a power series expansion at any point z0 in D, i.e.,

$$w(z) = \sum_{n=0}^{\infty} a_n (z - z_0)^n$$

where the coefficients an are given by

$$a_n = \frac{w^{(n)}(z_0)}{n!}$$

- A complex function that is analytic in a domain D has an antiderivative or primitive in D, i.e., there exists a function F(z) such that F'(z) = w(z) for all z in D.



### Limit for the notes of the Unit 4 - Complex Variable–Differentiation in the subject of ENGINEERING MATHEMATICS-II

- Complex variable–differentiation is the study of functions of a complex variable and their derivatives.
- A complex variable is a variable that can take values in the complex numbers, which are numbers of the form $z = x + iy$, where $x$ and $y$ are real numbers and $i$ is the imaginary unit such that $i^2 = -1$.
- The complex numbers can be represented geometrically as points in the complex plane, where the horizontal axis is the real axis and the vertical axis is the imaginary axis.
- A function of a complex variable is a rule that assigns a complex number to each complex number in its domain, which is a subset of the complex plane. For example, $f(z) = z^2$ is a function of a complex variable that maps each complex number $z$ to its square $z^2$.
- The derivative of a function of a complex variable is a measure of how fast the function changes with respect to a small change in the input variable. The derivative of $f(z)$ at a point $z_0$ in its domain is denoted by $f'(z_0)$ and defined by the limit
$$f'(z_0) = \lim_{\Delta z \to 0} \frac{f(z_0 + \Delta z) - f(z_0)}{\Delta z}$$
where $\Delta z$ is a complex number that approaches zero.
- The derivative of a function of a complex variable has the following properties:
  - Linearity: If $f(z)$ and $g(z)$ are differentiable functions and $c$ is a constant, then $(cf + g)'(z) = cf'(z) + g'(z)$.
  - Product rule: If $f(z)$ and $g(z)$ are differentiable functions, then $(fg)'(z) = f'(z)g(z) + f(z)g'(z)$.
  - Quotient rule: If $f(z)$ and $g(z)$ are differentiable functions and $g(z) \neq 0$, then $(f/g)'(z) = \frac{f'(z)g(z) - f(z)g'(z)}{g(z)^2}$.
  - Chain rule: If $f(z)$ and $g(z)$ are differentiable functions, then $(f \circ g)'(z) = f'(g(z))g'(z)$, where $f \circ g$ denotes the composition of $f$ and $g$.
  - Power rule: If $f(z) = z^n$, where $n$ is a constant, then $f'(z) = nz^{n-1}$.
  - Exponential rule: If $f(z) = e^z$, then $f'(z) = e^z$.
  - Logarithmic rule: If $f(z) = \log z$, where $\log z$ is the principal branch of the complex logarithm, then $f'(z) = \frac{1}{z}$.
  - Trigonometric rules: If $f(z) = \sin z$, then $f'(z) = \cos z$. If $f(z) = \cos z$, then $f'(z) = -\sin z$. If $f(z) = \tan z$, then $f'(z) = \frac{1}{\cos^2 z}$.
  - Hyperbolic rules: If $f(z) = \sinh z$, then $f'(z) = \cosh z$. If $f(z) = \cosh z$, then $f'(z) = \sinh z$. If $f(z) = \tanh z$, then $f'(z) = \frac{1}{\cosh^2 z}$.
- A function of a complex variable is said to be analytic or holomorphic at a point $z_0$ in its domain if it has a derivative at $z_0$ and at every point in some neighborhood of $z_0$. A function is said to be analytic or holomorphic in a domain if it is analytic at every point in that domain.
- A remarkable feature of complex differentiation is that the existence of one complex derivative automatically implies the existence of infinitely many. This is in contrast to the case of the function of real variable $g(x



### Continuity and Differentiability of Complex Functions

- A complex function is a function that maps complex numbers to complex numbers, such as f(z) = z^2 + 1.
- A complex function is continuous at a point z_0 if the limit of the function as z approaches z_0 is equal to the value of the function at z_0, i.e., lim_(z->z_0) f(z) = f(z_0) .
- A complex function is differentiable at a point z_0 if the limit of the difference quotient as h approaches zero exists and is finite, i.e., lim_(h->0) (f(z_0 + h) - f(z_0))/h = f'(z_0) .
- The derivative of a complex function is also a complex function that gives the rate of change of the function at each point in its domain.
- A complex function that is differentiable at every point in its domain is called an analytic function or a holomorphic function .
- A complex function that is differentiable at a point z_0 is also continuous at that point, but the converse is not true. There are continuous complex functions that are not differentiable at some or all points in their domain .
- Some examples of complex functions and their continuity and differentiability are:

  - f(z) = z is continuous and differentiable at every point in the complex plane, and f'(z) = 1 .
  - f(z) = |z| is continuous at every point in the complex plane, but not differentiable at any point, because the difference quotient does not have a unique limit as h approaches zero from different directions .
  - f(z) = e^z is continuous and differentiable at every point in the complex plane, and f'(z) = e^z .
  - f(z) = log(z) is continuous and differentiable at every point in the complex plane except the origin and the negative real axis, where it has a branch cut. The derivative is f'(z) = 1/z .
  - f(z) = sin(z) is continuous and differentiable at every point in the complex plane, and f'(z) = cos(z) .



### Analytic functions

- A function of a complex variable $z = x + iy$ is called **analytic** in a region $R$ of the complex plane if it has a derivative at each point of $R$ and if it is single valued.
- An analytic function is also called **holomorphic** or **complex differentiable**.
- An analytic function can be represented by a **power series** in the variable $z$ in a neighborhood of any point in its domain.
- An analytic function satisfies the **Cauchy-Riemann equations**, which relate the partial derivatives of its real and imaginary parts.
- An analytic function has many remarkable properties, such as:
  - It is **infinitely differentiable** and has **Taylor series** and **Laurent series** expansions.
  - It is **conformal**, which means it preserves angles and shapes locally.
  - It satisfies the **maximum modulus principle**, which states that the modulus of an analytic function cannot have a local maximum in its domain.
  - It satisfies the **Cauchy integral formula** and the **Cauchy integral theorem**, which relate the values of an analytic function inside and on the boundary of a closed contour.
  - It has a **residue** at each isolated singularity, which is a complex number that captures the behavior of the function near the singularity.
  - It has a **Liouville's theorem**, which states that a bounded entire function (analytic in the whole complex plane) must be constant.
- The study of analytic functions is called **complex analysis**, which is a branch of mathematical analysis that investigates functions of complex numbers.
- Complex analysis has applications in many branches of mathematics, such as algebraic geometry, number theory, analytic combinatorics, applied mathematics, as well as in physics, such as hydrodynamics, thermodynamics, and quantum mechanics.
- There is also a generalization of analytic functions to more than one complex variable, which is called **function of several complex variables**. However, the theory of functions of several complex variables is much more complicated and less understood than the theory of functions of one complex variable.



### Cauchy-Riemann equations (Cartesian and Polar form)

- The Cauchy-Riemann equations are a system of two partial differential equations that form a necessary and sufficient condition for a complex function to be holomorphic (complex differentiable) .
- If f(z) = u(x, y) + iv(x, y) is a complex function of a single complex variable z = x + iy, where u and v are real-valued functions of two real variables x and y, then the Cauchy-Riemann equations are:

  - (1a) `@u/@x = @v/@y`
  - (1b) `@u/@y = -@v/@x`

- These equations state that the partial derivatives of u and v must be continuous and satisfy the above equalities at every point in the domain of f .
- If f is holomorphic, then it has a complex derivative given by:

  - (2) `f'(z) = @u/@x + i@v/@x = @v/@y - i@u/@y`

- This derivative is independent of the direction of approach to z, as long as the limit exists .
- The Cauchy-Riemann equations can also be written in polar form, using the transformation:

  - (3) `x = r cos(theta), y = r sin(theta), z = re^(i theta)`

- where r and theta are the polar coordinates of z. Then, if f(z) = u(r, theta) + iv(r, theta), the Cauchy-Riemann equations in polar form are:

  - (4a) `@u/@r = (1/r) @v/@theta`
  - (4b) `@v/@r = -(1/r) @u/@theta`

- These equations state that the partial derivatives of u and v with respect to r and theta must be continuous and satisfy the above equalities at every point in the domain of f .
- If f is holomorphic, then it has a complex derivative given by:

  - (5) `f'(z) = e^(-i theta) (@u/@r + i@v/@r) = (1/r) e^(-i theta) (@v/@theta - i@u/@theta)`

- This derivative is independent of the direction of approach to z, as long as the limit exists .
- The Cauchy-Riemann equations are useful for checking if a complex function is holomorphic, and for computing its complex derivative. They also imply some important properties of holomorphic functions, such as the harmonic nature of u and v, and the conformal mapping of f .

: https://en.wikipedia.org/wiki/Cauchy%E2%80%93Riemann_equations
: https://math.libretexts.org/Bookshelves/Analysis/Complex_Variables_with_Applications_(Orloff)/02%3A_Analytic_Functions/2.06%3A_Cauchy-Riemann_Equations
: https://sites.math.washington.edu/~hart/m427/Lecture10.pdf



### Harmonic function for the notes of the Unit 4 - Complex Variable–Differentiation in the subject of ENGINEERING MATHEMATICS-II

- A harmonic function is a function that satisfies Laplace's equation, which is a partial differential equation of the form: ∇^2 u = u_xx + u_yy = 0, where u is a function of x and y .
- Harmonic functions are important in complex analysis, because they are related to holomorphic functions, which are functions that are complex differentiable everywhere in a domain.
- A holomorphic function can be written as f(z) = u(x,y) + iv(x,y), where z = x + iy is a complex variable, and u and v are real functions of x and y .
- The real part u and the imaginary part v of a holomorphic function are both harmonic functions in the same domain .
- Conversely, if u is a harmonic function in a connected domain, then there exists a holomorphic function f such that u is the real part of f.
- This means that harmonic functions can be obtained by taking the real or imaginary part of a holomorphic function, and holomorphic functions can be constructed by finding a harmonic conjugate of a harmonic function .
- A harmonic conjugate of a harmonic function u is a function v such that u + iv is holomorphic. It can be found by solving the Cauchy-Riemann equations, which are: u_x = v_y and u_y = -v_x .
- Some examples of harmonic functions are: u(x,y) = x, u(x,y) = y, u(x,y) = e^x cos y, u(x,y) = ln(x^2 + y^2), etc .
- Some properties of harmonic functions are: they are infinitely differentiable, they satisfy the mean value property, they have the maximum principle, they are conformal, etc  .
- The mean value property states that the value of a harmonic function at a point is equal to the average value of the function on a circle centered at that point .
- The maximum principle states that a harmonic function cannot have a local maximum or minimum in the interior of its domain, unless it is constant .
- Conformal means that a harmonic function preserves the angles between curves at every point in its domain .
- Harmonic functions have applications in physics and engineering, such as heat conduction, electrostatics, fluid dynamics, potential theory, etc .



### Method to find Analytic functions for the notes of the Unit 4 - Complex Variable–Differentiation in the subject of ENGINEERING MATHEMATICS-II

- A function of a complex variable is said to be **analytic** in a region of the complex plane if it has a derivative at each point of the region and if it is single valued.
- A function of a complex variable is also called **holomorphic** or **complex analytic** if it is analytic in the whole complex plane or in an open subset of it .
- A function of a complex variable is analytic if and only if it satisfies the **Cauchy-Riemann equations** in the region of analyticity .
- The Cauchy-Riemann equations are a pair of partial differential equations that relate the real and imaginary parts of a complex function. If $f(z) = u(x,y) + iv(x,y)$, where $z = x + iy$ and $u$ and $v$ are real functions, then the Cauchy-Riemann equations are:

$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}$$

$$\frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$$

- A function of a complex variable is analytic if and only if it is **conformal**, meaning that it preserves the angles between curves at each point of the region of analyticity .
- A function of a complex variable is analytic if and only if it has a **power series expansion** in a neighborhood of each point of the region of analyticity .
- A power series expansion of a complex function is a series of the form:

$$f(z) = \sum_{n=0}^{\infty} a_n (z - z_0)^n$$

where $a_n$ are complex coefficients and $z_0$ is a fixed point in the region of analyticity.

- A function of a complex variable is analytic if and only if it satisfies the **Cauchy integral formula**, which relates the value of the function at a point to the values of the function on a closed contour around the point .
- The Cauchy integral formula is:

$$f(z_0) = \frac{1}{2\pi i} \oint_C \frac{f(z)}{z - z_0} dz$$

where $C$ is a simple closed curve that encloses $z_0$ and is oriented counterclockwise, and $f(z)$ is analytic inside and on $C$.

- A function of a complex variable is analytic if and only if it satisfies the **Morera's theorem**, which states that if the integral of the function along any closed curve in a region is zero, then the function is analytic in that region .
- The Morera's theorem is:

$$\oint_C f(z) dz = 0 \implies f(z) \text{ is analytic in } R$$

where $C$ is any simple closed curve in a region $R$ and $f(z)$ is continuous in $R$.



### Milne’s Thompson Method for the notes of the Unit 4 - Complex Variable–Differentiation in the subject of ENGINEERING MATHEMATICS-II

- Milne's Thompson method is a technique to find an analytic function $f(z) = u(x,y) + iv(x,y)$ in a region $R$ of the complex plane, if either the real part $u(x,y)$ or the imaginary part $v(x,y)$ is known as an analytic expression in terms of $x$ and $y$ .
- The method is based on the Cauchy-Riemann equations, which relate the partial derivatives of $u$ and $v$ as follows:
$$
\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \quad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}
$$
- The method consists of three steps:
  - Step 1: Find the harmonic conjugate of the given function, i.e., the function that satisfies the Cauchy-Riemann equations with the given function. For example, if $u(x,y)$ is given, find $v(x,y)$ such that $u$ and $v$ are harmonic conjugates.
  - Step 2: Express $u$ and $v$ in terms of $z$ and $\bar{z}$, where $z = x + iy$ and $\bar{z} = x - iy$. This can be done by using the identities:
  $$
  x = \frac{z + \bar{z}}{2}, \quad y = \frac{z - \bar{z}}{2i}, \quad \frac{\partial}{\partial x} = \frac{1}{2}\left(\frac{\partial}{\partial z} + \frac{\partial}{\partial \bar{z}}\right), \quad \frac{\partial}{\partial y} = \frac{1}{2i}\left(\frac{\partial}{\partial z} - \frac{\partial}{\partial \bar{z}}\right)
  $$
  - Step 3: Eliminate $\bar{z}$ from the expressions of $u$ and $v$ by using the fact that $f(z)$ is analytic in $R$, which implies that $\frac{\partial f}{\partial \bar{z}} = 0$ in $R$. This gives $f(z) = u(z,\bar{z}) + iv(z,\bar{z})$ as a function of $z$ only.
- The method can be applied to different cases depending on the form of the given function:
  - Case I: The given function is a polynomial in $x$ and $y$. In this case, the harmonic conjugate can be found by integrating the Cauchy-Riemann equations and using the fact that the constant of integration must be a polynomial of the same degree as the given function.
  - Case II: The given function is a product of a polynomial and an exponential function in $x$ and $y$. In this case, the harmonic conjugate can be found by using the method of undetermined coefficients, i.e., assuming that the harmonic conjugate has the same form as the given function and solving for the coefficients by equating the partial derivatives.
  - Case III: The given function is a function of $x^2 + y^2$ and $x^2 - y^2$. In this case, the harmonic conjugate can be found by using the method of substitution, i.e., letting $r^2 = x^2 + y^2$ and $s^2 = x^2 - y^2$ and solving for the harmonic conjugate in terms of $r$ and $s$ by integrating the Cauchy-Riemann equations. Then, the expressions of $u$ and $v$ in terms of $z$ and $\bar{z}$ can be obtained by using the identities:
  $$
  r^2 = \frac{z\bar{z}}{2}, \quad s^2 = \frac{z^2 + \bar{z}^2}{4}, \quad \frac{\partial}{\partial r} = \frac{z}{2r}\frac{\partial}{\partial z} + \frac{\bar{z}}{2r}\frac{\partial}{\partial \bar{z}},



### Conformal mapping

- A conformal mapping is a function defined on the complex plane that transforms a given curve or region, preserving the angles between any two curves that cross each other .
- A conformal mapping is also called a conformal transformation or an angle-preserving transformation.
- A conformal mapping is differentiable and has a nonzero derivative at every point in its domain .
- A conformal mapping is not necessarily one-to-one or onto, unless it is a biholomorphic function, which is a conformal mapping that has an inverse that is also conformal.
- A conformal mapping can be used to map complex functions or harmonic functions from one region to another, or to map the surface of a sphere or the earth to a plane .

#### Examples of conformal mappings

- The simplest example of a conformal mapping is a similarity transformation, which is a linear function of the form \(f(z) = az + b\), where \(a\) and \(b\) are complex constants and \(a \neq 0\). A similarity transformation maps circles to circles and preserves the size of angles.
- Another example of a conformal mapping is the exponential function \(f(z) = e^z\), which maps the horizontal strip \(\{z : -\pi < \Im(z) < \pi\}\) to the punctured plane \(\{w : w \neq 0\}\). The exponential function maps horizontal lines to circles and vertical lines to rays.
- A third example of a conformal mapping is the Joukowsky transformation \(f(z) = z + 1/z\), which maps the exterior of the unit circle \(\{z : |z| > 1\}\) to the complex plane with a slit along the negative real axis \(\{w : w \notin (-\infty, -2]\}\). The Joukowsky transformation maps circles that pass through the origin to airfoils, which are shapes that generate lift in aerodynamics.



### Mobius transformation and their properties

- A Mobius transformation is a function of the form `f(z) = (az + b) / (cz + d)` where `a, b, c, d` are complex numbers and `ad - bc ≠ 0`.
- A Mobius transformation maps the extended complex plane `C ∪ {∞}` to itself. It is also called a fractional linear transformation or a linear fractional transformation.
- A Mobius transformation is a composition of four elementary maps, namely translations, dilations, rotations, and inversions.
  - Translations: `z → z + z0` such that `z0 ∈ C`
  - Dilations: `z → λz` where `λ > 0` and `λ ∈ R`
  - Rotations: `z → eiθz` where `θ ∈ R`
  - Inversions: `z → 1/z`
- A Mobius transformation is completely determined by any three input-output pairs. This means that for any triple of distinct input values `z1, z2, z3` in `C ∪ {∞}` and any triple of distinct output values `w1, w2, w3` in `C ∪ {∞}`, there is a unique `T ∈ M` such that `Tzi = wi` for `i = 1, 2, 3`.
- A Mobius transformation is conformal, meaning that it preserves angles and orientation locally.
- A Mobius transformation maps circles and lines to circles and lines. More precisely, it maps generalized circles (circles or lines) to generalized circles.
- The Mobius transformations form a group called the Mobius group, which is the projective linear group `PGL(2,C)`. It has a subgroup called the special Mobius group, which is the special linear group `SL(2,C)`. These groups have numerous applications in mathematics and physics, such as group theory, hyperbolic geometry, and relativity.



## Unit 5 - Complex Variable –Integration

- Complex integration is the process of finding the value of a complex function along a curve or a contour in the complex plane.
- The basic theorem of complex integration is the Cauchy-Goursat theorem, which states that if a function is analytic in a simply connected domain, then the integral of the function along any closed contour in that domain is zero.
- The Cauchy-Goursat theorem can be extended to multiply connected domains using the concept of winding numbers, which measure how many times a contour winds around a point in the complex plane.
- The Cauchy integral formula is a powerful result that relates the value of a function at a point to the integral of the function along a circle around that point. It also gives a formula for the derivatives of an analytic function in terms of the function itself.
- The residue theorem is another important tool for complex integration, which allows us to evaluate integrals along closed contours by finding the residues of the function at its singularities. A residue is the coefficient of the term with power -1 in the Laurent series expansion of the function around a singularity.
- The residue theorem can be used to compute real integrals that involve trigonometric, exponential, or rational functions, by converting them to complex integrals and applying the theorem.
- The residue theorem can also be used to find the number of zeros and poles of a function inside a contour, by using the argument principle or Rouche's theorem. These theorems relate the change in the argument of the function along the contour to the difference between the number of zeros and poles inside the contour.



### Complex integration for the notes of the Unit 5 - Complex Variable –Integration in the subject of ENGINEERING MATHEMATICS-II

- Complex integration is an intuitive extension of real integration. It involves integrating a complex-valued function along a path in the complex plane.
- A complex-valued function of a real variable, such as $f(t) = u(t) + iv(t)$, can be integrated as a vector function, by integrating its real and imaginary parts separately.
- A complex-valued function of a complex variable, such as $f(z) = u(x,y) + iv(x,y)$, where $z = x + iy$, can be integrated along a curve $C$ in the complex plane, by using the parametric representation of the curve and the chain rule.
- The complex integral of $f(z)$ along $C$ is denoted by $\int_C f(z) dz$, and it is defined as the limit of the Riemann sums of $f(z)$ over the subintervals of $C$.
- The complex integral of $f(z)$ along $C$ depends on the path $C$, not just the endpoints of $C$. However, if $f(z)$ is analytic in a simply connected domain $D$, then the complex integral of $f(z)$ along any closed curve in $D$ is zero.
- The Cauchy integral theorem states that if $f(z)$ is analytic in a simply connected domain $D$, and $C$ is a simple closed curve in $D$, then the complex integral of $f(z)$ along $C$ is zero.
- The Cauchy integral formula states that if $f(z)$ is analytic in a simply connected domain $D$, and $C$ is a simple closed curve in $D$ that encloses a point $z_0$, then $f(z_0) = \frac{1}{2\pi i} \int_C \frac{f(z)}{z-z_0} dz$.
- The Cauchy integral formula can be used to find the derivatives of analytic functions, as well as to evaluate complex integrals that involve rational functions or trigonometric functions.
- The residue theorem states that if $f(z)$ is analytic in a simply connected domain $D$, except for a finite number of isolated singularities, and $C$ is a simple closed curve in $D$ that encloses all the singularities, then $\int_C f(z) dz = 2\pi i \sum_{k=1}^n Res(f, z_k)$, where $Res(f, z_k)$ is the residue of $f(z)$ at the singularity $z_k$.
- The residue theorem can be used to evaluate complex integrals that involve functions with poles, branch points, or essential singularities.
- The principal value of a complex integral is defined as the limit of the integral over a symmetric interval around the singularity, as the interval shrinks to zero.
- The principal value of a complex integral can be used to deal with integrals that have singularities on the real axis.



### Cauchy- Integral theorem

- The Cauchy- Integral theorem is a statement about line integrals for holomorphic functions in the complex plane.
- A holomorphic function is a complex-valued function that is differentiable at every point in its domain.
- The Cauchy- Integral theorem states that if a function f(z) is holomorphic in a simply connected domain D, then the line integral of f(z) along any closed curve C in D is zero.
- A simply connected domain is a region that has no holes or gaps in it.
- A closed curve is a path that starts and ends at the same point.
- The line integral of f(z) along C is defined as the sum of f(z) times the infinitesimal change in z along C.
- Mathematically, the Cauchy- Integral theorem can be written as:

$$\oint_C f(z) dz = 0$$

- The Cauchy- Integral theorem can be derived from Stokes' theorem, which relates the line integral of a vector field to the flux of its curl through a surface.
- The Cauchy- Integral theorem can be generalized to a multiply connected domain, which is a region that has one or more holes or gaps in it.
- The generalized Cauchy- Integral theorem states that if a function f(z) is holomorphic in a multiply connected domain D, then the line integral of f(z) along any closed curve C in D is equal to the sum of the line integrals of f(z) along the boundaries of the holes or gaps in D.
- Mathematically, the generalized Cauchy- Integral theorem can be written as:

$$\oint_C f(z) dz = \sum_{k=1}^n \oint_{C_k} f(z) dz$$

- where C_k are the closed curves around the holes or gaps in D, oriented in the opposite direction of C.
- The Cauchy- Integral theorem is a powerful tool in complex analysis, as it implies many important properties and formulas for holomorphic functions, such as the Cauchy- Integral formula, the Morera's theorem, the Liouville's theorem, the maximum modulus principle, and the residue theorem  .



### Cauchy integral formula

- The Cauchy integral formula is a fundamental result in complex analysis that relates the values of a holomorphic function inside a disk to the values of that function on the boundary of the disk  .
- The formula can be stated as follows: if f(z) is a holomorphic function on a simply-connected domain U, and γ is a positively oriented simple closed contour in U that encloses a point z_0, then

f(z_0) = \frac{1}{2\pi i} \oint_\gamma \frac{f(z)}{z-z_0} dz

- The formula can be generalized to higher-order derivatives of f(z), as follows :

f^{(n)}(z_0) = \frac{n!}{2\pi i} \oint_\gamma \frac{f(z)}{(z-z_0)^{n+1}} dz

- The Cauchy integral formula has many important consequences, such as the identity theorem, the maximum modulus principle, the Liouville theorem, and the residue theorem .



### Taylor’s and Laurent’s series

- A **power series** is a series of the form

$$\sum_{n=0}^{\infty} a_n (z-z_0)^n$$

where $a_n$ and $z_0$ are complex constants and $z$ is a complex variable.

- A power series with non-negative power terms is called a **Taylor series**. A Taylor series represents a function $f(z)$ that is analytic in a disk around $z_0$ as

$$f(z) = \sum_{n=0}^{\infty} \frac{f^{(n)}(z_0)}{n!} (z-z_0)^n$$

where $f^{(n)}(z_0)$ denotes the $n$-th derivative of $f(z)$ at $z_0$.

- A power series with both positive and negative power terms is called a **Laurent series**. A Laurent series represents a function $f(z)$ that is analytic in an annulus around $z_0$ as

$$f(z) = \sum_{n=-\infty}^{\infty} a_n (z-z_0)^n$$

where $a_n$ are complex coefficients given by

$$a_n = \frac{1}{2\pi i} \int_C \frac{f(z)}{(z-z_0)^{n+1}} dz$$

where $C$ is a simple closed contour in the annulus that encloses $z_0$.

- A Laurent series can be used to express complex functions in cases where a Taylor series expansion cannot be applied, such as when the function has a singularity at $z_0$.

- A Laurent series can be divided into two parts: the **principal part**, which contains the negative power terms, and the **analytic part**, which contains the non-negative power terms. The principal part can be written as

$$\sum_{n=1}^{\infty} a_{-n} (z-z_0)^{-n}$$

and the analytic part can be written as

$$\sum_{n=0}^{\infty} a_n (z-z_0)^n$$

- The principal part of a Laurent series is also called the **residue series**, because the coefficient $a_{-1}$ is equal to the **residue** of $f(z)$ at $z_0$, denoted by $\text{Res}(f,z_0)$. The residue is a useful quantity for evaluating complex integrals using the **residue theorem**.



### Singularities and its classification for the notes of the Unit 5 - Complex Variable –Integration in the subject of ENGINEERING MATHEMATICS-II

- A singularity is a point in the domain of a complex function where the function fails to be analytic.
- A function is analytic if it is complex differentiable in an open set containing the point.
- Complex differentiable means that the function satisfies the Cauchy-Riemann equations and has a well-defined derivative.
- There are different types of singularities depending on the behavior of the function near the point  .
- The main types of singularities are:

  - Isolated singularities: These are points where the function is analytic in a punctured disk around the point, i.e., there is a positive radius r such that the function is analytic in {z: 0 < |z - z0| < r}.
  - Nonisolated singularities: These are points where the function is not analytic in any punctured disk around the point, i.e., there is no positive radius r such that the function is analytic in {z: 0 < |z - z0| < r}.
  - Branch points: These are points where the function is multivalued and has different branches defined by different cuts in the complex plane.

- Isolated singularities can be further classified into:

  - Removable singularities: These are points where the function has a finite limit as z approaches z0, i.e., lim(z->z0) f(z) exists and is finite .
  - Poles: These are points where the function has an infinite limit as z approaches z0, i.e., lim(z->z0) f(z) = infinity or lim(z->z0) 1/f(z) = 0 .
  - Essential singularities: These are points where the function has no limit as z approaches z0, i.e., lim(z->z0) f(z) does not exist or lim(z->z0) 1/f(z) does not exist .

- The order of a pole is the smallest positive integer n such that lim(z->z0) (z - z0)^n f(z) is finite and nonzero .
- A pole of order 1 is also called a simple pole .
- The residue of a function at a pole is the coefficient of the term (z - z0)^-1 in the Laurent series expansion of the function around the pole .
- The Laurent series of a function is a generalization of the Taylor series that allows negative powers of (z - z0) in the expansion .
- The principal part of a function at a singularity is the sum of the terms with negative powers of (z - z0) in the Laurent series expansion of the function around the singularity .
- The coefficient of the term (z - z0)^-1 in the principal part is also called the residue of the function at the singularity .
- The residue theorem states that the integral of a function around a closed contour that encloses a finite number of isolated singularities is equal to 2 pi i times the sum of the residues of the function at those singularities  .
- The residue theorem is a powerful tool for evaluating complex integrals, especially when the integrand has poles inside the contour  .
- Complex integration is the process of finding the antiderivative of a complex function, or the value of a complex integral along a curve or a contour.
- Complex integration is based on the concept of complex line integrals, which are defined as the limit of the sum of the products of the function values and the infinitesimal line elements along the curve or the contour.
- Complex integration has many applications in physics, engineering, and mathematics, such as evaluating real integrals, solving differential equations, finding harmonic functions, computing Fourier transforms, and studying analytic continuation.



### Zeros of Analytic Functions

- An analytic function is a complex function that is differentiable at every point of its domain. 
- A zero of an analytic function is a point where the function vanishes, or its value becomes zero. 
- Zeros of analytic functions are analogous to zeros of real polynomial functions. 
- Zeros of analytic functions have the following properties:
  - Zeros of analytic functions are isolated, meaning that there is a neighborhood around each zero where the function has no other zeros.  
  - Zeros of analytic functions have a multiplicity, meaning that the function can be written as a product of a power of a linear factor and another analytic function that is nonzero at the zero. 
  - Zeros of analytic functions are invariant under conformal mappings, meaning that if two analytic functions are related by a conformal mapping, then they have the same number and multiplicity of zeros in any region. 
  - Zeros of analytic functions in more than one variable are never discrete, meaning that they form a set that has no isolated points.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is some content on the topic of residues for the notes of the unit 5 - complex variable integration in the subject of engineering mathematics-II.

### Residues

- A residue is a complex number that represents the coefficient of the term with power -1 in the Laurent series expansion of a complex function around a singularity.
- A singularity is a point where a complex function is not defined or not analytic. There are two types of singularities: isolated and non-isolated. An isolated singularity is a point where a function is not analytic, but it is analytic in a punctured disk around it. A non-isolated singularity is a point where a function is not analytic, and it is also not analytic in any punctured disk around it.
- The residue theorem is a powerful tool that relates the integral of a complex function along a closed contour to the sum of the residues of the function at the isolated singularities inside the contour. The residue theorem states that if f is a complex function that is analytic in a simply connected domain D except for a finite number of isolated singularities z1, z2, ..., zn, then for any positively oriented simple closed contour C in D that encloses the singularities, we have

  $$\oint_C f(z) dz = 2\pi i \sum_{k=1}^n \text{Res}(f, z_k)$$

  where Res(f, z_k) denotes the residue of f at z_k.
- To calculate the residue of a function f at an isolated singularity z_0, we can use the following methods:

  - If z_0 is a simple pole, that is, a pole of order 1, then

    $$\text{Res}(f, z_0) = \lim_{z \to z_0} (z - z_0) f(z)$$

  - If z_0 is a pole of order m, that is, a zero of order m of the denominator of f, then

    $$\text{Res}(f, z_0) = \frac{1}{(m-1)!} \lim_{z \to z_0} \frac{d^{m-1}}{dz^{m-1}} \left[(z - z_0)^m f(z)\right]$$

  - If z_0 is a removable singularity, that is, a point where f can be defined to make it analytic, then

    $$\text{Res}(f, z_0) = 0$$

  - If z_0 is an essential singularity, that is, a point where f has an infinite number of terms with negative powers in its Laurent series, then

    $$\text{Res}(f, z_0) = \text{the coefficient of } \frac{1}{z - z_0} \text{ in the Laurent series of } f \text{ around } z_0$$

- Residues can be used to evaluate real integrals that involve trigonometric, exponential, or rational functions. The general steps are:

  - Express the real integral as a complex integral along a suitable contour, such as a circle, a semicircle, or a rectangle.
  - Identify the singularities of the complex function inside the contour and calculate their residues.
  - Apply the residue theorem to obtain the value of the complex integral.
  - Use the properties of the contour, such as symmetry, periodicity, or limits, to relate the complex integral to the real integral.



### Cauchy's Residue Theorem and its Application

- Cauchy's residue theorem is a powerful tool to evaluate line integrals of analytic functions over closed curves; it can often be used to compute real integrals and infinite series as well .
- It generalizes the Cauchy integral theorem and Cauchy's integral formula, which are results for reasoning about isolated singularities and zeros of holomorphic functions in complex analysis .
- The residue theorem states that if a function f is analytic inside and on a simple closed contour C, except for a finite number of isolated singularities inside C, then the integral of f over C is equal to 2πi times the sum of the residues of f at those singularities .
- A residue of f at a singularity z0 is the coefficient of the term 1/(z-z0) in the Laurent series expansion of f around z0 .
- The residue theorem can be used to evaluate real integrals of the form ∫f(x)dx, where f is a rational function of trigonometric functions, by converting them into complex integrals of the form ∫f(e^iz)dz over a unit circle.
- The residue theorem can also be used to evaluate real integrals of the form ∫f(x)dx, where f is a rational function of x, by converting them into complex integrals of the form ∫f(z)dz over a suitable contour that encloses the poles of f in the upper or lower half-plane.
- The residue theorem can also be used to evaluate infinite series of the form ∑f(n), where f is a meromorphic function, by converting them into complex integrals of the form ∫f(z)dz over a large circle and applying the argument principle or the Rouche's theorem.

