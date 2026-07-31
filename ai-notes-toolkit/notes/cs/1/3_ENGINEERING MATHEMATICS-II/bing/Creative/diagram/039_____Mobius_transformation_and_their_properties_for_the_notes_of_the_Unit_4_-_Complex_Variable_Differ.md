### Mobius transformation and their properties

- A Mobius transformation is a function of the form

$$T(z) = \frac{az+b}{cz+d}$$

where $a, b, c, d$ are complex constants and $ad-bc \neq 0$.

- A Mobius transformation is also called a fractional linear transformation or a linear fractional transformation.

- A Mobius transformation is a composition of four elementary maps, namely translations, dilations, rotations, and inversions.

  - Translations: $z \to z + z_0$ such that $z_0 \in \mathbb{C}$

  - Dilations: $z \to \lambda z$ such that $\lambda > 0$ and $\lambda \in \mathbb{R}$

  - Rotations: $z \to e^{i\theta} z$ such that $\theta \in \mathbb{R}$

  - Inversions: $z \to \frac{1}{z}$

- A Mobius transformation is a conformal map, which means it preserves angles and orientation locally.

- A Mobius transformation is a bijective map, which means it is one-to-one and onto.

- A Mobius transformation can be extended to the Riemann sphere by defining $T(\infty) = \frac{a}{c}$ and $T(-\frac{d}{c}) = \infty$ if $c \neq 0$, and $T(\infty) = \infty$ if $c = 0$.

- A Mobius transformation maps circles and lines to circles and lines. That is, the image of a circle is either a circle or a line, and the image of a line is either a circle or a line.

- A Mobius transformation is determined by its action on three distinct points in the extended complex plane. That is, given any three distinct points $z_1, z_2, z_3$ and any three distinct points $w_1, w_2, w_3$ in the extended complex plane, there exists a unique Mobius transformation $T$ such that $T(z_i) = w_i$ for $i = 1, 2, 3$.

- A Mobius transformation can be represented by a $2 \times 2$ matrix with nonzero determinant, such that

$$T(z) = \frac{az+b}{cz+d} = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} z \\ 1 \end{pmatrix}$$

The matrix representation allows us to compose and invert Mobius transformations using matrix operations.

- The set of all Mobius transformations forms a group under composition, called the Mobius group or the projective linear group.

: https://byjus.com/maths/mobius-transformations/

: https://www.johndcook.com/blog/2021/02/26/smith-transform/

: https://bing.com/search?q=Mobius+transformation+and+their+properties

: https://math.libretexts.org/Bookshelves/Geometry/Geometry_with_an_Introduction_to_Cosmic_Topology_(Hitchman)/03%3A_Transformations/3.04%3A_Mobius_Transformations