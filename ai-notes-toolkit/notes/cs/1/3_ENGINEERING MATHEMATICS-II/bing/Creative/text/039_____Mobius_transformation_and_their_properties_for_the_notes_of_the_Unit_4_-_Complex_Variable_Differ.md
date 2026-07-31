### Mobius transformation and their properties

- A Mobius transformation is a function of the form `f(z) = (az + b) / (cz + d)`, where `a, b, c, d` are complex numbers and `ad - bc ≠ 0`.
- A Mobius transformation maps the extended complex plane `C ∪ {∞}` to itself, where `∞` is the point at infinity.
- A Mobius transformation is a composition of four elementary maps, namely translations, dilations, rotations, and inversions.
  - Translations: `z → z + z0` such that `z0 ∈ C`
  - Dilations: `z → λz`; `λ > 0` and `λ ∈ R`
  - Rotations: `z → eiθ z`; `θ ∈ R`
  - Inversions: `z → 1/z`
- A Mobius transformation is conformal, meaning it preserves angles and orientation locally.
- A Mobius transformation is bijective, meaning it is one-to-one and onto.
- A Mobius transformation is completely determined by any three input-output pairs. This means that for any triple of distinct input values `z1, z2, z3` in `C ∪ {∞}` and any triple of distinct output values `w1, w2, w3` in `C ∪ {∞}`, there is a unique `T ∈ M` such that `Tzi = wi` for `i = 1, 2, 3`.
- A Mobius transformation maps circles and lines to circles and lines. More precisely, it maps generalized circles, which are circles or lines, to generalized circles.
- A Mobius transformation has at most two fixed points, which are the solutions of `f(z) = z`. If it has two fixed points, it is called parabolic. If it has one fixed point, it is called elliptic. If it has no fixed points, it is called hyperbolic.
- The Mobius transformations form a group called the Mobius group, which is the projective linear group `PGL(2,C)`. This means that the composition of two Mobius transformations is another Mobius transformation, and the inverse of a Mobius transformation is also a Mobius transformation. The identity transformation is `f(z) = z`, and the inverse of `f(z) = (az + b) / (cz + d)` is `f-1(z) = (dz - b) / (-cz + a)`.
- The Mobius group has subgroups that correspond to different types of Mobius transformations. For example, the subgroup of translations is `T = {z → z + z0 | z0 ∈ C}`, and the subgroup of rotations is `R = {z → eiθ z | θ ∈ R}`.