# Mobius transformation and their properties

A Mobius transformation is a function of the form

$$
f(z) = \frac{az + b}{cz + d}
$$

where $a, b, c, d$ are complex numbers and $ad - bc \neq 0$.

A Mobius transformation maps the extended complex plane $\hat{\mathbb{C}} = \mathbb{C} \cup \{\infty\}$ to itself. It is also called a fractional linear transformation or a linear fractional transformation.

Some properties of Mobius transformations are:

- A Mobius transformation is a composition of four elementary maps, namely translations, dilations, rotations, and inversions.
- A Mobius transformation is completely determined by any three input-output pairs. This means that for any triple of distinct input values $z_1, z_2, z_3$ in $\hat{\mathbb{C}}$ and any triple of distinct output values $w_1, w_2, w_3$ in $\hat{\mathbb{C}}$, there is a unique $f \in M$ such that $f(z_i) = w_i$ for $i = 1, 2, 3$.
- A Mobius transformation preserves the cross ratio of four points, that is, for any four points $z_1, z_2, z_3, z_4$ in $\hat{\mathbb{C}}$ and any $f \in M$, we have

$$
\frac{(f(z_1) - f(z_2))(f(z_3) - f(z_4))}{(f(z_1) - f(z_3))(f(z_2) - f(z_4))} = \frac{(z_1 - z_2)(z_3 - z_4)}{(z_1 - z_3)(z_2 - z_4)}
$$

- A Mobius transformation maps circles and lines to circles and lines. Moreover, it preserves the orientation and the angle of intersection of circles and lines.
- The Mobius transformations form a group called the Mobius group, which is the projective linear group $PGL(2, \mathbb{C})$. This group has a subgroup called the special Mobius group, which is the projective special linear group $PSL(2, \mathbb{C})$. These groups have numerous applications in mathematics and physics, such as group theory, hyperbolic geometry, and relativity.