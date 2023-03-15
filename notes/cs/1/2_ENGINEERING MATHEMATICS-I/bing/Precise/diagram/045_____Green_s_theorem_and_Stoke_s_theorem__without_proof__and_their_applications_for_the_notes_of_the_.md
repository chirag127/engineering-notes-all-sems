### Green’s Theorem and Stoke’s Theorem (without proof) and their applications

#### Green’s Theorem
Green’s Theorem relates a line integral around a simple closed curve C to a double integral over the plane region D bounded by C. It states that if L and M are functions of (x, y) defined on an open region containing D and have continuous partial derivatives there, then:

$$\oint_C (L dx + M dy) = \iint_D (\frac{\partial M}{\partial x} - \frac{\partial L}{\partial y}) dA$$

#### Applications of Green’s Theorem
1. Finding the area of a plane region: Green’s Theorem can be used to find the area of a plane region D by choosing L(x, y) = 0 and M(x, y) = x.
2. Evaluating line integrals: Green’s Theorem can be used to evaluate line integrals by converting them into double integrals.

#### Stoke’s Theorem
Stoke’s Theorem relates a surface integral of the curl of a vector field over a surface S to a line integral of the vector field around the boundary curve C of S. It states that if S is an oriented piecewise-smooth surface that is bounded by a simple, closed, piecewise-smooth boundary curve C with positive orientation and F is a vector field whose components have continuous partial derivatives on an open region in R3 that contains S, then:

$$\int_C F \cdot dr = \iint_S curl F \cdot dS$$

#### Applications of Stoke’s Theorem
1. Evaluating line integrals: Stoke’s Theorem can be used to evaluate line integrals by converting them into surface integrals.
2. Finding the circulation and flux of a vector field: Stoke’s Theorem can be used to find the circulation and flux of a vector field around a closed curve by evaluating the surface integral of the curl of the vector field over a surface bounded by the curve.
