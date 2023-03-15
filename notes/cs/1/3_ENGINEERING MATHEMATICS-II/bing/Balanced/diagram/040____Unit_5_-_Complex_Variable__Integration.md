## Unit 5 - Complex Variable –Integration

- Complex variable integration is the process of finding the value of a function of a complex variable along a curve or a contour in the complex plane.
- The basic concepts and properties of complex variable integration are similar to those of real variable integration, but there are some important differences and extensions.
- The most common types of complex variable integration are line integrals and contour integrals.
- A line integral of a complex function f(z) along a curve C is defined as

$$\int_C f(z) dz = \int_a^b f(z(t)) z'(t) dt$$

where z(t) is a parametric representation of C and a and b are the endpoints of the parameter interval.

- A contour integral of a complex function f(z) along a contour C is defined as the sum of line integrals over the finite number of smooth curves that make up C.

$$\int_C f(z) dz = \sum_{k=1}^n \int_{C_k} f(z) dz$$

where C is divided into n subcurves C_k.

- The main advantage of complex variable integration is that it can be used to evaluate some real integrals that are difficult or impossible to solve by other methods, such as trigonometric integrals, improper integrals, and definite integrals involving special functions.
- The main tool for complex variable integration is the Cauchy integral theorem, which states that if f(z) is analytic in a simply connected domain D and C is a closed contour in D, then

$$\int_C f(z) dz = 0$$

- The Cauchy integral theorem implies that the value of a contour integral does not depend on the choice of the contour, as long as it encloses the same region and has the same orientation. This property is called the independence of path.
- The Cauchy integral theorem also leads to the Cauchy integral formula, which states that if f(z) is analytic in a simply connected domain D and C is a positively oriented simple closed contour in D, then for any point z_0 inside C,

$$f(z_0) = \frac{1}{2\pi i} \int_C \frac{f(z)}{z-z_0} dz$$

- The Cauchy integral formula can be used to find the values of analytic functions inside a contour, to calculate their derivatives, and to express them as power series.
- Another important result of complex variable integration is the residue theorem, which states that if f(z) is analytic in a domain D except for a finite number of isolated singularities z_1, z_2, ..., z_n, and C is a positively oriented simple closed contour in D that encloses all the singularities, then

$$\int_C f(z) dz = 2\pi i \sum_{k=1}^n \text{Res}(f,z_k)$$

where Res(f,z_k) is the residue of f(z) at z_k, which is the coefficient of the (z-z_k)^(-1) term in the Laurent series expansion of f(z) around z_k.

- The residue theorem can be used to evaluate contour integrals that involve rational functions, trigonometric functions, exponential functions, logarithmic functions, and other functions with isolated singularities. It can also be used to evaluate some real integrals by applying the method of contour integration, which involves choosing a suitable contour in the complex plane and applying the residue theorem to the corresponding complex integral.