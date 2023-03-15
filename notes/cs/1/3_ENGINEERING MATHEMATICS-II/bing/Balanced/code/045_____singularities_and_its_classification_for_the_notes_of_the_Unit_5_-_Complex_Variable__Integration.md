### Singularities and its classification for the notes of the Unit 5 - Complex Variable –Integration in the subject of ENGINEERING MATHEMATICS-II

- A singularity is a point in the domain of a complex function where the function fails to be analytic .
- A function is analytic at a point if it has a convergent power series expansion in some neighborhood of that point.
- There are different types of singularities depending on the behavior of the function near the singularity.
- The main types of singularities are:
  - Isolated singularities: These are points where the function is not analytic, but there exists a neighborhood around them where the function is analytic everywhere else. Isolated singularities can be further classified into :
    - Removable singularities: These are points where the function has a finite limit, but the function is not defined or has a different value at that point. These singularities can be removed by redefining the function at that point to match the limit .
    - Poles: These are points where the function has an infinite limit. A pole of order n is a point where the function behaves like 1/(z-z0)^n near the singularity, where z0 is the location of the pole and n is a positive integer .
    - Essential singularities: These are points where the function has no finite or infinite limit, and the function oscillates wildly near the singularity. These singularities cannot be removed or reduced to a pole .
  - Nonisolated singularities: These are points where the function is not analytic, and there is no neighborhood around them where the function is analytic everywhere else. An example of a nonisolated singularity is a branch point, where the function has multiple values depending on the branch of a multivalued function.
- The principal part of a function at an isolated singularity is the part of the Laurent series expansion that involves negative powers of z-z0, where z0 is the location of the singularity .
- The residue of a function at an isolated singularity is the coefficient of the term 1/(z-z0) in the principal part of the function. The residue plays an important role in complex analysis, especially in the calculation of contour integrals using the residue theorem .