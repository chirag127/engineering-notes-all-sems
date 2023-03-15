### Beta and Gamma Function and their Properties

The Beta and Gamma functions are special functions that have important applications in probability theory, statistics, and mathematical analysis. They are defined as follows:

#### Beta Function
The Beta function is defined as an improper integral for positive values of x and y:

`B(x, y) = ∫[0,1] t^(x-1) * (1-t)^(y-1) dt`

Some properties of the Beta function include:
- The Beta function is symmetric: `B(x, y) = B(y, x)`
- The Beta function can be expressed in terms of the Gamma function: `B(x, y) = Γ(x) * Γ(y) / Γ(x + y)`
- The Beta function satisfies the following recurrence relation: `B(x + 1, y) = x / (x + y) * B(x, y)`

#### Gamma Function
The Gamma function is defined as an improper integral for positive values of x:

`Γ(x) = ∫[0,∞] t^(x-1) * e^(-t) dt`

Some properties of the Gamma function include:
- The Gamma function is a generalization of the factorial function: `Γ(n + 1) = n!` for positive integers n
- The Gamma function satisfies the following recurrence relation: `Γ(x + 1) = x * Γ(x)`
- The Gamma function has the following reflection formula: `Γ(x) * Γ(1 - x) = π / sin(πx)`

These functions and their properties are important in the study of multiple integration in the subject of Engineering Mathematics-I. They can be used to evaluate certain types of integrals and to derive various mathematical results. It is important to understand their definitions and properties in order to apply them effectively in mathematical analysis.