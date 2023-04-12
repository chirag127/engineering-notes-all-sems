

Hello, I am Sydney, your AI assistant. I can help you with any topic you want to learn about. You have chosen the topic of:

# Nuclear Fusion

Nuclear fusion is the process of combining two or more atomic nuclei into a single, heavier nucleus, releasing a large amount of energy in the process. Nuclear fusion is the source of energy for the Sun and other stars.

Some of the main points to know about nuclear fusion are:

- Nuclear fusion requires high temperatures and pressures to overcome the electrostatic repulsion between positively charged nuclei. The conditions for fusion are achieved in the cores of stars, where the temperature is about 15 million degrees Celsius and the pressure is about 250 billion atmospheres.
- The most common fusion reaction in stars is the proton-proton chain, which converts four hydrogen nuclei (protons) into one helium nucleus (alpha particle), releasing two positrons, two neutrinos, and gamma rays. This reaction releases about 26.7 MeV of energy per helium nucleus formed.
- Another fusion reaction that occurs in stars is the carbon-nitrogen-oxygen (CNO) cycle, which uses carbon, nitrogen, and oxygen as catalysts to fuse hydrogen into helium. This reaction releases about 25 MeV of energy per helium nucleus formed and dominates in stars that are more massive than the Sun.
- The fusion reaction that is most feasible for human-made reactors is the deuterium-tritium (D-T) reaction, which fuses a deuterium nucleus (one proton and one neutron) and a tritium nucleus (one proton and two neutrons) into a helium nucleus and a neutron, releasing 17.6 MeV of energy. Deuterium is abundant in seawater, while tritium can be produced from lithium.
- The main challenge for achieving controlled nuclear fusion on Earth is to confine the hot plasma of fusion fuel long enough and at a high enough density to sustain the fusion reaction. Two main approaches for plasma confinement are magnetic confinement and inertial confinement.
- Magnetic confinement uses strong magnetic fields to contain the plasma in a torus-shaped device called a tokamak or a stellarator. The plasma is heated by electric currents, radio waves, or neutral beams. The most advanced magnetic confinement experiment is the International Thermonuclear Experimental Reactor (ITER), which aims to produce 500 MW of fusion power from 50 MW of input power for at least 400 seconds by 2035.
- Inertial confinement uses powerful lasers or ion beams to compress and heat a small pellet of fusion fuel to ignite the fusion reaction. The fusion energy is released in a short burst of a few nanoseconds. The most advanced inertial confinement experiment is the National Ignition Facility (NIF), which aims to achieve ignition and energy gain by 2024.



# Engineering Mathematics-II

Engineering Mathematics-II is a course that covers various topics in mathematics that are relevant and useful for engineering students. The course aims to develop the students' skills in solving mathematical problems and applying them to engineering situations. The course may have different syllabi depending on the institution, but some common topics are:

- Calculus: This topic covers the techniques and applications of differentiation and integration, such as finding the area, volume, work, arc length, surface area, and center of mass of various shapes and functions. It also covers improper integrals, approximate integration, and numerical methods for solving differential equations.
- Vector Algebra and Statics: This topic covers the concepts and operations of vectors, such as addition, subtraction, scalar multiplication, dot product, cross product, and projection. It also covers the applications of vectors to statics, such as finding the resultant force, moment, equilibrium, and center of gravity of a system of forces.
- Complex Analysis: This topic covers the properties and functions of complex numbers, such as modulus, argument, conjugate, polar form, and exponential form. It also covers the concepts and theorems of complex functions, such as analyticity, Cauchy-Riemann equations, harmonic functions, line integrals, Cauchy's integral theorem, Cauchy's integral formula, Taylor series, Laurent series, and residue theorem.
- Transform Techniques: This topic covers the methods and applications of various transforms, such as Laplace transform, Fourier transform, and Z-transform. It also covers the concepts and properties of these transforms, such as linearity, convolution, inverse transform, frequency domain, and transfer function.

The course may also include other topics, such as matrix algebra, eigenvalues and eigenvectors, quadratic forms, analytic geometry, infinite series, power series, and computer algebra. The course may require the use of software tools, such as MATLAB, Mathematica, or Maple, to perform calculations and simulations.

The course is usually assessed by assignments, quizzes, midterms, and final exams. The course may also require the students to complete projects or presentations on selected topics. The course may have prerequisites, such as Engineering Mathematics-I, Calculus, or Linear Algebra. The course may also have co-requisites, such as Engineering Physics, Engineering Mechanics, or Differential Equations. The course may have credits, such as 3 or 4, depending on the institution and the curriculum. The course may have a textbook, such as Engineering Mathematics by K.A. Stroud and D.J. Booth, Advanced Engineering Mathematics by Erwin Kreyszig, or Engineering Mathematics by N.P. Bali and Manish Goyal. The course may also have online resources, such as NPTEL, Khan Academy, or MIT OpenCourseWare.



## Unit 1 - Ordinary Differential Equation of Higher Order

- An ordinary differential equation (ODE) is an equation that involves one or more derivatives of an unknown function with respect to a single independent variable.
- The order of an ODE is the highest order of the derivative appearing in the equation. For example, the ODE \frac{d^4y}{dx^4} + y = 0 is of fourth order.
- A linear ODE is an ODE that can be written in the form \sum_{i=0}^n a_i(x) \frac{d^iy}{dx^i} = b(x), where a_i(x) and b(x) are given functions of x, and y is the unknown function.
- A homogeneous linear ODE is a linear ODE with b(x) = 0. A nonhomogeneous linear ODE is a linear ODE with b(x) \neq 0.
- The general solution of an ODE is the most general function that satisfies the equation. It usually contains arbitrary constants that can be determined by initial or boundary conditions.
- The general solution of a homogeneous linear ODE of order n can be written as y = c_1 y_1 + c_2 y_2 + \cdots + c_n y_n, where c_i are arbitrary constants and y_i are linearly independent solutions of the ODE.
- The general solution of a nonhomogeneous linear ODE of order n can be written as y = y_h + y_p, where y_h is the general solution of the corresponding homogeneous ODE, and y_p is a particular solution of the nonhomogeneous ODE.
- To find a particular solution of a nonhomogeneous linear ODE, various methods can be used, such as the method of undetermined coefficients, the method of variation of parameters, or the method of Laplace transform.



# Linear differential equation of nth order with constant coefficients

- A linear differential equation of nth order with constant coefficients is an equation of the form

$$a_n y^{(n)} + a_{n-1} y^{(n-1)} + \cdots + a_1 y' + a_0 y = f(x)$$

where $a_n, a_{n-1}, \ldots, a_1, a_0$ are constants and $f(x)$ is a given function of $x$.

- The equation is called **homogeneous** if $f(x) = 0$ and **non-homogeneous** otherwise.

- The general solution of a homogeneous linear differential equation of nth order with constant coefficients is a linear combination of $n$ linearly independent solutions, which can be found by solving the **characteristic equation**

$$a_n r^n + a_{n-1} r^{n-1} + \cdots + a_1 r + a_0 = 0$$

- The characteristic equation may have real or complex roots, which may be distinct or repeated. Depending on the nature of the roots, the general solution may involve exponential, trigonometric, or hyperbolic functions.

- The general solution of a non-homogeneous linear differential equation of nth order with constant coefficients is the sum of the general solution of the homogeneous equation and a **particular solution** of the non-homogeneous equation, which can be found by various methods, such as **undetermined coefficients** or **variation of parameters**.

- The method of undetermined coefficients involves guessing a particular solution of the same form as $f(x)$, with some unknown coefficients, and then substituting it into the equation to determine the coefficients. This method works only if $f(x)$ is a polynomial, exponential, sine, cosine, or a linear combination of these functions.

- The method of variation of parameters involves finding $n$ functions $u_1(x), u_2(x), \ldots, u_n(x)$ such that the particular solution is of the form

$$y_p(x) = u_1(x) y_1(x) + u_2(x) y_2(x) + \cdots + u_n(x) y_n(x)$$

where $y_1(x), y_2(x), \ldots, y_n(x)$ are the linearly independent solutions of the homogeneous equation. The functions $u_1(x), u_2(x), \ldots, u_n(x)$ can be found by solving a system of linear equations involving the Wronskian of the homogeneous solutions and the function $f(x)$. This method works for any function $f(x)$, but it may be more complicated than the method of undetermined coefficients.



# Simultaneous Linear Differential Equations

- A simultaneous differential equation is one of the mathematical equations for an indefinite function of one or more than one variables that relate the values of the function.
- A system of simultaneous linear differential equations is a set of two or more linear differential equations that involve the same independent variable and two or more dependent variables.
- A linear differential equation is one that can be written in the form:

$$a_n(x)\frac{d^ny}{dx^n}+a_{n-1}(x)\frac{d^{n-1}y}{dx^{n-1}}+\cdots+a_1(x)\frac{dy}{dx}+a_0(x)y=b(x)$$

where $a_n(x),a_{n-1}(x),\ldots,a_0(x)$ and $b(x)$ are given functions of $x$ and $y$ is the unknown function.
- A system of simultaneous linear differential equations can be written in matrix form as:

$$\mathbf{A}(x)\mathbf{y}'(x)+\mathbf{B}(x)\mathbf{y}(x)=\mathbf{c}(x)$$

where $\mathbf{A}(x)$ and $\mathbf{B}(x)$ are matrices of coefficients, $\mathbf{y}(x)$ and $\mathbf{y}'(x)$ are vectors of dependent variables and their derivatives, and $\mathbf{c}(x)$ is a vector of constants.
- To solve a system of simultaneous linear differential equations, one can use various methods such as elimination, substitution, matrix inversion, eigenvalues and eigenvectors, Laplace transform, etc  .
- The general solution of a system of simultaneous linear differential equations is a linear combination of particular solutions that satisfy the given initial or boundary conditions.



# Second order linear differential equations with variable coefficients

- A second-order linear differential equation is an equation of the form

  $$a_2(x)y'' + a_1(x)y' + a_0(x)y = r(x)$$

  where $a_2(x), a_1(x), a_0(x)$ and $r(x)$ are functions of the independent variable $x$ and $a_2(x)$ is not identically zero.

- If $r(x) \equiv 0$, the equation is called **homogeneous**; otherwise, it is called **nonhomogeneous**.

- The general solution of a homogeneous equation is a linear combination of two linearly independent solutions, which can be found by using methods such as the **characteristic equation**, the **reduction of order**, or the **method of Frobenius**.

- The general solution of a nonhomogeneous equation is the sum of the general solution of the corresponding homogeneous equation and a **particular solution** of the nonhomogeneous equation, which can be found by using methods such as the **method of undetermined coefficients**, the **method of variation of parameters**, or the **method of power series**.

- Some examples of second-order linear differential equations with variable coefficients are:

  - The **Legendre equation**:

    $$(1-x^2)y'' - 2xy' + n(n+1)y = 0$$

    where $n$ is a constant. The solutions are called **Legendre polynomials**.

  - The **Bessel equation**:

    $$x^2y'' + xy' + (x^2 - n^2)y = 0$$

    where $n$ is a constant. The solutions are called **Bessel functions**.

  - The **Airy equation**:

    $$y'' - xy = 0$$

    The solutions are called **Airy functions**.

  - The **Chebyshev equation**:

    $$(1-x^2)y'' - xy' + n^2y = 0$$

    where $n$ is a constant. The solutions are called **Chebyshev polynomials**.



Hello, I am Sydney, your AI assistant. I can help you with your study material for Engineering Mathematics-II. Here is some information on the topic of solution by changing independent variable for the notes of the Unit 1 - Ordinary Differential Equation of Higher Order.

# Solution by changing independent variable for the notes of the Unit 1 - Ordinary Differential Equation of Higher Order

- A differential equation is an equation involving an unknown function y = f(x) and one or more of its derivatives.
- A solution to a differential equation is a function y = f(x) that satisfies the differential equation when f and its derivatives are substituted into the equation.
- A general solution of a differential equation is a solution that contains one or more arbitrary constants.
- A particular solution of a differential equation is a solution that is obtained by assigning specific values to the arbitrary constants in the general solution.
- A change of variable is a technique that can be used to simplify or transform a differential equation into a different form.
- A change of variable can involve changing the independent variable, the dependent variable, or both.
- A change of variable can be useful for solving differential equations that are homogeneous, separable, linear, or of other special forms  .
- To perform a change of variable, one needs to find a suitable substitution for the original variable(s), and then use the chain rule or other methods to express the derivatives in terms of the new variable(s) .
- After performing a change of variable, one needs to solve the transformed differential equation, and then return to the original variable(s) to obtain the general or particular solution of the original differential equation .
- An example of a change of variable for a first-order differential equation is y = ux, where u is a function of x. This substitution can be used to solve homogeneous differential equations of the form f(x,y)dy = g(x,y)dx, where f and g are homogeneous functions of the same degree of x and y.
- An example of a change of variable for a second-order differential equation is z = y', where z is a function of x. This substitution can be used to reduce a second-order differential equation to a first-order differential equation of the form z' = h(x,z).



# Method of Variation of Parameters

- The method of variation of parameters is a general method to find a particular solution of a non-homogeneous linear differential equation of the form Lx(t) = F(t), where L is a linear differential operator, x(t) is the unknown function, and F(t) is a given function.
- The method is based on replacing the constants in the solution of the corresponding homogeneous equation Lx(t) = 0 by functions and determining these functions such that the original equation is satisfied .
- The method can be applied to differential equations of any order, but it is usually easier to use for second-order equations .
- The steps of the method for a second-order equation are as follows :
  - Find the complementary solution x_c(t) of the homogeneous equation Lx(t) = 0 by using the characteristic equation or other methods.
  - Write the complementary solution as x_c(t) = c_1 y_1(t) + c_2 y_2(t), where c_1 and c_2 are constants and y_1(t) and y_2(t) are linearly independent solutions of the homogeneous equation.
  - Assume that the particular solution x_p(t) has the same form as x_c(t), but with c_1 and c_2 replaced by functions u_1(t) and u_2(t), that is, x_p(t) = u_1(t) y_1(t) + u_2(t) y_2(t).
  - Differentiate x_p(t) once and twice to obtain x_p'(t) and x_p''(t).
  - Substitute x_p(t), x_p'(t), and x_p''(t) into the original equation Lx(t) = F(t) and simplify.
  - Use the fact that y_1(t) and y_2(t) are solutions of the homogeneous equation to eliminate some terms and obtain an equation involving only u_1(t), u_2(t), and their derivatives.
  - Impose the condition that u_1'(t) y_1(t) + u_2'(t) y_2(t) = 0, which ensures that x_p(t) and x_c(t) are linearly independent. This condition reduces the equation to a simpler one that can be solved for u_1'(t) and u_2'(t).
  - Integrate u_1'(t) and u_2'(t) to find u_1(t) and u_2(t), using F(t) as the integrand and applying the method of integration by parts if necessary.
  - Substitute u_1(t) and u_2(t) into x_p(t) to obtain the particular solution.
  - Add x_c(t) and x_p(t) to obtain the general solution x(t) = x_c(t) + x_p(t).



# Cauchy-Euler Equation

- A Cauchy-Euler equation is a linear homogeneous ordinary differential equation with variable coefficients of the form :

$$a_nx^ny^{(n)} + a_{n-1}x^{n-1}y^{(n-1)} + \cdots + a_1xy' + a_0y = f(x)$$

where $a_0, a_1, \ldots, a_n$ are constants and $f(x)$ is a given function.

- The most common Cauchy-Euler equation is the second-order equation, which appears in many physics and engineering applications, such as when solving Laplace's equation in polar coordinates . The second-order Cauchy-Euler equation is:

$$ax^2y'' + bxy' + cy = f(x)$$

- The solutions of Cauchy-Euler equations can be found using the characteristic equation :

$$ar(r-1) + br + c = 0$$

- Just like the constant coefficient differential equation, we have a quadratic equation and the nature of the roots again leads to three classes of solutions:

  - If the roots are distinct and real, say $r_1$ and $r_2$, then the general solution is:

  $$y(x) = c_1x^{r_1} + c_2x^{r_2}$$

  - If the roots are repeated, say $r_1 = r_2 = r$, then the general solution is:

  $$y(x) = c_1x^r + c_2x^r\ln x$$

  - If the roots are complex, say $r_1 = \alpha + i\beta$ and $r_2 = \alpha - i\beta$, then the general solution is:

  $$y(x) = x^\alpha(c_1\cos(\beta\ln x) + c_2\sin(\beta\ln x))$$

- The constants $c_1$ and $c_2$ can be determined by the initial or boundary conditions of the problem.

- If the given function $f(x)$ is not zero, then the equation is non-homogeneous and we need to find a particular solution using methods such as undetermined coefficients or variation of parameters. The general solution is then the sum of the complementary solution (the solution of the homogeneous equation) and the particular solution.



# Application of differential equations in solving engineering problems

- Differential equations are mathematical equations that relate the rate of change of a physical quantity, such as temperature, pressure, displacement, velocity, stress, strain, current, voltage, or concentration of a pollutant, with the change of time or location, or both .
- Differential equations are useful for modeling physical problems using mathematical equations, and then solving these equations to study the behavior of the systems concerned .
- Some examples of engineering subjects that are based on the theory of differential equations are:
  - Mechanical vibration or structural dynamics: The motion of a mass-spring system, a pendulum, a beam, a bridge, or a building can be described by second-order differential equations that involve the displacement, velocity, acceleration, and external forces acting on the system .
  - Heat transfer: The temperature distribution in a solid, a liquid, or a gas can be modeled by partial differential equations that involve the heat flux, the heat capacity, the thermal conductivity, and the heat sources or sinks in the medium .
  - Theory of electric circuits: The voltage and current in a circuit that contains resistors, capacitors, inductors, and sources can be determined by first-order differential equations that involve the resistance, capacitance, inductance, and electromotive force in the circuit .
- Some of the methods for solving differential equations are:
  - Analytical methods: These methods involve finding exact or approximate solutions of differential equations using algebraic, trigonometric, exponential, or logarithmic functions, or series expansions . Examples of analytical methods are separation of variables, integrating factors, variation of parameters, undetermined coefficients, Laplace transform, Fourier series, etc.
  - Numerical methods: These methods involve finding numerical approximations of the solutions of differential equations using algorithms that discretize the domain and the range of the equations. Examples of numerical methods are Euler's method, Runge-Kutta method, finite difference method, finite element method, etc.



## Unit 2 - Laplace Transform

- The Laplace transform is a mathematical technique that converts a function of time, f(t), into a function of a complex variable, F(s), where s is the Laplace variable.
- The Laplace transform is useful for solving linear differential equations with constant coefficients, as well as for analyzing the behavior of linear systems in the frequency domain.
- The Laplace transform of a function f(t) is defined as:

  `F(s) = L{f(t)} = ∫<sub>0</sub><sup>∞</sup> f(t) e<sup>-st</sup> dt`

  where s is a complex variable of the form s = σ + jω, and j is the imaginary unit.

- The inverse Laplace transform of a function F(s) is defined as:

  `f(t) = L<sup>-1</sup>{F(s)} = (1/2πj) ∫<sub>γ-j∞</sub><sup>γ+j∞</sup> F(s) e<sup>st</sup> ds`

  where γ is a real constant such that all the singularities of F(s) lie to the left of the line Re(s) = γ.

- The Laplace transform has some important properties, such as:

  - Linearity: L{af(t) + bg(t)} = aL{f(t)} + bL{g(t)}
  - Shifting in time: L{f(t-a)u(t-a)} = e<sup>-as</sup>F(s), where u(t) is the unit step function
  - Shifting in frequency: L{e<sup>at</sup>f(t)} = F(s-a)
  - Scaling: L{f(at)} = (1/a)F(s/a)
  - Differentiation: L{f'(t)} = sF(s) - f(0), L{f''(t)} = s<sup>2</sup>F(s) - sf(0) - f'(0), etc.
  - Integration: L{∫<sub>0</sub><sup>t</sup> f(τ) dτ} = (1/s)F(s)
  - Convolution: L{f(t) * g(t)} = F(s)G(s), where * denotes the convolution operation
  - Initial value theorem: lim<sub>t→0</sub> f(t) = lim<sub>s→∞</sub> sF(s), if f(t) and f'(t) are both Laplace transformable
  - Final value theorem: lim<sub>t→∞</sub> f(t) = lim<sub>s→0</sub> sF(s), if f(t) and sF(s) are both Laplace transformable and all the singularities of sF(s) are in the left half-plane

- Some common Laplace transforms are:

  - L{1} = 1/s
  - L{t<sup>n</sup>} = n!/s<sup>n+1</sup>, n = 0, 1, 2, ...
  - L{e<sup>at</sup>} = 1/(s-a)
  - L{sin(at)} = a/(s<sup>2</sup>+a<sup>2</sup>)
  - L{cos(at)} = s/(s<sup>2</sup>+a<sup>2</sup>)
  - L{sinh(at)} = a/(s<sup>2</sup>-a<sup>2</sup>)
  - L{cosh(at)} = s/(s<sup>2</sup>-a<sup>2</sup>)
  - L{δ(t)} = 1, where δ(t) is the Dirac delta function
  - L{u(t)} = 1/s, where u(t) is the unit step function
  - L{r(t)} = 1/s<sup>2</sup>, where r(t) is the unit ramp function
  - L{t<sup>n</sup>e<sup>at</sup>} = n!/((s-a)<sup>n+1</sup>), n = 0, 1, 2, ...
  - L{e<sup>at</sup>sin(bt)} = b/((s-a)<sup>2</sup>+b<sup>2</sup>)
  - L{e<sup>at</sup>cos(bt)} = (s-a)/((s-a)<sup>2</sup>+b<sup



# Laplace Transform

The Laplace transform is a mathematical technique that converts a function of a real variable (usually time) into a function of a complex variable (usually frequency). It is useful for solving differential equations, analyzing systems, and studying signals and systems.

## Definition of the Laplace Transform

The Laplace transform of a function f(t) is defined as

$$F(s) = \mathcal{L}\{f(t)\} = \int_0^\infty e^{-st} f(t) dt$$

where s is a complex variable of the form s = σ + jω, and the integral is taken over the positive real axis. The function F(s) is called the image or transform of f(t), and the variable s is called the complex frequency.

The Laplace transform exists if f(t) is piecewise continuous and satisfies the following condition:

$$|f(t)| \leq Me^{ct}$$

for some constants M and c, and for all sufficiently large t. This condition ensures that the integral converges.

## Properties of the Laplace Transform

The Laplace transform has many important properties that make it easier to work with. Some of the most common properties are:

- Linearity: If a and b are constants, then

$$\mathcal{L}\{af(t) + bg(t)\} = a\mathcal{L}\{f(t)\} + b\mathcal{L}\{g(t)\}$$

- Time shifting: If a is a constant, then

$$\mathcal{L}\{f(t-a)\} = e^{-as} \mathcal{L}\{f(t)\}$$

- Frequency shifting: If a is a constant, then

$$\mathcal{L}\{e^{at} f(t)\} = F(s-a)$$

- Scaling: If a is a constant, then

$$\mathcal{L}\{f(at)\} = \frac{1}{a} F\left(\frac{s}{a}\right)$$

- Differentiation in time: If f(t) and f'(t) are both Laplace transformable, then

$$\mathcal{L}\{f'(t)\} = s\mathcal{L}\{f(t)\} - f(0)$$

- Integration in time: If f(t) is Laplace transformable, then

$$\mathcal{L}\left\{\int_0^t f(\tau) d\tau\right\} = \frac{1}{s} \mathcal{L}\{f(t)\}$$

- Convolution: If f(t) and g(t) are both Laplace transformable, then

$$\mathcal{L}\{f(t) * g(t)\} = \mathcal{L}\{f(t)\} \mathcal{L}\{g(t)\}$$

where * denotes the convolution operation defined as

$$f(t) * g(t) = \int_0^t f(\tau) g(t-\tau) d\tau$$

- Initial value theorem: If f(t) and f'(t) are both Laplace transformable and f(t) is bounded as t → 0, then

$$\lim_{s \to \infty} sF(s) = f(0)$$

- Final value theorem: If f(t) and f'(t) are both Laplace transformable and f(t) → 0 as t → ∞, then

$$\lim_{s \to 0} sF(s) = \lim_{t \to \infty} f(t)$$

## Examples of Laplace Transforms

Here are some examples of Laplace transforms of common functions:

- Constant function: If f(t) = c, then

$$\mathcal{L}\{c\} = \frac{c}{s}$$

- Exponential function: If f(t) = e^{at}, then

$$\mathcal{L}\{e^{at}\} = \frac{1}{s-a}$$

- Sine function: If f(t) = sin(at), then

$$\mathcal{L}\{sin(at)\} = \frac{a}{s^2 + a^2}$$

- Cosine function: If f(t) = cos(at), then

$$\mathcal{L}\{cos(at)\} = \frac{s}{s^2 + a^2}



# Existence theorem for the notes of the Unit 2 - Laplace Transform in the subject of ENGINEERING MATHEMATICS-II

- The existence theorem is a criterion that determines whether a function has a Laplace transform or not.
- The Laplace transform of a function f(t) is defined as L(f(t)) = F(s) = ∫∞ 0e − stf(t)dt, where s is a complex variable and t is a real variable.
- The existence theorem states that if f(t) is piecewise continuous on every finite interval in [0, ∞) and satisfies the condition |f(t)| ≤ Meαt for some constants M and α and for all t ≥ 0, then L(f(t)) exists for all s > α  .
- The condition |f(t)| ≤ Meαt means that f(t) is of exponential order, that is, it does not grow faster than an exponential function as t → ∞.
- The condition s > α ensures that the integral ∫∞ 0e − stf(t)dt converges, since e − st decreases faster than eαt as t → ∞.
- The existence theorem is a sufficient but not necessary condition for the Laplace transform to exist. There may be some functions that do not satisfy the condition but still have a Laplace transform, such as f(t) = sin(t2).
- The existence theorem is useful for checking whether a given function has a Laplace transform before applying the transform to solve differential equations or other problems.



# Properties of Laplace Transform

The Laplace transform is a powerful tool for solving linear differential equations and analyzing linear systems. It transforms a function of time, f(t), into a function of a complex variable, s, F(s). The Laplace transform has several properties that make it useful and convenient. Here are some of the most important ones:

- **Linearity**: The Laplace transform is a linear operator, which means that it preserves the operations of addition and scalar multiplication. That is, if a and b are constants and f and g are functions, then L(af + bg) = aL(f) + bL(g). This property allows us to easily find the Laplace transform of linear combinations of known functions.

- **Differentiation**: The Laplace transform transforms differentiation in time to multiplication by s in the complex domain. That is, if f is a function with continuous derivatives, then L(f') = sL(f) - f(0), L(f'') = s^2L(f) - sf(0) - f'(0), and so on. This property allows us to solve differential equations by transforming them into algebraic equations.

- **Integration**: The Laplace transform transforms integration in time to division by s in the complex domain. That is, if f is a function with Laplace transform F, then L(integral of f(t) dt from 0 to t) = F(s)/s. This property allows us to find the Laplace transform of integrals of known functions.

- **Multiplication by t**: The Laplace transform transforms multiplication by t in time to differentiation with respect to s in the complex domain. That is, if f is a function with Laplace transform F, then L(tf(t)) = -dF/ds. This property allows us to find the Laplace transform of functions that involve t as a factor.

- **Frequency shifting**: The Laplace transform transforms multiplication by e^(at) in time to shifting by a in the complex domain. That is, if f is a function with Laplace transform F, then L(e^(at)f(t)) = F(s-a). This property allows us to find the Laplace transform of functions that involve exponential factors.

- **Time scaling**: The Laplace transform transforms scaling by a in time to scaling by 1/a in the complex domain. That is, if f is a function with Laplace transform F, then L(f(at)) = (1/a)F(s/a). This property allows us to find the Laplace transform of functions that involve time scaling.

- **Time shifting**: The Laplace transform transforms shifting by a in time to multiplication by e^(-as) in the complex domain. That is, if f is a function with Laplace transform F, then L(f(t-a)) = e^(-as)F(s). This property allows us to find the Laplace transform of functions that involve time delays.

- **Convolution**: The Laplace transform transforms convolution in time to multiplication in the complex domain. That is, if f and g are functions with Laplace transforms F and G, then L(f * g) = F * G, where f * g is the convolution of f and g defined by (f * g)(t) = integral of f(tau)g(t-tau) dtau from -infinity to infinity. This property allows us to find the Laplace transform of functions that involve convolution.

- **Conjugation**: The Laplace transform transforms complex conjugation in time to complex conjugation in the complex domain. That is, if f is a function with Laplace transform F, then L(f*) = F*, where f* is the complex conjugate of f defined by f*(t) = f(t). This property allows us to find the Laplace transform of complex-valued functions.

- **Periodic function**: The Laplace transform transforms a periodic function in time to a sum of terms in the complex domain. That is, if f is a function with period T, then L(f) = (1 - e^(-sT))/s * F, where F is the Laplace transform of one period of f. This property allows us to find the Laplace transform of periodic functions.



# Laplace Transform of Derivatives and Integrals

## Definition

The Laplace transform is an integral transform that converts a function of a real variable (usually time) to a function of a complex variable (usually frequency). It is useful for solving differential equations, integral equations, and other problems involving functions of time.

The Laplace transform of a function f(t) is defined as

L{f(t)} = F(s) = ∫<sub>0</sub><sup>∞</sup> f(t) e<sup>-st</sup> dt

where s is a complex variable and the integral is taken over the positive real axis.

## Properties

The Laplace transform has many properties that make it easier to manipulate and apply. Some of the most important ones are:

- Linearity: L{af(t) + bg(t)} = aL{f(t)} + bL{g(t)} for any constants a and b
- Shift in time: L{f(t-a)u(t-a)} = e<sup>-as</sup>F(s) where u(t) is the unit step function
- Shift in frequency: L{e<sup>at</sup>f(t)} = F(s-a)
- Scaling: L{f(at)} = (1/a)F(s/a) for any constant a ≠ 0
- Derivative in time: L{f'(t)} = sF(s) - f(0)
- Derivative in frequency: L{(-t)f(t)} = F'(s)
- Integral in time: L{∫<sub>0</sub><sup>t</sup> f(τ) dτ} = (1/s)F(s)
- Integral in frequency: L{f(t)/t} = ∫<sub>s</sub><sup>∞</sup> F(σ) dσ
- Convolution: L{f(t) * g(t)} = F(s)G(s) where * denotes the convolution operation
- Initial value theorem: lim<sub>t→0</sub> f(t) = lim<sub>s→∞</sub> sF(s) if f(t) and f'(t) are of exponential order
- Final value theorem: lim<sub>t→∞</sub> f(t) = lim<sub>s→0</sub> sF(s) if f(t) and f'(t) are of exponential order and all the poles of F(s) are in the left half-plane

## Examples

Here are some examples of how to use the Laplace transform to find the solutions of differential equations and integral equations.

### Example 1: Differential equation

Solve the differential equation y'' + 2y' + y = e<sup>-t</sup> with y(0) = 0 and y'(0) = 1.

Solution:

Taking the Laplace transform of both sides, we get

L{y'' + 2y' + y} = L{e<sup>-t</sup>}

Using the properties of linearity and derivative in time, we get

s<sup>2</sup>Y(s) - sy(0) - y'(0) + 2sY(s) - 2y(0) + Y(s) = (1/s+1)

Substituting the initial conditions y(0) = 0 and y'(0) = 1, we get

(s<sup>2</sup> + 2s + 1)Y(s) - 1 = (1/s+1)

Solving for Y(s), we get

Y(s) = (1 + s)/((s+1)(s<sup>2</sup> + 2s + 1))

Using partial fraction decomposition, we get

Y(s) = (1/2)(1/s+1) + (1/2)(1/s+1)<sup>2</sup> - (1/s<sup>2</sup> + 2s + 1)

Taking the inverse Laplace transform of both sides, we get

y(t) = (1/2)e<sup>-t</sup> + (1/2)t e<sup>-t</sup> - e<sup>-t</sup> cos t

This is the solution of the differential equation.

### Example 2: Integral equation

Solve the integral equation y(t) = 2 + ∫<sub>0</sub><sup>t</sup> (t -



# Unit step function for the notes of the Unit 2 - Laplace Transform in the subject of ENGINEERING MATHEMATICS-II

- The unit step function is a function that is zero for negative values of the argument and one for positive values. It is denoted by u(t) and defined as:

u(t) = {1 for t ≥ 0 0 for t < 0

- The unit step function can be used to model a switch that turns on or off at a certain time. For example, u(t - a) is a function that is zero for t < a and one for t > a, meaning that the switch turns on at time a.

- The Laplace transform of the unit step function is given by :

L[u(t)] = ∫∞ 0u(t)e − stdt = ∫∞ 0e − stdt = [e − st − s]∞ 0 = 1 s

- The Laplace transform of a shifted unit step function is given by :

L[u(t - a)] = ∫∞ 0u(t - a)e − stdt = ∫a ∞e − stdt = [e − st − s]∞ a = e − as s

- This result can be generalized to the time displacement theorem, which states that if F(s) is the Laplace transform of f(t), then:

L[u(t - a)f(t - a)] = e − as F(s)

- The time displacement theorem can be used to find the Laplace transform of piecewise continuous functions, which are functions that are continuous on each interval of a finite partition of the real line, and have finite jumps at the endpoints of the intervals. For example, if f(t) is defined as:

f(t) = {t for 0 ≤ t < 1 2 for 1 ≤ t < 2 3 − t for 2 ≤ t < 3 0 for t ≥ 3

- Then f(t) can be written as a linear combination of shifted unit step functions and their products:

f(t) = tu(1 - t) + 2u(t - 1) - tu(t - 1) + (3 - t)u(t - 2) - (3 - t)u(t - 3)

- Applying the time displacement theorem to each term, we get the Laplace transform of f(t):

L[f(t)] = L[tu(1 - t)] + L[2u(t - 1)] - L[tu(t - 1)] + L[(3 - t)u(t - 2)] - L[(3 - t)u(t - 3)]

= e − s s2 + 2e − s s - e − s s2 + e − 2s s2 - 3e − 2s s + e − 2s s2 - e − 3s s2 + 3e − 3s s

= 1 s2 - 2e − s s2 + 2e − 2s s2 - e − 3s s2

- The Laplace transform of piecewise continuous functions can be used to solve differential equations with discontinuous forcing functions, such as the following example:

y′′ + 2y′ + 2y = f(t), y(0) = 0, y′(0) = 0

where f(t) is the same function as above. Taking the Laplace transform of both sides, we get:

s2Y(s) + 2sY(s) + 2Y(s) = 1 s2 - 2e − s s2 + 2e − 2s s2 - e − 3s s2

Solving for Y(s), we get:

Y(s) = 1 s2 + 2s + 2 - 2e − s s2 + 2s + 2 + 2e − 2s s2 + 2s + 2 - e − 3s s2 + 2s + 2

Using partial fraction decomposition and inverse Laplace transform, we get the solution for y(t):

y(t) = 1 2 (1 − e − t cos t) − 1 2 e − t sin t + u(t − 1)(e − (t −



# Laplace transform of periodic function

- A periodic function is a function that repeats itself after a fixed interval of time, called the period.
- The Laplace transform of a periodic function can be obtained by using the time-shifting property of the Laplace transform, which states that if F(s) is the Laplace transform of f(t), then e^(-sT)F(s) is the Laplace transform of f(t-T), where T is a constant.
- If f(t) is a periodic function with period T, then f(t) = f(t+nT) for any integer n. Therefore, we can write f(t) as a sum of shifted copies of f(t) over one period, as follows:

  f(t) = f(t) + e^(-sT)f(t) + e^(-2sT)f(t) + ... + e^(-nsT)f(t) + ...

- Taking the Laplace transform of both sides, we get:

  F(s) = F(s) + e^(-sT)F(s) + e^(-2sT)F(s) + ... + e^(-nsT)F(s) + ...

- This is an infinite geometric series with common ratio e^(-sT). If |e^(-sT)| < 1, then the series converges and we can use the formula for the sum of an infinite geometric series:

  F(s) = F(s) / (1 - e^(-sT))

- This is the formula for the Laplace transform of a periodic function with period T. Note that F(s) is the Laplace transform of f(t) over one period, i.e., F(s) = L{f(t)} from 0 to T.

- Example: Find the Laplace transform of the periodic function f(t) shown below, where T = 2.

  periodic function

- Solution: The function f(t) is periodic with period T = 2. To find the Laplace transform of f(t), we need to find the Laplace transform of f(t) over one period, i.e., from 0 to 2. We can split f(t) into two parts: f(t) = f1(t) + f2(t), where f1(t) is the function from 0 to 1 and f2(t) is the function from 1 to 2. Then, we can use the linearity property of the Laplace transform to write:

  F(s) = L{f(t)} from 0 to 2 = L{f1(t)} from 0 to 1 + L{f2(t)} from 1 to 2

- The Laplace transform of f1(t) is:

  L{f1(t)} from 0 to 1 = L{1} from 0 to 1 = 1/s

- The Laplace transform of f2(t) is:

  L{f2(t)} from 1 to 2 = L{-1} from 1 to 2 = -e^(-s)/s

- Therefore, the Laplace transform of f(t) over one period is:

  F(s) = L{f(t)} from 0 to 2 = 1/s - e^(-s)/s = (1 - e^(-s))/s

- Using the formula for the Laplace transform of a periodic function with period T = 2, we get:

  F(s) = (1 - e^(-s))/s / (1 - e^(-2s)) = 1 / (s(1 + e^(-s)))

- This is the final answer.



# Inverse Laplace Transform

- The inverse Laplace transform is the transformation of a Laplace transform into a function of time.  
- If F(s) is the Laplace transform of f(t), then f(t) is the inverse Laplace transform of F(s), denoted by L^-1{F}(t).  
- The inverse Laplace transform can be obtained by using standard transforms, such as those in Table 6.1. 
- The inverse Laplace transform can also be obtained by using the Bromwich integral, the Fourier–Mellin integral, or Mellin's inverse formula, which are complex integrals of the form:  

$$
f(t) = \frac{1}{2\pi i} \int_{\gamma - i\infty}^{\gamma + i\infty} F(s) e^{st} ds
$$

where $\gamma$ is a real number so that the contour path of integration is in the region of convergence of F(s). 

- The inverse Laplace transform can be used to solve differential equations, find the impulse response of a system, and analyze the stability of a system.



# Convolution Theorem

- The convolution theorem states that the Laplace transform of a convolution of two functions is the product of the Laplace transforms of the individual functions .
- The convolution of two functions f and g is defined as

  ```math
  f * g = \int_0^t f(\tau) g(t - \tau) d\tau
  ```

- The convolution theorem can be written as

  ```math
  \mathcal{L}[f * g] = F(s) G(s)
  ```

  where F(s) and G(s) are the Laplace transforms of f and g respectively .

- The convolution theorem can be used to simplify the inverse Laplace transform of a product of two functions.
- The convolution theorem can also be used to solve linear differential equations with constant coefficients and non-homogeneous boundary conditions .



# Application of Laplace Transform to solve ordinary differential equations and simultaneous differential equations

- Laplace transform is a powerful integral transform that can switch a function from the time domain to the s-domain, where s is a complex variable.
- Laplace transform can be used to solve linear ordinary differential equations (ODEs) with constant or variable coefficients, as well as simultaneous differential equations, by transforming them into algebraic equations in the s-domain.
- The general steps for solving ODEs using Laplace transform are:

  1. Take the Laplace transform of both sides of the ODE, using the properties of the transform such as linearity, differentiation, and initial value.
  2. Solve for the Laplace transform of the unknown function, denoted by Y(s), by algebraic manipulation.
  3. Take the inverse Laplace transform of Y(s) to obtain the solution of the ODE in the time domain, denoted by y(t), using the properties of the inverse transform such as partial fraction decomposition, convolution, and final value.
  4. Check the solution by substituting it into the original ODE and verifying that it satisfies the initial conditions.

- The general steps for solving simultaneous differential equations using Laplace transform are:

  1. Take the Laplace transform of each equation in the system, using the properties of the transform such as linearity, differentiation, and initial value.
  2. Solve for the Laplace transforms of the unknown functions, denoted by X(s), Y(s), Z(s), etc., by algebraic manipulation, such as elimination, substitution, or matrix inversion.
  3. Take the inverse Laplace transform of each function to obtain the solution of the system in the time domain, denoted by x(t), y(t), z(t), etc., using the properties of the inverse transform such as partial fraction decomposition, convolution, and final value.
  4. Check the solution by substituting it into the original system and verifying that it satisfies the initial conditions.

- Some examples of ODEs and systems that can be solved by Laplace transform are:

  - Second order linear ODE with constant coefficients: y'' + ay' + by = g(t), y(0) = y0, y'(0) = y1
  - Second order linear ODE with variable coefficients: y'' + p(t)y' + q(t)y = g(t), y(0) = y0, y'(0) = y1
  - Simultaneous first order linear ODEs with constant coefficients: x' + ax = by + f(t), y' + cy = dx + g(t), x(0) = x0, y(0) = y0
  - Simultaneous second order linear ODEs with constant coefficients: x'' + ax' + bx = cy' + dy + f(t), y'' + ey' + fy = gx' + hx + g(t), x(0) = x0, x'(0) = x1, y(0) = y0, y'(0) = y1

- For more details and examples, please refer to the following sources:

  -  Applications of the Laplace transform in solving ordinary differential equations
  -  Applications of Laplace Transformation for Solving Various Differential Equations with Variable Coefficients
  -  Applications of Laplace Transforms
  -  Transforms of derivatives and ODEs
  -  Laplace transform applied to differential equations



## Unit 3 - Sequence and Series

- A **sequence** is a list of numbers or objects that follow a certain rule or pattern.
- A **series** is the sum of the terms of a sequence.
- An **arithmetic sequence** is a sequence where each term is obtained by adding or subtracting a constant value, called the **common difference**, to the previous term.
- An **arithmetic series** is the sum of the terms of an arithmetic sequence.
- A **geometric sequence** is a sequence where each term is obtained by multiplying or dividing a constant value, called the **common ratio**, to the previous term.
- A **geometric series** is the sum of the terms of a geometric sequence.
- A **finite sequence** or **finite series** has a fixed number of terms.
- An **infinite sequence** or **infinite series** has an unlimited number of terms.
- A **convergent series** is an infinite series that has a finite sum.
- A **divergent series** is an infinite series that does not have a finite sum.
- A **recursive formula** defines the nth term of a sequence in terms of one or more previous terms.
- An **explicit formula** defines the nth term of a sequence in terms of n, without referring to previous terms.
- A **sigma notation** is a compact way of writing a series using the Greek letter sigma (∑) and an index variable.
- A **partial sum** is the sum of the first n terms of a series.
- A **general term** is the expression that represents the nth term of a sequence or series.



# Definition of Sequence and Series with Examples

- A **sequence** is an ordered list of numbers or objects that follow a certain rule or pattern. For example, 1, 3, 5, 7, 9 is a sequence of odd numbers. A sequence can be finite or infinite, depending on how many terms it has.
- A **series** is the sum of the terms of a sequence. For example, 1 + 3 + 5 + 7 + 9 is a series that adds up to 25. A series can be convergent or divergent, depending on whether the sum approaches a finite value or not.
- A sequence can be represented by a general term or a formula that gives the nth term of the sequence. For example, the general term of the sequence 1, 3, 5, 7, 9 is a_n = 2n - 1, where n is the term number.
- A series can be represented by a partial sum or a formula that gives the sum of the first n terms of the series. For example, the partial sum of the series 1 + 3 + 5 + 7 + 9 is S_n = n^2, where n is the number of terms.
- Some common types of sequences and series are:
  - **Arithmetic sequence and series**: A sequence and series where the difference between consecutive terms is constant. For example, 2, 5, 8, 11, 14 is an arithmetic sequence with a common difference of 3, and 2 + 5 + 8 + 11 + 14 is an arithmetic series with a sum of 40.
  - **Geometric sequence and series**: A sequence and series where the ratio between consecutive terms is constant. For example, 2, 6, 18, 54, 162 is a geometric sequence with a common ratio of 3, and 2 + 6 + 18 + 54 + 162 is a geometric series with a sum of 242.
  - **Harmonic sequence and series**: A sequence and series where the reciprocal of each term is an arithmetic sequence and series. For example, 1, 1/2, 1/3, 1/4, 1/5 is a harmonic sequence with a common difference of -1/2, and 1 + 1/2 + 1/3 + 1/4 + 1/5 is a harmonic series with a sum of 2.28.



# Convergence of Series

- A series is an expression of the form $\sum_{n=1}^{\infty} a_n = a_1 + a_2 + a_3 + \cdots$, where $a_n$ are the terms of the series.
- A series is convergent if the sequence of its partial sums $S_n = \sum_{k=1}^n a_k$ tends to a limit $L$ as $n$ goes to infinity, that is, $\lim_{n \to \infty} S_n = L$  .
- A series is divergent if the sequence of its partial sums does not tend to any limit, or tends to infinity, as $n$ goes to infinity  .
- The limit $L$ of a convergent series is called the sum of the series, and is denoted by $\sum_{n=1}^{\infty} a_n = L$.
- A series can be convergent or divergent depending on the behavior of its terms $a_n$ as $n$ goes to infinity. There are various tests and criteria to determine the convergence or divergence of a series, such as the nth term test, the comparison test, the ratio test, the root test, the integral test, the alternating series test, and others .
- The convergence or divergence of a series is an important property to study, as it has applications in mathematics, physics, engineering, and other fields. For example, convergent series can be used to approximate functions, solve differential equations, compute integrals, and represent numbers  .



# Tests for convergence of series

A series is a sum of infinitely many terms, such as

$$\sum_{n=1}^{\infty} a_n = a_1 + a_2 + a_3 + \cdots$$

A series is said to converge if the partial sums

$$S_N = \sum_{n=1}^{N} a_n$$

approach a finite limit as $N$ goes to infinity. Otherwise, the series is said to diverge.

There are several tests that can be used to determine whether a series converges or diverges. Some of the most common tests are:

- **The n-th term test**: This test states that if $\lim_{n \to \infty} a_n \neq 0$, then the series $\sum_{n=1}^{\infty} a_n$ diverges. This test can only be used to show divergence, not convergence.
- **The comparison test**: This test compares a given series with another series that is known to converge or diverge. If the given series is smaller than a convergent series, then it also converges. If the given series is larger than a divergent series, then it also diverges.
- **The geometric test**: This test applies to series of the form $\sum_{n=1}^{\infty} ar^n$, where $a$ and $r$ are constants. Such a series converges if and only if $|r| < 1$.
- **The ratio test**: This test uses the limit of the ratio of consecutive terms of the series. If $\lim_{n \to \infty} \left|\frac{a_{n+1}}{a_n}\right| = L$, then the series converges if $L < 1$, diverges if $L > 1$, and the test is inconclusive if $L = 1$.
- **The root test**: This test uses the limit of the n-th root of the n-th term of the series. If $\lim_{n \to \infty} \sqrt[n]{|a_n|} = L$, then the series converges if $L < 1$, diverges if $L > 1$, and the test is inconclusive if $L = 1$.

There are other tests for convergence of series, such as the integral test, the alternating series test, the Leibniz test, the Dirichlet test, and the Cauchy condensation test, but they are beyond the scope of this note. For more details and examples, please refer to the sources     in the search results.



# Ratio Test

The ratio test is a method for testing the convergence of a series of real or complex numbers. It is based on the idea of comparing the ratio of successive terms of the series to a limit value. The test was first published by Jean le Rond d'Alembert and is sometimes known as d'Alembert's ratio test or as the Cauchy ratio test.

## Statement of the test

Let $\sum_{n=1}^{\infty} a_n$ be a series of nonzero terms, and let

$$L = \lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right|$$

be the limit of the ratio of consecutive terms. The ratio test states that:

- If $L < 1$, then the series converges absolutely.
- If $L > 1$, then the series diverges.
- If $L = 1$ or the limit fails to exist, then the test is inconclusive, because there exist both convergent and divergent series that satisfy this case.

## Examples

- The series $\sum_{n=1}^{\infty} \frac{1}{n^2}$ converges by the ratio test, because

$$L = \lim_{n \to \infty} \left| \frac{\frac{1}{(n+1)^2}}{\frac{1}{n^2}} \right| = \lim_{n \to \infty} \left( \frac{n^2}{(n+1)^2} \right) = 1 - \lim_{n \to \infty} \frac{2n+1}{(n+1)^2} = 1 - 0 = 1 < 1$$

- The series $\sum_{n=1}^{\infty} \frac{n!}{n^n}$ converges by the ratio test, because

$$L = \lim_{n \to \infty} \left| \frac{\frac{(n+1)!}{(n+1)^{n+1}}}{\frac{n!}{n^n}} \right| = \lim_{n \to \infty} \left( \frac{n^n}{(n+1)^n} \right) = \lim_{n \to \infty} \left( \frac{1}{(1+\frac{1}{n})^n} \right) = \frac{1}{e} < 1$$

- The series $\sum_{n=1}^{\infty} \frac{1}{n}$ diverges by the ratio test, because

$$L = \lim_{n \to \infty} \left| \frac{\frac{1}{n+1}}{\frac{1}{n}} \right| = \lim_{n \to \infty} \left( \frac{n}{n+1} \right) = 1 - \lim_{n \to \infty} \frac{1}{n+1} = 1 - 0 = 1 = 1$$

- The series $\sum_{n=1}^{\infty} \frac{(-1)^n}{n}$ is inconclusive by the ratio test, because

$$L = \lim_{n \to \infty} \left| \frac{\frac{(-1)^{n+1}}{n+1}}{\frac{(-1)^n}{n}} \right| = \lim_{n \to \infty} \left( \frac{n}{n+1} \right) = 1 - \lim_{n \to \infty} \frac{1}{n+1} = 1 - 0 = 1 = 1$$

However, this series converges by the alternating series test.

## Advantages and disadvantages of the test

The ratio test is useful for testing the convergence of series that involve factorials, exponentials, or powers of n. It is also easy to apply, as it only requires finding the limit of a simple ratio.

However, the ratio test has some limitations. It cannot be used for series that have zero terms, or series that have terms with different signs. It also does not give any information about the rate of convergence or the value of the sum. Moreover, it is often inconclusive when the limit of the ratio is equal to one, which requires using other



# D’ Alembert’s test for convergence of series

- D’ Alembert’s test, also known as the ratio test, is a criterion for the convergence of a series of real or complex numbers, where each term is nonzero when n is large .
- The test was first published by Jean le Rond d'Alembert in 1768.
- The test is based on the limit of the ratio of consecutive terms of the series .
- The test can be stated as follows:

  - Let $\sum_{n=1}^{\infty} a_n$ be a series of real or complex numbers, and let the sequence $a_n$ satisfy: $$\lim_{n \to \infty} \frac{a_{n+1}}{a_n} = L$$
  - If $L > 1$, then the series diverges.
  - If $L < 1$, then the series converges absolutely.
  - If $L = 1$, then the test is inconclusive and the series may converge or diverge.

- The test can be applied to any series of the form $\sum_{n=1}^{\infty} a_n$, where $a_n$ is nonzero for large n, and the limit of the ratio exists or is $\pm \infty$.
- The test can be used to determine the radius of convergence of a power series .
- The test can be modified to handle cases where the limit of the ratio does not exist, by using the limit superior or limit inferior instead.
- The test can be generalized to series of functions, by using uniform convergence instead of absolute convergence.



# Raabe's test

- Raabe's test is a test for the convergence of a series $\sum_{n=1}^{\infty} a_n$ where each term is a real or complex number .
- Raabe's test was developed by Swiss mathematician Joseph Ludwig Raabe.
- Raabe's test is based on the ratio test, which compares the ratio of consecutive terms of a series to a limit.
- Raabe's test uses the following formula to compute the limit:

$$
\lim_{n \to \infty} n \left( \frac{a_n}{a_{n+1}} - 1 \right) = L
$$

- Raabe's test states that:

  - If $L > 1$, the series converges absolutely  .
  - If $L < 1$, the series diverges  .
  - If $L = 1$, the test is inconclusive and another test is needed .

- Raabe's test is easy to use, but not as effective as some other tests, such as Gauss's test, Kummer's test or Maclaurin's integral test.
- Raabe's test can be generalized to the Raabe-Duhamel's test, which uses a different sequence of positive constants .



# Comparison test for the notes of the Unit 3 - Sequence and Series in the subject of ENGINEERING MATHEMATICS-II

- The comparison test is a method to test the convergence or divergence of a series by comparing it to another series whose convergence or divergence is known.
- The comparison test is based on the following principle: if a series of positive terms is smaller than a convergent series, then it also converges; if a series of positive terms is larger than a divergent series, then it also diverges.
- The comparison test can be applied to a series ∑∞n=1an if the terms an are positive and a suitable series ∑∞n=1bn can be found such that an≤bn or an≥bn for all n.
- The comparison test can be stated as follows:

  - If 0≤an≤bn for all n and ∑∞n=1bn converges, then ∑∞n=1an also converges.
  - If 0≤bn≤an for all n and ∑∞n=1bn diverges, then ∑∞n=1an also diverges.

- The comparison test is useful when the series ∑∞n=1an has a similar form to a known series, such as a geometric series or a p-series, which can be used as ∑∞n=1bn.
- The comparison test can be illustrated by the following examples:

  - Example 1: Test the convergence of the series ∑∞n=1(1+1/n)^(n^2)/n!.
    - Solution: We can compare this series to the series ∑∞n=1e^n/n!, where e is the base of the natural logarithm. We know that the latter series converges by the ratio test. To use the comparison test, we need to show that 0≤(1+1/n)^(n^2)/n!≤e^n/n! for all n. This is equivalent to showing that 0≤(1+1/n)^n≤e for all n, which is true by the definition of e as the limit of (1+1/n)^n as n approaches infinity. Therefore, by the comparison test, the series ∑∞n=1(1+1/n)^(n^2)/n! converges.
  - Example 2: Test the convergence of the series ∑∞n=1(1/n)^(1+1/n).
    - Solution: We can compare this series to the series ∑∞n=11/n, which is a harmonic series and diverges. To use the comparison test, we need to show that 0≤1/n≤(1/n)^(1+1/n) for all n. This is equivalent to showing that 0≤n≤n^(1+1/n) for all n, which is true by the property of exponential functions. Therefore, by the comparison test, the series ∑∞n=1(1/n)^(1+1/n) diverges.



# Fourier Series

- A Fourier series is an expansion of a periodic function f(x) in terms of an infinite sum of sines and cosines  .
- Fourier series can be used to represent periodic functions as a linear combination of sine and cosine functions .
- Fourier series make use of the orthogonality relationships of the sine and cosine functions .
- Fourier series are analogous to Taylor series, which represent functions as possibly infinite sums of monomial terms.
- Fourier series are very powerful tools in connection with various problems involving partial differential equations .

## Definition and Formula

- A periodic function f(x) with period T can be expressed as a Fourier series of the form  :

f(x) = a0/2 + sum(n=1 to infinity) [an cos(n pi x/T) + bn sin(n pi x/T)]

- where the coefficients a0, an, and bn are given by the following formulas  :

a0 = (2/T) integral(x=0 to T) f(x) dx

an = (2/T) integral(x=0 to T) f(x) cos(n pi x/T) dx

bn = (2/T) integral(x=0 to T) f(x) sin(n pi x/T) dx

- The term a0/2 is called the constant term or the average value of the function  .
- The terms an cos(n pi x/T) and bn sin(n pi x/T) are called the harmonic terms or the Fourier terms  .
- The number n pi/T is called the frequency or the angular frequency of the harmonic term  .

## Examples

- Example 1: Find the Fourier series of the function f(x) = x defined on the interval [-pi, pi] and extended periodically .

Solution:

- The period of the function is T = 2 pi, so the Fourier series is of the form:

f(x) = a0/2 + sum(n=1 to infinity) [an cos(n x) + bn sin(n x)]

- To find the coefficients, we use the formulas:

a0 = (2/T) integral(x=0 to T) f(x) dx

an = (2/T) integral(x=0 to T) f(x) cos(n pi x/T) dx

bn = (2/T) integral(x=0 to T) f(x) sin(n pi x/T) dx

- Substituting T = 2 pi and f(x) = x, we get:

a0 = (1/pi) integral(x=0 to 2 pi) x dx = (1/pi) [x^2/2] from 0 to 2 pi = 0

an = (1/pi) integral(x=0 to 2 pi) x cos(n x) dx = (1/pi) [x sin(n x)/n - cos(n x)/n^2] from 0 to 2 pi = 0

bn = (1/pi) integral(x=0 to 2 pi) x sin(n x) dx = (1/pi) [-x cos(n x)/n - sin(n x)/n^2] from 0 to 2 pi = -2/n (for n not equal to 0)

- Therefore, the Fourier series is:

f(x) = sum(n=1 to infinity) [-2/n sin(n x)]

- Example 2: Find the Fourier series of the function f(x) = |x| defined on the interval [-pi, pi] and extended periodically .

Solution:

- The period of the function is T = 2 pi, so the Fourier series is of the form:

f(x) = a0/2 + sum(n=1 to infinity) [an cos(n x) + bn sin(n x)]

- To find the coefficients, we use the formulas:

a0 = (2/T) integral(x=0 to T) f(x) dx

an = (2/T) integral(x=0 to T) f(x) cos(n pi x/T) dx

bn = (2/T)



# Half range Fourier sine and cosine series

- A half range Fourier series is a Fourier series that is defined over half the range of the original function, instead of the full range.
- A half range Fourier series can be either a sine series or a cosine series, depending on the symmetry of the function.
- A sine series is a Fourier series that contains only sine terms, and it is used to represent odd functions, which are functions that satisfy f(-x) = -f(x) for all x.
- A cosine series is a Fourier series that contains only cosine terms, and it is used to represent even functions, which are functions that satisfy f(-x) = f(x) for all x.
- To find the half range Fourier series of a function f(x) defined over the interval [0, L], we need to extend the function to the interval [-L, L] in a way that preserves its symmetry. For example, if f(x) is odd, we can extend it as f(x) = -f(-x) for x < 0, and if f(x) is even, we can extend it as f(x) = f(-x) for x < 0.
- The coefficients of the half range Fourier series are given by the following formulas, where n is a positive integer:

  - For the sine series:

    - a0 = 0
    - an = 0
    - bn = (2/L) * integral from 0 to L of f(x) * sin(n * pi * x / L) dx

  - For the cosine series:

    - a0 = (1/L) * integral from 0 to L of f(x) dx
    - an = (2/L) * integral from 0 to L of f(x) * cos(n * pi * x / L) dx
    - bn = 0

- The half range Fourier series of f(x) is then given by the following sums, depending on the type of series:

  - For the sine series:

    - f(x) = sum from n = 1 to infinity of bn * sin(n * pi * x / L)

  - For the cosine series:

    - f(x) = a0 / 2 + sum from n = 1 to infinity of an * cos(n * pi * x / L)

- The half range Fourier series can be used to approximate the function f(x) over the interval [0, L], and to analyze its properties such as periodicity, symmetry, and convergence.



## Unit 4 - Complex Variable–Differentiation

- Complex differentiation is the process of finding the rate of change of a complex-valued function with respect to a complex variable.
- The definition of complex derivative is similar to the derivative of a real function: if f(z) is a complex function, then its derivative at a point z0 is given by

  $$f'(z_0) = \lim_{\Delta z \to 0} \frac{f(z_0 + \Delta z) - f(z_0)}{\Delta z}$$

  if the limit exists and is independent of the direction of approach of $\Delta z$ to zero.
- A complex function that is differentiable at every point in a domain is called holomorphic or analytic in that domain.
- A remarkable feature of complex differentiation is that the existence of one complex derivative automatically implies the existence of infinitely many derivatives, and that the function is equal to its own Taylor series expansion in a neighborhood of any point in the domain.
- A necessary condition for a complex function to be differentiable is that it satisfies the Cauchy-Riemann equations, which are partial differential equations that link the real and imaginary parts of the function . These equations are given by

  $$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \quad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$$

  where $f(z) = u(x,y) + iv(x,y)$ and $z = x + iy$.
- A sufficient condition for a complex function to be differentiable is that it is continuous and satisfies the Cauchy-Riemann equations in a domain.
- Complex differentiation can be used to study various properties of complex functions, such as harmonic functions, conformal mappings, analytic continuation, residues, and contour integration.
- Complex differentiation can also be applied to real-valued functions of a real variable, using a technique called complex step differentiation, which avoids the loss of precision inherent in traditional finite differences. This technique involves evaluating the function at a small imaginary step and taking the imaginary part of the result as an approximation of the derivative. For example, if f(x) is a real function, then

  $$f'(x) \approx \frac{\mathrm{Im}(f(x + ih))}{h}$$

  where h is a small positive number and $\mathrm{Im}$ denotes the imaginary part.



# Functions of complex variable

- A complex function is a function that maps complex numbers to complex numbers.
- A complex number is a number of the form z = x + iy, where x and y are real numbers and i is the imaginary unit, such that i^2 = -1.
- A complex function can be written as w = u + iv, where u and v are real-valued functions of x and y.
- A complex function can also be written as w = f(z), where f is a rule that assigns a complex number w to each complex number z.
- A complex function is said to be differentiable at a point z0 if the limit

$$f'(z_0) = \lim_{z \to z_0} \frac{f(z) - f(z_0)}{z - z_0}$$

exists and is independent of the direction of approach of z to z0.
- A complex function is said to be analytic or holomorphic at a point z0 if it is differentiable at z0 and at every point in some neighborhood of z0.
- A complex function is said to be entire if it is analytic at every point in the complex plane.
- A complex function is said to be meromorphic if it is analytic at every point in the complex plane except for a set of isolated singularities.
- Some examples of complex functions are:

  - The exponential function: $$e^z = e^{x + iy} = e^x (\cos y + i \sin y)$$
  - The trigonometric functions: $$\sin z = \frac{e^{iz} - e^{-iz}}{2i}$$ $$\cos z = \frac{e^{iz} + e^{-iz}}{2}$$
  - The logarithmic function: $$\log z = \log |z| + i \arg z$$ where |z| is the modulus of z and arg z is the principal argument of z, such that -pi < arg z <= pi
  - The power function: $$z^a = |z|^a e^{ia \arg z}$$ where a is any complex number
  - The complex polynomials: $$p(z) = a_0 + a_1 z + a_2 z^2 + ... + a_n z^n$$ where a0, a1, ..., an are complex coefficients
  - The rational functions: $$r(z) = \frac{p(z)}{q(z)}$$ where p and q are complex polynomials and q(z) != 0 for all z in the domain of r
- Some properties of complex functions are:

  - The sum, difference, product, and quotient of two complex functions are also complex functions, provided that the quotient is well-defined.
  - The composition of two complex functions is also a complex function, provided that the domain and range of the functions are compatible.
  - The derivative of a complex function is also a complex function, provided that the function is differentiable.
  - The derivative of a complex function satisfies the Cauchy-Riemann equations, which are necessary and sufficient conditions for analyticity. The Cauchy-Riemann equations are:

$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}$$

$$\frac{\partial u}{\partial y} = - \frac{\partial v}{\partial x}$$

  - The derivative of a complex function satisfies the chain rule, the product rule, and the quotient rule, which are similar to the rules for real functions. The chain rule is:

$$\frac{d}{dz} f(g(z)) = f'(g(z)) g'(z)$$

The product rule is:

$$\frac{d}{dz} (f(z) g(z)) = f'(z) g(z) + f(z) g'(z)$$

The quotient rule is:

$$\frac{d}{dz} \frac{f(z)}{g(z)} = \frac{f'(z) g(z) - f(z) g'(z)}{g(z)^2}$$

  - The derivative of a complex function satisfies the Cauchy integral formula, which relates the value of a function at a point to the values of the function on a closed contour around the point[^3



# Unit 4 - Complex Variable–Differentiation

- Complex differentiation is the study of how complex functions change with respect to complex variables.
- A complex function is a function that maps complex numbers to complex numbers, such as f(z) = z^2 + 2z + 1, where z is a complex variable.
- A complex variable is a variable that can take on complex values, such as z = x + iy, where x and y are real variables and i is the imaginary unit.
- A complex function can be written in terms of its real and imaginary parts, such as f(z) = u(x,y) + iv(x,y), where u and v are real functions of two real variables.
- A complex function is said to be differentiable at a point z if the limit

  `f'(z) = lim_(h->0) (f(z+h) - f(z))/h`

  exists and is independent of the direction of h, where h is a complex number.
- A complex function is said to be analytic or holomorphic at a point z if it is differentiable at z and at every point in some neighborhood of z.
- A complex function is said to be entire if it is analytic at every point in the complex plane.
- A complex function is said to be meromorphic if it is analytic except at isolated points, called poles, where it has a certain type of singularity.
- A key result in complex differentiation is the Cauchy-Riemann equations, which state that a complex function f(z) = u(x,y) + iv(x,y) is differentiable at a point z = x + iy if and only if

  `u_x = v_y` and `u_y = -v_x`

  where the subscripts denote partial derivatives.
- The Cauchy-Riemann equations link the real and imaginary parts of a complex function and show that complex differentiation is more restrictive than real differentiation.
- Another important result in complex differentiation is the Cauchy integral formula, which states that if f is a holomorphic function inside and on a simple closed contour C, and z is any point inside C, then

  `f(z) = (1/(2pi i)) int_C (f(w)/(w-z)) dw`

  where i is the imaginary unit and dw is the differential along C.
- The Cauchy integral formula allows us to compute the value of a holomorphic function at any point inside a contour by using the values of the function on the contour and the complex variable w.
- The Cauchy integral formula also implies that a holomorphic function is infinitely differentiable and equal to its own Taylor series, which is a power series expansion of the form

  `f(z) = sum_(n=0)^infty a_n (z-z_0)^n`

  where z_0 is a fixed point and a_n are the coefficients given by

  `a_n = (f^(n)(z_0))/(n!)`

  where f^(n) denotes the nth derivative of f.
- Complex differentiation is the basis of complex analysis, which is the study of the properties and applications of complex functions. Complex analysis has many applications in mathematics, physics, engineering, and other fields.



# Continuity and Differentiability of Complex Functions

- A complex function is a function that maps complex numbers to complex numbers, such as f(z) = z^2 + 1.
- A complex function is continuous at a point z_0 if the limit of the function as z approaches z_0 is equal to the value of the function at z_0, i.e., lim_(z->z_0) f(z) = f(z_0) .
- A complex function is differentiable at a point z_0 if the limit of the difference quotient as h approaches zero exists and is finite, i.e., lim_(h->0) (f(z_0 + h) - f(z_0))/h exists and is finite .
- The derivative of a complex function f(z) at a point z_0 is denoted by f'(z_0) and is equal to the value of the limit of the difference quotient, i.e., f'(z_0) = lim_(h->0) (f(z_0 + h) - f(z_0))/h .
- A complex function is said to be analytic or holomorphic at a point z_0 if it is differentiable at z_0 and in some neighborhood of z_0 .
- A complex function is said to be entire if it is analytic in the whole complex plane .
- A complex function is said to be smooth or infinitely differentiable if it has derivatives of all orders at every point in its domain .
- Some examples of complex functions and their continuity and differentiability are:

  - f(z) = z is continuous and differentiable at every point in the complex plane, and f'(z) = 1 for all z .
  - f(z) = z^2 is continuous and differentiable at every point in the complex plane, and f'(z) = 2z for all z .
  - f(z) = |z| is continuous at every point in the complex plane, but not differentiable at any point, since the limit of the difference quotient does not exist .
  - f(z) = e^z is continuous and differentiable at every point in the complex plane, and f'(z) = e^z for all z. It is also entire and smooth .
  - f(z) = 1/z is continuous and differentiable at every point in the complex plane except z = 0, where it is undefined. It is also analytic in the complex plane except z = 0 .



# Analytic functions

- A function f(z) of a complex variable z is **analytic** if it has a complex derivative f'(z) at every point in its domain .
- A complex derivative f'(z) is defined as the limit of the difference quotient f(z+h)-f(z)/h as h approaches zero, where h is a complex number.
- A function f(z) is analytic if and only if it is **holomorphic**, i.e. it is complex differentiable.
- A function f(z) is analytic if and only if its **Taylor series** about z0 converges to the function in some neighborhood for every z0 in its domain.
- Analytic functions have many properties that do not generally hold for real differentiable functions, such as the **Cauchy-Riemann equations**, the **Cauchy integral formula**, and the **maximum modulus principle** .
- Analytic functions are also called **regular functions** or **differentiable functions**.



# Cauchy-Riemann equations (Cartesian and Polar form)

- The Cauchy-Riemann equations are a system of two partial differential equations that form a necessary and sufficient condition for a complex function to be holomorphic (complex differentiable) .
- A complex function f(z) = u(x, y) + iv(x, y) is holomorphic if and only if it satisfies the Cauchy-Riemann equations in Cartesian form:
  - (1a) ∂u/∂x = ∂v/∂y
  - (1b) ∂u/∂y = -∂v/∂x
- The Cauchy-Riemann equations can also be written in polar form, using the polar coordinates z = r(cos θ + i sin θ) and f(z) = U(r, θ) + iV(r, θ):
  - (2a) ∂U/∂r = (1/r) ∂V/∂θ
  - (2b) ∂V/∂r = -(1/r) ∂U/∂θ
- The Cauchy-Riemann equations allow us to check if a complex function has a complex derivative and to compute that derivative .
- If f(z) = u(x, y) + iv(x, y) is holomorphic, then its complex derivative is given by:
  - f'(z) = ∂u/∂x + i ∂v/∂x = ∂v/∂y - i ∂u/∂y
- If f(z) = U(r, θ) + iV(r, θ) is holomorphic, then its complex derivative is given by:
  - f'(z) = e^(-iθ) (∂U/∂r + i ∂V/∂r) = (1/r) e^(-iθ) (∂V/∂θ - i ∂U/∂θ)
- The Cauchy-Riemann equations are useful for proving many properties and theorems in complex analysis, such as the Cauchy integral formula, the Cauchy integral theorem, and the maximum modulus principle .



# Harmonic Function for the Notes of the Unit 4 - Complex Variable–Differentiation in the Subject of Engineering Mathematics-II

- A harmonic function is a function that satisfies Laplace's equation, which is a partial differential equation of the form: ∇^2 u = u_xx + u_yy = 0  .
- Laplace's equation arises in many physical problems, such as heat conduction, electrostatics, fluid flow, etc.
- A harmonic function is twice continuously differentiable and can be locally expressed as a power series.
- A harmonic function is also the real or imaginary part of a holomorphic function, which is a complex-valued function that is differentiable in a complex domain  .
- A holomorphic function can be written as f(z) = u(x,y) + iv(x,y), where z = x + iy is a complex variable, and u and v are real-valued functions of x and y.
- If f(z) is holomorphic in a region A, then both u and v are harmonic in A, and they satisfy the Cauchy-Riemann equations: u_x = v_y and u_y = -v_x  .
- Conversely, if u(x,y) is harmonic in a connected region A, then there exists a holomorphic function f(z) = u(x,y) + iv(x,y) such that u is the real part of f  . The function v is called a harmonic conjugate of u, and it can be found by integrating the Cauchy-Riemann equations.
- Some examples of harmonic functions are: u(x,y) = x, u(x,y) = y, u(x,y) = e^x cos y, u(x,y) = ln(x^2 + y^2), etc. These are also the real parts of the holomorphic functions f(z) = z, f(z) = iz, f(z) = e^z, f(z) = ln z, etc. respectively .
- Some properties of harmonic functions are: 
  - They satisfy the mean value property, which states that the value of a harmonic function at a point is equal to the average of its values on a circle centered at that point .
  - They satisfy the maximum principle, which states that a harmonic function cannot have a local maximum or minimum in the interior of its domain, unless it is constant .
  - They satisfy the uniqueness theorem, which states that a harmonic function is uniquely determined by its values on the boundary of its domain, if it exists .
  - They are orthogonal to their harmonic conjugates, which means that the integral of their product over a closed curve is zero.
  - They can be represented by harmonic polynomials, which are linear combinations of monomials of the form x^m y^n, where m and n are non-negative integers and m - n is even.



# Method to find Analytic functions for the notes of the Unit 4 - Complex Variable–Differentiation in the subject of ENGINEERING MATHEMATICS-II

- A function of a complex variable is said to be **analytic** in a region of the complex plane if it has a derivative at each point of the region and if it is single valued.
- A function of a complex variable is also called **holomorphic** or **complex analytic** if it is analytic in the whole complex plane or in an open subset of it .
- A function of a complex variable can be represented by a **power series** in the variable around any point in its domain of analyticity.
- To find if a function of a complex variable is analytic, one can use the following methods:
  - **Cauchy-Riemann equations**: These are two partial differential equations that relate the real and imaginary parts of a complex function. If a function satisfies these equations in a region, then it is analytic in that region.
  - **Harmonic functions**: These are real-valued functions that satisfy Laplace's equation, which is a second-order partial differential equation. If the real and imaginary parts of a complex function are both harmonic in a region, then the function is analytic in that region.
  - **Conformal mapping**: This is a transformation that preserves angles and shapes locally. If a function is analytic in a region, then it is a conformal mapping in that region, except at the points where its derivative is zero.
  - **Integration**: This is a method of finding the value of a complex function by integrating along a path in the complex plane. If a function is analytic in a simply connected region, then its value at any point in the region depends only on the value at a fixed point and the path of integration.



# Milne's Thompson Method for the notes of the Unit 4 - Complex Variable–Differentiation in the subject of ENGINEERING MATHEMATICS-II

- Milne's Thompson method is a technique to find an analytic function $f(z)$ from its real or imaginary part, when the latter is given as an analytic expression in terms of $x$ and $y$.
- The method is based on the following theorem :

> If $f(z) = u(x,y) + iv(x,y)$ is an analytic function in a domain $D$, then $\overline{f(\overline{z})} = u(x,-y) - iv(x,-y)$ is also an analytic function in $D$.

- The theorem implies that if we know $u(x,y)$, we can find $v(x,y)$ by the following steps:
  - Replace $y$ by $-y$ in $u(x,y)$ to get $u(x,-y)$.
  - Find an analytic function $g(z)$ such that $g(z) = u(x,-y) + iv(x,-y)$ in $D$.
  - Then $f(z) = u(x,y) + iv(x,y) = \overline{g(\overline{z})}$ in $D$.
- Similarly, if we know $v(x,y)$, we can find $u(x,y)$ by the following steps:
  - Replace $y$ by $-y$ in $v(x,y)$ to get $v(x,-y)$.
  - Find an analytic function $g(z)$ such that $g(z) = u(x,-y) + iv(x,-y)$ in $D$.
  - Then $f(z) = u(x,y) + iv(x,y) = g(z) - iv(x,-y)$ in $D$.
- The method can be applied to different cases depending on the form of $u(x,y)$ or $v(x,y)$. Some examples are :
  - Case I: $u(x,y)$ or $v(x,y)$ is a polynomial in $x$ and $y$.
  - Case II: $u(x,y)$ or $v(x,y)$ is a rational function in $x$ and $y$.
  - Case III: $u(x,y)$ or $v(x,y)$ is a function of $x^2 + y^2$ and $x^2 - y^2$.
  - Case IV: $u(x,y)$ or $v(x,y)$ is a function of $x^2 + y^2$ and $xy$.
  - Case V: $u(x,y)$ or $v(x,y)$ is a function of $e^{x+iy}$ and $e^{x-iy}$.
- The method can also be used to find the complex potential of a flow with no rigid boundaries, no singularities inside $|z|=a$, when introducing the solid cylinder $|z|=a$, by the formula:

$$w(z) = f(z) + \overline{f\left(\frac{a^2}{z}\right)}$$

for $|z| \geq a$.



# Conformal Mapping

- A conformal mapping is a function that preserves the angles and orientations of curves in the complex plane.
- A conformal mapping is also called a conformal map, conformal transformation, angle-preserving transformation, or biholomorphic map .
- A complex function is conformal at any point where it is analytic and has a nonzero derivative .
- A conformal mapping can be used to transform simple harmonic solutions into those applicable to more complicated shapes.
- Some examples of conformal mappings are the identity function, the exponential function, the logarithmic function, and the Möbius transformation.
- A conformal mapping can be visualized as a mapping that does not distort the shape of infinitesimal circles.



# Mobius transformation and their properties

A Mobius transformation is a function of the form

$$f(z) = \frac{az + b}{cz + d}$$

where $a, b, c, d$ are complex numbers and $ad - bc \neq 0$.

A Mobius transformation maps the extended complex plane $\hat{\mathbb{C}} = \mathbb{C} \cup \{\infty\}$ to itself. It is also called a fractional linear transformation or a linear fractional transformation.

Some properties of Mobius transformations are:

- A Mobius transformation is a composition of four elementary maps, namely translations, dilations, rotations, and inversions. Translations: $z \to z + z_0$ such that $z_0 \in \mathbb{C}$. Dilations: $z \to \lambda z$; $\lambda > 0$ and $\lambda \in \mathbb{R}$. Rotations: $z \to e^{i\theta} z$; $\theta \in \mathbb{R}$. Inversions: $z \to 1/z$.
- A Mobius transformation is conformal, meaning that it preserves angles and orientation locally.
- A Mobius transformation is one-to-one and onto, meaning that it is invertible and its inverse is also a Mobius transformation.
- A Mobius transformation maps circles and lines to circles and lines. More precisely, it maps generalized circles, which are circles or lines, to generalized circles. The inverse image of a generalized circle under a Mobius transformation is also a generalized circle.
- A Mobius transformation is completely determined by any three input-output pairs. This means that for any triple of distinct input values $z_1, z_2, z_3$ in $\hat{\mathbb{C}}$ and any triple of distinct output values $w_1, w_2, w_3$ in $\hat{\mathbb{C}}$, there is a unique $T \in M$ such that $Tz_i = w_i$ for $i = 1, 2, 3$.
- A Mobius transformation preserves the cross ratio of four points, which is defined as

$$[z_1, z_2, z_3, z_4] = \frac{(z_1 - z_3)(z_2 - z_4)}{(z_1 - z_4)(z_2 - z_3)}$$

This means that for any four points $z_1, z_2, z_3, z_4$ in $\hat{\mathbb{C}}$ and any Mobius transformation $T$, we have

$$[Tz_1, Tz_2, Tz_3, Tz_4] = [z_1, z_2, z_3, z_4]$$

- The Mobius transformations form a group called the Mobius group, which is the projective linear group $PGL(2, \mathbb{C})$. This means that the composition of two Mobius transformations is also a Mobius transformation, the identity function is a Mobius transformation, and every Mobius transformation has an inverse that is also a Mobius transformation. The Mobius group is isomorphic to the group of orientation-preserving isometries of the hyperbolic plane.



## Unit 5 - Complex Variable –Integration

- Complex integration is the process of finding the value of a complex function along a curve or a contour in the complex plane.
- The curve or contour can be either closed or open, and can be oriented in either direction.
- The basic formula for complex integration is:

$$\int_C f(z) dz = \int_a^b f(z(t)) z'(t) dt$$

where $C$ is the curve or contour, $f(z)$ is the complex function, $z(t)$ is the parametric representation of the curve, and $z'(t)$ is the derivative of $z(t)$ with respect to $t$.

- Some properties of complex integration are:

  - Linearity: $\int_C (af(z) + bg(z)) dz = a \int_C f(z) dz + b \int_C g(z) dz$, where $a$ and $b$ are constants.
  - Additivity: $\int_C f(z) dz = \int_{C_1} f(z) dz + \int_{C_2} f(z) dz$, where $C_1$ and $C_2$ are two subcontours of $C$.
  - Independence of path: $\int_C f(z) dz$ is the same for any two curves $C_1$ and $C_2$ that have the same endpoints and lie in the same domain where $f(z)$ is analytic (i.e., has a derivative at every point).
  - Cauchy's integral theorem: If $f(z)$ is analytic in a simply connected domain $D$, then $\int_C f(z) dz = 0$ for any closed contour $C$ in $D$.
  - Cauchy's integral formula: If $f(z)$ is analytic in a simply connected domain $D$, and $C$ is a positively oriented simple closed contour in $D$ that encloses a point $z_0$, then $f(z_0) = \frac{1}{2\pi i} \int_C \frac{f(z)}{z-z_0} dz$.
  - Residue theorem: If $f(z)$ is analytic in a simply connected domain $D$ except for a finite number of isolated singularities, and $C$ is a positively oriented simple closed contour in $D$ that encloses all the singularities, then $\int_C f(z) dz = 2\pi i \sum_{k=1}^n \text{Res}(f, z_k)$, where $\text{Res}(f, z_k)$ is the residue of $f(z)$ at the singularity $z_k$.

- Some applications of complex integration are:

  - Evaluating real integrals using contour integration, such as $\int_{-\infty}^{\infty} \frac{p(x)}{q(x)} dx$, where $p(x)$ and $q(x)$ are polynomials and $q(x)$ has no real roots.
  - Solving boundary value problems in potential theory, such as Laplace's equation, using the method of conformal mapping, which transforms a complex domain into a simpler one where the solution can be found easily.
  - Computing Fourier and Laplace transforms of complex functions using contour integration, such as $\mathcal{F}(f)(\omega) = \int_{-\infty}^{\infty} f(t) e^{-i\omega t} dt$ and $\mathcal{L}(f)(s) = \int_{0}^{\infty} f(t) e^{-st} dt$, where $f(t)$ is a complex function of a real variable $t$.
  - Finding the zeros and poles of complex functions using the argument principle, which relates the change in the argument of a function along a contour to the number of zeros and poles inside the contour.
  - Studying the asymptotic behavior of complex functions using the method of steepest descent, which approximates the integral of a function along a contour by the value of the function at the saddle point of the contour.



# Complex integration

Complex integration is a generalization of real integration to the complex domain. It is useful for studying analytic functions, which are complex functions that are differentiable in some domain. Complex integration also has applications in physics, engineering, and other fields.

Some of the topics covered in complex integration are:

- Complex line integrals: These are integrals of complex functions along a curve in the complex plane. They depend on the function and the path, but not on the parametrization of the path. They can be computed using the parametric form of the function and the path, or using the Cauchy integral formula if the function is analytic and the path is a closed contour.
- Cauchy integral formula: This is a fundamental result of complex analysis that relates the value of an analytic function at a point inside a closed contour to the integral of the function along the contour. It also implies that an analytic function has infinitely many derivatives and that they can be obtained by differentiating the integral formula.
- Cauchy integral theorem: This is a special case of the Cauchy integral formula that states that the integral of an analytic function along a closed contour is zero. It also implies that the value of an analytic function is independent of the path between two points in the same domain.
- Residue theorem: This is a powerful tool for evaluating complex integrals that involve singularities, which are points where the function is not defined or not analytic. The residue theorem states that the integral of a function along a closed contour that encloses some singularities is equal to 2πi times the sum of the residues of the function at those singularities. The residue of a function at a singularity is a constant that depends on the type and order of the singularity and can be computed using various methods.
- Applications of complex integration: Some of the applications of complex integration include evaluating real integrals using contour integration, finding the inverse Laplace transform of a function, solving differential equations using the method of complex variables, calculating the electric potential and the magnetic field using complex potentials, and deriving the Fourier and Laurent series of a function.



# Cauchy- Integral theorem

- The Cauchy- Integral theorem is a fundamental result in complex analysis that relates the line integral of a holomorphic function over a closed curve to the values of the function inside the curve.
- The theorem states that if f(z) is a holomorphic function defined on a simply connected domain D, and C is a piecewise smooth, simple closed curve in D, then

$$\oint_C f(z) dz = 0$$

- This means that the line integral of f(z) over C does not depend on the choice of C, as long as C is contained in D and does not enclose any singularities of f(z).
- The theorem can be generalized to multiply connected domains by using the concept of homology, which measures the number of times a curve winds around the holes in the domain.
- The theorem can also be extended to higher dimensions by using the Cauchy integral formula, which gives an expression for the value of f(z) at any point inside C in terms of the integral of f(z) over C.
- The Cauchy integral formula also implies that f(z) is infinitely differentiable and that its derivatives can be computed by differentiating under the integral sign.
- The Cauchy integral theorem and formula are powerful tools for studying the properties of holomorphic functions, such as their Taylor and Laurent series expansions, their residues and poles, and their conformal mappings .



# Cauchy Integral Formula

- The Cauchy integral formula is a fundamental result in complex analysis that relates the value of a holomorphic function at a point to its values on a circle around that point.
- The formula can be stated as follows: if f(z) is a holomorphic function on a domain U and γ is a positively oriented simple closed contour in U that encloses a point z_0, then

  f(z_0) = \frac{1}{2\pi i} \oint_\gamma \frac{f(z)}{z-z_0} dz

- The formula can be proved using the Cauchy-Goursat theorem, which says that the integral of a holomorphic function over a simple closed contour is zero, and the residue theorem, which says that the integral of a function with a simple pole at z_0 over a circle around z_0 is equal to 2\pi i times the residue of the function at z_0.
- The Cauchy integral formula has several important consequences and applications, such as:

  - It implies that holomorphic functions are infinitely differentiable and analytic, meaning that they can be expressed as power series around any point in their domain.
  - It provides a formula for the derivatives of a holomorphic function, namely

    f^{(n)}(z_0) = \frac{n!}{2\pi i} \oint_\gamma \frac{f(z)}{(z-z_0)^{n+1}} dz

    for any positive integer n.
  - It allows us to evaluate integrals of holomorphic functions over simple closed contours using the values of the function at the interior points, without knowing the function explicitly.
  - It enables us to define the concept of a harmonic function, which is a real-valued function that satisfies Laplace's equation, as the real or imaginary part of a holomorphic function.



# Taylor's and Laurent's series

- A **power series** is a series of the form

$$\sum_{n=0}^{\infty} a_n (z-z_0)^n$$

where $a_n$ are complex coefficients and $z_0$ is a complex number.

- A power series with non-negative power terms is called a **Taylor series**. A Taylor series represents a complex function $f(z)$ that is analytic in a disk around $z_0$ as

$$f(z) = \sum_{n=0}^{\infty} \frac{f^{(n)}(z_0)}{n!} (z-z_0)^n$$

where $f^{(n)}(z_0)$ denotes the $n$-th derivative of $f(z)$ at $z_0$.

- A power series with both positive and negative power terms is called a **Laurent series**. A Laurent series represents a complex function $f(z)$ that is analytic in an annulus around $z_0$ as

$$f(z) = \sum_{n=-\infty}^{\infty} a_n (z-z_0)^n$$

where $a_n$ are complex coefficients that can be obtained by integrating $f(z)$ along a closed contour in the annulus.

- A Laurent series can be used to express complex functions in cases where a Taylor series expansion cannot be applied, such as when the function has singularities or is not analytic at a point.

- A Laurent series can be split into two parts: the **principal part** and the **analytic part**. The principal part consists of the terms with negative powers of $(z-z_0)$ and the analytic part consists of the terms with non-negative powers of $(z-z_0)$. The principal part is also called the **singular part** because it reflects the behavior of the function near the singularity at $z_0$.

- The **order** of a singularity at $z_0$ is the largest positive integer $m$ such that the coefficient $a_{-m}$ in the Laurent series is nonzero. The order of a singularity indicates how fast the function diverges near the singularity.

- A singularity at $z_0$ is called **isolated** if there is a disk around $z_0$ that contains no other singularities of the function. A singularity at $z_0$ is called **removable** if the function can be defined at $z_0$ in such a way that it becomes analytic in a disk around $z_0$. A removable singularity has a Laurent series with only the analytic part.

- A singularity at $z_0$ is called a **pole** if it is isolated and has a finite order. A pole of order $m$ has a Laurent series with a principal part of the form

$$\sum_{n=1}^{m} \frac{a_{-n}}{(z-z_0)^n}$$

where $a_{-m} \neq 0$. A pole of order $1$ is also called a **simple pole**.

- A singularity at $z_0$ is called **essential** if it is isolated and has an infinite order. An essential singularity has a Laurent series with an infinite number of nonzero terms in the principal part. An essential singularity has a very erratic behavior near $z_0$ and cannot be approximated by a polynomial or a rational function.



# Singularities and its classification for the notes of the Unit 5 - Complex Variable –Integration in the subject of ENGINEERING MATHEMATICS-II

- A **singularity** of a complex function is a point where the function fails to be analytic.
- A function is **analytic** if it is complex differentiable in an open set.
- A function is **complex differentiable** if it satisfies the Cauchy-Riemann equations and has a well-defined derivative.
- There are different types of singularities, depending on the behavior of the function near the point.
- The main types of singularities are:
  - **Isolated singularities**: These are points where the function is analytic in a punctured disk around the point, i.e., there is a positive radius such that the function is analytic in the disk with the point removed.
  - **Nonisolated singularities**: These are points where the function is not analytic in any punctured disk around the point, i.e., there is no positive radius such that the function is analytic in the disk with the point removed.
  - **Branch points**: These are points where the function is multivalued and has different branches in a neighborhood of the point.
- Isolated singularities can be further classified into three subtypes:
  - **Removable singularities**: These are points where the function has a finite limit as the variable approaches the point, i.e., the function can be extended to a continuous and analytic function at the point by defining the value of the function to be the limit.
  - **Poles**: These are points where the function has an infinite limit as the variable approaches the point, i.e., the function can be written as a quotient of two analytic functions, where the denominator has a zero of finite order at the point.
  - **Essential singularities**: These are points where the function has no finite or infinite limit as the variable approaches the point, i.e., the function has an infinite number of terms with negative powers in its Laurent series expansion around the point.
- The **Laurent series** of a function is a generalization of the Taylor series that allows negative powers of the variable.
- The **principal part** of the Laurent series is the sum of the terms with negative powers.
- The **residue** of a function at an isolated singularity is the coefficient of the term with power -1 in the Laurent series.
- The **residue theorem** states that the integral of a function over a closed contour that encloses an isolated singularity is equal to 2πi times the residue of the function at that point.
- The residue theorem can be used to evaluate complex integrals that involve singularities, by choosing a suitable contour and applying the Cauchy integral formula.
- The **Cauchy integral formula** states that the value of a function at a point inside a closed contour is equal to the integral of the function over the contour divided by 2πi times the difference between the variable and the point.

: Singularity -- from Wolfram MathWorld
: Complex Analysis
: Singularity (mathematics) - Wikipedia
: Complex integration using singularities - Mathematics Stack Exchange
: Introduction to Complex Variables and Applications
: Complex integration - University of Arizona



# Zeros of Analytic Functions

- An analytic function is a complex function that is differentiable at every point of its domain.
- A zero of an analytic function is a point where the function vanishes, or its value becomes zero.
- Zeros of analytic functions have the following properties   :
  - Zeros of analytic functions are isolated, meaning that if a function has a zero at a point, then there is a neighborhood around that point where the function has no other zeros.
  - Zeros of analytic functions have a multiplicity, meaning that if a function has a zero of order m at a point, then the function can be written as a product of a power of a linear factor and another analytic function that is nonzero at that point.
  - Zeros of analytic functions are counted by the argument principle, meaning that the number of zeros of a function inside a simple closed contour is equal to the change in the argument of the function divided by 2π as the contour is traversed once in the positive direction.
  - Zeros of analytic functions are related to the Taylor series of the function, meaning that the coefficients of the Taylor series at a point are determined by the derivatives of the function at that point, and vice versa.
  - Zeros of analytic functions are preserved by analytic continuation, meaning that if two analytic functions agree on a subset of their domains, then they have the same zeros on their entire domains.



# Residues

- A residue is a complex number that measures the behavior of a meromorphic function near a singularity.
- A meromorphic function is a function that is analytic everywhere except at a finite number of isolated singularities.
- A singularity is a point where a function is not defined or not analytic.
- A residue can be computed from the Laurent series expansion of the function around the singularity.
- A Laurent series is a generalization of a Taylor series that allows negative powers of z.
- The residue is the coefficient of the term with power -1 in the Laurent series.
- The residue can also be computed from the Cauchy residue theorem, which relates the contour integral of a function around a closed curve to the sum of the residues inside the curve .
- The Cauchy residue theorem is a powerful tool for evaluating real or complex integrals that involve rational functions, trigonometric functions, exponential functions, etc.
- The residue can also be used to find the behavior of a function at infinity by considering a large circle as the contour and applying the residue theorem.
- The residue at infinity is the negative of the coefficient of the term with power 1 in the Laurent series at infinity.



# Cauchy's Residue Theorem and its Application

- Cauchy's residue theorem is a powerful tool to evaluate line integrals of analytic functions over closed curves.
- It can often be used to compute real integrals and infinite series as well.
- It generalizes the Cauchy integral theorem and Cauchy's integral formula.
- The theorem states that if f(z) is analytic in a region A except for a set of isolated singularities, and C is a simple closed curve in A that does not go through any of the singularities of f and is oriented counterclockwise, then

$$\oint_C f(z) dz = 2\pi i \sum_{k=1}^n \text{Res}_{z=z_k} f(z)$$

where $z_k$ are the singularities of f inside C, and $\text{Res}_{z=z_k} f(z)$ is the residue of f at $z_k$  .

- The residue of f at a singularity $z_0$ is the coefficient of $(z-z_0)^{-1}$ in the Laurent series expansion of f around $z_0$ .
- The residue can be computed by various methods, such as the limit formula, the Cauchy's integral formula, or the residue at infinity.
- The residue theorem can be applied to evaluate real integrals and infinite series by using contour integration techniques, such as choosing suitable contours, using Jordan's lemma, or using the method of indented paths.
- Some examples of applications of the residue theorem are:

  - Computing the inverse Laplace transform of a function.
  - Computing the inverse Fourier transform of a function.
  - Computing the value of $\pi$ and other constants.
  - Computing the number of zeros of a function inside a region.
  - Solving differential equations with constant coefficients.

