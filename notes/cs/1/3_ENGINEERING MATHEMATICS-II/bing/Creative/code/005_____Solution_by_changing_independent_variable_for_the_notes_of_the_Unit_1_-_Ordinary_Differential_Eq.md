Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of Solution by changing independent variable for the notes of the Unit 1 - Ordinary Differential Equation of Higher Order in the subject of ENGINEERING MATHEMATICS-II.

### Solution by changing independent variable

- Sometimes, a differential equation of higher order can be reduced to a differential equation of lower order by changing the independent variable.
- This method is useful when the differential equation contains a function of the independent variable only, or a function of the dependent variable and its derivatives only, or a function of a linear combination of the independent variable and the dependent variable.
- The general steps for this method are:

  1. Identify the function of the independent variable only, or the function of the dependent variable and its derivatives only, or the function of a linear combination of the independent variable and the dependent variable in the given differential equation.
  2. Let the function be equal to a new variable, say z, and differentiate it with respect to the original independent variable, say x, to obtain dz/dx.
  3. Substitute z and dz/dx in the given differential equation and simplify to obtain a differential equation in terms of z and x.
  4. If possible, change the independent variable from x to z by using the inverse function of z, and obtain a differential equation in terms of z only.
  5. Solve the differential equation in terms of z and obtain the general solution.
  6. Substitute back the original function of z in terms of x and/or y to obtain the general solution in terms of x and y.

- Here are some examples of this method:

  - Example 1: Solve the differential equation y''' + y'' = e^x.

    - Solution: The function of the independent variable only is e^x. Let z = e^x, then dz/dx = e^x = z. Substituting z and dz/dx in the given differential equation, we get

      ```
      y''' + y'' = z
      ```

    - Changing the independent variable from x to z, we get

      ```
      (d^3y/dz^3)(dz/dx)^3 + (d^2y/dz^2)(dz/dx)^2 = z
      ```

    - Simplifying, we get

      ```
      z^3 d^3y/dz^3 + z^2 d^2y/dz^2 = z
      ```

    - Dividing by z^2, we get

      ```
      z d^3y/dz^3 + d^2y/dz^2 = 1/z
      ```

    - This is a second order linear differential equation with constant coefficients, which can be solved by the method of undetermined coefficients. The general solution is

      ```
      y(z) = c1 + c2 z + c3 z ln z + z^2/4
      ```

    - Substituting back z = e^x, we get

      ```
      y(x) = c1 + c2 e^x + c3 e^x ln e^x + e^(2x)/4
      ```

    - Simplifying, we get

      ```
      y(x) = c1 + c2 e^x + c3 x e^x + e^(2x)/4
      ```

    - This is the general solution of the original differential equation.

  - Example 2: Solve the differential equation (y')^2 - y y'' = 0.

    - Solution: The function of the dependent variable and its derivatives only is (y')^2 - y y''. Let z = (y')^2 - y y'', then dz/dx = 2 y' y'' - y'' - y y'''. Substituting z and dz/dx in the given differential equation, we get

      ```
      z - y dz/dx = 0
      ```

    - Simplifying, we get

      ```
      y dz/dx = z
      ```

    - This is a first order linear differential equation, which can be solved by the method of integrating factors. The general solution is

      ```
      y^2/2 = z x + c
      ```

    - Substituting back z = (y')^2 - y y'', we get

      ```
      y^2/2 = ((y')^2 - y y'') x + c
      ```

    - This is the general solution of the original differential equation.