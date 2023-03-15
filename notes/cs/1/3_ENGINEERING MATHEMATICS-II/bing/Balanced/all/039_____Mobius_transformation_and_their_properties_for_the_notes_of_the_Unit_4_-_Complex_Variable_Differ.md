# Mobius transformation and their properties

A Mobius transformation is a function of the form

$$f(z) = \frac{az + b}{cz + d}$$

where $a, b, c, d$ are complex numbers and $ad - bc \neq 0$.

A Mobius transformation maps the extended complex plane $\hat{\mathbb{C}} = \mathbb{C} \cup \{\infty\}$ to itself. It is also called a fractional linear transformation or a linear fractional transformation.

Some properties of Mobius transformations are:

- A Mobius transformation is a composition of four elementary maps, namely translations, dilations, rotations, and inversions. Translations: $z \to z + z_0$ such that $z_0 \in \mathbb{C}$. Dilations: $z \to \lambda z$; $\lambda > 0$ and $\lambda \in \mathbb{R}$. Rotations: $z \to e^{i\theta} z$; $\theta \in \mathbb{R}$. Inversions: $z \to 1/z$.
- A Mobius transformation is conformal, meaning that it preserves angles and orientation locally.
- A Mobius transformation is one-to-one and onto, meaning that it is invertible and its inverse is also a Mobius transformation.
- A Mobius transformation maps circles and lines to circles and lines. More precisely, it maps generalized circles, which are circles or lines, to generalized circles. The inverse image of a generalized circle under a Mobius transformation is also a generalized circle.
- A Mobius transformation is completely determined by any three input-output pairs. This means that for any triple of distinct input values $z_1, z_2, z_3$ in $\hat{\mathbb{C}}$ and any triple of distinct output values $w_1, w_2, w_3$ in $\hat{\mathbb{C}}$, there is a unique $T \in M$ such that $Tz_i = w_i$ for $i = 1, 2, 3$.
- A Mobius transformation preserves the cross ratio of four points, which is defined as

$$[z_1, z_2, z_3, z_4] = \frac{(z_1 - z_3)(z_2 - z_4)}{(z_1 - z_4)(z_2 - z_3)}$$

This means that for any four points $z_1, z_2, z_3, z_4$ in $\hat{\mathbb{C}}$ and any Mobius transformation $T$, we have

$$[Tz_1, Tz_2, Tz_3, Tz_4] = [z_1, z_2, z_3, z_4]$$

- The Mobius transformations form a group called the Mobius group, which is the projective linear group $PGL(2, \mathbb{C})$. This means that the composition of two Mobius transformations is also a Mobius transformation, the identity function is a Mobius transformation, and every Mobius transformation has an inverse that is also a Mobius transformation. The Mobius group is isomorphic to the group of orientation-preserving isometries of the hyperbolic plane.