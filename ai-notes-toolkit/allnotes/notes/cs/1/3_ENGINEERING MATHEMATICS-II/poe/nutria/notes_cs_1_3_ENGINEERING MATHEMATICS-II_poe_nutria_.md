


# ENGINEERING MATHEMATICS-II

* Vector Calculus: This includes topics such as divergence, curl, and Green's theorem.
* Complex Analysis: This includes topics such as Cauchy's theorem, Laurent series, and contour integration.
* Fourier Analysis: This includes topics such as Fourier series and Fourier transforms.
* Numerical Analysis: This includes topics such as numerical integration and numerical solution of differential equations.
* Probability and Statistics: This includes topics such as probability distributions, random variables, and statistical analysis.
* Optimization: This includes topics such as linear programming, convex optimization, and nonlinear optimization.




## Unit 1 - Ordinary Differential Equation of Higher Order

* Ordinary Differential Equations (ODEs) are equations that involve derivatives of a single variable. 
* ODEs of order n are equations that contain nth derivatives of a single variable. 
* An nth order ODE can be written as: 
$$a_n \frac{d^ny}{dx^n} + a_{n-1} \frac{d^{n-1}y}{dx^{n-1}} + \cdots + a_1 \frac{dy}{dx} + a_0 y = f(x)$$
* ODEs of order n can be reduced to a system of first order ODEs by introducing n-1 auxiliary variables.
* Solutions to ODEs can be found using analytical methods such as separation of variables and Laplace transforms, or numerical methods such as Euler's method, Runge-Kutta methods, and the shooting method.




### Linear differential equation of nth order with constant coefficients

A linear differential equation of nth order with constant coefficients is an equation of the form:

$$a_n \frac{d^ny}{dx^n} + a_{n-1}\frac{d^{n-1}y}{dx^{n-1}} + \dots + a_1 \frac{dy}{dx} + a_0y = g(x)$$

where $a_n, a_{n-1}, \dots, a_1, a_0$ are constants and $g(x)$ is a given function of $x$.

The general solution of this equation can be expressed as a linear combination of $n$ linearly independent solutions of the homogeneous equation:

$$a_n \frac{d^ny}{dx^n} + a_{n-1}\frac{d^{n-1}y}{dx^{n-1}} + \dots + a_1 \frac{dy}{dx} + a_0y = 0$$

The homogeneous equation can be solved using the method of undetermined coefficients. The general solution of the homogeneous equation is given by:

$$y = c_1y_1 + c_2y_2 + \dots + c_ny_n$$

where $y_1, y_2, \dots, y_n$ are the $n$ linearly independent solutions of the homogeneous equation and $c_1, c_2, \dots, c_n$ are arbitrary constants.

The particular solution of the non-homogeneous equation can be obtained by the method of variation of parameters. The particular solution of the non-homogeneous equation is given by:

$$y_p = y_1u_1 + y_2u_2 + \dots + y_nu_n$$

where $u_1, u_2, \dots, u_n$ are the solutions of the system of $n$ linear equations:

$$\begin{cases}
  a_n \frac{d^ny_1}{dx^n} + a_{n-1}\frac{d^{n-1}y_1}{dx^{n-1}} + \dots + a_1 \frac{dy_1}{dx} + a_0y_1 = g(x) \\
  a_n \frac{d^ny_2}{dx^n} + a_{n-1}\frac{d^{n-1}y_2}{dx^{n-1}} + \dots + a_1 \frac{dy_2}{dx} + a_0y_2 = 0 \\
  \vdots \\
  a_n \frac{d^ny_n}{dx^n} + a_{n-1}\frac{d^{n-1}y_n}{dx^{n-1}} + \dots + a_1 \frac{dy_n}{dx} + a_0y_n = 0
\end{cases}$$

The general solution of the non-homogeneous equation is given by:

$$y = c_1y_1 + c_2y_2 + \dots + c_ny_n + y_p$$




### Simultaneous linear differential equations for the notes of the Unit 1 - Ordinary Differential Equation of Higher Order in the subject of ENGINEERING MATHEMATICS-II

1. A simultaneous linear differential equation is a system of two or more linear differential equations with the same set of independent variables. 
2. The general form of a simultaneous linear differential equation is given by: 
    $$a_1(x,y) \frac{dy}{dx} + a_2(x,y)y = f(x)$$
    $$b_1(x,y) \frac{dy}{dx} + b_2(x,y)y = g(x)$$
3. The order of a simultaneous linear differential equation is the highest order of the derivatives of the dependent variables appearing in the equation. 
4. The degree of a simultaneous linear differential equation is the highest power of the derivatives of the dependent variables appearing in the equation.
5. The solution of a simultaneous linear differential equation can be obtained by solving a system of linear equations.
6. The solution of a simultaneous linear differential equation can also be obtained by using the method of undetermined coefficients.
7. The solution of a simultaneous linear differential equation can also be obtained by using the method of variation of parameters.




### Second order linear differential equations with variable coefficients

* A second order linear differential equation with variable coefficients is an equation of the form $$a_2\frac{d^2y}{dx^2} + a_1\frac{dy}{dx} + a_0y = f(x)$$
* The coefficients $a_2, a_1, a_0$ and $f(x)$ are all functions of the independent variable $x$.
* The general solution of a second order linear differential equation with variable coefficients can be found using the method of variation of parameters.
* The solution is given by $$y=y_c + y_p$$ where $y_c$ is the complementary function and $y_p$ is the particular integral.
* The complementary function is the solution of the homogeneous equation $$a_2\frac{d^2y}{dx^2} + a_1\frac{dy}{dx} + a_0y = 0$$
* The particular integral is the solution of the non-homogeneous equation $$a_2\frac{d^2y}{dx^2} + a_1\frac{dy}{dx} + a_0y = f(x)$$
* The particular integral can be found by the method of undetermined coefficients or the method of variation of parameters.





### Solution by Changing Independent Variable for the Notes of the Unit 1 - Ordinary Differential Equation of Higher Order in the subject of ENGINEERING MATHEMATICS-II

1. The process of changing the independent variable in an ordinary differential equation (ODE) is known as a **change of variables**. 
2. The goal of changing the independent variable is to simplify the equation, or to make it easier to solve. 
3. In order to do this, the new independent variable must be chosen so that the resulting equation is easier to solve than the original equation. 
4. In order to change the independent variable, one must first solve for the dependent variable in terms of the independent variable. 
5. The new independent variable is then substituted into the equation, and the equation is rearranged so that the dependent variable is expressed as a function of the new independent variable. 
6. The equation is then solved for the new independent variable, and the solution is found. 
7. This process can be used to solve any ODE, regardless of its order.




### Method of Variation of Parameters for the Notes of the Unit 1 - Ordinary Differential Equation of Higher Order in the subject of ENGINEERING MATHEMATICS-II

1. Variation of parameters is a method used to solve linear differential equations when the general solution is not known. 
2. The method of variation of parameters is used to solve differential equations of the form $y'' + p(x)y' + q(x)y = g(x)$, where $p(x)$, $q(x)$, and $g(x)$ are known functions of $x$. 
3. To solve a differential equation using the method of variation of parameters, one must first find the general solution of the associated homogeneous equation $y'' + p(x)y' + q(x)y = 0$. 
4. Once the general solution of the homogeneous equation is known, one can use the variation of parameters method to find a particular solution of the form $y = u(x)y_1 + v(x)y_2$, where $u(x)$ and $v(x)$ are arbitrary functions of $x$ and $y_1$ and $y_2$ are the two linearly independent solutions of the homogeneous equation. 
5. The functions $u(x)$ and $v(x)$ can be found by solving a system of two linear first-order differential equations. 
6. Finally, the particular solution can be written as $y = u(x)y_1 + v(x)y_2 + c$, where $c$ is a constant.




### Cauchy-Euler equation for the notes of the Unit 1 - Ordinary Differential Equation of Higher Order in the subject of ENGINEERING MATHEMATICS-II

- The Cauchy-Euler equation is a second order ordinary differential equation with variable coefficients. 
- It can be written in the form: $$ay'' + by' + cy = 0$$
- The Cauchy-Euler equation has two linearly independent solutions: $$y_1 = x^r, y_2 = x^s$$
- Where $r$ and $s$ are the roots of the characteristic equation: $$ar^2 + br + c = 0$$
- The general solution of the Cauchy-Euler equation is given by: $$y = c_1x^r + c_2x^s$$
- The Cauchy-Euler equation has many applications in engineering, physics, and mathematics.




### Application of Differential Equations in Solving Engineering Problems

1. Differential equations are mathematical equations that involve derivatives, and they are used to solve a variety of engineering problems. 
2. Ordinary differential equations (ODEs) are equations that involve a single independent variable and its derivatives. 
3. ODEs can be used to model the behavior of physical systems, such as mechanical systems, electrical circuits, and chemical reactions. 
4. ODEs of higher order (greater than one) can be solved using numerical methods such as the Runge-Kutta method. 
5. The numerical solutions of ODEs can be used to design and analyze engineering systems. 
6. Differential equations also have applications in control systems, signal processing, and optimization.




## Unit 2 - Laplace Transform

- Laplace Transform is a mathematical technique used to solve certain types of differential equations.
- It is a linear operator that takes a function of a real variable t (usually time) to a function of a complex variable s (complex frequency). 
- The Laplace Transform is used to convert a function of time (a signal) into a function of frequency.
- It can be used to solve differential equations by transforming them into algebraic equations.
- The inverse Laplace Transform is used to find the solution to the differential equations.
- The Laplace Transform can be used to find the transfer function of a system, which is the ratio of the output to the input of the system.
- It can also be used to analyze the stability of a system.
- The Laplace Transform can be used to solve problems involving the convolution of two functions.
- It can also be used to find the Fourier Transform of a function.




### Laplace Transform for the Notes of the Unit 2 - Laplace Transform in the Subject of Engineering Mathematics-II

1. Laplace transform is a mathematical technique used to transform a function of time into a function of complex frequency. 
2. It is widely used in the analysis of linear time-invariant systems in the field of engineering. 
3. The Laplace transform is used to convert a system's differential equation into an algebraic equation, which is simpler to solve. 
4. The Laplace transform is a powerful tool for solving differential equations, as it allows us to solve problems that would otherwise be too difficult to solve using traditional methods. 
5. The Laplace transform can be used to solve initial value problems, boundary value problems, and integral equations. 
6. The inverse Laplace transform is used to convert a function of complex frequency back into a function of time. 
7. The Laplace transform is an important tool for solving linear differential equations, and it is used in many areas of engineering, such as electrical engineering, mechanical engineering, and control theory.




### Existence Theorem for the Notes of the Unit 2 - Laplace Transform in the Subject of ENGINEERING MATHEMATICS-II

1. The Laplace transform is a powerful tool for solving ordinary differential equations and is used to represent the solution of a differential equation in the form of a power series.

2. The Laplace transform can be used to solve linear differential equations with constant coefficients.

3. The Laplace transform is a linear operator and can be used to solve linear systems of equations.

4. The Laplace transform of a function is a function of a complex variable and can be used to represent the solution of a differential equation in the form of a power series.

5. The Laplace transform is an integral transform and can be used to solve integral equations.

6. The Laplace transform is a linear operator and can be used to solve linear systems of equations.

7. The Laplace transform is a linear operator and can be used to solve linear systems of equations with constant coefficients.

8. The Laplace transform is a linear operator and can be used to solve linear systems of equations with variable coefficients.

9. The Laplace transform can be used to solve differential equations with variable coefficients.

10. The Laplace transform can be used to solve integral equations with variable coefficients.




### Properties of Laplace Transform
1. Laplace transform is a mathematical tool used to solve linear differential equations with constant coefficients.
2. Laplace transform converts a time-domain signal into its corresponding frequency-domain representation.
3. Laplace transform is a linear operator which is used to convert a function from the time-domain to the frequency-domain.
4. The Laplace transform of a function is the integral of the function with respect to time, from zero to infinity.
5. The inverse Laplace transform is used to convert the frequency-domain representation back to the time-domain.
6. Laplace transform can be used to solve linear differential equations with constant coefficients.
7. Laplace transform can be used to solve linear integral equations.
8. Laplace transform can be used to solve linear difference equations.
9. Laplace transform can be used to solve linear partial differential equations.
10. Laplace transform can be used to solve linear systems of equations.




### Laplace Transform of Derivatives and Integrals

* Laplace transform is a mathematical technique used to transform a function of time into a function of a complex frequency.
* The Laplace transform is used to solve differential equations that involve derivatives and integrals.
* The Laplace transform of a derivative is the same as the derivative of the Laplace transform.
* The Laplace transform of an integral is the same as the integral of the Laplace transform.
* The Laplace transform can be used to solve linear differential equations with constant coefficients.
* The inverse Laplace transform can be used to find the solution to a differential equation with initial conditions.




### Unit Step Function for the Notes of the Unit 2 - Laplace Transform in the Subject of ENGINEERING MATHEMATICS-II

1. A unit step function is a type of mathematical function that is usually denoted by the symbol u(t). It is a function of a real variable t, and is defined as follows:

* u(t) = 0, for t < 0
* u(t) = 1, for t ≥ 0

2. The unit step function is used in the Laplace transform to represent the behavior of a system over time. The Laplace transform is a mathematical tool used to solve linear differential equations. It is based on the concept of the unit step function, which is used to represent the behavior of a system over time.

3. The Laplace transform is used to transform a function of time into a function of a complex variable. This transformation is used to solve differential equations. The Laplace transform of a unit step function is given by the following equation:

* F(s) = 1/s, where s is the complex variable.

4. The Laplace transform of a unit step function can be used to solve linear differential equations. For example, the Laplace transform can be used to solve the following differential equation:

* dy/dt = -ay, where a is a constant.

5. The solution to this differential equation can be found by taking the Laplace transform of both sides of the equation. The Laplace transform of the left side of the equation is given by:

* F(s) = sY(s) - y(0), where y(0) is the initial value of the function at t = 0.

6. The Laplace transform of the right side of the equation is given by:

* F(s) = -aY(s).

7. By solving for Y(s), we get the following equation:

* Y(s) = y(0)/(s + a).

8. The inverse Laplace transform of this equation gives us the solution to the differential equation:

* y(t) = y(0)e^(-at), where a is a constant.




### Laplace Transform of Periodic Function

1. A periodic function is a function that repeats itself after a certain interval of time.
2. The Laplace transform of a periodic function is defined as the sum of the Laplace transform of the function evaluated at all the values of the period.
3. The Laplace transform of a periodic function can be expressed as:

$$\mathcal{L}\{f(t)\} = \sum_{n=-\infty}^{\infty} F(s+2\pi nj)$$

where $F(s)$ is the Laplace transform of the function $f(t)$.

4. The inverse Laplace transform of a periodic function can be expressed as:

$$f(t) = \frac{1}{2\pi}\sum_{n=-\infty}^{\infty} F(s+2\pi nj)$$

where $F(s)$ is the Laplace transform of the function $f(t)$.

5. The Laplace transform of a periodic function can be used to solve differential equations with periodic boundary conditions.




### Inverse Laplace Transform

Inverse Laplace transform is an important concept in Engineering Mathematics-II. It is used to convert a Laplace transform into its corresponding time domain function.

- The inverse Laplace transform of a function $F(s)$ is defined as the function $f(t)$ such that:
$$\mathcal{L}^{-1}\left\{F(s)\right\} = f(t) $$

- The inverse Laplace transform can be calculated using the formula:
$$f(t) = \frac{1}{2\pi j}\int_{\gamma - \infty}^{\gamma + \infty} F(s)e^{st}ds$$
where $\gamma$ is a real number such that all the poles of $F(s)$ lie to the left of $\gamma$.

- The inverse Laplace transform can also be calculated using the partial fraction expansion method or the convolution theorem.

- The inverse Laplace transform is used to solve differential equations, analyze electrical circuits and analyze the stability of a system.




### Convolution Theorem for Unit 2 - Laplace Transform in ENGINEERING MATHEMATICS-II

1. The convolution theorem states that the Laplace transform of the convolution of two functions is equal to the product of their Laplace transforms.

2. This theorem can be used to solve linear differential equations with variable coefficients.

3. In order to use the convolution theorem, one must first obtain the Laplace transform of each of the two functions.

4. The convolution of two functions can then be calculated by integrating the product of the two functions over the entire range of integration.

5. The result of this integration is the convolution of the two functions.

6. Finally, the Laplace transform of the convolution can be calculated by multiplying the Laplace transforms of the two functions.




### Application of Laplace Transform to solve ordinary differential equations and simultaneous differential equations

1. Laplace Transform is a mathematical tool used to convert a function of time into a function of a complex frequency variable. 
2. It is commonly used to solve ordinary differential equations (ODEs) and simultaneous differential equations.
3. The Laplace transform of a function is defined as the integral of the function multiplied by a complex exponential, from 0 to infinity.
4. The inverse Laplace transform is used to find the solution to the ODEs and simultaneous differential equations.
5. The inverse Laplace transform is defined as the integral of the function multiplied by a complex exponential, from -infinity to infinity.
6. The Laplace transform can be used to solve linear ODEs and simultaneous differential equations with constant coefficients.
7. The Laplace transform can also be used to solve non-linear ODEs and simultaneous differential equations.
8. The Laplace transform can be used to solve boundary value problems.
9. The Laplace transform can be used to solve initial value problems.
10. The Laplace transform can be used to solve integral equations.




## Unit 3 - Sequence and Series

* A sequence is a set of numbers or objects that are arranged in a particular order. 
* A series is the sum of the terms of a sequence. 
* Sequences can be described in terms of a rule or formula. 
* Arithmetic sequences are sequences that have a common difference between consecutive terms. 
* Geometric sequences are sequences that have a common ratio between consecutive terms. 
* Finite sequences are sequences with a fixed number of terms. 
* Infinite sequences are sequences with an infinite number of terms. 
* A series can be convergent or divergent. 
* A convergent series is a series that sums to a finite number. 
* A divergent series is a series that sums to an infinite number. 
* The nth term test can be used to determine whether a series is convergent or divergent. 
* The ratio test can be used to determine whether a series is convergent or divergent.




### Definition of Sequence and Series 

A **sequence** is a collection of numbers or objects in a specific order. A **series** is the sum of the terms of a sequence. 

Examples of sequences include: 
1. The Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, etc. 
2. The prime numbers: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, etc.

Examples of series include:
1. The sum of the first 10 Fibonacci numbers: 88
2. The sum of the first 10 prime numbers: 129




### Convergence of Series 

* A series is said to be convergent if it has a finite sum, otherwise it is divergent. 
* The **Riemann Series Theorem** states that if the sequence of partial sums of a series is bounded then the series converges. 
* The **Leibniz Test** is used to determine the convergence of an alternating series, which is a series where the terms alternate in sign. 
* The **Root Test** is used to determine the convergence of a series where the terms are raised to a power. 
* The **Ratio Test** is used to determine the convergence of a series where the terms form a ratio. 
* The **Comparison Test** is used to determine the convergence of a series by comparing it to a known convergent series. 
* The **Integral Test** is used to determine the convergence of a series where the terms are the values of a continuous function. 
* The **Alternating Series Test** is used to determine the convergence of an alternating series. 
* The **Absolute Convergence Test** is used to determine the convergence of a series by comparing the terms to a known convergent series. 
* The **Limit Comparison Test** is used to determine the convergence of a series by comparing the limit of the terms to a known convergent series.




### Tests for Convergence of Series

1. **Comparison Test**: This test states that if a series $\sum_{n=1}^{\infty} a_n$ is such that $|a_n| \leq b_n$ for all $n$ and the series $\sum_{n=1}^{\infty} b_n$ converges, then the series $\sum_{n=1}^{\infty} a_n$ also converges.

2. **Limit Comparison Test**: This test states that if a series $\sum_{n=1}^{\infty} a_n$ is such that $\lim_{n \to \infty} \frac{a_n}{b_n} = c$ where $c$ is a constant and the series $\sum_{n=1}^{\infty} b_n$ converges, then the series $\sum_{n=1}^{\infty} a_n$ also converges.

3. **Ratio Test**: This test states that if a series $\sum_{n=1}^{\infty} a_n$ is such that $\lim_{n \to \infty} \frac{a_{n+1}}{a_n} = L$ then the series $\sum_{n=1}^{\infty} a_n$ converges if $L < 1$ and diverges if $L > 1$.

4. **Root Test**: This test states that if a series $\sum_{n=1}^{\infty} a_n$ is such that $\lim_{n \to \infty} \sqrt[n]{|a_n|} = L$ then the series $\sum_{n=1}^{\infty} a_n$ converges if $L < 1$ and diverges if $L > 1$.

5. **Integral Test**: This test states that if a series $\sum_{n=1}^{\infty} a_n$ is such that $a_n$ is a positive, decreasing, continuous function and $f(x)$ is its continuous, positive, increasing indefinite integral then the series $\sum_{n=1}^{\infty} a_n$ converges if $\sum_{n=1}^{\infty} f(n)$ converges and diverges if $\sum_{n=1}^{\infty} f(n)$ diverges.




### Ratio Test

* Ratio test is a method used to determine the convergence or divergence of a series. 
* It is based on the ratio of the terms of the series. 
* This test is applicable only for series with positive terms. 
* Consider the series $\sum_{n=1}^{\infty} a_n$ where $a_n > 0$ for all $n \in \mathbb{N}$.
* The ratio test states that if the limit of the ratio of successive terms of the series exists and is less than 1, then the series converges. 
* If the limit of the ratio of successive terms of the series exists and is greater than 1, then the series diverges. 
* If the limit of the ratio of successive terms of the series is equal to 1, then the ratio test is inconclusive. 
* The ratio test is helpful in determining the convergence of a series without having to calculate the sum of the series.




### D’ Alembert’s test for the notes of the Unit 3 - Sequence and Series in the subject of ENGINEERING MATHEMATICS-II

1. D’ Alembert’s test is a method of determining whether a series converges or diverges.
2. To use D’ Alembert’s test, the series must be written in the form of a summation of terms.
3. The test states that if the limit of the ratio of the terms of the series is less than 1, then the series converges; if the limit is greater than 1, then the series diverges.
4. In the case of an alternating series, the absolute value of the ratio of the terms must be less than 1 for the series to converge.
5. The D’ Alembert’s test is useful for determining the convergence or divergence of a series, but it is not always reliable. It is possible for a series to pass the test and still be divergent.




### Raabe’s Test
Raabe’s test is a useful tool for determining whether a given sequence converges or diverges. It states that if the limit of the ratio of two consecutive terms of a sequence is greater than one, the sequence diverges.

1. Let the given sequence be $\{a_n\}$
2. Calculate the limit of the ratio of two consecutive terms of the sequence, i.e. $\lim\limits_{n\to\infty}\frac{a_{n+1}}{a_n}$
3. If the limit is greater than one, the sequence diverges. Otherwise, it converges.




### Comparison Test for the Notes of the Unit 3 - Sequence and Series in the Subject of Engineering Mathematics-II

1. A comparison test is a method for determining whether a given series converges or diverges. 
2. The comparison test states that if the terms of a series are less than the terms of a second series, and the second series converges, then the first series must also converge. 
3. Similarly, if the terms of the first series are greater than the terms of the second series and the second series diverges, then the first series must also diverge. 
4. The comparison test is useful for determining the convergence or divergence of a series when the series has a complex form. 
5. The comparison test can be used to compare the terms of a series with the terms of a known convergent or divergent series. 
6. The most commonly used comparison tests are the limit comparison test, the integral comparison test, and the ratio test. 
7. The limit comparison test states that if the limit of the ratio of the terms of two series is a finite number, then the two series have the same convergence or divergence. 
8. The integral comparison test states that if the integral of the terms of a series can be compared to the integral of a known convergent or divergent series, then the two series have the same convergence or divergence. 
9. The ratio test states that if the ratio of the terms of a series tends to a finite number, then the series converges. 
10. If the ratio tends to infinity, then the series diverges.




### Fourier Series for the Notes of the Unit 3 - Sequence and Series in the Subject of Engineering Mathematics-II

* Fourier series is a way of representing a periodic function as an infinite sum of sine and cosine functions.
* It is named after French mathematician Joseph Fourier, who showed that any periodic function can be represented as a sum of sines and cosines.
* The Fourier series of a periodic function is composed of the sum of its harmonics, which are sine and cosine functions with different frequencies and amplitudes.
* The Fourier series of a function can be used to calculate the coefficients of the sine and cosine functions that make up the series.
* The Fourier coefficients are used to calculate the frequency, phase, and amplitude of each harmonic in the series.
* The Fourier series can also be used to calculate the Fourier transform of a function, which is a representation of the function in the frequency domain.
* The Fourier series can also be used to solve differential equations, such as the heat equation and the wave equation.




### Half range Fourier sine and cosine series

* Half range Fourier sine and cosine series is a type of Fourier series that is used to represent a periodic function over a half-interval. 
* It is an extension of the standard Fourier series, which is used to represent a periodic function over a full interval.
* The half range Fourier series can be expressed in terms of sine and cosine functions.
* The half range Fourier series is used to represent periodic functions with discontinuities, such as square waves, sawtooth waves and triangle waves.
* The half range Fourier series can also be used to represent non-periodic functions.
* The coefficients of the half range Fourier series can be calculated using the formula:

$$a_n = \frac{2}{T}\int_{-T/2}^{T/2}f(x)\cos(n\pi x/T)dx$$

$$b_n = \frac{2}{T}\int_{-T/2}^{T/2}f(x)\sin(n\pi x/T)dx$$

where $T$ is the period of the function and $f(x)$ is the function to be represented.




## Unit 4 - Complex Variable–Differentiation

1. Complex numbers are defined as numbers of the form a + bi, where a and b are real numbers and i is the imaginary unit.
2. The conjugate of a complex number is defined as the number a – bi.
3. Complex numbers can be added and subtracted using the same rules as for real numbers.
4. Complex numbers can be multiplied and divided using the same rules as for real numbers.
5. Complex numbers can be raised to powers using the same rules as for real numbers.
6. The modulus of a complex number is defined as the square root of the sum of the squares of its real and imaginary parts.
7. The argument of a complex number is defined as the angle between the positive real axis and the vector representing the complex number in the complex plane.
8. The differentiation of a complex function is defined as the operation of finding the derivative of the function with respect to a complex variable.
9. The Cauchy-Riemann equations are a set of two equations that must be satisfied for a complex function to be differentiable.
10. The Laplace operator is a differential operator that can be used to calculate the second derivative of a complex function.




### Functions of complex variable for the notes of the Unit 4 - Complex Variable–Differentiation in the subject of ENGINEERING MATHEMATICS-II

* A complex variable is a variable whose values are complex numbers. 
* Complex variables are used to describe physical phenomena in various branches of engineering, such as electrical engineering, mechanical engineering, and control engineering.
* Complex variables can be differentiated and integrated in order to solve problems related to linear and nonlinear systems.
* Differentiation of a complex variable is the process of finding the derivative of a function of a complex variable.
* Integration of a complex variable is the process of finding the integral of a function of a complex variable.
* The Cauchy-Riemann equations are a set of equations that are used to determine whether a function is differentiable or not.
* The Laplace transform is a powerful tool for solving linear differential equations with constant coefficients.
* The Fourier transform is a tool used to decompose a function into its constituent frequencies.
* The residue theorem is used to evaluate integrals of complex functions.




### Limit for the notes of the Unit 4 - Complex Variable–Differentiation in the subject of ENGINEERING MATHEMATICS-II

1. Limits of a complex function are defined as the values that the function approaches as the independent variable approaches a certain value.

2. The limit of a complex function can be determined by using the limit definition of a complex function.

3. The limit definition states that the limit of a complex function is equal to the limit of its real part plus the limit of its imaginary part.

4. Differentiation of a complex function can be done using the Cauchy-Riemann equations.

5. The Cauchy-Riemann equations are a set of equations that relate the real and imaginary parts of a complex function.

6. The Cauchy-Riemann equations can be used to find the derivative of a complex function.

7. The chain rule can be used to find the derivatives of composite complex functions.

8. The Taylor series can be used to approximate the value of a complex function at a given point.

9. Taylor series can also be used to find the derivatives of a complex function.




### Continuity and Differentiability

* A complex function is said to be continuous at a point z0 if the limit of the function f(z) as z approaches z0 is equal to f(z0). 
* A complex function is said to be differentiable at a point z0 if the limit of the difference quotient (f(z)-f(z0))/(z-z0) as z approaches z0 exists and is finite.
* Cauchy-Riemann equations are necessary and sufficient conditions for a complex function to be differentiable.
* The complex derivative of a function is defined as the derivative of the real and imaginary parts of the function.
* The Cauchy-Riemann equations can be used to calculate the complex derivatives of a function.
* The Cauchy-Riemann equations can also be used to determine the continuity and differentiability of a complex function.
* The complex derivative of a function can be used to calculate the local maximum and minimum points of a function, as well as the points of inflection.




### Analytic functions for the notes of the Unit 4 - Complex Variable–Differentiation in the subject of ENGINEERING MATHEMATICS-II

1. Analytic functions are functions that can be written as a power series in some neighborhood of every point in their domain. 
2. In order to be considered an analytic function, a function must be differentiable at every point in its domain.
3. The most important example of an analytic function is the complex exponential function, which is defined as: 
$$f(z) = e^z = \sum_{n=0}^{\infty}\frac{z^n}{n!}$$
4. The derivative of an analytic function can be calculated using the formula: 
$$f'(z) = \sum_{n=1}^{\infty}\frac{n z^{n-1}}{n!}$$
5. Analytic functions can be used to solve complex equations, as well as to calculate integrals and derivatives of complex functions. 
6. Cauchy's integral formula is an example of an application of analytic functions. It states that if a function is analytic in a region, then its integral over a closed contour in that region is equal to zero. 
7. The Cauchy-Riemann equations are a set of equations which are necessary and sufficient for a function to be analytic. They are given by: 
$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}$$
$$\frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$$
where $u$ and $v$ are the real and imaginary parts of the function. 
8. The maximum modulus principle states that the maximum value of an analytic function on a region is attained on the boundary of the region. 
9. The Liouville's theorem states that an analytic function which is bounded in a region must be a constant. 
10. The residue theorem is a powerful tool for calculating integrals of analytic functions. It states that if a function is analytic in a region, then its integral over a closed contour in that region is equal to the sum of the residues of the poles of the function inside the contour.




### Cauchy-Riemann Equations (Cartesian and Polar Form)

1. Cauchy-Riemann equations are a set of equations used to describe complex functions in terms of their real and imaginary components.

2. These equations are commonly used in engineering mathematics-II to analyze the properties of complex variables.

3. In Cartesian form, the Cauchy-Riemann equations are written as follows:

$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}$$
$$\frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$$

4. In Polar form, the Cauchy-Riemann equations are written as follows:

$$\frac{\partial u}{\partial r} = \frac{1}{r}\frac{\partial v}{\partial \theta}$$
$$\frac{\partial u}{\partial \theta} = -r\frac{\partial v}{\partial r}$$

5. These equations are used to determine the differentiability of a complex function, and can be used to analyze its properties such as continuity, analyticity, and the existence of an antiderivative.




### Harmonic Function

A harmonic function is an analytic function of complex variables which satisfies Laplace's equation. It is a type of solution to a differential equation, and is used in many areas of mathematics, engineering, and physics.

1. Definition: A harmonic function is a function $f(z)$ of a complex variable $z=x+iy$, where $x$ and $y$ are real numbers, that satisfies Laplace's equation $$\frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2} = 0.$$

2. Properties: A harmonic function has the following properties:

- It is real-valued and continuous.
- It is analytic, meaning it can be written as a power series in $z$.
- Its partial derivatives $\frac{\partial f}{\partial x}$ and $\frac{\partial f}{\partial y}$ exist and are continuous.
- Its second partial derivatives $\frac{\partial^2 f}{\partial x^2}$ and $\frac{\partial^2 f}{\partial y^2}$ exist and are continuous.

3. Examples:

- The real and imaginary parts of a complex analytic function are both harmonic functions.
- The real and imaginary parts of a complex sinusoidal wave are both harmonic functions.
- The real and imaginary parts of the exponential function $e^{iz}$ are both harmonic functions.
- The real and imaginary parts of the complex logarithm $Log(z)$ are both harmonic functions.




### Method to find Analytic functions for the notes of the Unit 4 - Complex Variable–Differentiation in the subject of ENGINEERING MATHEMATICS-II

1. Analytic functions are those whose derivatives can be calculated from their definition, rather than from a graph.

2. Analytic functions can be found by first solving the differential equation that defines the function.

3. Once the differential equation is solved, the function can be written in terms of its derivatives and the initial conditions.

4. Analytic functions can also be found using the Cauchy-Riemann equations. These equations relate the real and imaginary parts of the function to its derivatives.

5. The Cauchy-Riemann equations can be used to find the derivatives of a function, and thus the analytic function itself.

6. Finally, analytic functions can be found by integrating a power series. This is done by first finding the coefficients of the power series, and then integrating the series.




### Milne’s Thompson Method for the notes of the Unit 4 - Complex Variable–Differentiation in the subject of ENGINEERING MATHEMATICS-II

1. Milne’s Thompson Method is a method used to differentiate complex variables. 
2. It involves taking the derivative of a function in terms of its real and imaginary parts. 
3. The method consists of two steps: the first step is to differentiate the real and imaginary parts of the function separately and the second step is to combine the results of the first step. 
4. This method is useful for finding the derivatives of functions that involve complex numbers. 
5. It can also be used to find the derivatives of functions that involve multiple variables. 
6. The main advantage of this method is that it eliminates the need to use the chain rule when taking derivatives of complex variables. 
7. This makes the process of taking derivatives much easier and faster.




### Conformal Mapping for the Notes of the Unit 4 - Complex Variable–Differentiation in the Subject of ENGINEERING MATHEMATICS-II

1. Conformal Mapping is a type of mathematical transformation which preserves angles between curves. It is used to transform a region of the complex plane into another region of the complex plane.

2. Conformal mapping can be used to solve problems in fluid mechanics, electrostatics, and other areas of engineering.

3. The most common conformal mapping is the Riemann mapping theorem, which states that any simply connected domain in the complex plane can be mapped conformally to the unit disk.

4. The Schwarz–Christoffel transformation is another type of conformal mapping which is used to map a polygon onto the unit disk.

5. The Cauchy–Riemann equations are necessary and sufficient conditions for a function to be conformal.

6. The theory of conformal mapping can be used to solve boundary value problems in complex analysis.

7. Conformal mapping can also be used to map a region of the complex plane to another region of the complex plane. This is useful for solving problems in fluid mechanics, electrostatics, and other areas of engineering.




### Mobius Transformation and their Properties

1. A Mobius transformation is a complex function which maps points in the complex plane to other points in the complex plane.
2. It is a one-to-one conformal mapping, meaning that it preserves angles and the shape of figures, but not necessarily the size.
3. It is named after August Ferdinand Mobius, who discovered it in 1827.
4. A Mobius transformation is a composition of two linear fractional transformations (LFTs).
5. An LFT is a transformation of the form z → (az + b)/(cz + d), where a, b, c and d are complex constants.
6. A Mobius transformation can be represented by a 3×3 matrix with complex entries.
7. The most general Mobius transformation is of the form z → (az + b)/(cz + d), where a, b, c and d are complex constants.
8. The Mobius transformation has the property that it maps circles and lines to circles and lines.
9. It also preserves angles and the shape of figures, but not necessarily the size.
10. The Mobius transformation can be used to solve various problems in complex analysis, such as finding the inverse of a complex function.
11. It can also be used to solve problems in engineering, such as finding the transfer function of a linear system.
12. The Mobius transformation can also be used to solve problems in geometry, such as finding the center of a circle.




## Unit 5 - Complex Variable –Integration

1. Complex variables are variables that are expressed in terms of real and imaginary numbers.
2. Complex integration is the process of calculating the integral of a complex function.
3. The Cauchy-Goursat theorem states that the integral of a complex function over a closed contour is equal to zero.
4. The Cauchy integral formula is a powerful tool for computing complex integrals. It states that the integral of a complex function over a closed contour is equal to the sum of the integrals of the function over all the paths that form the contour.
5. The Cauchy residue theorem is a powerful tool for computing complex integrals. It states that the integral of a complex function over a closed contour is equal to the sum of the residues of the function at the poles of the contour.
6. The residue theorem can be used to calculate the integral of a complex function over a semi-infinite contour.
7. The Laurent series is a powerful tool for computing complex integrals. It states that a complex function can be written as a sum of its Taylor series and its Laurent series.
8. The residue theorem can be used to calculate the integral of a complex function over a finite contour.
9. The integral of a complex function over a closed contour can be expressed as a sum of its residues at the poles of the contour.
10. The evaluation of complex integrals is a powerful tool for solving complex problems in mathematics, engineering, and physics.




### Complex integration for the notes of the Unit 5 - Complex Variable –Integration in the subject of ENGINEERING MATHEMATICS-II

1. Complex integration is a type of integration that involves the integration of functions of complex variables.
2. Complex integration can be used to solve problems in a variety of fields, including engineering, physics, and mathematics.
3. Complex integration involves the use of Cauchy’s theorem and Cauchy’s integral formula.
4. Cauchy’s theorem states that any holomorphic function can be represented as a power series.
5. Cauchy’s integral formula states that the integral of a function around a closed contour is equal to the sum of the residues of the poles inside the contour.
6. The Cauchy-Riemann equations are a set of equations which can be used to determine the differentiability of a function at a point.
7. The Cauchy-Riemann equations can be used to determine whether a function is holomorphic or not.
8. The Cauchy-Goursat theorem states that the integral of a holomorphic function over a closed contour is equal to zero.
9. The residue theorem states that the integral of a function over a closed contour is equal to the sum of the residues of the poles inside the contour.
10. The Laurent series is a power series which can be used to represent a function in the complex plane.




### Cauchy- Integral Theorem

1. The Cauchy-Integral Theorem states that if a complex-valued function $f(z)$ is analytic in a region $\Omega$, then its integral over any closed contour $C$ in $\Omega$ is equal to zero.

2. This theorem can be used to calculate the value of a complex integral by expressing it as a line integral around a closed contour.

3. The Cauchy-Integral Theorem is a special case of the more general Cauchy-Goursat Theorem.

4. The Cauchy-Integral Theorem is related to the Fundamental Theorem of Calculus, which states that the integral of a function over a closed interval is equal to the difference between the values of the function at the endpoints of the interval.




### Cauchy Integral Formula

* The Cauchy Integral Formula is a powerful tool for evaluating complex integrals.
* It states that if a function $f$ is analytic on and inside a closed contour $C$, then: $$\oint_C f(z)dz = \int_{\partial C} f(z)dz = 2\pi i \sum_{k=1}^n Res(f, z_k)$$
* Here, $z_k$ are the poles of $f$ inside the contour $C$.
* Moreover, the Cauchy Integral Formula can be used to calculate the value of a complex integral if the integrand is known to be analytic in the region of integration.
* It can also be used to calculate the values of derivatives of a function at a point inside the contour.




### Taylor’s and Laurent’s series for the notes of Unit 5 - Complex Variable –Integration in the subject of ENGINEERING MATHEMATICS-II

1. Taylor series is a type of power series which is used to represent a function as an infinite sum of terms. It is named after the mathematician Brook Taylor.
2. The Taylor series of a function f(x) is the sum of the terms of its Taylor polynomial.
3. The Taylor polynomial of degree n of a function f at a point a is the polynomial of degree n that is obtained by taking the first n terms of the Taylor series of f at a.
4. Laurent series is a type of power series which is used to represent a function as an infinite sum of terms. It is named after the mathematician Pierre-Simon de Laurent.
5. The Laurent series of a function f(z) is the sum of the terms of its Laurent polynomial.
6. The Laurent polynomial of degree n of a function f at a point a is the polynomial of degree n that is obtained by taking the first n terms of the Laurent series of f at a.
7. Complex variable integration is a method of calculating integrals of functions of complex variables.
8. The Cauchy integral theorem states that if a function is analytic within a simply connected region, then the integral of the function over the boundary of the region is zero.
9. The Cauchy integral formula states that the value of a function at a point inside a region can be calculated by integrating the function over the boundary of the region.
10. The residue theorem states that the integral of a function over a closed contour is equal to the sum of the residues of the poles of the function inside the contour.




### Singularities and its Classification for Unit 5 - Complex Variable –Integration in ENGINEERING MATHEMATICS-II

1. **Singularities:** Singularities are points in a complex plane where the function is not defined. These points are essential for the study of complex analysis.

2. **Classification of Singularities:** There are two main types of singularities: isolated and non-isolated singularities. Isolated singularities are those which are not part of any other singularity and can be classified into removable, pole, and essential singularities. Non-isolated singularities are those which are part of another singularity and can be classified into isolated singularities, branch points, and essential singularities.

3. **Removable Singularities:** Removable singularities are those which can be removed by a simple change of variable. These singularities can be further divided into two types: isolated and non-isolated. Isolated removable singularities are those which are not part of any other singularity and can be removed by a simple change of variable. Non-isolated removable singularities are those which are part of another singularity and can be removed by a simple change of variable.

4. **Pole Singularities:** Pole singularities are those which cannot be removed by a simple change of variable. These singularities can be further divided into two types: isolated and non-isolated. Isolated pole singularities are those which are not part of any other singularity and can be removed by a simple change of variable. Non-isolated pole singularities are those which are part of another singularity and can be removed by a complex change of variable.

5. **Essential Singularities:** Essential singularities are those which cannot be removed by any change of variable. These singularities can be further divided into two types: isolated and non-isolated. Isolated essential singularities are those which are not part of any other singularity and can be removed by a complex change of variable. Non-isolated essential singularities are those which are part of another singularity and can be removed by a complex change of variable.




### Zeros of Analytic Functions 

1. An analytic function is a function that can be written as a power series in a neighborhood of any point in its domain. 
2. The zeros of an analytic function are the values of the independent variable at which the function is equal to zero. 
3. In complex analysis, a zero of an analytic function is a point in the complex plane at which the function takes the value zero. 
4. The zeros of an analytic function can be found by solving the equation f(z)=0, where z is the complex variable. 
5. The zeros of an analytic function can be used to determine the maximum and minimum values of the function, as well as the location of its critical points. 
6. The number of zeros of an analytic function is related to the order of the power series representation of the function. 
7. The zeros of an analytic function can be used to determine the location of its poles, which are the points at which the function is not defined. 
8. The zeros of an analytic function can be used to determine the behavior of the function in the vicinity of the zeros. 
9. The zeros of an analytic function can be used to determine the location of its essential singularities, which are points at which the function is not defined but has an infinite limit. 
10. The zeros of an analytic function can be used to determine the behavior of the function in the vicinity of the essential singularities.




### Residues for the notes of the Unit 5 - Complex Variable –Integration in the subject of ENGINEERING MATHEMATICS-II

1. Residue theorem is a powerful tool in complex analysis which allows us to evaluate certain integrals.
2. A residue is the coefficient of the pole of a rational function in its Laurent series expansion.
3. The residue of a function at a pole is equal to the coefficient of the pole in the Laurent series expansion of the function.
4. The residue theorem states that the integral of a function around a closed contour is equal to the sum of the residues of the function inside the contour.
5. The residue theorem can be used to evaluate real integrals by transforming them into complex integrals.
6. The residue theorem can be used to evaluate improper integrals by transforming them into a sum of residues.
7. The residue theorem can be used to evaluate contour integrals by transforming them into a sum of residues.
8. The residue theorem can also be used to solve certain differential equations.




### Cauchy’s Residue Theorem and Its Application for the Notes of the Unit 5 - Complex Variable –Integration in the Subject of ENGINEERING MATHEMATICS-II KCS

1. Cauchy's Residue Theorem states that the sum of the residues of a function at its poles is equal to the integral of the function over a closed contour. 
2. This theorem is used to evaluate certain types of integrals, particularly those involving complex variables or functions with singularities. 
3. It can also be used to solve certain types of differential equations. 
4. The theorem is named after Augustin-Louis Cauchy, who proved it in 1827.
5. The theorem can be applied to any function that is analytic (has derivatives of all orders) in a region of the complex plane, except at its poles.
6. A pole is a point at which the function is not analytic and cannot be defined. 
7. The residues of a function at its poles are the coefficients of the Laurent series expansion of the function around the pole.
8. The residue of a function at a pole can be computed by taking the limit of the function as the point approaches the pole.
9. The Cauchy Residue Theorem can be used to evaluate integrals of the form 
$$\int_C f(z)dz$$
where C is a closed contour in the complex plane and f(z) is analytic in the region enclosed by C except for a finite number of poles.
10. The integral is equal to the sum of the residues of the function at its poles. 
11. The theorem can also be used to solve certain types of differential equations. 
12. For example, if a function f(z) is analytic in a region of the complex plane except at a finite number of poles, then the solution to the differential equation 
$$\frac{df}{dz}=g(z)$$
can be expressed in terms of the residues of f(z) at its poles.

