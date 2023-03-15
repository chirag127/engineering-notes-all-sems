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