### Solution by changing independent variable for the notes of the Unit 1 - Ordinary Differential Equation of Higher Order in the subject of ENGINEERING MATHEMATICS-II

- An ordinary differential equation (ODE) is an equation that involves the derivatives of an unknown function of a single variable. The order of an ODE is the highest order of any derivative that appears in the equation .
- A solution of an ODE is a function that satisfies the equation when substituted into it. A general solution of an ODE contains arbitrary constants that can be determined by initial or boundary conditions .
- Sometimes, an ODE can be simplified by changing the independent variable. This is done by using the chain rule to express the derivatives of the original function in terms of the new variable and the new function.
- For example, consider the ODE:

  $$y'' + \frac{y'}{x} - \frac{y}{x^2} = 0$$

  where $y = y(x)$ and $y'$ and $y''$ denote the first and second derivatives of $y$ with respect to $x$.

  If we change the independent variable from $x$ to $s$ by letting $s = 1/x$, then we can define a new function $v = v(s)$ by $v(s) = y(x) = y(1/s)$. Then, by the chain rule, we have:

  $$y' = \frac{dy}{dx} = \frac{dy}{ds} \frac{ds}{dx} = -\frac{1}{s^2} \frac{dv}{ds} = -\frac{v'}{s^2}$$

  and

  $$y'' = \frac{d^2y}{dx^2} = \frac{d}{dx} \left( -\frac{v'}{s^2} \right) = -\frac{1}{s^2} \frac{d}{ds} \left( -\frac{v'}{s^2} \right) \frac{ds}{dx} = \frac{1}{s^4} \left( v'' + \frac{2v'}{s} \right)$$

  Substituting these expressions into the original ODE, we get:

  $$\frac{1}{s^4} \left( v'' + \frac{2v'}{s} \right) + \frac{1}{s^2} \left( -\frac{v'}{s^2} \right) - \frac{v}{s^4} = 0$$

  Simplifying, we obtain:

  $$v'' + \frac{v'}{s} - v = 0$$

  which is a simpler ODE to solve. The general solution of this ODE is:

  $$v(s) = c_1 e^s + c_2 e^{-s}$$

  where $c_1$ and $c_2$ are arbitrary constants. To find the solution of the original ODE, we substitute back $s = 1/x$ and $v(s) = y(x)$, and get:

  $$y(x) = c_1 e^{1/x} + c_2 e^{-1/x}$$

  which is the general solution of the original ODE.

- Changing the independent variable can be useful when the original ODE has coefficients that depend on the independent variable in a complicated way. By choosing a suitable transformation, the coefficients can be simplified or eliminated, making the ODE easier to solve.

Some possible mnemonics and learning tricks for differential equations are:

- To remember the general solution of a linear homogeneous ODE of the form $y'' + ay' + by = 0$, where $a$ and $b$ are constants, use the acronym **DOR** (Discriminant, Overdamped, Resonant):

  - If the discriminant $D = a^2 - 4b$ is positive, then the solution is **D**istinct and has the form $y = c_1 e^{r_1 x} + c_2 e^{r_2 x}$, where $r_1$ and $r_2$ are the roots of the characteristic equation $r^2 + ar + b = 0$.
  - If the discriminant $D = a^2 - 4b$ is zero, then the solution is **O**verdamped and has the form $y = (c_1 + c_2 x) e^{r x}$, where $r$ is the repeated root of the characteristic equation $r^2 + ar + b = 0$.
  - If the discriminant $D = a^2 - 4b$ is negative, then the solution is **R**esonant and has the form $y = e^{\alpha x} (c_1 \cos \beta x + c_2 \sin \beta x)$, where $\alpha = -a/2$ and $\beta = \sqrt{-D}/2$ are the real and imaginary parts of the complex roots of the characteristic equation $r^2 + ar + b = 0$.

- To remember the method of undetermined coefficients for finding a particular solution of a nonhomogeneous ODE of the form $y'' + ay' + by = f(x)$, where $a$ and $b$ are constants and $f(x)$ is a function of $x$, use the acronym **SHIELDS** (Sine, Hyperbolic, Inverse, Exponential, Logarithmic, Degree, Sum):

  - If $f(x)$ is a **S**ine or cosine function, then the trial solution is $y_p = A \cos kx + B \sin kx$, where $A$ and $B$ are undetermined coefficients and $k$ is the frequency of $f(x)$.
  - If $f(x)$ is a **H**yperbolic sine or cosine function, then the trial solution is $y_p = A \sinh kx + B \cosh kx$, where $A$ and $B$ are undetermined coefficients and $k$ is the frequency of $f(x)$.
  - If $f(x)$ is an **I**nverse function, such as $1/x$, then the trial solution is $y_p = A/x$, where $A$ is an undetermined coefficient.
  - If $f(x)$ is an **E**xponential function, then the trial solution is $y_p = A e^{kx}$, where $A$ is an undetermined coefficient and $k$ is the exponent of $f(x)$.
  - If $f(x)$ is a **L**ogarithmic function, then the trial solution is $y_p = A \ln x + B$, where $A$ and $B$ are undetermined coefficients.
  - If $f(x)$ is a polynomial function of **D**egree $n$, then the trial solution is $y_p = A_n x^n + A_{n-1} x^{n-1} + \cdots + A_1 x + A_0$, where $A_n, A_{n-1}, \ldots, A_0$ are undetermined coefficients.
  - If $f(x)$ is a **S**um of two or more functions, then the trial solution is the sum of the trial solutions for each function.

- To remember the general solution of a second-order ODE with constant coefficients and a forcing function of the form $y'' + ay' + by = e^{kx} \cos \omega x$, where $a$, $b$, $k$, and $\omega$ are constants, use the mnemonic **ECCO** (Exponential, Cosine, Cosine, Odd):

  - The general solution is $y = y_h + y_p$, where $y_h$ is the general solution of the homogeneous ODE $y'' + ay