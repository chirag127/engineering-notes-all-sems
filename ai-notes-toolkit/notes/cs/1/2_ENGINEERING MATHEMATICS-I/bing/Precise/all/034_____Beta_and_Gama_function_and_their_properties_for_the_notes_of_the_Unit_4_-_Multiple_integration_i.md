### Unit 4 - Multiple Integration: Beta and Gamma Functions and their Properties

#### Beta Function
- The Beta function, also known as the Euler integral of the first kind, is a special function defined by the integral:
  `B(x, y) = ∫[0,1] t^(x-1) * (1-t)^(y-1) dt` for `Re(x) > 0` and `Re(y) > 0`.
- The Beta function is symmetric, meaning that `B(x, y) = B(y, x)`.
- The Beta function is related to the Gamma function by the following identity: `B(x, y) = Γ(x) * Γ(y) / Γ(x + y)`.

#### Gamma Function
- The Gamma function, denoted by `Γ(x)`, is an extension of the factorial function to complex numbers.
- For positive integers `n`, `Γ(n) = (n-1)!`.
- The Gamma function is defined for all complex numbers except for non-positive integers.
- The Gamma function satisfies the functional equation `Γ(x+1) = x * Γ(x)`.

#### Properties
- The Beta and Gamma functions have several important properties that are useful in multiple integration.
- One such property is the duplication formula for the Gamma function: `Γ(x) * Γ(x + 1/2) = 2^(1-2x) * √π * Γ(2x)`.
- Another property is the reflection formula for the Gamma function: `Γ(x) * Γ(1-x) = π / sin(πx)`.
- These properties, along with others, can be used to evaluate integrals and solve problems in multiple integration.
