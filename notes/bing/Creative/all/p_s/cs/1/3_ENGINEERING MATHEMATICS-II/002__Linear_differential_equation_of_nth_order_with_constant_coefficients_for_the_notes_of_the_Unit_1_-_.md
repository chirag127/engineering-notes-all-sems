### Linear differential equation of nth order with constant coefficients

- A linear differential equation of nth order with constant coefficients is an equation of the form

  ```math
  a_n y^{(n)} + a_{n-1} y^{(n-1)} + \cdots + a_1 y' + a_0 y = f(x)
  ```

  where \(a_n, a_{n-1}, \ldots, a_1, a_0\) are constants and \(f(x)\) is a given function of \(x\).

- The equation is called **homogeneous** if \(f(x) = 0\) and **nonhomogeneous** otherwise.

- The general solution of a homogeneous linear differential equation of nth order with constant coefficients is given by

  ```math
  y_h(x) = c_1 y_1(x) + c_2 y_2(x) + \cdots + c_n y_n(x)
  ```

  where \(c_1, c_2, \ldots, c_n\) are arbitrary constants and \(y_1(x), y_2(x), \ldots, y_n(x)\) are linearly independent solutions of the equation.

- To find the linearly independent solutions of the homogeneous equation, we assume a solution of the form

  ```math
  y(x) = e^{rx}
  ```

  where \(r\) is a constant. Substituting this into the equation, we get

  ```math
  a_n r^n e^{rx} + a_{n-1} r^{n-1} e^{rx} + \cdots + a_1 r e^{rx} + a_0 e^{rx} = 0
  ```

  Dividing by \(e^{rx}\), we obtain

  ```math
  a_n r^n + a_{n-1} r^{n-1} + \cdots + a_1 r + a_0 = 0
  ```

  This is called the **characteristic equation** of the differential equation. The roots of the characteristic equation are called the **characteristic roots** of the differential equation.

- Depending on the nature of the characteristic roots, there are different cases for the linearly independent solutions of the homogeneous equation.

  - If the characteristic equation has \(n\) distinct real roots \(r_1, r_2, \ldots, r_n\), then the linearly independent solutions are

    ```math
    y_1(x) = e^{r_1 x}, y_2(x) = e^{r_2 x}, \ldots, y_n(x) = e^{r_n x}
    ```

  - If the characteristic equation has repeated real roots, then we need to multiply the solutions by powers of \(x\) to obtain linearly independent solutions. For example, if \(r\) is a root of multiplicity \(k\), then the linearly independent solutions are

    ```math
    y_1(x) = e^{rx}, y_2(x) = xe^{rx}, \ldots, y_k(x) = x^{k-1} e^{rx}
    ```

  - If the characteristic equation has complex roots, then we need to use the Euler's formula to express the solutions in terms of real and imaginary parts. For example, if \(r = \alpha + i \beta\) is a complex root, then the corresponding solutions are

    ```math
    y_1(x) = e^{\alpha x} \cos (\beta x), y_2(x) = e^{\alpha x} \sin (\beta x)
    ```

    If \(r\) is a repeated complex root of multiplicity \(k\), then we need to multiply the solutions by powers of \(x\) as before.

- The general solution of a nonhomogeneous linear differential equation of nth order with constant coefficients is given by

  ```math
  y(x) = y_h(x) + y_p(x)
  ```

  where \(y_h(x)\) is the general solution of the corresponding homogeneous equation and \(y_p(x)\) is a **particular solution** of the nonhomogeneous equation.

- To find a particular solution of the nonhomogeneous equation, we can use various methods, such as the **method of undetermined coefficients**, the **method of variation of parameters**, or the **Laplace transform method**.

- The method of undetermined coefficients is based on guessing

Some possible mnemonics and learning tricks for the topic are:

- To remember the form of the characteristic equation, you can use the acronym **CARE**:

  ```math
  C: Coefficients
  A: Add
  R: Raise to the power
  E: Equal to zero
  ```

  For example, if the differential equation is

  ```math
  y'' - 3y' + 2y = 0
  ```

  then the characteristic equation is

  ```math
  r^2 - 3r + 2 = 0
  ```

- To remember the form of the linearly independent solutions for distinct real roots, you can use the acronym **DRE**:

  ```math
  D: Distinct
  R: Real
  E: Exponential
  ```

  For example, if the characteristic equation has distinct real roots \(r_1\) and \(r_2\), then the linearly independent solutions are

  ```math
  y_1(x) = e^{r_1 x}, y_2(x) = e^{r_2 x}
  ```

- To remember the form of the linearly independent solutions for repeated real roots, you can use the acronym **RREX**:

  ```math
  R: Repeated
  R: Real
  E: Exponential
  X: Multiply by x
  ```

  For example, if the characteristic equation has a repeated real root \(r\) of multiplicity \(3\), then the linearly independent solutions are

  ```math
  y_1(x) = e^{rx}, y_2(x) = xe^{rx}, y_3(x) = x^2 e^{rx}
  ```

- To remember the form of the linearly independent solutions for complex roots, you can use the acronym **COSI**:

  ```math
  C: Complex
  O: Oscillatory
  S: Sine
  I: Imaginary
  ```

  For example, if the characteristic equation has a complex root \(r = \alpha + i \beta\), then the corresponding solutions are

  ```math
  y_1(x) = e^{\alpha x} \cos (\beta x), y_2(x) = e^{\alpha x} \sin (\beta x)
  ```

  Note that the real part of the complex root determines the exponential factor, while the imaginary part determines the oscillatory factor.