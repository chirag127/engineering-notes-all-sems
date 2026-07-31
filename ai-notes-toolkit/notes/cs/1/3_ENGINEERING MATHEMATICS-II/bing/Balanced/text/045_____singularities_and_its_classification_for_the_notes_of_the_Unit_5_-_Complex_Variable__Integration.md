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