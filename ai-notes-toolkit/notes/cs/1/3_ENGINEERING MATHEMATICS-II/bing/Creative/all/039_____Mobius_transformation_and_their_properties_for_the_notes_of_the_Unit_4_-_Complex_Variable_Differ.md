# Mobius transformation and their properties

A Mobius transformation is a function of the form

$$f(z) = \frac{az + b}{cz + d}$$

where $a, b, c, d$ are complex numbers and $ad - bc \neq 0$.

A Mobius transformation maps the extended complex plane $\hat{\mathbb{C}} = \mathbb{C} \cup \{\infty\}$ to itself. It is also called a fractional linear transformation or a linear fractional transformation.

Some properties of Mobius transformations are:

- A Mobius transformation is a composition of four elementary maps, namely translations, dilations, rotations, and inversions.
  - Translations: $z \mapsto z + z_0$ such that $z_0 \in \mathbb{C}$
  - Dilations: $z \mapsto \lambda z$; $\lambda > 0$ and $\lambda \in \mathbb{R}$
  - Rotations: $z \mapsto e^{i\theta} z$; $\theta \in \mathbb{R}$
  - Inversions: $z \mapsto \frac{1}{z}$
- A Mobius transformation is conformal, meaning that it preserves angles and orientation.
- A Mobius transformation maps circles and lines to circles and lines. More precisely, it maps generalized circles, which are circles or lines, to generalized circles.
- A Mobius transformation has at most two fixed points, which are the solutions of $f(z) = z$. If it has two fixed points, it is called parabolic. If it has one fixed point, it is called elliptic. If it has no fixed points, it is called hyperbolic.
- A Mobius transformation is completely determined by any three input-output pairs. This means that for any triple of distinct input values $z_1, z_2, z_3$ in $\hat{\mathbb{C}}$ and any triple of distinct output values $w_1, w_2, w_3$ in $\hat{\mathbb{C}}$, there is a unique $f \in M$ such that $f(z_i) = w_i$ for $i = 1, 2, 3$.
- The Mobius transformations form a group under composition, called the Mobius group, which is the projective linear group $PGL(2, \mathbb{C})$. This group has a subgroup called the special Mobius group, which is the projective special linear group $PSL(2, \mathbb{C})$. This subgroup consists of Mobius transformations with determinant one, i.e. $ad - bc = 1$.

: https://byjus.com/maths/mobius-transformations/
: https://www.nagwa.com/en/explainers/182153831081/
: https://www.johndcook.com/blog/2021/02/26/smith-transform/
: https://en.wikipedia.org/wiki/M%C3%B6bius_transformation
: https://math.libretexts.org/Bookshelves/Analysis/Book%3A_Complex_Analysis_(Trench)/3%3A_M%C3%B6bius_Geometry/3.2%3A_M%C3%B6bius_Geometry