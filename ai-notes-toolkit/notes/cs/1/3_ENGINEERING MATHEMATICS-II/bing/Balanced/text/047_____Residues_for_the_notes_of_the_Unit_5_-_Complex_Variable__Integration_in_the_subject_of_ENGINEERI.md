Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is some content on the topic of residues for the notes of the unit 5 - complex variable integration in the subject of engineering mathematics-II.

### Residues

- A residue is a complex number that represents the coefficient of the term with power -1 in the Laurent series expansion of a complex function around a singularity.
- A singularity is a point where a complex function is not defined or not analytic. There are two types of singularities: isolated and non-isolated. An isolated singularity is a point where a function is not analytic, but it is analytic in a punctured disk around it. A non-isolated singularity is a point where a function is not analytic, and it is also not analytic in any punctured disk around it.
- The residue theorem is a powerful tool that relates the integral of a complex function along a closed contour to the sum of the residues of the function at the isolated singularities inside the contour. The residue theorem states that if f is a complex function that is analytic in a simply connected domain D except for a finite number of isolated singularities z1, z2, ..., zn, then for any positively oriented simple closed contour C in D that encloses the singularities, we have

  $$\oint_C f(z) dz = 2\pi i \sum_{k=1}^n \text{Res}(f, z_k)$$

  where Res(f, z_k) denotes the residue of f at z_k.
- To calculate the residue of a function f at an isolated singularity z_0, we can use the following methods:

  - If z_0 is a simple pole, that is, a pole of order 1, then

    $$\text{Res}(f, z_0) = \lim_{z \to z_0} (z - z_0) f(z)$$

  - If z_0 is a pole of order m, that is, a zero of order m of the denominator of f, then

    $$\text{Res}(f, z_0) = \frac{1}{(m-1)!} \lim_{z \to z_0} \frac{d^{m-1}}{dz^{m-1}} \left[(z - z_0)^m f(z)\right]$$

  - If z_0 is a removable singularity, that is, a point where f can be defined to make it analytic, then

    $$\text{Res}(f, z_0) = 0$$

  - If z_0 is an essential singularity, that is, a point where f has an infinite number of terms with negative powers in its Laurent series, then

    $$\text{Res}(f, z_0) = \text{the coefficient of } \frac{1}{z - z_0} \text{ in the Laurent series of } f \text{ around } z_0$$

- Residues can be used to evaluate real integrals that involve trigonometric, exponential, or rational functions. The general steps are:

  - Express the real integral as a complex integral along a suitable contour, such as a circle, a semicircle, or a rectangle.
  - Identify the singularities of the complex function inside the contour and calculate their residues.
  - Apply the residue theorem to obtain the value of the complex integral.
  - Use the properties of the contour, such as symmetry, periodicity, or limits, to relate the complex integral to the real integral.