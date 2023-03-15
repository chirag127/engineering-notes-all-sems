### Equilibrium equations and support reactions

- Equilibrium equations are the conditions that must be satisfied for a structure or a body to be in static equilibrium, i.e., the sum of all forces and moments acting on the structure or the body must be zero in any direction.
- Support reactions are the forces and moments that are exerted by the supports on the structure or the body to prevent its displacement or rotation.
- To determine the support reactions, one must first identify the type of supports and the number of unknown reaction components. Then, one must apply the equilibrium equations to the whole structure or a part of it (free body diagram) and solve for the unknowns.
- The types of supports commonly used in engineering are:
  - Fixed support: It prevents both displacement and rotation of the structure or the body at the point of contact. It has two reaction forces (horizontal and vertical) and one reaction moment.
  - Pinned support: It prevents displacement but allows rotation of the structure or the body at the point of contact. It has two reaction forces (horizontal and vertical) but no reaction moment.
  - Roller support: It prevents displacement in one direction but allows displacement and rotation in the other direction. It has one reaction force (vertical or horizontal) but no reaction moment.
- The number of unknown reaction components depends on the number and type of supports. For example, a simply supported beam with two pinned supports has four unknown reaction components (two horizontal and two vertical forces), while a cantilever beam with one fixed support has three unknown reaction components (one horizontal and one vertical force and one moment).
- The equilibrium equations for a planar structure or a body are:
  - Sum of forces in x-direction is zero: $\sum F_x = 0$
  - Sum of forces in y-direction is zero: $\sum F_y = 0$
  - Sum of moments about any point is zero: $\sum M = 0$
- The equilibrium equations for a three-dimensional structure or a body are:
  - Sum of forces in x-direction is zero: $\sum F_x = 0$
  - Sum of forces in y-direction is zero: $\sum F_y = 0$
  - Sum of forces in z-direction is zero: $\sum F_z = 0$
  - Sum of moments about x-axis is zero: $\sum M_x = 0$
  - Sum of moments about y-axis is zero: $\sum M_y = 0$
  - Sum of moments about z-axis is zero: $\sum M_z = 0$
- To solve for the support reactions, one must choose a convenient point or axis to take moments and a suitable direction to take forces. One must also consider the sign convention for forces and moments (positive or negative) and the units of measurement (SI or imperial).
- An example of solving for the support reactions of a simply supported beam with a point load at the center is shown below:

![Simply supported beam with a point load](https://www.calcresource.com/statics-simple-beam-reactions_files/image002.png)

- The beam has two pinned supports at A and B, so there are four unknown reaction components: $A_x$, $A_y$, $B_x$, and $B_y$.
- Applying the equilibrium equations to the whole beam, we get:

  - $\sum F_x = 0 \implies A_x + B_x = 0$ (1)
  - $\sum F_y = 0 \implies A_y + B_y - P = 0$ (2)
  - $\sum M_A = 0 \implies -B_y \times L + P \times \frac{L}{2} = 0$ (3)

- Solving for the unknowns, we get:

  - From equation (1), $A_x = -B_x$ (4)
  - From equation (3), $B_y = \frac{P}{2}$ (5)
  - Substituting equation (5) into equation (2), $A_y = \frac{P}{2}$ (6)

- Therefore, the support reactions are:

  - $A_x = -B_x = 0$ (zero horizontal force)
  - $A_y = B_y = \frac{P}{2}$ (equal and opposite vertical forces)